"""Runtime patch for xsdata: chameleon schema ordering fix.

Apply this before generating nfelib bindings when the installed xsdata does
not yet include the directory generation fix.
"""

from __future__ import annotations

import re

from xsdata.codegen import opener
from xsdata.codegen.transformer import ResourceTransformer


def _has_target_namespace(self: ResourceTransformer, uri: str) -> bool:
    """Read the schema root and return whether it declares a target namespace."""
    try:
        data = opener.open(uri).read()
    except OSError:
        return False

    text = data.decode("utf-8", errors="ignore")
    match = re.search(r"<(?:xs?:)?schema\b[^>]*>", text, re.IGNORECASE | re.DOTALL)
    if match:
        return bool(re.search(r"targetNamespace\s*=", match.group(0)))

    return False


def _process_schemas(self: ResourceTransformer, uris: list[str]) -> None:
    """Process schemas with a target namespace before chameleon schemas."""
    sorted_uris = sorted(uris, key=lambda uri: not self.has_target_namespace(uri))
    for uri in sorted_uris:
        self.process_schema(uri)


def apply_patch() -> None:
    """Monkey-patch xsdata.codegen.transformer.ResourceTransformer."""
    ResourceTransformer.process_schemas = _process_schemas
    ResourceTransformer.has_target_namespace = _has_target_namespace
