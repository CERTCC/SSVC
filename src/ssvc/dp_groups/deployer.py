#!/usr/bin/env python
"""
file: deployer
author: adh
created_at: 9/21/23 11:40 AM
"""

from ssvc.decision_points.automatable import AUTOMATABLE_1
from ssvc.decision_points.exploitation import EXPLOITATION_1
from ssvc.decision_points.human_impact import HUMAN_IMPACT_1
from ssvc.decision_points.mission_impact import MISSION_IMPACT_1, MISSION_IMPACT_2
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1
from ssvc.decision_points.system_exposure import (
    SYSTEM_EXPOSURE_1,
    SYSTEM_EXPOSURE_1_0_1,
)
from ssvc.decision_points.utility import UTILITY_1_0_1
from ssvc.decision_points.value_density import VALUE_DENSITY_1
from ssvc.dp_groups.base import SsvcDecisionPointGroup

PATCH_APPLIER_1 = SsvcDecisionPointGroup(
    name="SSVC Patch Applier",
    description="The decision points used by the patch applier.",
    version="1.0.0",
    decision_points=[
        EXPLOITATION_1,
        SYSTEM_EXPOSURE_1,
        MISSION_IMPACT_1,
        SAFETY_IMPACT_1,
    ],
)
"""
In SSVC v1, Patch Applier v1 represents the decision points used by the patch applier.
It includes decision points:

- Exploitation v1.0.0
- System Exposure v1.0.0
- Mission Impact v1.0.0
- Safety Impact v1.0.0.
"""


# alias for forward compatibility
DEPLOYER_1 = PATCH_APPLIER_1

# SSVC v2
DEPLOYER_2 = SsvcDecisionPointGroup(
    name="SSVC Deployer",
    description="The decision points used by the deployer.",
    version="2.0.0",
    decision_points=[
        EXPLOITATION_1,
        SYSTEM_EXPOSURE_1_0_1,
        MISSION_IMPACT_1,
        SAFETY_IMPACT_1,
        UTILITY_1_0_1,
        AUTOMATABLE_1,
        VALUE_DENSITY_1,
        HUMAN_IMPACT_1,
    ],
)
"""
Deployer v2.0.0 is renamed from Patch Applier v1.0.0.
It includes decision points:

- Exploitation v1.0.0
- System Exposure v1.0.1
- Human Impact v1.0.0 (consolidate Mission Impact v1.0.0 and Safety Impact v1.0.0)
  - Safety Impact v1.0.0
  - Mission Impact v1.0.0
- Utility v1.0.1 (consolidate Automatable v1.0.0 and Value Density v1.0.0)
  - Automatable v1.0.0
  - Value Density v1.0.0

Changes from Patch Applier v1.0.0:
- System Exposure v1.0.0 -> v1.0.1
- Utility v1.0.1 is added, which depends on Automatable v1.0.0 and Value Density v1.0.0
- Human Impact v1.0.0 is added, which depends on Mission Impact v1.0.0 and Safety Impact v1.0.0
"""

DEPLOYER_3 = SsvcDecisionPointGroup(
    name="SSVC Deployer",
    description="The decision points used by the deployer.",
    version="3.0.0",
    decision_points=(
        EXPLOITATION_1,
        SYSTEM_EXPOSURE_1_0_1,
        MISSION_IMPACT_2,
        SAFETY_IMPACT_1,
        AUTOMATABLE_1,
        HUMAN_IMPACT_1,
    ),
)
"""
In SSVC 2.1, Deployer 3.0.0 includes decision points:

- Exploitation 1.0.0
- System Exposure 1.0.1
- Automatable 1.0.0
- Human Impact 1.0.0
  - Safety Impact 1.0.0
  - Mission Impact 2.0.0
 
Changes from v2.0.0: 
- removes Utility v1.0.1 in favor of Automatable v1.0.0.
- Mission Impact v1.0.0 -> v2.0.0
"""


def main():
    print(PATCH_APPLIER_1.to_json(indent=2))
    print(DEPLOYER_2.to_json(indent=2))
    print(DEPLOYER_3.to_json(indent=2))


if __name__ == "__main__":
    main()
