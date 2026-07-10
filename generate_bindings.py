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
import sys
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
    """Apply both local patches to the installed xsdata."""
    _ensure_patches()

    # Import xsdata modules so they can be patched.
    import xsdata.codegen.handlers.merge_attributes  # noqa: F401
    import xsdata.codegen.handlers.update_attributes_effective_choice  # noqa: F401
    import xsdata.codegen.transformer  # noqa: F401
    import xsdata.codegen.writer  # noqa: F401

    # 1. Chameleon ordering fix: replace the methods on the real class.
    chameleon_globals: dict = {}
    exec(CHAMELEON_PATCH.read_text(), chameleon_globals)  # noqa: S102
    chameleon_globals["apply_patch"]()

    # 2. xsdata_odoo NFe hook. The hook expects XSDATA_SCHEMA=nfe to be set.
    env_before = os.environ.get("XSDATA_SCHEMA")
    os.environ["XSDATA_SCHEMA"] = "nfe"
    try:
        hook_globals: dict = {"__name__": "__nfelib_hook__"}
        exec(HOOK_PATCH.read_text(), hook_globals)  # noqa: S102
    finally:
        if env_before is None:
            os.environ.pop("XSDATA_SCHEMA", None)
        else:
            os.environ["XSDATA_SCHEMA"] = env_before


# ---------------------------------------------------------------------------
# xsdata invocation
# ---------------------------------------------------------------------------


def _run_xsdata(schema_dir: Path, package: str, *, single_package: bool = False) -> None:
    """Invoke xsdata generate for the given schema target."""
    cmd: list[str] = [sys.executable, "-m", "xsdata", "generate"]
    if single_package:
        cmd.extend(["-ss", "single-package"])
    cmd.extend(["--include-header", str(schema_dir), "--package", package])

    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


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
        help="Download schemas with erpbrasil-edoc-gen-download-schema before generating.",
    )
    parser.add_argument(
        "--skip-patches",
        action="store_true",
        help="Skip monkey-patching xsdata (only if installed xsdata is already patched).",
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

        _run_xsdata(
            schema_path,
            config.package,
            single_package=config.single_package is not None,
        )


if __name__ == "__main__":
    main()
