#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 4 as a decision point.
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

# EQ4 → SC/SI/SA with 3 levels specified in Table 27
# 0	MSI:S or MSA:S	SC:H/SI:S/SA:S
# 1	not (MSI:S or MSA:S) and (SC:H or SI:H or SA:H)	SC:H/SI:H/SA:H
# 2	not (MSI:S or MSA:S) and not (SC:H or SI:H or SA:H)	SC:L/SI:L/SA:L
TWO = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="2: not (MSI:S or MSA:S) and not (SC:H or SI:H or SA:H)",
)
ONE = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="1: not (MSI:S or MSA:S) and (SC:H or SI:H or SA:H)",
)
ZERO = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="0: MSI:S or MSA:S",
)
EQ4 = CvssDecisionPoint(
    name="Equivalence Set 4",
    key="EQ4",
    description="SC/SI/SA with 3 levels specified in Table 27",
    version="1.0.0",
    values=(
        TWO,
        ONE,
        ZERO,
    ),
)

VERSIONS = (EQ4,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
