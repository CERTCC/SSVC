#!/usr/bin/env python
#  Copyright (c) 2023-2025 Carnegie Mellon University.
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
"""
Provides tools to assist with generating documentation for SSVC decision points.

Writes the following files for each decision point:
- a json example that can be used in the decision point documentation

Examples

To generate the documentation for the decision points, use the following command:

    python -m ssvc.doctools --overwrite --datadir ./tmp/json_out`

To regenerate the existing docs, use the following command:

    python -m ssvc.doctools --overwrite --datadir data

"""
import importlib
import json
import logging
import os
import re

import ssvc.dp_groups.base
from ssvc.decision_points.base import (
    DecisionPoint,
)
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint
from ssvc.decision_tables.base import (
    DecisionTable,
    decision_table_to_longform_df,
)
from ssvc.registry import get_registry
from ssvc.registry.base import SsvcObjectRegistry, get_all
from ssvc.selection import SelectionList
from ssvc.utils.misc import order_schema

logger = logging.getLogger(__name__)


def find_modules_to_import(
    directory: str = "../decision_points",
    package: str = "ssvc.decision_points",
) -> bool:
    """
    Find all modules that contain decision points and import them.

    This is necessary to ensure that all decision points are registered.
    """
    imported_modules = []
    for root, _, files in os.walk(os.path.abspath(directory)):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                # build the module name relative to the package
                relative_path = os.path.relpath(root, directory)
                module_name = os.path.join(relative_path, file[:-3]).replace(
                    os.sep, "."
                )

                full_module_name = f"{package}.{module_name}"
                # import the module
                try:
                    logger.info(f"Importing module {full_module_name}")
                    module = importlib.import_module(full_module_name)
                    imported_modules.append(module)
                except ImportError as e:
                    logger.error(f"Failed to import {full_module_name}: {e}")
    return imported_modules


def _filename_friendly(name: str, replacement="_") -> str:
    """
    Given a string, return a version that is friendly for use in a filename.

    Args:
        name (str): The string to make friendly for use in a filename.

    Returns:
        str: A version of the string that is friendly for use in a filename.
    """
    # replace all non-alphanumeric characters with underscores and convert to lowercase
    name = re.sub(r"[^a-zA-Z0-9]", replacement, name)
    name = name.lower()
    # replace any sequence of underscores with a single underscore
    name = re.sub(rf"{replacement}+", replacement, name)

    return name


# create a runtime context that ensures that dir exists
class EnsureDirExists:
    """
    A runtime context that ensures that a directory exists or creates it otherwise.

    Example:

        with EnsureDirExists(dir):
            assert os.path.exists(dir)
    """

    def __init__(self, dir: str):
        """
        Create a new EnsureDirExists context.

        Args:
            dir (str): The directory to ensure exists.

        Returns:
            EnsureDirExists: The new EnsureDirExists context.
        """
        self.dir = dir

    def __enter__(self):
        os.makedirs(self.dir, exist_ok=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def remove_if_exists(file):
    try:
        os.remove(file)
        logger.debug(f"Removed {file}")
    except FileNotFoundError:
        logger.debug(f"File {file} does not exist, nothing to remove")


def dump_decision_point(
    jsondir: str, dp: SsvcDecisionPoint, overwrite: bool
) -> None:
    """
    Generate the markdown table, json example, and markdown table file for a decision point.

    Args:
        jsondir (str): The directory to write the json example to.
        outdir (str): The directory to write the markdown table file to.
        dp (SsvcDecisionPoint): The decision point to generate documentation for.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        dict: A dictionary with the following keys:
            - include_file: The path to the markdown table file.
            - symlink: The path to the symlink that points to the markdown table file.
            - json_file: The path to the json example file.
    """
    # make dp.name safe for use in a filename
    basename = (
        _filename_friendly(dp.name) + f"_{_filename_friendly(dp.version)}"
    )
    # - generate json example
    dump_json(basename, dp, jsondir, overwrite)


def dump_json(
    basename: str, dp: DecisionPoint, jsondir: str, overwrite: bool
) -> str:
    """
    Generate the json example for a decision point.

    Args:
        basename (str): The basename of the json example file.
        dp (SsvcDecisionPoint): The decision point to generate documentation for.
        jsondir (str): The directory to write the json example to.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        str: The path to the json example file.
    """
    # if namespace is ssvc, it goes in jsondir
    filename = f"{basename}.json"
    parts = [
        jsondir,
    ]
    parts.append(_filename_friendly(dp.namespace))
    dirname = os.path.join(*parts)

    parts.append(filename)

    json_file = os.path.join(*parts)

    if overwrite:
        remove_if_exists(json_file)
    with EnsureDirExists(dirname):
        try:
            logger.info(f"Writing {json_file}")
            with open(json_file, "x") as f:
                f.write(dp.model_dump_json(indent=2))
                f.write("\n")  # newline at end of file
        except FileExistsError:
            logger.warning(
                f"File {json_file} already exists, use --overwrite to replace"
            )
    return str(json_file)


def dump_schema(filepath: str, schema: dict) -> None:
    schema = order_schema(schema)
    logger.info(f"Writing schema to {filepath}")
    with open(filepath, "w") as f:
        json.dump(schema, f, indent=2)
        f.write("\n")


def dump_schemas(jsondir):
    import ssvc.selection
    import ssvc.decision_tables.base

    # dump the selection schema
    schemadir = os.path.abspath(os.path.join(jsondir, "..", "schema", "v2"))
    schemapaths: list[dict(str, str)] = []

    # selection schema
    schemafile = f"Decision_Point_Value_Selection-{_filename_friendly(ssvc.selection.SCHEMA_VERSION, replacement='-')}.schema.json"
    schemapath = os.path.join(schemadir, schemafile)
    selection_schema = SelectionList.model_json_schema()
    schemapaths.append({"filepath": schemapath, "schema": selection_schema})

    # registry schema
    registry_schema_file = f"Ssvc_Object_Registry-{_filename_friendly(ssvc.registry.base.SCHEMA_VERSION, replacement='-')}.schema.json"
    registry_schema_path = os.path.join(schemadir, registry_schema_file)
    registry_schema = SsvcObjectRegistry.model_json_schema()
    schemapaths.append(
        {"filepath": registry_schema_path, "schema": registry_schema}
    )

    # decision point schema
    dp_schema_file = f"Decision_Point-{_filename_friendly(ssvc.decision_points.base.SCHEMA_VERSION, replacement='-')}.schema.json"
    dp_schema_path = os.path.join(schemadir, dp_schema_file)
    dp_schema = DecisionPoint.model_json_schema()
    schemapaths.append({"filepath": dp_schema_path, "schema": dp_schema})

    # decision table schema
    decision_table_schema_file = f"Decision_Table-{_filename_friendly(ssvc.decision_tables.base.SCHEMA_VERSION, replacement='-')}.schema.json"
    decision_table_schema_path = os.path.join(
        schemadir, decision_table_schema_file
    )
    decision_table_schema = DecisionTable.model_json_schema()
    schemapaths.append(
        {
            "filepath": decision_table_schema_path,
            "schema": decision_table_schema,
        }
    )

    # decision point group schema
    dp_group_schema_file = f"Decision_Point_Group-{_filename_friendly(ssvc.dp_groups.base.SCHEMA_VERSION, replacement='-')}.schema.json"
    dp_group_schema_path = os.path.join(schemadir, dp_group_schema_file)
    dp_group_schema = (
        ssvc.dp_groups.base.DecisionPointGroup.model_json_schema()
    )
    schemapaths.append(
        {"filepath": dp_group_schema_path, "schema": dp_group_schema}
    )

    with EnsureDirExists(schemadir):
        for d in schemapaths:
            path = d["filepath"]
            schema = d["schema"]
            dump_schema(filepath=path, schema=schema)


def dump_decision_table(
    jsondir: str, dt: DecisionTable, overwrite: bool
) -> None:
    # make dp.name safe for use in a filename
    basename = (
        _filename_friendly(dt.name) + f"_{_filename_friendly(dt.version)}"
    )

    filename = f"{basename}.json"
    parts = [
        jsondir,
    ]
    parts.append(_filename_friendly(dt.namespace))
    dirname = os.path.join(*parts)

    parts.append(filename)

    json_file = os.path.join(*parts)

    if overwrite:
        remove_if_exists(json_file)
    with EnsureDirExists(dirname):
        try:
            logger.info(f"Writing {json_file}")
            with open(json_file, "x") as f:
                f.write(dt.model_dump_json(indent=2))
                f.write("\n")  # newline at end of file
        except FileExistsError:
            logger.warning(
                f"File {json_file} already exists, use --overwrite to replace"
            )


def dump_decision_table_csv(
    csvdir: str, dt: DecisionTable, overwrite: bool
) -> None:
    basename = (
        _filename_friendly(dt.name) + f"_{_filename_friendly(dt.version)}"
    )
    filename = f"{basename}.csv"
    parts = [
        csvdir,
    ]
    parts.append(_filename_friendly(dt.namespace))
    dirname = os.path.join(*parts)
    parts.append(filename)
    csv_file = os.path.join(*parts)
    if overwrite:
        remove_if_exists(csv_file)
    with EnsureDirExists(dirname):
        try:
            logger.info("Writing {csv_file}")
            with open(csv_file, "x") as f:
                df = decision_table_to_longform_df(dt=dt)
                # set the index title
                df.index.name = "row"
                f.write(df.to_csv(index=True))
        except FileExistsError:
            logger.warning(
                f"File {csv_file} already exists, use --overwrite to replace"
            )


def main():
    """Generate the json examples for decision points and decision tables.

    Emits the following files:
    - json examples for each decision point in datadir/json/decision_points/<namespace>/
    - json examples for each decision table in datadir/json/decision_tables/<namespace>/
    - csv examples for each decision table in datadir/csv/<namespace>/
    - the ssvc object registry in datadir/json/ssvc_object_registry.json
    - the json schemas for decision points, decision tables, selection lists, and the registry in datadir/schema/v2/
    """

    import argparse

    parser = argparse.ArgumentParser(
        description="Generate json, json schema, and csv examples for SSVC Decision Points and Decision Tables"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite existing files",
        default=False,
    )

    parser.add_argument(
        "--datadir", help="json output directory", default="./tmp"
    )
    args = parser.parse_args()

    overwrite = args.overwrite
    jsondir = os.path.join(os.path.abspath(args.datadir), "json")
    csvdir = os.path.join(os.path.abspath(args.datadir), "csv")

    dp_dir = os.path.join(os.path.abspath(jsondir), "decision_points")
    dt_dir = os.path.join(os.path.abspath(jsondir), "decision_tables")

    find_modules_to_import(
        "./src/ssvc/decision_points", "ssvc.decision_points"
    )
    find_modules_to_import("./src/ssvc/outcomes", "ssvc.outcomes")
    find_modules_to_import(
        "./src/ssvc/decision_tables", "ssvc.decision_tables"
    )

    registry = get_registry()

    # for each decision point:
    for dp in get_all("DecisionPoint", registry=registry):
        dump_decision_point(dp_dir, dp, overwrite)

    # for each decision table:
    for dt in get_all("DecisionTable", registry=registry):
        dump_decision_table(dt_dir, dt, overwrite)
        dump_decision_table_csv(csvdir, dt, overwrite)

    # dump the registry
    registry_json = os.path.join(jsondir, "ssvc_object_registry.json")
    if overwrite:
        remove_if_exists(registry_json)
    with EnsureDirExists(jsondir):
        try:
            logger.info(f"Writing {registry_json}")
            with open(registry_json, "x") as f:
                f.write(registry.model_dump_json(indent=2, exclude_none=True))
                f.write("\n")  # newline at end of file
        except FileExistsError:
            logger.warning(
                f"File {registry_json} already exists, use --overwrite to replace"
            )

    dump_schemas(jsondir)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if not logger.hasHandlers():
        hdlr = logging.StreamHandler()
        logger.addHandler(hdlr)

    main()
