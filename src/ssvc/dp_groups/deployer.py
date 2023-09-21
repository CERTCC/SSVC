#!/usr/bin/env python
"""
file: deployer
author: adh
created_at: 9/21/23 11:40 AM
"""
from copy import deepcopy

from ssvc.decision_points.automatable import AUTOMATABLE_1
from ssvc.decision_points.exploitation import EXPLOITATION_1
from ssvc.decision_points.system_exposure import (
    SYSTEM_EXPOSURE_1,
    SYSTEM_EXPOSURE_1_0_1,
)
from ssvc.decision_points.human_impact import HUMAN_IMPACT_1
from ssvc.decision_points.mission_impact import MISSION_IMPACT_1, MISSION_IMPACT_2
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1
from ssvc.decision_points.utility import UTILITY_1_0_1
from ssvc.decision_points.value_density import VALUE_DENSITY_1
from ssvc.dp_groups.base import SsvcDecisionPointGroup


PATCH_APPLIER_1 = SsvcDecisionPointGroup(
    name="SSVC Patch Applier",
    description="The decision points used by the patch applier.",
    key="PA",
    version="1.0.0",
    decision_points=[
        EXPLOITATION_1,
        SYSTEM_EXPOSURE_1,
        MISSION_IMPACT_1,
        SAFETY_IMPACT_1,
    ],
)

# alias for forward compatibility
DEPLOYER_1 = PATCH_APPLIER_1

# SSVC v2
DEPLOYER_2 = deepcopy(DEPLOYER_1)
# change name to SSVC Deployer
DEPLOYER_2.name = "SSVC Deployer"
DEPLOYER_2.key = "D"
DEPLOYER_2.version = "2.0.0"
# update exposure
DEPLOYER_2.decision_points.remove(SYSTEM_EXPOSURE_1)
DEPLOYER_2.decision_points.append(SYSTEM_EXPOSURE_1_0_1)
# add UTILITY (AUTOMATABLE + VALUE DENSITY)
DEPLOYER_2.decision_points.append(UTILITY_1_0_1)
DEPLOYER_2.decision_points.append(AUTOMATABLE_1)
DEPLOYER_2.decision_points.append(VALUE_DENSITY_1)
# condense MISSION_IMPACT_1 and SAFETY_IMPACT_1 into HUMAN_IMPACT_1
DEPLOYER_2.decision_points.append(HUMAN_IMPACT_1)


# SSVC v2.1
DEPLOYER_3 = deepcopy(DEPLOYER_2)
DEPLOYER_3.version = "3.0.0"
# replace UTILITY (AUTOMATABLE + VALUE DENSITY) with just AUTOMATABLE
DEPLOYER_3.decision_points.remove(UTILITY_1_0_1)
DEPLOYER_3.decision_points.remove(VALUE_DENSITY_1)

# update MISSION_IMPACT_1 to MISSION_IMPACT_2
DEPLOYER_3.decision_points.remove(MISSION_IMPACT_1)
DEPLOYER_3.decision_points.append(MISSION_IMPACT_2)


def main():
    print(PATCH_APPLIER_1.to_json(indent=2))
    print(DEPLOYER_2.to_json(indent=2))
    print(DEPLOYER_3.to_json(indent=2))


if __name__ == "__main__":
    main()
