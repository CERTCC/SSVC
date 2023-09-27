#!/usr/bin/env python
"""
file: eo_critical
author: adh
created_at: 9/21/23 2:03 PM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

YES = SsvcValue(
    name="Yes",
    key="Y",
    description="System meets a critical software definition.",
)

NO = SsvcValue(
    name="No",
    key="N",
    description="System does not meet a critical software definition.",
)

CRITICAL_SOFTWARE_1 = SsvcDecisionPoint(
    name="Critical Software",
    description="Denotes whether a system meets a critical software definition.",
    namespace="SSVC",
    key="CS",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)


def main():
    print(CRITICAL_SOFTWARE_1.to_json(indent=2))


if __name__ == "__main__":
    main()
