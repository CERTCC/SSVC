#!/usr/bin/env python
"""
file: patch_developer
author: adh
created_at: 9/21/23 10:27 AM
"""
from ssvc.decision_points.exploitation import EXPLOITATION_1 as EXPLOITATION
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1 as SAFETY_IMPACT
from ssvc.decision_points.technical_impact import TECHNICAL_IMPACT_1 as TECHNICAL_IMPACT
from ssvc.decision_points.utility import UTILITY_1 as UTILITY
from ssvc.decision_points.value_density import VALUE_DENSITY_1 as VALUE_DENSITY
from ssvc.decision_points.virulence import VIRULENCE_1 as VIRULENCE
from ssvc.dp_groups.base import SsvcDecisionPointGroup


PATCH_DEVELOPER_1 = SsvcDecisionPointGroup(
    name="SSVC Patch Developer",
    description="The decision points used by the patch developer.",
    key="PD",
    version="1.0.0",
    decision_points=[
        EXPLOITATION,
        UTILITY,
        TECHNICAL_IMPACT,
        VIRULENCE,
        VALUE_DENSITY,
        SAFETY_IMPACT,
    ],
)


def main():
    print(PATCH_DEVELOPER_1.to_json(indent=2))


if __name__ == "__main__":
    main()
