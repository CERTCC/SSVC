#!/usr/bin/env python
"""
Models the CVSS Attack Complexity metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="A successful attack depends on conditions beyond the attacker's control.",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Specialized access conditions or extenuating circumstances do not exist. An attacker can expect repeatable success against the vulnerable component.",
)

ATTACK_COMPLEXITY_1 = CvssDecisionPoint(
    name="Attack Complexity",
    description="This metric describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability.",
    key="AC",
    version="1.0.0",
    values=(
        _LOW,
        _HIGH,
    ),
)
"""
Defines LOW and HIGH values for CVSS Attack Complexity.
"""


def main():
    print(ATTACK_COMPLEXITY_1.to_json(indent=2))


if __name__ == "__main__":
    main()
