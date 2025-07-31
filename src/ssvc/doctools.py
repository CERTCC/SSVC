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

    python -m ssvc.doctools --overwrite --jsondir ./tmp/json_out`

To regenerate the existing docs, use the following command:

    python -m ssvc.doctools --overwrite --jsondir data/json/decision_points

"""
import importlib
import json
import logging
import os
import re

from ssvc.decision_points.base import (
    DecisionPoint,
    REGISTERED_DECISION_POINTS,
)
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint
from ssvc.selection import SelectionList

logger = logging.getLogger(__name__)


def find_modules_to_import(
    directory: str = "../decision_points", package: str = "ssvc.decision_points"
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


def _filename_friendly(name: str) -> str:
    """
    Given a string, return a version that is friendly for use in a filename.

    Args:
        name (str): The string to make friendly for use in a filename.

    Returns:
        str: A version of the string that is friendly for use in a filename.
    """
    # replace all non-alphanumeric characters with underscores and convert to lowercase
    name = re.sub(r"[^a-zA-Z0-9]", "_", name)
    name = name.lower()
    # replace any sequence of underscores with a single underscore
    name = re.sub(r"_+", "_", name)

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


def dump_decision_point(jsondir: str, dp: SsvcDecisionPoint, overwrite: bool) -> None:
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
    basename = _filename_friendly(dp.name) + f"_{_filename_friendly(dp.version)}"
    # - generate json example
    dump_json(basename, dp, jsondir, overwrite)


def dump_json(basename: str, dp: DecisionPoint, jsondir: str, overwrite: bool) -> str:
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


def dump_selection_schema(filepath: str) -> None:
    """
    Dump the schema for the SelectionList model to a file.
    Args:
        filepath: The path to the file to write the schema to.

    Returns:
        None

    """
    logger.info(f"Dumping schema to {filepath}")
    schema = SelectionList.model_json_schema()
    with open(filepath, "w") as f:
        json.dump(schema, f, indent=2)
        f.write("\n")  # newline at end of file


def main():
    # we are going to generate three files for each decision point:
    # - a markdown table that can be used in the decision point documentation
    # - a json example that can be used in the decision point documentation
    # - a markdown file that builds an mkdocs table to switch between the markdown description and the json
    #   example using markdown-include plugin of mkdocs

    # parse command line args
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate decision point documentation"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite existing files",
        default=False,
    )

    parser.add_argument(
        "--jsondir", help="json output directory", default="./tmp/json_out"
    )
    args = parser.parse_args()

    overwrite = args.overwrite
    jsondir = args.jsondir

    dp_dir = os.path.join(os.path.abspath(jsondir), "decision_points")

    find_modules_to_import("./src/ssvc/decision_points", "ssvc.decision_points")
    find_modules_to_import("./src/ssvc/outcomes", "ssvc.outcomes")

    # import collections to ensure they are registered too
    import ssvc.dp_groups.ssvc.collections  # noqa: F401
    import ssvc.dp_groups.cvss.collections  # noqa: F401

    # for each decision point:
    for dp in REGISTERED_DECISION_POINTS:
        dump_decision_point(dp_dir, dp, overwrite)

    # dump the selection schema
    schemadir = os.path.abspath(os.path.join(jsondir, "..", "schema", "v2"))
    schemafile = os.path.join(
        schemadir, "Decision_Point_Value_Selection-2-0-0.schema.json"
    )
    dump_selection_schema(schemafile)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if not logger.hasHandlers():
        hdlr = logging.StreamHandler()
        logger.addHandler(hdlr)

    main()
