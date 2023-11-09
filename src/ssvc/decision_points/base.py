#!/usr/bin/env python
"""
file: decisionpoints
author: adh
created_at: 9/20/23 10:07 AM
"""
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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

import logging
from dataclasses import dataclass
from typing import Iterable

from dataclasses_json import dataclass_json

from ssvc._mixins import _Base, _Commented, _Keyed, _Namespaced, _Versioned

logger = logging.getLogger(__name__)


REGISTERED_DECISION_POINTS = []


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPointValue(_Base, _Keyed):
    """
    Models a single value option for a decision point.
    """

    pass


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPoint(
    _Base,
    _Keyed,
    _Versioned,
    _Namespaced,
    _Commented,
):
    """
    Models a single decision point as a list of values.
    """

    values: Iterable[SsvcDecisionPointValue] = ()

    def __iter__(self):
        """
        Allow iteration over the decision points in the group.
        """
        return iter(self.values)

    def __post_init__(self):
        global REGISTERED_DECISION_POINTS

        REGISTERED_DECISION_POINTS.append(self)


def dp_to_table(dp: SsvcDecisionPoint) -> str:
    """
    Convert a decision point to a markdown table.
    :param dp: The decision point to convert.
    :return: a string containing the markdown table.
    """
    rows = []
    rows.append(f"{dp.description}")
    rows.append("")

    headings = ["Value", "Key", "Description"]

    def make_row(items):
        return "| " + " | ".join(items) + " |"

    rows.append(make_row(headings))
    rows.append(make_row(["---" for _ in headings]))

    for value in dp.values:
        rows.append(make_row([value.name, value.key, value.description]))

    return "\n".join(rows)


def main():
    opt_none = SsvcDecisionPointValue(
        name="None", key="N", description="No exploit available"
    )
    opt_poc = SsvcDecisionPointValue(
        name="PoC", key="P", description="Proof of concept exploit available"
    )
    opt_active = SsvcDecisionPointValue(
        name="Active", key="A", description="Active exploitation observed"
    )
    opts = [opt_none, opt_poc, opt_active]

    dp = SsvcDecisionPoint(
        _comment="This is an optional comment that will be included in the object.",
        values=opts,
        name="Exploitation",
        description="Is there an exploit available?",
        key="E",
        version="1.0.0",
    )

    print(dp.to_json(indent=2))


if __name__ == "__main__":
    main()
