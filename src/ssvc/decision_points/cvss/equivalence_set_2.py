#!/usr/bin/env python
"""
This module provides an object representing the CVSS Equivalence Set 2 as a decision point.
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

# EQ2 → AC/AT with 2 levels specified in Table 25
# Levels	Constraints	Highest Severity Vector(s)
# 0	AC:L and AT:N	AC:L/AT:N
# 1	not (AC:L and AT:N)	AC:L/AT:P or AC:H/AT:N
ONE = DecisionPointValue(
    name="Low",
    key="L",
    definition="1: not (AC:L and AT:N)",
)
ZERO = DecisionPointValue(
    name="High",
    key="H",
    definition="0: AC:L and AT:N",
)

EQ2 = CvssDecisionPoint(
    name="Equivalence Set 2",
    key="EQ2",
    definition="AC/AT with 2 levels specified in Table 25",
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
