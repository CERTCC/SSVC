#!/usr/bin/env python

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
"""
Provides the Value/Complexity outcome group for the `x_basic` namespace.
"""

from ssvc.decision_points.base import (
    DecisionPoint,
    DecisionPointValue as DecisionPointValue,
)
from ssvc.decision_points.helpers import print_versions_and_diffs

_DROP = DecisionPointValue(name="Drop", key="D", description="Drop")

_RECONSIDER = DecisionPointValue(
    name="Reconsider Later", key="R", description="Reconsider Later"
)

_EASY_WIN = DecisionPointValue(name="Easy Win", key="E", description="Easy Win")

_DO_FIRST = DecisionPointValue(name="Do First", key="F", description="Do First")

VALUE_COMPLEXITY = DecisionPoint(
    name="Value, Complexity",
    key="VALUE_COMPLEXITY",
    description="The Value/Complexity outcome group.",
    version="1.0.0",
    namespace="x_basic",
    values=(
        _DROP,
        _RECONSIDER,
        _EASY_WIN,
        _DO_FIRST,
    ),
)
"""
The Value/Complexity outcome group.
"""

VERSIONS = (VALUE_COMPLEXITY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
