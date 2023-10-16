#!/usr/bin/env python
"""
file: public_safety_impact
author: adh
created_at: 9/21/23 10:43 AM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

SIGNIFICANT = SsvcDecisionPointValue(
    name="Significant",
    description="Safety impact of Major, Hazardous, or Catastrophic.",
    key="S",
)

MINIMAL = SsvcDecisionPointValue(
    name="Minimal", description="Safety impact of None or Minor.", key="M"
)

PUBLIC_SAFETY_IMPACT_1 = SsvcDecisionPoint(
    name="Public Safety Impact",
    description="A coarse-grained representation of impact to public safety.",
    key="PSI",
    version="1.0.0",
    values=(
        MINIMAL,
        SIGNIFICANT,
    ),
)


def main():
    print(PUBLIC_SAFETY_IMPACT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
