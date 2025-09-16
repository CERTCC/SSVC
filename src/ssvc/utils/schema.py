#!/usr/bin/env python
"""
Utility functions for SSVC json schema handling.
"""

#  Copyright (c) 2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from typing import Any

#  Copyright (c) 2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278
from ssvc.utils.defaults import SCHEMA_ORDER


def reorder_title_first(obj):
    if isinstance(obj, dict):
        if "title" in obj:
            reordered = {"title": obj["title"]}
            for k, v in obj.items():
                if k != "title":
                    reordered[k] = reorder_title_first(v)
            return reordered
        else:
            return {k: reorder_title_first(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [reorder_title_first(item) for item in obj]
    else:
        return obj


def order_schema(schema: dict) -> dict:
    # create a new dict with the preferred order of fields first
    ordered_schema = {k: schema[k] for k in (SCHEMA_ORDER) if k in schema}

    # add the rest of the fields in their original order
    other_keys = [k for k in schema if k not in ordered_schema]
    for k in other_keys:
        ordered_schema[k] = schema[k]

    # recursively move "title" to the front of any nested objects
    ordered_schema = reorder_title_first(ordered_schema)

    return ordered_schema


def strip_nullable_anyof(schema: dict) -> dict:
    """Recursively rewrite schema to drop `anyOf` [string, null] constructs."""
    if isinstance(schema, dict):
        # If schema has "anyOf"
        if "anyOf" in schema:
            anyof: list[dict[str, Any]] = schema["anyOf"]
            string_schema = None
            has_null = False

            for option in anyof:
                if option.get("type") == "string":
                    string_schema = option
                elif option.get("type") == "null":
                    has_null = True

            # Replace with string schema if this was the pattern
            if string_schema and has_null and len(anyof) == 2:
                # Preserve the title if it was in the parent
                title = schema.get("title")
                schema = dict(string_schema)  # copy
                if title:
                    schema["title"] = title
                # Drop any default:null
                schema.pop("default", None)

        # Recurse into nested dicts/lists
        for key, value in list(schema.items()):
            schema[key] = strip_nullable_anyof(value)

    elif isinstance(schema, list):
        return [strip_nullable_anyof(item) for item in schema]

    return schema
