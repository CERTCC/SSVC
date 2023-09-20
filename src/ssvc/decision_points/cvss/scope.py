#!/usr/bin/env python
"""
file: scope
author: adh
created_at: 9/20/23 2:47 PM
"""

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

SCOPE_1 = CvssDecisionPoint(
    name="Scope",
    description="the ability for a vulnerability in one software component to impact resources beyond its means, or privileges",
    key="S",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Unchanged",
            key="U",
            description="An exploited vulnerability can only affect resources managed by the same authority. In this case the vulnerable component and the impacted component are the same.",
        ),
        SsvcValue(
            name="Changed",
            key="C",
            description="An exploited vulnerability can affect resources beyond the authorization privileges intended by the vulnerable component. In this case the vulnerable component and the impacted component are different.",
        ),
    ],
)


def main():
    print(SCOPE_1.to_json(indent=2))


if __name__ == "__main__":
    main()
