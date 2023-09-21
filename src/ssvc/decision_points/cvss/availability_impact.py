#!/usr/bin/env python
"""
file: availability_impact
author: adh
created_at: 9/20/23 1:46 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

AVAILABILITY_IMPACT_1 = CvssDecisionPoint(
    name="Availability Impact",
    description="This metric measures the impact on availability a successful exploit of the vulnerability will have on the target system.",
    key="A",
    version="1.0.0",
    values=[
        SsvcValue(name="None", key="N", description="No impact on availability."),
        SsvcValue(
            name="Partial",
            key="P",
            description="Considerable lag in or interruptions in resource availability. For example, a network-based flood attack that reduces available bandwidth to a web server farm to such an extent that only a small number of connections successfully complete.",
        ),
        SsvcValue(
            name="Complete",
            key="C",
            description="Total shutdown of the affected resource. The attacker can render the resource completely unavailable.",
        ),
    ],
)

AVAILABILITY_IMPACT_2 = deepcopy(AVAILABILITY_IMPACT_1)
AVAILABILITY_IMPACT_2.version = "2.0.0"
AVAILABILITY_IMPACT_2.description = "This metric measures the impact to availability of a successfully exploited vulnerability."
AVAILABILITY_IMPACT_2.values = [
    SsvcValue(
        name="None",
        key="N",
        description="There is no impact to the availability of the system.",
    ),
    SsvcValue(
        name="Low",
        key="L",
        description="There is reduced performance or interruptions in resource availability.",
    ),
    SsvcValue(
        name="High",
        key="H",
        description="There is total loss of availability, resulting in the attacker being able to fully deny access to resources in the impacted component; this loss is either sustained (while the attacker continues to deliver the attack) or persistent (the condition persists even after the attack has completed).",
    ),
]


def main():
    print(AVAILABILITY_IMPACT_1.to_json(indent=2))
    print(AVAILABILITY_IMPACT_2.to_json(indent=2))


if __name__ == "__main__":
    main()
