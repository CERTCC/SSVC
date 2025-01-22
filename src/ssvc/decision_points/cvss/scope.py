#!/usr/bin/env python
"""
Models CVSS Scope as an SSVC decision point.
"""

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

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_CHANGED = SsvcDecisionPointValue(
    name="Changed",
    key="C",
    description="An exploited vulnerability can affect resources beyond the authorization privileges intended by the "
    "vulnerable component. In this case the vulnerable component and the impacted component are different.",
)

_UNCHANGED = SsvcDecisionPointValue(
    name="Unchanged",
    key="U",
    description="An exploited vulnerability can only affect resources managed by the same authority. In this case the "
    "vulnerable component and the impacted component are the same.",
)

SCOPE_1 = CvssDecisionPoint(
    name="Scope",
    description="the ability for a vulnerability in one software component to impact resources beyond its means, "
    "or privileges",
    key="S",
    version="1.0.0",
    values=(
        _UNCHANGED,
        _CHANGED,
    ),
)
"""
Defines Changed and Unchanged values for CVSS Scope.
"""

versions = [
    SCOPE_1,
]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
