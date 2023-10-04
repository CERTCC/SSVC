#!/usr/bin/env python
"""
file: human_impact
author: adh
created_at: 9/21/23 10:49 AM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

VERY_HIGH = SsvcDecisionPointValue(
    name="Very High",
    key="VH",
    description="Safety=Catastrophic OR Mission=Mission Failure",
)

HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Safety=Hazardous, Mission=None/Degraded/Crippled/MEF Failure OR Safety=Major, Mission=MEF Failure",
)

MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Safety=None/Minor, Mission=MEF Failure OR Safety=Major, Mission=None/Degraded/Crippled",
)

LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Safety=None/Minor, Mission=None/Degraded/Crippled",
)

HUMAN_IMPACT_1 = SsvcDecisionPoint(
    name="Human Impact",
    description="Human Impact",
    key="HI",
    version="1.0.0",
    values=(
        LOW,
        MEDIUM,
        HIGH,
        VERY_HIGH,
    ),
)


def main():
    print(HUMAN_IMPACT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
