#!/usr/bin/env python
"""
Provides median-based decision points for SSVC
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

BELOW = DecisionPointValue(
    name="Below Median",
    key="B",
    definition="Quantile < 0.50. The lower half of the range of possible values.",
)
ABOVE = DecisionPointValue(
    name="Above Median",
    key="A",
    definition="0.50 <= Quantile <= 1.0. The upper half of the range of possible values.",
)


MEDIAN = BasicDecisionPoint(
    name="Median Split",
    definition="A median split divides a distribution into two equal parts, with 50% of the values falling below the median and 50% above it.",
    key="MEDIAN",
    version="1.0.0",
    values=(
        BELOW,
        ABOVE,
    ),
)

VERSIONS = [MEDIAN]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)
    pass


if __name__ == "__main__":
    main()
