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
    description="System meets NIST's critical software definition.",
)

NO = SsvcValue(
    name="No",
    key="N",
    description="System does not meet NIST's critical software definition.",
)

EO_CRITICAL = SsvcDecisionPoint(
    name="EO Critical",
    description="Denotes whether a system meets NIST's critical software definition. "
    "Based on https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity/critical-software-definition-explanatory",
    namespace="nist",
    key="EOCS",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)


def main():
    print(EO_CRITICAL.to_json(indent=2))


if __name__ == "__main__":
    main()
