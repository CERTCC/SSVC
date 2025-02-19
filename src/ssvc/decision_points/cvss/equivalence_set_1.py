#!/usr/bin/env python
"""
Provides an object representing the CVSS Equivalence Set 1 as a decision point.
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

TWO = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="2: AV:P or not(AV:N or PR:N or UI:N)",
)

ONE = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="1: (AV:N or PR:N or UI:N) and not (AV:N and PR:N and UI:N) and not AV:P",
)

ZERO = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="0: AV:N and PR:N and UI:N",
)

# EQ1 → AV/PR/UI with 3 levels specified in Table 24
# Levels	Constraints	Highest Severity Vector(s)
# 0	AV:N and PR:N and UI:N	AV:N/PR:N/UI:N
# 1	(AV:N or PR:N or UI:N) and not (AV:N and PR:N and UI:N) and not AV:P	AV:A/PR:N/UI:N or AV:N/PR:L/UI:N or AV:N/PR:N:/UI:P
# 2	AV:P or not(AV:N or PR:N or UI:N)	AV:P/PR:N/UI:N or AV:A/PR:L/UI:P
EQ1 = CvssDecisionPoint(
    name="Equivalence Set 1",
    key="EQ1",
    description="AV/PR/UI with 3 levels specified in Table 24",
    version="1.0.0",
    values=(
        TWO,
        ONE,
        ZERO,
    ),
)

VERSIONS = (EQ1,)
LATEST = EQ1


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
