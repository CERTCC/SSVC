#!/usr/bin/env python
"""
Provides a boolean decision point that can be used to indicate if another value is near a boundary condition.
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

JUST_BELOW_BOUNDARY = DecisionPointValue(
    name="Just Below Boundary",
    key="JB",
    definition="The value is just below a boundary condition",
)
JUST_ABOVE_BOUNDARY = DecisionPointValue(
    name="Just Above Boundary",
    key="JA",
    definition="The value is just above a boundary condition",
)

NOT_NEAR_BOUNDARY = DecisionPointValue(
    name="Not Near Boundary",
    key="NN",
    definition="The value is not near a boundary condition",
)
BOUNDARY_PROXIMITY = BasicDecisionPoint(
    name="Boundary Proximity",
    key="BP",
    definition="Indicates whether another value is near a boundary condition, indicating that special consideration may be needed.",
    version="1.0.0",
    values=(
        NOT_NEAR_BOUNDARY,
        JUST_ABOVE_BOUNDARY,
        JUST_BELOW_BOUNDARY,
    ),
)

VERSIONS = (BOUNDARY_PROXIMITY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
