#!/usr/bin/env python
"""
file: attack_complexity
author: adh
created_at: 9/20/23 2:32 PM
"""

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

ATTACK_COMPLEXITY_1 = CvssDecisionPoint(
    name="Attack Complexity",
    description="This metric describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability.",
    key="AC",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Low",
            key="L",
            description="Specialized access conditions or extenuating circumstances do not exist. An attacker can expect repeatable success against the vulnerable component.",
        ),
        SsvcValue(
            name="High",
            key="H",
            description="A successful attack depends on conditions beyond the attacker's control.",
        ),
    ],
)


def main():
    print(ATTACK_COMPLEXITY_1.to_json(indent=2))


if __name__ == "__main__":
    main()
