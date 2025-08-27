#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 4 as a decision point.
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

# EQ4 → SC/SI/SA with 3 levels specified in Table 27
# 0	MSI:S or MSA:S	SC:H/SI:S/SA:S
# 1	not (MSI:S or MSA:S) and (SC:H or SI:H or SA:H)	SC:H/SI:H/SA:H
# 2	not (MSI:S or MSA:S) and not (SC:H or SI:H or SA:H)	SC:L/SI:L/SA:L
TWO = DecisionPointValue(
    name="Low",
    key="L",
    definition="2: not (MSI:S or MSA:S) and not (SC:H or SI:H or SA:H)",
)
ONE = DecisionPointValue(
    name="Medium",
    key="M",
    definition="1: not (MSI:S or MSA:S) and (SC:H or SI:H or SA:H)",
)
ZERO = DecisionPointValue(
    name="High",
    key="H",
    definition="0: MSI:S or MSA:S",
)
EQ4 = CvssDecisionPoint(
    name="Equivalence Set 4",
    key="EQ4",
    definition="SC/SI/SA with 3 levels specified in Table 27",
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
