#!/usr/bin/env python
"""
file: impact_bias
author: adh
created_at: 9/20/23 1:47 PM
"""

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

IMPACT_BIAS_1 = CvssDecisionPoint(
    name="Impact Bias",
    description="This metric measures the impact bias of the vulnerability.",
    key="IB",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Normal",
            key="N",
            description="Confidentiality Impact, Integrity Impact, and Availability Impact are all assigned the same weight.",
        ),
        SsvcValue(
            name="Confidentiality",
            key="C",
            description="Confidentiality impact is assigned greater weight than Integrity Impact or Availability Impact.",
        ),
        SsvcValue(
            name="Integrity",
            key="I",
            description="Integrity Impact is assigned greater weight than Confidentiality Impact or Availability Impact.",
        ),
        SsvcValue(
            name="Availability",
            key="A",
            description="Availability Impact is assigned greater weight than Confidentiality Impact or Integrity Impact.",
        ),
    ],
)


def main():
    print(IMPACT_BIAS_1.to_json(indent=2))


if __name__ == "__main__":
    main()
