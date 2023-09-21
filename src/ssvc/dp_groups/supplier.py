#!/usr/bin/env python
'''
file: supplier
author: adh
created_at: 9/21/23 11:41 AM
'''
from copy import deepcopy

from ssvc.decision_points.automatable import AUTOMATABLE_1
from ssvc.decision_points.exploitation import EXPLOITATION_1
from ssvc.decision_points.public_safety_impact import PUBLIC_SAFETY_IMPACT_1
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1
from ssvc.decision_points.technical_impact import TECHNICAL_IMPACT_1
from ssvc.decision_points.utility import UTILITY_1, UTILITY_1_0_1
from ssvc.decision_points.value_density import VALUE_DENSITY_1
from ssvc.decision_points.virulence import VIRULENCE_1
from ssvc.dp_groups.base import SsvcDecisionPointGroup



PATCH_DEVELOPER_1 = SsvcDecisionPointGroup(
        name="SSVC Patch Developer",
        description="The decision points used by the patch developer.",
        key="PD",
        version="1.0.0",
        decision_points=[
            EXPLOITATION_1,
            UTILITY_1,
            TECHNICAL_IMPACT_1,
            VIRULENCE_1,
            VALUE_DENSITY_1,
            SAFETY_IMPACT_1,
        ],
)

# alias for forward compatibility
SUPPLIER_1 = PATCH_DEVELOPER_1

# SSVC v2 renamed to SSVC Supplier
SUPPLIER_2 = deepcopy(SUPPLIER_1)
SUPPLIER_2.name = "Supplier",
SUPPLIER_2.description = "The decision points used by the supplier.",
SUPPLIER_2.version = "2.0.0"
# replace UTILITY 1 with UTILITY 1.0.1
SUPPLIER_2.decision_points.remove(UTILITY_1)
SUPPLIER_2.decision_points.append(UTILITY_1_0_1)
# add PUBLIC_SAFETY_IMPACT_1
SUPPLIER_2.decision_points.append(PUBLIC_SAFETY_IMPACT_1)


def main():
    print(PATCH_DEVELOPER_1.to_json(indent=2))
    print(SUPPLIER_2.to_json(indent=2))


if __name__ == '__main__':
    main()
