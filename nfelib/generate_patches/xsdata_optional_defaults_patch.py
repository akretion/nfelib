"""Runtime patch for xsdata >= 25: keep required fields optional with a default.

xsdata 24.x generated every field as ``Optional[...] = None`` (schema-required
elements carried a ``required=True`` metadata but still had a ``None`` default),
which lets the parser accept real-world documents that omit elements the schema
marks mandatory (e.g. an unsigned NF-e without ``<Signature>``) and lets callers
build partial objects incrementally (as Odoo / spec_driven_model do).

xsdata >= 25 instead emits schema-required fields with **no default** (and
``kw_only=True``), so parsing such documents raises ``TypeError: missing
required keyword-only argument`` and ``cls()`` no longer works.

This patch restores the 24.x behaviour by forcing every field to be optional:

* ``field_default_value`` returns ``None`` where it would return ``False``
  (i.e. for otherwise-required fields), so the field gets ``= None``.
* ``field_type`` wraps the annotation as ``None | <type>`` to match the
  ``None`` default (xsdata only does this for already-optional fields).

It only affects generated defaults/annotations, never the runtime models or the
``required`` validation metadata (so serialization still enforces the schema).
"""

from __future__ import annotations

from xsdata.formats.dataclass.filters import Filters

_original_field_default_value = Filters.field_default_value
_original_field_type = Filters.field_type


def _field_default_value(self, attr, ns_map=None):  # noqa: ANN001
    value = _original_field_default_value(self, attr, ns_map)
    # False means "no default" -> required field. Force an optional None default
    # so the generated dataclasses stay backward compatible (Python 3.8 / Odoo).
    if value is False and not attr.is_prohibited:
        return None
    return value


def _field_type(self, obj, attr):  # noqa: ANN001
    result = _original_field_type(self, attr=attr, obj=obj)
    # Mirror the forced None default in the annotation. Skip collection/prohibited
    # fields and anything xsdata already made optional.
    if (
        attr.is_prohibited
        or attr.is_list
        or attr.is_tokens
        or attr.is_dict
        or result.startswith("None | ")
        or result.startswith("Optional[")
    ):
        return result
    return f"None | {result}"


def apply_patch() -> None:
    """Monkey-patch xsdata.formats.dataclass.filters.Filters."""
    Filters.field_default_value = _field_default_value
    Filters.field_type = _field_type
