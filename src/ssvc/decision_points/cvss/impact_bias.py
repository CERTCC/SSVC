#!/usr/bin/env python
"""
Model the CVSS Impact Bias as an SSVC decision point.
"""
from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_AVAILABILITY = SsvcDecisionPointValue(
    name="Availability",
    key="A",
    description="Availability Impact is assigned greater weight than Confidentiality Impact or Integrity Impact.",
)

_INTEGRITY = SsvcDecisionPointValue(
    name="Integrity",
    key="I",
    description="Integrity Impact is assigned greater weight than Confidentiality Impact or Availability Impact.",
)

_CONFIDENTIALITY = SsvcDecisionPointValue(
    name="Confidentiality",
    key="C",
    description="Confidentiality impact is assigned greater weight than Integrity Impact or Availability Impact.",
)

_NORMAL = SsvcDecisionPointValue(
    name="Normal",
    key="N",
    description="Confidentiality Impact, Integrity Impact, and Availability Impact are all assigned the same weight.",
)

IMPACT_BIAS_1 = CvssDecisionPoint(
    name="Impact Bias",
    description="This metric measures the impact bias of the vulnerability.",
    key="IB",
    version="1.0.0",
    values=(
        _NORMAL,
        _CONFIDENTIALITY,
        _INTEGRITY,
        _AVAILABILITY,
    ),
)
"""
Defines Normal, Confidentiality, Integrity, and Availability values for CVSS Impact Bias.
"""


def main():
    print(IMPACT_BIAS_1.to_json(indent=2))


if __name__ == "__main__":
    main()
