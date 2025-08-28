#!/usr/bin/env python
"""
file: supplier
author: adh
created_at: 9/21/23 11:41 AM
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

from ssvc.decision_points.ssvc.automatable import AUTOMATABLE_2, VIRULENCE_1
from ssvc.decision_points.ssvc.exploitation import EXPLOITATION_1
from ssvc.decision_points.ssvc.safety_impact import SAFETY_IMPACT_1
from ssvc.decision_points.ssvc.technical_impact import TECHNICAL_IMPACT_1
from ssvc.decision_points.ssvc.utility import UTILITY_1, UTILITY_1_0_1
from ssvc.decision_points.ssvc.value_density import VALUE_DENSITY_1
from ssvc.dp_groups.base import DecisionPointGroup

PATCH_DEVELOPER_1 = DecisionPointGroup(
    name="SSVC Patch Developer",
    definition="The decision points used by the patch developer.",
    version="1.0.0",
    decision_points=(
        EXPLOITATION_1,
        UTILITY_1,
        TECHNICAL_IMPACT_1,
        VIRULENCE_1,
        VALUE_DENSITY_1,
        SAFETY_IMPACT_1,
    ),
)
"""
In SSVC v1, Patch Developer v1 represents the decision points used by the patch developer.

It includes decision points:

- Exploitation v1.0.0
- Utility v1.0.0
    - Virulence v1.0.0
    - Value Density v1.0.0
- Technical Impact v1.0.0
- Safety Impact v1.0.0
"""

# alias for forward compatibility
SUPPLIER_1 = PATCH_DEVELOPER_1

# SSVC v2 renamed to SSVC Supplier
SUPPLIER_2 = DecisionPointGroup(
    name="SSVC Supplier",
    definition="The decision points used by the supplier.",
    version="2.0.0",
    decision_points=(
        EXPLOITATION_1,
        UTILITY_1_0_1,
        TECHNICAL_IMPACT_1,
        AUTOMATABLE_2,
        VALUE_DENSITY_1,
        SAFETY_IMPACT_1,
    ),
)
"""
In SSVC v2, Supplier v2 represents the decision points used by the supplier.
It includes decision points:

- Exploitation v1.0.0
- Utility v1.0.1
    - Automatable v1.0.0
    - Value Density v1.0.0
- Technical Impact v1.0.0
- Public Safety Impact v1.0.0
    - Safety Impact v1.0.0
    
Changes from Patch Developer v1:

- Name change from Patch Developer v1 -> Supplier v2
- Utility v1.0.0 -> v1.0.1
- Virulence v1.0.0 replaced by Automatable v1.0.0
- Public Safety Impact v1.0.0 added, which subsumes Safety Impact v1.0.0
"""

VERSIONS = (PATCH_DEVELOPER_1, SUPPLIER_2)
LATEST = VERSIONS[-1]


def main():
    for version in VERSIONS:
        print(version.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
