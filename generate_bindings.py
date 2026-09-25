#! /usr/bin/env python3
"""Generate nfelib bindings from XSD schemas with local xsdata patches.

Usage:
    python generate_bindings.py nfe
    python generate_bindings.py cte mdfe bpe
    python generate_bindings.py all --download

This script monkey-patches xsdata at runtime with:
1. The chameleon-schema ordering fix from `xsdata/codegen/transformer.py`.
2. The NFe-specific attribute merge hooks from `xsdata_odoo/hook.py`.

Both patches are copied into this repo so generation remains self-contained
and independent of whether the patches are merged upstream.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path
from typing import Final

# ---------------------------------------------------------------------------
# Local patch sources
# ---------------------------------------------------------------------------

ROOT: Final = Path(__file__).parent.resolve()
PATCH_DIR: Final = ROOT / "nfelib" / "generate_patches"

CHAMELEON_PATCH: Final = PATCH_DIR / "xsdata_chameleon_patch.py"
HOOK_PATCH: Final = PATCH_DIR / "xsdata_odoo_hook.py"


# ---------------------------------------------------------------------------
# Schema configuration
# ---------------------------------------------------------------------------


class SchemaConfig:
    """Describe one schema / binding target."""

    def __init__(
        self,
        name: str,
        schema_dir: str,
        package: str,
        single_package: str | None = None,
        download_url: str | None = None,
    ) -> None:
        self.name = name
        self.schema_dir = schema_dir
        self.package = package
        self.single_package = single_package
        self.download_url = download_url


SCHEMAS: Final[dict[str, SchemaConfig]] = {
    "nfe": SchemaConfig(
        name="nfe",
        schema_dir="nfelib/nfe/schemas/v4_0",
        package="nfelib.nfe.bindings.v4_0",
    ),
    "nfe_dist_dfe": SchemaConfig(
        name="nfe_dist_dfe",
        schema_dir="nfelib/nfe_dist_dfe/schemas/v1_0",
        package="nfelib.nfe_dist_dfe.bindings.v1_0",
    ),
    "nfe_evento_generico": SchemaConfig(
        name="nfe_evento_generico",
        schema_dir="nfelib/nfe_evento_generico/schemas/v1_0",
        package="nfelib.nfe_evento_generico.bindings.v1_0",
    ),
    "nfe_evento_cancel": SchemaConfig(
        name="nfe_evento_cancel",
        schema_dir="nfelib/nfe_evento_cancel/schemas/v1_0",
        package="nfelib.nfe_evento_cancel.bindings.v1_0",
    ),
    "nfe_evento_cce": SchemaConfig(
        name="nfe_evento_cce",
        schema_dir="nfelib/nfe_evento_cce/schemas/v1_0",
        package="nfelib.nfe_evento_cce.bindings.v1_0",
    ),
    "nfe_evento_mde": SchemaConfig(
        name="nfe_evento_mde",
        schema_dir="nfelib/nfe_evento_mde/schemas/v1_0",
        package="nfelib.nfe_evento_mde.bindings.v1_0",
    ),
    "nfe_cons": SchemaConfig(
        name="nfe_cons",
        schema_dir="nfelib/nfe_cons/schemas/v2_0",
        package="nfelib.nfe_cons.bindings.v2_0",
    ),
    "nfe_ator_interessado": SchemaConfig(
        name="nfe_ator_interessado",
        schema_dir="nfelib/nfe_ator_interessado/schemas/v1_0",
        package="nfelib.nfe_ator_interessado.bindings.v1_0",
    ),
    "nfe_epec_110140": SchemaConfig(
        name="nfe_epec_110140",
        schema_dir="nfelib/nfe_epec/schemas/v1_0/e110140_v1.00.xsd",
        package="nfelib.nfe_epec.bindings.v1_0.e110140_v1_00",
        single_package="e110140_v1_00",
    ),
    "nfe_epec_leiaute": SchemaConfig(
        name="nfe_epec_leiaute",
        schema_dir="nfelib/nfe_epec/schemas/v1_0/leiauteEPEC_v1.00.xsd",
        package="nfelib.nfe_epec.bindings.v1_0.leiaute_epec_v1_00",
        single_package="leiaute_epec_v1_00",
    ),
    "nfe_entrega": SchemaConfig(
        name="nfe_entrega",
        schema_dir="nfelib/nfe_entrega/schemas/v1_0",
        package="nfelib.nfe_entrega.bindings.v1_0",
    ),
    "nfe_insucesso": SchemaConfig(
        name="nfe_insucesso",
        schema_dir="nfelib/nfe_insucesso/schemas/v1_0",
        package="nfelib.nfe_insucesso.bindings.v1_0",
    ),
    "cte": SchemaConfig(
        name="cte",
        schema_dir="nfelib/cte/schemas/v4_0",
        package="nfelib.cte.bindings.v4_0",
    ),
    "cte_dist_dfe": SchemaConfig(
        name="cte_dist_dfe",
        schema_dir="nfelib/cte_dist_dfe/schemas/v1_0",
        package="nfelib.cte_dist_dfe.bindings.v1_0",
    ),
    "mdfe": SchemaConfig(
        name="mdfe",
        schema_dir="nfelib/mdfe/schemas/v3_0",
        package="nfelib.mdfe.bindings.v3_0",
    ),
    "mdfe_dist_dfe": SchemaConfig(
        name="mdfe_dist_dfe",
        schema_dir="nfelib/mdfe_dist_dfe/schemas/v1_0",
        package="nfelib.mdfe_dist_dfe.bindings.v1_0",
    ),
    "bpe": SchemaConfig(
        name="bpe",
        schema_dir="nfelib/bpe/schemas/v1_0",
        package="nfelib.bpe.bindings.v1_0",
    ),
    "nfse": SchemaConfig(
        name="nfse",
        schema_dir="nfelib/nfse/schemas/v1_0",
        package="nfelib.nfse.bindings.v1_0",
    ),
}

DOWNLOAD_URLS: Final[dict[str, str]] = {
    "nfe": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Uk1T1otPFqI=",
    "nfe_dist_dfe": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=n3Kn9%20YZNak=",
    "nfe_evento_generico": "http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YaiBe2csOmA=",
    "nfe_evento_cancel": "http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=MtjAJ1Rurjc=",
    "nfe_evento_cce": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=P/FXaGiLKo0=",
    "nfe_evento_mde": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=y2nVL6/GFlU=",
    "nfe_cons": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=/KLQ3Wi0ckY=",
    "nfe_ator_interessado": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ufthUw%20oQd8=",
    "nfe_epec": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=HcoVPI2JvY0=",
    "nfe_entrega": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2AWmHNFOCe8=",
    "nfe_insucesso": "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=qvyq5vuft74=",
    "cte": "https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=1hNQGC4YA/o=",
    "cte_dist_dfe": "https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=l6I2ehbBicE=",
    "mdfe": "https://mdfe-portal.svrs.rs.gov.br/MDFE/DownloadArquivoEstatico/?sistema=MDFE&tipoArquivo=2&nomeArquivo=PL_MDFe_300a_NT022021.zip",
    "mdfe_dist_dfe": "https://dfe-portal.svrs.rs.gov.br/MDFE/DownloadArquivoEstatico/?sistema=MDFE&tipoArquivo=2&nomeArquivo=PL_MDFeDistDFe_100.zip",
    "bpe": "https://dfe-portal.svrs.rs.gov.br/BPE/DownloadArquivoEstatico/?sistema=BPE&tipoArquivo=2&nomeArquivo=PL_BPe_100b_NT012021.zip",
    "nfse": "https://www.gov.br/nfse/pt-br/documentacao-tecnica/xsd_pl_nfse_1-00-producao.zip/@@download/file/XSD_PL_NFSe_1.00-Produ%C3%A7%C3%A3o.zip",
}


# ---------------------------------------------------------------------------
# Patch helpers
# ---------------------------------------------------------------------------


def _ensure_patches() -> None:
    """Copy the two local patches into the project if they are not present."""
    PATCH_DIR.mkdir(parents=True, exist_ok=True)

    if not CHAMELEON_PATCH.exists():
        xsdata_transformer = (
            ROOT.parent / "xsdata" / "xsdata" / "codegen" / "transformer.py"
        ).resolve()
        if xsdata_transformer.exists():
            shutil.copy(xsdata_transformer, CHAMELEON_PATCH)
        else:
            raise FileNotFoundError(
                "Chameleon patch source not found. Expected "
                f"{xsdata_transformer} or {CHAMELEON_PATCH}"
            )

    if not HOOK_PATCH.exists():
        xsdata_odoo_hook = (
            ROOT.parent / "xsdata-odoo" / "xsdata_odoo" / "hook.py"
        ).resolve()
        if xsdata_odoo_hook.exists():
            shutil.copy(xsdata_odoo_hook, HOOK_PATCH)
        else:
            raise FileNotFoundError(
                "Hook patch source not found. Expected "
                f"{xsdata_odoo_hook} or {HOOK_PATCH}"
            )


def _apply_patches() -> None:
    """Apply both local patches to the installed xsdata.

    The NFe attribute-merge hook reads ``XSDATA_SCHEMA`` at generation time, so
    that variable is set per-binding in ``main`` (around ``_run_xsdata``), not
    here. This step only registers the patched methods on xsdata's classes.
    """
    _ensure_patches()

    # Import xsdata modules so they can be patched.
    import xsdata.codegen.handlers.merge_attributes
    import xsdata.codegen.handlers.update_attributes_effective_choice
    import xsdata.codegen.transformer
    import xsdata.codegen.writer  # noqa: F401

    # 1. Chameleon ordering fix: replace the methods on the real class.
    chameleon_globals: dict = {}
    exec(CHAMELEON_PATCH.read_text(), chameleon_globals)
    chameleon_globals["apply_patch"]()

    # 2. xsdata_odoo NFe hook: registers patched merge methods. The hook's
    #    NFe-specific branch is gated on XSDATA_SCHEMA, set later per-binding.
    hook_globals: dict = {"__name__": "__nfelib_hook__"}
    exec(HOOK_PATCH.read_text(), hook_globals)


# ---------------------------------------------------------------------------
# xsdata invocation
# ---------------------------------------------------------------------------


def _run_xsdata(
    schema_dir: Path,
    package: str,
    *,
    single_package: bool = False,
    output_format: str | None = None,
) -> None:
    """Invoke xsdata generate in-process for the given schema target.

    Generation runs in-process (not via a subprocess) so the runtime
    monkey-patches applied by ``_apply_patches`` are in effect. A subprocess
    would import a fresh, unpatched xsdata and miss both the chameleon fix and
    the NFe attribute-merge hook.
    """
    from xsdata.cli import resolve_source
    from xsdata.codegen.transformer import ResourceTransformer
    from xsdata.models.config import GeneratorConfig, StructureStyle

    config_file = ROOT / ".xsdata.xml"
    if config_file.exists():
        config = GeneratorConfig.read(config_file)
    else:
        config = GeneratorConfig()

    config.output.package = package
    config.output.include_header = True
    if single_package:
        config.output.structure_style = StructureStyle.SINGLE_PACKAGE
    if output_format:
        config.output.format.value = output_format

    print(
        f"Generating {package} from {schema_dir} (output={output_format or 'default'})"
    )
    transformer = ResourceTransformer(config=config)
    uris = sorted(resolve_source(str(schema_dir), recursive=False))
    transformer.process(uris)


# ---------------------------------------------------------------------------
# Download helpers
# ---------------------------------------------------------------------------


def _download_schemas(name: str, config: SchemaConfig) -> None:
    """Download and install schemas using erpbrasil-edoc-gen-download-schema."""
    if name not in DOWNLOAD_URLS:
        print(f"No download URL configured for {name}, skipping.")
        return

    url = DOWNLOAD_URLS[name]

    tmp_generated = Path("/tmp/generated")
    tmp_schemas = tmp_generated / name / "schemas" / Path(config.schema_dir).name

    if tmp_generated.exists():
        shutil.rmtree(tmp_generated)

    cmd = [
        "erpbrasil-edoc-gen-download-schema",
        "-n",
        name,
        "-v",
        Path(config.schema_dir).name,
        "-u",
        url,
    ]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    if name == "nfe_evento_mde":
        target = tmp_schemas / "retEnvConfRecebto_v1.00.xsd"
        if target.exists():
            subprocess.run(
                [
                    "iconv",
                    "-f",
                    "iso-8859-1",
                    "-t",
                    "UTF-8",
                    "-o",
                    str(target),
                    str(target),
                ],
                check=True,
            )

    if name == "nfe_cons":
        for path in tmp_schemas.glob("*v2.00.xsd"):
            path.unlink()

    if name == "nfe_epec":
        src = tmp_generated / "nfe_ator_interessado" / "schemas"
        if src.exists():
            if tmp_schemas.exists():
                shutil.rmtree(tmp_schemas)
            shutil.copytree(src, tmp_schemas)

    dest = Path(config.schema_dir).parent
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(tmp_schemas, dest)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate nfelib bindings from XSD schemas.",
    )
    parser.add_argument(
        "bindings",
        nargs="+",
        help="Binding(s) to generate. Use 'all' for every known binding.",
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help=(
            "Download schemas with erpbrasil-edoc-gen-download-schema first. "
            "WARNING: this relies on an unmaintained experimental tool; "
            "prefer using the committed schemas and avoid this option."
        ),
    )
    parser.add_argument(
        "--output",
        dest="output_format",
        default=None,
        help=(
            "xsdata output format passed to the generator "
            "(e.g. 'pydataclass', 'dataclasses', or a plugin alias). "
            "Use 'odoo' with the xsdata-odoo plugin to generate Odoo abstract models."
        ),
    )
    parser.add_argument(
        "--skip-patches",
        action="store_true",
        help="Skip patching xsdata (only if installed xsdata is already patched).",
    )
    return parser.parse_args()


def _resolve_names(names: list[str]) -> list[str]:
    """Expand 'all' and validate binding names."""
    if "all" in names:
        return list(SCHEMAS.keys())

    unknown = [n for n in names if n not in SCHEMAS]
    if unknown:
        raise SystemExit(f"Unknown binding(s): {', '.join(unknown)}")
    return names


def main() -> None:
    """Parse arguments, patch xsdata, and generate the requested bindings."""
    args = _parse_args()
    names = _resolve_names(args.bindings)

    if not args.skip_patches:
        _apply_patches()

    for name in names:
        config = SCHEMAS[name]

        if args.download:
            _download_schemas(name, config)

        schema_path = Path(config.schema_dir)
        if not schema_path.exists():
            print(f"Skipping {name}: schema path not found {schema_path}")
            continue

        # Set schema/version env vars so xsdata-odoo can apply the correct field
        # prefixes (e.g. nfe40_, cte40_, mdfe30_). The version is derived from
        # the schema directory name (v4_0 -> 40, v3_0 -> 30, v1_0 -> 10).
        env_before = os.environ.get("XSDATA_SCHEMA")
        version_before = os.environ.get("XSDATA_VERSION")
        lang_before = os.environ.get("XSDATA_LANG")
        schema_name = name.split("_")[0]
        os.environ["XSDATA_SCHEMA"] = schema_name
        version = Path(config.schema_dir).name.lstrip("v").replace("_", "")
        os.environ["XSDATA_VERSION"] = version
        os.environ["XSDATA_LANG"] = "portuguese"

        # When generating Odoo models, write them to a different package path so
        # they do not overwrite the standard Python dataclass bindings.
        package = config.package
        if args.output_format == "odoo":
            package = package.replace(".bindings.", ".odoo.")

        try:
            _run_xsdata(
                schema_path,
                package,
                single_package=config.single_package is not None,
                output_format=args.output_format,
            )
        finally:
            if env_before is None:
                os.environ.pop("XSDATA_SCHEMA", None)
            else:
                os.environ["XSDATA_SCHEMA"] = env_before
            if version_before is None:
                os.environ.pop("XSDATA_VERSION", None)
            else:
                os.environ["XSDATA_VERSION"] = version_before
            if lang_before is None:
                os.environ.pop("XSDATA_LANG", None)
            else:
                os.environ["XSDATA_LANG"] = lang_before


if __name__ == "__main__":
    main()
