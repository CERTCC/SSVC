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
Provides the Eisenhower outcome group for the `x_basic` namespace.
"""

from ssvc.decision_points.base import (
    DecisionPoint,
    DecisionPointValue as DecisionPointValue,
)
from ssvc.decision_points.helpers import print_versions_and_diffs

_DELETE = DecisionPointValue(name="Delete", key="D", description="Delete")

_DELEGATE = DecisionPointValue(name="Delegate", key="G", description="Delegate")

_SCHEDULE = DecisionPointValue(name="Schedule", key="S", description="Schedule")

_DO = DecisionPointValue(name="Do", key="O", description="Do")

EISENHOWER = DecisionPoint(
    name="Do, Schedule, Delegate, Delete",
    key="IKE",
    description="The Eisenhower outcome group.",
    namespace="x_basic",
    version="1.0.0",
    values=(
        _DELETE,
        _DELEGATE,
        _SCHEDULE,
        _DO,
    ),
)
"""
The Eisenhower outcome group.
"""

VERSIONS = (EISENHOWER,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
