#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 3 as a decision point.
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

# EQ3 → VC/VI/VA with 3 levels specified in Table 26
# Levels	Constraints	Highest Severity Vector(s)
# 0	VC:H and VI:H	VC:H/VI:H/VA:H
# 1	not (VC:H and VI:H) and (VC:H or VI:H or VA:H)	VC:L/VI:H/VA:H or VC:H/VI:L/VA:H
# 2	not (VC:H or VI:H or VA:H)	VC:L/VI:L/VA:L
TWO = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="2: not (VC:H or VI:H or VA:H)",
)
ONE = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="1: not (VC:H and VI:H) and (VC:H or VI:H or VA:H)",
)
ZERO = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="0: VC:H and VI:H",
)

EQ3 = CvssDecisionPoint(
    name="Equivalence Set 3",
    key="EQ3",
    description="VC/VI/VA with 3 levels specified in Table 26",
    version="1.0.0",
    values=(
        TWO,
        ONE,
        ZERO,
    ),
)


VERSIONS = (EQ3,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
