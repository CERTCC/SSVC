#!/usr/bin/env python
"""
Models CVSS Target Distribution as an SSVC decision point.
"""

#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs


_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Targets exist inside the environment on a considerable scale. Between 50% - 100% of the total "
    "environment is considered at risk.",
)

_MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Targets exist inside the environment, but on a medium scale. Between 16% - 49% of the total "
    "environment is at risk.",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Targets exist inside the environment, but on a small scale. Between 1% - 15% of the total "
    "environment is at risk.",
)

_TD_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="No target systems exist, or targets are so highly specialized that they only exist in a laboratory "
    "setting. Effectively 0% of the environment is at risk.",
)

TARGET_DISTRIBUTION_1 = CvssDecisionPoint(
    name="Target Distribution",
    description="This metric measures the relative size of the field of target systems susceptible to the "
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
    description="This metric measures the relative size of the field of target systems susceptible to the "
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
