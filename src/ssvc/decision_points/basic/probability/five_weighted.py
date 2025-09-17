#!/usr/bin/env python
"""
Provides a 5-level ascending probability scale decision point for SSVC
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
from ssvc.decision_points.basic.base import BasicDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

P0_30 = DecisionPointValue(
    name="Less than 30%",
    key="P0_30",
    definition="Probability < 0.3",
)
P30_55 = DecisionPointValue(
    name="30% to 55%",
    key="P30_55",
    definition="0.3 <= Probability < 0.55",
)
P55_75 = DecisionPointValue(
    name="55% to 75%",
    key="P55_75",
    definition="0.55 <= Probability < 0.75",
)
P75_90 = DecisionPointValue(
    name="75% to 90%",
    key="P75_90",
    definition="0.75 <= Probability < 0.9",
)
P90_100 = DecisionPointValue(
    name="Greater than 90%",
    key="P90_100",
    definition="0.9 <= Probability <= 1.0",
)

P5W = BasicDecisionPoint(
    key="P_5W",
    version="1.0.0",
    name="Probability Scale in 5 weighted levels, ascending",
    definition="A probability scale with higher resolution as probability increases",
    values=(
        P0_30,
        P30_55,
        P55_75,
        P75_90,
        P90_100,
    ),
)

VERSIONS = [P5W]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
