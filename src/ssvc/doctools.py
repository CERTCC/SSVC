#!/usr/bin/env python
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University
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
import logging
import os

import ssvc.dp_groups.cvss.collections  # noqa
import ssvc.dp_groups.ssvc.collections  # noqa
from ssvc.decision_points.base import (
    REGISTERED_DECISION_POINTS,
    SsvcDecisionPoint,
)

logger = logging.getLogger(__name__)


def _filename_friendly(name: str) -> str:
    """
    Given a string, return a version that is friendly for use in a filename.

    Args:
        name (str): The string to make friendly for use in a filename.

    Returns:
        str: A version of the string that is friendly for use in a filename.
    """
    return name.lower().replace(" ", "_").replace(".", "_")


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


def dump_decision_point(jsondir: str, dp: SsvcDecisionPoint, overwrite: bool
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
    basename = _filename_friendly(dp.name) + f"_{_filename_friendly(dp.version)}"
    # - generate json example
    dump_json(basename, dp, jsondir, overwrite)


def dump_json(
    basename: str, dp: SsvcDecisionPoint, jsondir: str, overwrite: bool
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
    if dp.namespace != "ssvc":
        parts.append(_filename_friendly(dp.namespace))
    parts.append(filename)

    json_file = os.path.join(*parts)

    if overwrite:
        remove_if_exists(json_file)
    with EnsureDirExists(jsondir):
        try:
            with open(json_file, "x") as f:
                f.write(dp.model_dump_json(indent=2))
                f.write("\n")  # newline at end of file
        except FileExistsError:
            logger.warning(
                f"File {json_file} already exists, use --overwrite to replace"
            )
    return json_file


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

    # for each decision point:
    for dp in REGISTERED_DECISION_POINTS:
        dump_decision_point(jsondir, dp, overwrite)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if not logger.hasHandlers():
        hdlr = logging.StreamHandler()
        logger.addHandler(hdlr)

    main()
