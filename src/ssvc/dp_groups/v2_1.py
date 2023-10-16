#!/usr/bin/env python
"""
file: v2_1
author: adh
created_at: 9/21/23 11:45 AM
"""

from ssvc.dp_groups.base import SsvcDecisionPointGroup, get_all_decision_points_from

# convenience imports
from ssvc.dp_groups.coordinator_publication import COORDINATOR_PUBLICATION_1
from ssvc.dp_groups.coordinator_triage import COORDINATOR_TRIAGE_1
from ssvc.dp_groups.deployer import DEPLOYER_3
from ssvc.dp_groups.supplier import SUPPLIER_2

GROUPS = [COORDINATOR_PUBLICATION_1, COORDINATOR_TRIAGE_1, DEPLOYER_3, SUPPLIER_2]


SSVCv2_1 = SsvcDecisionPointGroup(
    name="SSVCv2.1",
    description="The second version of the SSVC.",
    version="2.1.0",
    decision_points=get_all_decision_points_from(GROUPS),
)


def main():
    for group in GROUPS:
        print(group.to_json(indent=2))
        print()
    print(SSVCv2_1.to_json(indent=2))


if __name__ == "__main__":
    main()
