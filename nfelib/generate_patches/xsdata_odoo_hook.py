import os

from xsdata.codegen.handlers.merge_attributes import MergeAttributes
from xsdata.codegen.handlers.update_attributes_effective_choice import (
    UpdateAttributesEffectiveChoice,
)
from xsdata.codegen.models import Attr, Class
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import collections


@classmethod  # type: ignore[misc]  # Suppresses "classmethod used with a non-method"
def process(cls, target: Class):
    """
    Detect same type attributes in order to merge them together with their
    restrictions.

    Two attributes are considered equal if they have the same name,
    tag and namespace.
    """
    result: list[Attr] = []
    for attr in target.attrs:
        pos = collections.find(result, attr)
        existing = result[pos] if pos > -1 else None

        if not existing:
            result.append(attr)
        elif not (attr.is_attribute or attr.is_enumeration):
            existing.help = existing.help or attr.help

            e_res = existing.restrictions
            a_res = attr.restrictions

            min_occurs = e_res.min_occurs or 0
            max_occurs = e_res.max_occurs or 1
            attr_min_occurs = a_res.min_occurs or 0
            attr_max_occurs = a_res.max_occurs or 1

            e_res.min_occurs = min(min_occurs, attr_min_occurs)
            if os.environ.get("XSDATA_SCHEMA") in ("nfe",):
                e_res.max_occurs = min(max_occurs, attr_max_occurs)  # this is the patch
            else:
                e_res.max_occurs = max_occurs + attr_max_occurs
            e_res.sequential = a_res.sequential or e_res.sequential
            existing.fixed = False
            existing.types.extend(attr.types)

    target.attrs = result
    ClassUtils.cleanup_class(target)


@classmethod  # type: ignore[misc]  # Suppresses "classmethod used with a non-method"
def merge_attrs(cls, target: Class, groups: list[list[int]]) -> list[Attr]:
    attrs = []

    for index, attr in enumerate(target.attrs):
        group = collections.find_connected_component(groups, index)

        if group == -1:
            attrs.append(attr)
            continue

        pos = collections.find(attrs, attr)
        if pos == -1:
            attr.restrictions.choice = (group * -1) - 1
            attrs.append(attr)
        else:
            existing = attrs[pos]
            assert existing.restrictions.min_occurs is not None
            assert existing.restrictions.max_occurs is not None

            existing.restrictions.min_occurs += attr.restrictions.min_occurs or 0
            if os.environ.get("XSDATA_SCHEMA") in ("nfe",) and attr.name == "IPI":
                existing.restrictions.max_occurs = min(
                    attr.restrictions.max_occurs or 0,
                    existing.restrictions.max_occurs,
                )
            else:
                existing.restrictions.max_occurs += attr.restrictions.max_occurs or 0

    return attrs


# workaround for the Brazilian NFe https://github.com/akretion/nfelib/issues/40
# another option would be to use the --compound-fields option but that would
# force us to rework a bit the spec_driven_model module logic a bit.
# see https://github.com/akretion/nfelib/issues/40
# NOTE: the original xsdata-odoo hook.py also registers an Odoo generator.
# That part is removed here because nfelib generation does not need it and it
# would add a dependency on the xsdata-odoo package.
if hasattr(UpdateAttributesEffectiveChoice, "merge_attrs"):
    # xsdata > 22.12
    merge_attrs._original_method = UpdateAttributesEffectiveChoice.merge_attrs  # type: ignore[attr-defined]
    UpdateAttributesEffectiveChoice.merge_attrs = merge_attrs
else:
    process._original_method = MergeAttributes.process  # type: ignore[attr-defined]
    MergeAttributes.process = process
