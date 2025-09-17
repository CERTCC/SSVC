#!/usr/bin/env python
"""
Models CVSS Target Distribution as an SSVC decision point.
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


_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="Targets exist inside the environment on a considerable scale. Between 50% - 100% of the total "
    "environment is considered at risk.",
)

_MEDIUM = DecisionPointValue(
    name="Medium",
    key="M",
    definition="Targets exist inside the environment, but on a medium scale. Between 16% - 49% of the total "
    "environment is at risk.",
)

_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="Targets exist inside the environment, but on a small scale. Between 1% - 15% of the total "
    "environment is at risk.",
)

_TD_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="No target systems exist, or targets are so highly specialized that they only exist in a laboratory "
    "setting. Effectively 0% of the environment is at risk.",
)

TARGET_DISTRIBUTION_1 = CvssDecisionPoint(
    name="Target Distribution",
    definition="This metric measures the relative size of the field of target systems susceptible to the "
    "vulnerability. It is meant as an environment-specific indicator in order to approximate the "
    "percentage of systems within the environment that could be affected by the vulnerability.",
    key="TD",
    version="1.0.0",
    values=(
        _TD_NONE,
        _LOW,
        _MEDIUM,
        _HIGH,
    ),
)
"""
Defines None, Low, Medium, and High values for CVSS Target Distribution.
"""

TARGET_DISTRIBUTION_1_1 = CvssDecisionPoint(
    name="Target Distribution",
    definition="This metric measures the relative size of the field of target systems susceptible to the "
    "vulnerability. It is meant as an environment-specific indicator in order to approximate the "
    "percentage of systems within the environment that could be affected by the vulnerability.",
    key="TD",
    version="1.1.0",
    values=(
        _TD_NONE,
        _LOW,
        _MEDIUM,
        _HIGH,
        NOT_DEFINED_X,
    ),
)
"""
Introduces Not Defined value.
"""

VERSIONS = (
    TARGET_DISTRIBUTION_1,
    TARGET_DISTRIBUTION_1_1,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
