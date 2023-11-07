#!/usr/bin/env python
"""
Models the CVSS Availability Impact metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is total loss of availability, resulting in the attacker being able to fully deny access to resources in the impacted component; this loss is either sustained (while the attacker continues to deliver the attack) or persistent (the condition persists even after the attack has completed).",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="There is reduced performance or interruptions in resource availability.",
)

_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no impact to the availability of the system.",
)

_COMPLETE = SsvcDecisionPointValue(
    name="Complete",
    key="C",
    description="Total shutdown of the affected resource. The attacker can render the resource completely unavailable.",
)

_PARTIAL = SsvcDecisionPointValue(
    name="Partial",
    key="P",
    description="Considerable lag in or interruptions in resource availability. For example, a network-based flood attack that reduces available bandwidth to a web server farm to such an extent that only a small number of connections successfully complete.",
)

_NONE_1 = SsvcDecisionPointValue(
    name="None", key="N", description="No impact on availability."
)

AVAILABILITY_IMPACT_1 = CvssDecisionPoint(
    name="Availability Impact",
    description="This metric measures the impact on availability a successful exploit of the vulnerability will have on the target system.",
    key="A",
    version="1.0.0",
    values=(
        _NONE_1,
        _PARTIAL,
        _COMPLETE,
    ),
)
"""
Defines None, Partial, and Complete values for CVSS Availability Impact.
"""

AVAILABILITY_IMPACT_2 = CvssDecisionPoint(
    name="Availability Impact",
    description="This metric measures the impact to availability of a successfully exploited vulnerability.",
    key="A",
    version="2.0.0",
    values=(
        _NONE_2,
        _LOW,
        _HIGH,
    ),
)
"""
Updates None. Removes Partial and Complete. Adds Low and High values for CVSS Availability Impact.
"""


def main():
    print(AVAILABILITY_IMPACT_1.to_json(indent=2))
    print(AVAILABILITY_IMPACT_2.to_json(indent=2))


if __name__ == "__main__":
    main()
