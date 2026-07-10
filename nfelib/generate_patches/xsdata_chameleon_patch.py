"""Runtime patch for xsdata: skip xs:included chameleon schemas.

When generating from a directory, a chameleon schema (no targetNamespace) that
is xs:included by a namespaced schema is also compiled standalone as a
directory entry, registering its types with no namespace. The later include is
then skipped (URI already processed) and references from the including schema
fall back to ``str`` with "Reset absent type" warnings.

This patch makes ``process_schemas`` skip, as top-level sources, the chameleon
schemas that are xs:included by a namespaced schema in the same batch; the
include compiles them with the correct namespace. Standalone chameleons that
nobody includes are still processed. Each source is read once (cached in
``preloaded``) so there is no double disk read.

Mirrors the upstream fix in xsdata/codegen/transformer.py. Apply it before
generating nfelib bindings when the installed xsdata does not yet include the
fix (e.g. xsdata 24.11, kept for Python 3.8 / Odoo 14 compatibility).
"""

from __future__ import annotations

import re
from urllib.parse import urljoin

from xsdata.codegen import opener
from xsdata.codegen.transformer import ResourceTransformer

_SCHEMA_RE = re.compile(r"<(?:\w+:)?schema\b[^>]*>", re.IGNORECASE | re.DOTALL)
_INCLUDE_RE = re.compile(
    r'<(?:\w+:)?include\b[^>]*schemaLocation="([^"]+)"', re.IGNORECASE
)


def _find_included_chameleons(self: ResourceTransformer, uris: list[str]) -> set[str]:
    """Return the chameleon schemas that are xs:included by a namespaced one."""
    has_ns: dict[str, bool] = {}
    includes: dict[str, set[str]] = {}
    for uri in uris:
        try:
            data = opener.open(uri).read()  # nosec
        except OSError:
            continue

        self.preloaded[uri] = data
        text = data.decode("utf-8", errors="ignore")
        header = _SCHEMA_RE.search(text)
        has_ns[uri] = bool(
            header and re.search(r"targetNamespace\s*=", header.group(0))
        )
        includes[uri] = {urljoin(uri, loc) for loc in _INCLUDE_RE.findall(text)}

    included_by_ns: set[str] = set()
    for uri, namespaced in has_ns.items():
        if namespaced:
            included_by_ns |= includes[uri]

    return {
        uri
        for uri, namespaced in has_ns.items()
        if not namespaced and uri in included_by_ns
    }


def _process_schemas(self: ResourceTransformer, uris: list[str]) -> None:
    """Process xsd sources, skipping xs:included chameleon schemas."""
    skip = self.find_included_chameleons(uris)
    for uri in uris:
        if uri not in skip:
            self.process_schema(uri)


def apply_patch() -> None:
    """Monkey-patch xsdata.codegen.transformer.ResourceTransformer."""
    ResourceTransformer.find_included_chameleons = _find_included_chameleons
    ResourceTransformer.process_schemas = _process_schemas
