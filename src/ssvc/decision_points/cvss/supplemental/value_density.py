#!/usr/bin/env python
"""
Provides the CVSS supplemental metric Value Density
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
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
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

DIFFUSE = DecisionPointValue(
    name="Diffuse",
    key="D",
    definition="The vulnerable system has limited resources. That is, the resources that the attacker will "
    "gain control over with a single exploitation event are relatively small.",
)
CONCENTRATED = DecisionPointValue(
    name="Concentrated",
    key="C",
    definition="The vulnerable system is rich in resources. Heuristically, such systems are often the direct "
    'responsibility of "system operators" rather than users.',
)
VALUE_DENSITY_1 = CvssDecisionPoint(
    name="Value Density",
    definition="Value Density describes the resources that the attacker will gain control over with a single "
    "exploitation event. It has two possible values, diffuse and concentrated.",
    key="V",
    version="1.0.0",
    values=(
        NOT_DEFINED_X,
        DIFFUSE,
        CONCENTRATED,
    ),
)

VERSIONS = (VALUE_DENSITY_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
