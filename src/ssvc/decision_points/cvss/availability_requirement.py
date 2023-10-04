#!/usr/bin/env python
"""
file: availability_requirement
author: adh
created_at: 9/20/23 2:11 PM
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

NOT_DEFINED = SsvcDecisionPointValue(
    name="Not Defined",
    key="ND",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
)

HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Loss of availability is likely to have a catastrophic adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)

MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Loss of availability is likely to have a serious adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)

LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Loss of availability is likely to have only a limited adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)


AVAILABILITY_REQUIREMENT_1 = CvssDecisionPoint(
    name="Availability Requirement",
    description="This metric measures the impact to the availability of a successfully exploited vulnerability.",
    key="CR",
    version="1.0.0",
    values=(
        LOW,
        MEDIUM,
        HIGH,
        NOT_DEFINED,
    ),
)


def main():
    print(AVAILABILITY_REQUIREMENT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
