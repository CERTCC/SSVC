#!/usr/bin/env python
"""
file: critical
author: adh
created_at: 9/21/23 2:09 PM
"""
from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.ossf.base import OssfDecisionPoint

NO = SsvcValue(
    name="No",
    key="N",
    description="System does not meet the Open Source Software Foundation's critical software definition.",
)
YES = SsvcValue(
    name="Yes",
    key="Y",
    description="System meets the Open Source Software Foundation's critical software definition.",
)

OSSF_CRITICAL_SOFTWARE = OssfDecisionPoint(
    name="OSSF Critical Software",
    description="Denotes whether a system meets the Open Source Software Foundation's critical software definition. "
    "Based on https://openssf.org/wp-content/uploads/2021/07/OSSF-Criticality-Definition-1.0.pdf",
    key="OSSFCS",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)


def main():
    print(OSSF_CRITICAL_SOFTWARE.to_json(indent=2))


if __name__ == "__main__":
    main()
