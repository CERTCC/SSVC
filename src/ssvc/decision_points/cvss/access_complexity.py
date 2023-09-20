#!/usr/bin/env python
"""
file: access_complexity
author: adh
created_at: 9/20/23 1:35 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

ACCESS_COMPLEXITY_1 = CvssDecisionPoint(
    name="Access Complexity",
    description="This metric measures the complexity of the attack required to exploit the vulnerability once an attacker has gained access to the target system.",
    key="AC",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Low",
            key="L",
            description="Specialized access conditions or extenuating circumstances do not exist; the system is always exploitable.",
        ),
        SsvcValue(
            name="High",
            key="H",
            description="Specialized access conditions exist; for example: the system is exploitable during specific windows of time (a race condition), the system is exploitable under specific circumstances (nondefault configurations), or the system is exploitable with victim interaction (vulnerability exploitable only if user opens e-mail)",
        ),
    ],
)

ACCESS_COMPLEXITY_2 = deepcopy(ACCESS_COMPLEXITY_1)
ACCESS_COMPLEXITY_2.version = "2.0.0"
ACCESS_COMPLEXITY_2.values = [
    SsvcValue(
        name="Low",
        key="L",
        description="Specialized access conditions or extenuating circumstances do not exist.",
    ),
    SsvcValue(
        name="Medium",
        key="M",
        description="The access conditions are somewhat specialized.",
    ),
    SsvcValue(name="High", key="H", description="Specialized access conditions exist."),
]


def main():
    print(ACCESS_COMPLEXITY_1.to_json(indent=2))
    print(ACCESS_COMPLEXITY_2.to_json(indent=2))


if __name__ == "__main__":
    main()
