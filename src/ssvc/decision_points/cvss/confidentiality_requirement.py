#!/usr/bin/env python
"""
file: confidentiality_requirement
author: adh
created_at: 9/20/23 2:11 PM
"""

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

CONFIDENTIALITY_REQUIREMENT_1 = CvssDecisionPoint(
    name="Confidentiality Requirement",
    description="This metric measures the impact to the confidentiality of a successfully exploited vulnerability.",
    key="CR",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Low",
            key="L",
            description="Loss of confidentiality is likely to have only a limited adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
        ),
        SsvcValue(
            name="Medium",
            key="M",
            description="Loss of confidentiality is likely to have a serious adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
        ),
        SsvcValue(
            name="High",
            key="H",
            description="Loss of confidentiality is likely to have a catastrophic adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
        ),
        SsvcValue(
            name="Not Defined",
            key="ND",
            description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
        ),
    ],
)


def main():
    print(CONFIDENTIALITY_REQUIREMENT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
