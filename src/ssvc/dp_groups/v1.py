#!/usr/bin/env python
"""
file: v1
author: adh
created_at: 9/21/23 9:52 AM
"""
from ssvc.decision_points.exploitation import EXPLOITATION_1 as EXPLOITATION
from ssvc.decision_points.exposure import EXPOSURE_1 as EXPOSURE
from ssvc.decision_points.mission_impact import MISSION_IMPACT_1 as MISSION_IMPACT
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1 as SAFETY_IMPACT
from ssvc.decision_points.technical_impact import TECHNICAL_IMPACT_1 as TECHNICAL_IMPACT
from ssvc.decision_points.value_density import VALUE_DENSITY_1 as VALUE_DENSITY
from ssvc.decision_points.virulence import VIRULENCE_1 as VIRULENCE
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.decision_points.utility import UTILITY_1 as UTILITY

SSVCv1 = SsvcDecisionPointGroup(
    name="SSVCv1",
    description="The first version of the SSVC.",
    key="SSVCv1",
    version="1.0.0",
    decision_points=[
        EXPLOITATION,
        TECHNICAL_IMPACT,
        UTILITY,
        VIRULENCE,
        VALUE_DENSITY,
        SAFETY_IMPACT,
        EXPOSURE,
        MISSION_IMPACT,
    ],
)

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

PATCH_APPLIER_1 = SsvcDecisionPointGroup(
    name="SSVC Patch Applier",
    description="The decision points used by the patch applier.",
    key="PA",
    version="1.0.0",
    decision_points=[EXPLOITATION, EXPOSURE, MISSION_IMPACT, SAFETY_IMPACT],
)


def main():
    print(SSVCv1.to_json(indent=2))
    print(PATCH_DEVELOPER_1.to_json(indent=2))
    print(PATCH_APPLIER_1.to_json(indent=2))


if __name__ == "__main__":
    main()
