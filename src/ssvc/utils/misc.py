#!/usr/bin/env python
"""
Provides miscellaneous utility functions for SSVC.
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

import re
import secrets

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


def obfuscate_dict(data: dict) -> tuple[dict, dict]:
    """Given a dictionary, obfuscate its keys by replacing them with random strings.
    Returns a tuple of two dictionaries: the obfuscated dictionary and the mapping
    of original keys to obfuscated keys.

    Args:
        data (dict): The dictionary to obfuscate.
    Returns:
        tuple[dict, dict]: A tuple containing the obfuscated dictionary and a translator
            dictionary mapping original keys to obfuscated keys.
    """
    token_len = 4
    obfuscated_dict = {}
    translator = {}

    def _generate_key() -> str:
        k = secrets.token_hex(token_len)
        # make the new key match NNNN-NNNN...
        k = "-".join(k[i : i + token_len] for i in range(0, len(k), token_len))
        # uppercase the new key
        k = k.upper()
        return k

    for old_key in data.keys():
        while True:
            new_key = _generate_key()
            if new_key not in translator:
                break

        # got a unique new_key
        translator[old_key] = new_key
        obfuscated_dict[new_key] = data[old_key]

    return (obfuscated_dict, translator)


def filename_friendly(name: str, replacement="_", to_lower=True) -> str:
    """
    Given a string, return a version that is friendly for use in a filename.

    Args:
        name (str): The string to make friendly for use in a filename.

    Returns:
        str: A version of the string that is friendly for use in a filename.
    """
    # replace all non-alphanumeric characters with underscores
    name = re.sub(r"[^a-zA-Z0-9]", replacement, name)

    # and (optionally) convert to lowercase
    if to_lower:
        name = name.lower()

    # replace any sequence of underscores with a single underscore
    name = re.sub(rf"{re.escape(replacement)}+", replacement, name)

    return name
