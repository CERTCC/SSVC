#!/usr/bin/env python
"""
file: doc_helpers
author: adh
created_at: 2/14/25 2:54 PM
"""
#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
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

from ssvc.decision_points.base import SsvcDecisionPoint

MD_TABLE_ROW_TEMPLATE = "| {value.name} | {value.description} |"


def markdown_table(dp: SsvcDecisionPoint, indent: int = 0) -> str:
    """
    Generate a markdown table for a decision point.

    Args:
        dp (SsvcDecisionPoint): The decision point to generate a markdown table for.

    Returns:
        str: The markdown table.
    """
    rows = []
    # prepend the header
    _indent = " " * indent
    rows.append(f"{_indent}{dp.description}")
    rows.append("")
    rows.append(f"{_indent}| Value | Definition |")
    rows.append(f"{_indent}|:-----|:-----------|")

    # add a row for each value
    for value in dp.values:
        rows.append(_indent + MD_TABLE_ROW_TEMPLATE.format(value=value))

    return "\n".join(rows)


def example_block_tabbed(dp: SsvcDecisionPoint, indent=4) -> str:
    """Given a decision point, return a markdown block that contains an example of the decision point."""

    indent_ = " " * 4
    rows = []
    rows.append(f'!!! note "{dp.name} v{dp.version}"')
    rows.append("")

    rows.append(indent_ + '=== "Table"')
    rows.append("")
    for row in markdown_table(dp, indent=4).splitlines():
        rows.append(indent_ + row)
    rows.append("")

    rows.append(indent_ + '=== "JSON"')
    rows.append("")
    for row in json_example(dp, indent=4).splitlines():
        rows.append(indent_ + row)

    return "\n".join(rows)


def example_block(dp: SsvcDecisionPoint, indent=4) -> str:
    """Given a decision point, return a markdown block that contains an example of the decision point."""

    indent_ = " " * 4
    rows = []
    rows.append(f'!!! note "{dp.name} v{dp.version}"')
    rows.append("")

    for row in markdown_table(dp).splitlines():
        rows.append(indent_ + row)
    rows.append("")

    rows.append(indent_ + f'??? example "{dp.name} v{dp.version} JSON Example"')
    rows.append("")
    for row in json_example(dp, indent=4).splitlines():
        rows.append(indent_ + row)

    return "\n".join(rows)


def prior_version(dp: SsvcDecisionPoint, indent=4) -> str:
    """Given a decision point, return a markdown block that contains an example of the decision point."""

    indent_ = " " * 4
    rows = []
    rows.append(f'!!! note "{dp.name} v{dp.version}"')
    rows.append("")

    rows.append("")
    for row in markdown_table(dp, indent=0).splitlines():
        rows.append(indent_ + row)

    return "\n".join(rows)


def json_example(dp, indent=0):
    """
    Generate a markdown block that contains a JSON example.

    Args:
        dp: the decision point object
        jstr:
        collapsible:

    Returns:

    """
    indent_ = " " * indent
    json_rows = [
        indent_ + "```json",
    ]

    jstr = dp.model_dump_json(indent=2).strip()

    for line in jstr.splitlines():
        json_rows.append(indent_ + line)

    json_rows.append(
        indent_ + "```",
    )
    json_block = "\n".join(json_rows)
    return json_block


def main():
    pass


if __name__ == "__main__":
    main()
