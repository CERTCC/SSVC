#!/usr/bin/env python
"""
Provides quartile-based decision points for SSVC
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

FIRST_QUARTILE = DecisionPointValue(
    name="First Quartile",
    key="Q1",
    definition="Quantile < 0.25. The lowest 25% of the range of possible values.",
)
SECOND_QUARTILE = DecisionPointValue(
    name="Second Quartile",
    key="Q2",
    definition="0.25 <= Quantile < 0.50. The second lowest 25% of the range of possible values.",
)
THIRD_QUARTILE = DecisionPointValue(
    name="Third Quartile",
    key="Q3",
    definition="0.50 <= Quantile < 0.75. The second highest 25% of the range of possible values.",
)
FOURTH_QUARTILE = DecisionPointValue(
    name="Fourth Quartile",
    key="Q4",
    definition="0.75 <= Quantile <= 1.0. The highest 25% of the range of possible values.",
)

QUARTILES = BasicDecisionPoint(
    name="Quartiles",
    definition="A quartile is one of four equal groups that a population can be divided into according to the distribution of values of a particular variable.",
    key="QUARTILES",
    version="1.0.0",
    values=(
        FIRST_QUARTILE,
        SECOND_QUARTILE,
        THIRD_QUARTILE,
        FOURTH_QUARTILE,
    ),
)

VERSIONS = [QUARTILES]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)
    pass


if __name__ == "__main__":
    main()
