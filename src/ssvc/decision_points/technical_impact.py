#!/usr/bin/env python
"""
file: technical_impact
author: adh
created_at: 9/21/23 9:49 AM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

TOTAL = SsvcDecisionPointValue(
    name="Total",
    key="T",
    description="The exploit gives the adversary total control over the behavior of the software, or it gives total disclosure of all information on the system that contains the vulnerability.",
)

PARTIAL = SsvcDecisionPointValue(
    name="Partial",
    key="P",
    description="The exploit gives the adversary limited control over, or information exposure about, the behavior of the software that contains the vulnerability. Or the exploit gives the adversary an importantly low stochastic opportunity for total control.",
)

TECHNICAL_IMPACT_1 = SsvcDecisionPoint(
    name="Technical Impact",
    description="The technical impact of the vulnerability.",
    key="TI",
    version="1.0.0",
    values=(
        PARTIAL,
        TOTAL,
    ),
)


def main():
    print(TECHNICAL_IMPACT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
