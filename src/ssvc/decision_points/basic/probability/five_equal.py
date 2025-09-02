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

P0_20 = DecisionPointValue(
    name="Less than 20%",
    key="P0_20",
    definition="Probability < 0.2",
)
P20_40 = DecisionPointValue(
    name="20% to 40%",
    key="P20_40",
    definition="0.2 <= Probability < 0.4",
)
P40_60 = DecisionPointValue(
    name="40% to 60%",
    key="P40_60",
    definition="0.4 <= Probability < 0.6",
)
P60_80 = DecisionPointValue(
    name="60% to 80%",
    key="P60_80",
    definition="0.6 <= Probability < 0.8",
)
P80_100 = DecisionPointValue(
    name="Greater than 80%",
    key="P80_100",
    definition="0.8 <= Probability <= 1.0",
)

P5A = BasicDecisionPoint(
    key="P_5A",
    version="1.0.0",
    name="Probability Scale in 5 equal levels, ascending",
    definition="A probability scale with 20% increments",
    values=(
        P0_20,
        P20_40,
        P40_60,
        P60_80,
        P80_100,
    ),
)

VERSIONS = [P5A]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
