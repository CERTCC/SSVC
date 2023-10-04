#!/usr/bin/env python
"""
file: v2
author: adh
created_at: 9/21/23 10:31 AM
"""

from ssvc.dp_groups.base import SsvcDecisionPointGroup, get_all_decision_points_from

# convenience imports
from ssvc.dp_groups.coordinator_publication import COORDINATOR_PUBLICATION_1  # noqa
from ssvc.dp_groups.coordinator_triage import COORDINATOR_TRIAGE_1  # noqa
from ssvc.dp_groups.deployer import DEPLOYER_2  # noqa
from ssvc.dp_groups.supplier import SUPPLIER_2  # noqa

GROUPS = [COORDINATOR_PUBLICATION_1, COORDINATOR_TRIAGE_1, DEPLOYER_2, SUPPLIER_2]


SSVCv2 = SsvcDecisionPointGroup(
    name="SSVCv2",
    description="The second version of the SSVC.",
    version="2.0.0",
    decision_points=get_all_decision_points_from(GROUPS),
)


def main():
    print(SSVCv2.to_json(indent=2))
    print(SUPPLIER_2.to_json(indent=2))
    print(DEPLOYER_2.to_json(indent=2))
    print(COORDINATOR_TRIAGE_1.to_json(indent=2))
    print(COORDINATOR_PUBLICATION_1.to_json(indent=2))


if __name__ == "__main__":
    main()
