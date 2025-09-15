#!/usr/bin/env python
"""
file: doc_helpers
author: adh
created_at: 2/14/25 2:54 PM
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

from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

MD_TABLE_ROW_TEMPLATE = "| {value.name} ({value.key}) | {value.definition} |"


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
    rows.append(f"{_indent}{dp.definition}")
    rows.append("")
    rows.append(f"{_indent}| Value | Definition |")
    rows.append(f"{_indent}|:-----|:-----------|")

    # add a row for each value
    for value in dp.values:
        rows.append(_indent + MD_TABLE_ROW_TEMPLATE.format(value=value))

    return "\n".join(rows)


def example_block_tabbed(dp: SsvcDecisionPoint, indent=4) -> str:
    """Given a decision point, return a markdown block that contains an example of the decision point."""

    dp_title_str = f"{dp.name} ({dp.id})"

    indent_ = " " * 4
    rows = []
    rows.append(f'!!! note "{dp_title_str}"')
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


def example_block(
    dp: SsvcDecisionPoint, indent: int = 4, include_json: bool = True
) -> str:
    """Given a decision point, return a markdown block that contains an example of the decision point."""

    dp_title_str = f"{dp.name} ({dp.id})"

    indent_ = " " * indent
    rows = []
    rows.append(f'!!! note "{dp_title_str}"')
    rows.append("")

    for row in markdown_table(dp).splitlines():
        rows.append(indent_ + row)
    rows.append("")

    if include_json:
        rows.append(indent_ + f'??? example "{dp_title_str} JSON Example"')
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
