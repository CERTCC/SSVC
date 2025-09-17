#!/usr/bin/env python
"""
file: deployer
author: adh
created_at: 9/21/23 11:40 AM
"""

#  Copyright (c) 2023-2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from ssvc.decision_points.ssvc.automatable import AUTOMATABLE_2
from ssvc.decision_points.ssvc.exploitation import EXPLOITATION_1
from ssvc.decision_points.ssvc.human_impact import HUMAN_IMPACT_2
from ssvc.decision_points.ssvc.mission_impact import (
    MISSION_IMPACT_1,
    MISSION_IMPACT_2,
)
from ssvc.decision_points.ssvc.safety_impact import SAFETY_IMPACT_1
from ssvc.decision_points.ssvc.system_exposure import (
    SYSTEM_EXPOSURE_1,
    SYSTEM_EXPOSURE_1_0_1,
)
from ssvc.decision_points.ssvc.utility import UTILITY_1_0_1
from ssvc.decision_points.ssvc.value_density import VALUE_DENSITY_1
from ssvc.dp_groups.base import DecisionPointGroup

PATCH_APPLIER_1 = DecisionPointGroup(
    name="SSVC Patch Applier",
    definition="The decision points used by the patch applier.",
    version="1.0.0",
    decision_points=(
        EXPLOITATION_1,
        SYSTEM_EXPOSURE_1,
        MISSION_IMPACT_1,
        SAFETY_IMPACT_1,
    ),
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
DEPLOYER_2 = DecisionPointGroup(
    name="SSVC Deployer",
    definition="The decision points used by the deployer.",
    version="2.0.0",
    decision_points=(
        EXPLOITATION_1,
        SYSTEM_EXPOSURE_1_0_1,
        MISSION_IMPACT_1,
        SAFETY_IMPACT_1,
        UTILITY_1_0_1,
        AUTOMATABLE_2,
        VALUE_DENSITY_1,
        HUMAN_IMPACT_2,
    ),
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

DEPLOYER_3 = DecisionPointGroup(
    name="SSVC Deployer",
    definition="The decision points used by the deployer.",
    version="3.0.0",
    decision_points=(
        EXPLOITATION_1,
        SYSTEM_EXPOSURE_1_0_1,
        MISSION_IMPACT_2,
        SAFETY_IMPACT_1,
        AUTOMATABLE_2,
        HUMAN_IMPACT_2,
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

VERSIONS = (PATCH_APPLIER_1, DEPLOYER_2, DEPLOYER_3)
LATEST = VERSIONS[-1]


def main():
    for version in VERSIONS:
        print(version.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
