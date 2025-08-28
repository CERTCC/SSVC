#!/usr/bin/env python
"""
Provides quintile-based decision points for SSVC
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

FIRST_QUINTILE = DecisionPointValue(
    name="First Quintile",
    key="Q1",
    definition="Quantile < 0.20. The lowest 20% of the range of possible values.",
)
SECOND_QUINTILE = DecisionPointValue(
    name="Second Quintile",
    key="Q2",
    definition="0.20 <= Quantile < 0.40. The second lowest 20% of the range of possible values.",
)
THIRD_QUINTILE = DecisionPointValue(
    name="Third Quintile",
    key="Q3",
    definition="0.40 <= Quantile < 0.60. The middle 20% of the range of possible values.",
)
FOURTH_QUINTILE = DecisionPointValue(
    name="Fourth Quintile",
    key="Q4",
    definition="0.60 <= Quantile < 0.80. The second highest 20% of the range of possible values.",
)
FIFTH_QUINTILE = DecisionPointValue(
    name="Fifth Quintile",
    key="Q5",
    definition="0.80 <= Quantile <= 1.0. The highest 20% of the range of possible values.",
)

QUINTILES = BasicDecisionPoint(
    name="Quintiles",
    definition="A quintile is one of five equal groups that a population can be divided into according to the distribution of values of a particular variable.",
    key="QUINTILES",
    version="1.0.0",
    values=(
        FIRST_QUINTILE,
        SECOND_QUINTILE,
        THIRD_QUINTILE,
        FOURTH_QUINTILE,
        FIFTH_QUINTILE,
    ),
)

VERSIONS = [QUINTILES]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)
    pass


if __name__ == "__main__":
    main()
