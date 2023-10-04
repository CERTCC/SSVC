#!/usr/bin/env python
"""
file: supplier_contacted
author: adh
created_at: 9/21/23 11:17 AM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

YES = SsvcDecisionPointValue(
    name="Yes",
    key="Y",
    description="The supplier has been contacted.",
)

NO = SsvcDecisionPointValue(
    name="No",
    key="N",
    description="The supplier has not been contacted.",
)

SUPPLIER_CONTACTED_1 = SsvcDecisionPoint(
    name="Supplier Contacted",
    description="Has the reporter made a good-faith effort to contact the supplier of the vulnerable component using a quality contact method?",
    key="SC",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)


def main():
    print(SUPPLIER_CONTACTED_1.to_json(indent=2))


if __name__ == "__main__":
    main()
