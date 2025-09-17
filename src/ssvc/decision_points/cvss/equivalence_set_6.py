#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 6 as a decision point.
"""
#  Copyright (c) 2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

# EQ6 → VC/VI/VA+CR/CI/CA with 2 levels specified in Table 29
# 0	(CR:H and VC:H) or (IR:H and VI:H) or (AR:H and VA:H)	VC:H/VI:H/VA:H/CR:H/IR:H/AR:H
# 1	not (CR:H and VC:H) and not (IR:H and VI:H) and not (AR:H and VA:H)	VC:H/VI:H/VA:H/CR:M/IR:M/AR:M or VC:H/VI:H/VA:L/CR:M/IR:M/AR:H or VC:H/VI:L/VA:H/CR:M/IR:H/AR:M or VC:H/VI:L/VA:L/CR:M/IR:H/AR:H or VC:L/VI:H/VA:H/CR:H/IR:M/AR:M or VC:L/VI:H/VA:L/CR:H/IR:M/AR:H or VC:L/VI:L/VA:H/CR:H/IR:H/AR:M or VC:L/VI:L/VA:L/CR:H/IR:H/AR:H
ONE = DecisionPointValue(
    name="Low",
    key="L",
    definition="1: not (CR:H and VC:H) and not (IR:H and VI:H) and not (AR:H and VA:H)",
)
ZERO = DecisionPointValue(
    name="High",
    key="H",
    definition="0: (CR:H and VC:H) or (IR:H and VI:H) or (AR:H and VA:H)",
)
EQ6 = CvssDecisionPoint(
    name="Equivalence Set 6",
    key="EQ6",
    definition="VC/VI/VA+CR/CI/CA with 2 levels specified in Table 29",
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


if __name__ == "__main__":
    main()
