#!/usr/bin/env python
"""
file: target_distribution
author: adh
created_at: 9/20/23 1:48 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

NOT_DEFINED = SsvcDecisionPointValue(
    name="Not Defined",
    key="ND",
    description="This value is not defined in any specification, but is used in the CVSS v3.0 vector string when a value is required by the specification, but cannot be provided. This is a special case value and should be used sparingly.",
)

HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Targets exist inside the environment on a considerable scale. Between 50% - 100% of the total environment is considered at risk.",
)

MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Targets exist inside the environment, but on a medium scale. Between 16% - 49% of the total environment is at risk.",
)

LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Targets exist inside the environment, but on a small scale. Between 1% - 15% of the total environment is at risk.",
)

TD_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="No target systems exist, or targets are so highly specialized that they only exist in a laboratory setting. Effectively 0% of the environment is at risk.",
)

TARGET_DISTRIBUTION_1 = CvssDecisionPoint(
    name="Target Distribution",
    description="This metric measures the relative size of the field of target systems susceptible to the vulnerability. It is meant as an environment-specific indicator in order to approximate the percentage of systems within the environment that could be affected by the vulnerability.",
    key="TD",
    version="1.0.0",
    values=(
        TD_NONE,
        LOW,
        MEDIUM,
        HIGH,
    ),
)

TARGET_DISTRIBUTION_1_1 = deepcopy(TARGET_DISTRIBUTION_1)
TARGET_DISTRIBUTION_1_1.version = "1.1.0"
TARGET_DISTRIBUTION_1_1.values = (
    TD_NONE,
    LOW,
    MEDIUM,
    HIGH,
    NOT_DEFINED,
)


def main():
    print(TARGET_DISTRIBUTION_1.to_json(indent=2))
    print(TARGET_DISTRIBUTION_1_1.to_json(indent=2))


if __name__ == "__main__":
    main()
