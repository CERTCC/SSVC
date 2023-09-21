#!/usr/bin/env python
"""
file: patch_applier
author: adh
created_at: 9/21/23 10:28 AM
"""
from ssvc.decision_points.exploitation import EXPLOITATION_1 as EXPLOITATION
from ssvc.decision_points.exposure import EXPOSURE_1 as EXPOSURE
from ssvc.decision_points.mission_impact import MISSION_IMPACT_1 as MISSION_IMPACT
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1 as SAFETY_IMPACT
from ssvc.dp_groups.base import SsvcDecisionPointGroup


PATCH_APPLIER_1 = SsvcDecisionPointGroup(
    name="SSVC Patch Applier",
    description="The decision points used by the patch applier.",
    key="PA",
    version="1.0.0",
    decision_points=[EXPLOITATION, EXPOSURE, MISSION_IMPACT, SAFETY_IMPACT],
)


def main():
    print(PATCH_APPLIER_1.to_json(indent=2))


if __name__ == "__main__":
    main()
