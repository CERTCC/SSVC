#!/usr/bin/env python
"""
file: integrity_requirement
author: adh
created_at: 9/20/23 2:11 PM
"""

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

NOT_DEFINED = SsvcValue(
    name="Not Defined",
    key="ND",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
)

HIGH = SsvcValue(
    name="High",
    key="H",
    description="Loss of integrity is likely to have a catastrophic adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)

MEDIUM = SsvcValue(
    name="Medium",
    key="M",
    description="Loss of integrity is likely to have a serious adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)

LOW = SsvcValue(
    name="Low",
    key="L",
    description="Loss of integrity is likely to have only a limited adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)

INTEGRITY_REQUIREMENT_1 = CvssDecisionPoint(
    name="Integrity Requirement",
    description="This metric measures the impact to the integrity of a successfully exploited vulnerability.",
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
    print(INTEGRITY_REQUIREMENT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
