#!/usr/bin/env python
"""
Provides a 2-level ascending probability scale decision point for SSVC
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

P0_50 = DecisionPointValue(
    name="Less than 50%",
    key="LT50",
    definition="0.0 <= Probability < 0.5",
)
P50_100 = DecisionPointValue(
    name="Greater than 50%",
    key="GT50",
    definition="0.5 <= Probability <= 1.0",
)

P2A = BasicDecisionPoint(
    key="P_2A",
    version="1.0.0",
    name="Probability Scale in 2 equal levels, ascending",
    definition="A probability scale that divides between less than 50% and greater than or equal to 50%",
    values=(
        P0_50,
        P50_100,
    ),
)

VERSIONS = [P2A]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
