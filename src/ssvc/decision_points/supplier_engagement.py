#!/usr/bin/env python
"""
file: supplier_engagement
author: adh
created_at: 9/21/23 11:22 AM
"""

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

UNRESPONSIVE = SsvcDecisionPointValue(
    name="Unresponsive",
    key="U",
    description="The supplier is not responding to the reporter’s contact effort and not actively participating in the coordination effort.",
)

ACTIVE = SsvcDecisionPointValue(
    name="Active",
    key="A",
    description="The supplier is responding to the reporter’s contact effort and actively participating in the coordination effort.",
)

SUPPLIER_ENGAGEMENT_1 = SsvcDecisionPoint(
    name="Supplier Engagement",
    description="Is the supplier responding to the reporter’s contact effort and actively participating in the coordination effort?",
    key="SE",
    version="1.0.0",
    values=(
        ACTIVE,
        UNRESPONSIVE,
    ),
)


def main():
    print(SUPPLIER_ENGAGEMENT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
