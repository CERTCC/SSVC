#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 5 as a decision point.
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

# EQ5 → E with 3 levels specified in Table 28
# 0	E:A	E:A
# 1	E:P	E:P
# 2	E:U	E:U
TWO = SsvcDecisionPointValue(name="Low", key="L", description="2: E:U", )
ONE = SsvcDecisionPointValue(name="Medium", key="M", description="1: E:P", )
ZERO = SsvcDecisionPointValue(name="High", key="H", description="0: E:A", )
EQ5 = CvssDecisionPoint(
    name="Equivalence Set 5",
    key="EQ5",
    description="E with 3 levels specified in Table 28",
    version="1.0.0",
    values=(
        TWO,
        ONE,
        ZERO,
),
)


VERSIONS = (EQ5,)
LATEST = VERSIONS[-1]

def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == '__main__':
    main()
