#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 2 as a decision point.
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

from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

# EQ2 → AC/AT with 2 levels specified in Table 25
# Levels	Constraints	Highest Severity Vector(s)
# 0	AC:L and AT:N	AC:L/AT:N
# 1	not (AC:L and AT:N)	AC:L/AT:P or AC:H/AT:N
ONE = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="1: not (AC:L and AT:N)",
)
ZERO = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="0: AC:L and AT:N",
)

EQ2 = CvssDecisionPoint(
    name="Equivalence Set 2",
    key="EQ2",
    description="AC/AT with 2 levels specified in Table 25",
    version="1.0.0",
    values=(
        ONE,
        ZERO,
    ),
)

VERSIONS = (EQ2,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
