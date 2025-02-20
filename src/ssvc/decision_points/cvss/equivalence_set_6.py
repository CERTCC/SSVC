#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 6 as a decision point.
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

# EQ6 → VC/VI/VA+CR/CI/CA with 2 levels specified in Table 29
# 0	(CR:H and VC:H) or (IR:H and VI:H) or (AR:H and VA:H)	VC:H/VI:H/VA:H/CR:H/IR:H/AR:H
# 1	not (CR:H and VC:H) and not (IR:H and VI:H) and not (AR:H and VA:H)	VC:H/VI:H/VA:H/CR:M/IR:M/AR:M or VC:H/VI:H/VA:L/CR:M/IR:M/AR:H or VC:H/VI:L/VA:H/CR:M/IR:H/AR:M or VC:H/VI:L/VA:L/CR:M/IR:H/AR:H or VC:L/VI:H/VA:H/CR:H/IR:M/AR:M or VC:L/VI:H/VA:L/CR:H/IR:M/AR:H or VC:L/VI:L/VA:H/CR:H/IR:H/AR:M or VC:L/VI:L/VA:L/CR:H/IR:H/AR:H
ONE = SsvcDecisionPointValue(name="Low", key="L",
                             description="1: not (CR:H and VC:H) and not (IR:H and VI:H) and not (AR:H and VA:H)", )
ZERO = SsvcDecisionPointValue(name="High", key="H",
                              description="0: (CR:H and VC:H) or (IR:H and VI:H) or (AR:H and VA:H)", )
EQ6 = CvssDecisionPoint(
    name="Equivalence Set 6",
    key="EQ6",
    description="VC/VI/VA+CR/CI/CA with 2 levels specified in Table 29",
    version="1.0.0",
    values=(
        ONE,
        ZERO,
    ),
)

VERSIONS = (EQ6,)
LATEST = VERSIONS[-1]

def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == '__main__':
    main()

