#!/usr/bin/env python
"""
file: report_public
author: adh
created_at: 9/21/23 11:15 AM
"""

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

REPORT_PUBLIC_1 = SsvcDecisionPoint(
    name="Report Public",
    description="Is a viable report of the details of the vulnerability already publicly available?",
    key="RP",
    version="1.0.0",
    values=[
        SsvcValue(
            name="No",
            key="N",
            description="No public report of the vulnerability exists.",
        ),
        SsvcValue(
            name="Yes",
            key="Y",
            description="A public report of the vulnerability exists.",
        ),
    ],
)


def main():
    print(REPORT_PUBLIC_1.to_json(indent=2))


if __name__ == "__main__":
    main()
