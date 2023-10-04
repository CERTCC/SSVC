#!/usr/bin/env python
"""
Models the CVSS Access Complexity metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_HIGH_2 = SsvcDecisionPointValue(
    name="High", key="H", description="Specialized access conditions exist."
)

_MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="The access conditions are somewhat specialized.",
)

_LOW_2 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Specialized access conditions or extenuating circumstances do not exist.",
)

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Specialized access conditions exist; for example: the system is exploitable during specific windows of time (a race condition), the system is exploitable under specific circumstances (nondefault configurations), or the system is exploitable with victim interaction (vulnerability exploitable only if user opens e-mail)",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Specialized access conditions or extenuating circumstances do not exist; the system is always exploitable.",
)


ACCESS_COMPLEXITY_1 = CvssDecisionPoint(
    name="Access Complexity",
    description="This metric measures the complexity of the attack required to exploit the vulnerability once an attacker has gained access to the target system.",
    key="AC",
    version="1.0.0",
    values=(
        _LOW,
        _HIGH,
    ),
)
"""
Defines LOW and HIGH values for CVSS Access Complexity.
"""

ACCESS_COMPLEXITY_2 = CvssDecisionPoint(
    name="Access Complexity",
    description="This metric measures the complexity of the attack required to exploit the vulnerability once an attacker has gained access to the target system.",
    key="AC",
    version="2.0.0",
    values=(
        _LOW_2,
        _MEDIUM,
        _HIGH_2,
    ),
)
"""
Updates LOW and HIGH definitions for CVSS Access Complexity. Adds MEDIUM value.
"""


def main():
    print(ACCESS_COMPLEXITY_1.to_json(indent=2))
    print(ACCESS_COMPLEXITY_2.to_json(indent=2))


if __name__ == "__main__":
    main()
