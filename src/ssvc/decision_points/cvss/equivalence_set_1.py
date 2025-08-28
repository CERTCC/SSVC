#!/usr/bin/env python
"""
Provides an object representing the CVSS Equivalence Set 1 as a decision point.
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

TWO = DecisionPointValue(
    name="Low",
    key="L",
    definition="2: AV:P or not(AV:N or PR:N or UI:N)",
)

ONE = DecisionPointValue(
    name="Medium",
    key="M",
    definition="1: (AV:N or PR:N or UI:N) and not (AV:N and PR:N and UI:N) and not AV:P",
)

ZERO = DecisionPointValue(
    name="High",
    key="H",
    definition="0: AV:N and PR:N and UI:N",
)

# EQ1 → AV/PR/UI with 3 levels specified in Table 24
# Levels	Constraints	Highest Severity Vector(s)
# 0	AV:N and PR:N and UI:N	AV:N/PR:N/UI:N
# 1	(AV:N or PR:N or UI:N) and not (AV:N and PR:N and UI:N) and not AV:P	AV:A/PR:N/UI:N or AV:N/PR:L/UI:N or AV:N/PR:N:/UI:P
# 2	AV:P or not(AV:N or PR:N or UI:N)	AV:P/PR:N/UI:N or AV:A/PR:L/UI:P
EQ1 = CvssDecisionPoint(
    name="Equivalence Set 1",
    key="EQ1",
    definition="AV/PR/UI with 3 levels specified in Table 24",
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
