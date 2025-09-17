#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 3 as a decision point.
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

# EQ3 → VC/VI/VA with 3 levels specified in Table 26
# Levels	Constraints	Highest Severity Vector(s)
# 0	VC:H and VI:H	VC:H/VI:H/VA:H
# 1	not (VC:H and VI:H) and (VC:H or VI:H or VA:H)	VC:L/VI:H/VA:H or VC:H/VI:L/VA:H
# 2	not (VC:H or VI:H or VA:H)	VC:L/VI:L/VA:L
TWO = DecisionPointValue(
    name="Low",
    key="L",
    definition="2: not (VC:H or VI:H or VA:H)",
)
ONE = DecisionPointValue(
    name="Medium",
    key="M",
    definition="1: not (VC:H and VI:H) and (VC:H or VI:H or VA:H)",
)
ZERO = DecisionPointValue(
    name="High",
    key="H",
    definition="0: VC:H and VI:H",
)

EQ3 = CvssDecisionPoint(
    name="Equivalence Set 3",
    key="EQ3",
    definition="VC/VI/VA with 3 levels specified in Table 26",
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
