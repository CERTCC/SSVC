#!/usr/bin/env python
"""
Models a high value asset as a decision point.
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

YES = SsvcDecisionPointValue(
    name="Yes",
    key="Y",
    description="System meets a high value asset definition.",
)

NO = SsvcDecisionPointValue(
    name="No",
    key="N",
    description="System does not meet a high value asset definition.",
)

HIGH_VALUE_ASSET_1 = SsvcDecisionPoint(
    name="High Value Asset",
    description="Denotes whether a system meets a high value asset definition.",
    namespace="SSVC",
    key="HVA",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)


def main():
    print(HIGH_VALUE_ASSET_1.to_json(indent=2))


if __name__ == "__main__":
    main()
