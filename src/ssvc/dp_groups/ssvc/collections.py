#!/usr/bin/env python
"""
Provides collections of decision points for each version of the SSVC.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University


from ssvc.dp_groups.base import (
    DecisionPointGroup,
    get_all_decision_points_from,
)
from ssvc.dp_groups.ssvc.coordinator_publication import (
    COORDINATOR_PUBLICATION_1,
)
from ssvc.dp_groups.ssvc.coordinator_triage import COORDINATOR_TRIAGE_1
from ssvc.dp_groups.ssvc.deployer import (
    DEPLOYER_2,
    DEPLOYER_3,
    PATCH_APPLIER_1,
)
from ssvc.dp_groups.ssvc.supplier import PATCH_DEVELOPER_1, SUPPLIER_2


SSVCv1 = DecisionPointGroup(
    name="SSVCv1",
    description="The first version of the SSVC.",
    version="1.0.0",
    decision_points=get_all_decision_points_from(
        PATCH_APPLIER_1, PATCH_DEVELOPER_1
    ),
)
SSVCv2 = DecisionPointGroup(
    name="SSVCv2",
    description="The second version of the SSVC.",
    version="2.0.0",
    decision_points=get_all_decision_points_from(
        COORDINATOR_PUBLICATION_1, COORDINATOR_TRIAGE_1, DEPLOYER_2, SUPPLIER_2
    ),
)
SSVCv2_1 = DecisionPointGroup(
    name="SSVCv2.1",
    description="The second version of the SSVC.",
    version="2.1.0",
    decision_points=get_all_decision_points_from(
        COORDINATOR_PUBLICATION_1, COORDINATOR_TRIAGE_1, DEPLOYER_3, SUPPLIER_2
    ),
)

VERSIONS = (SSVCv1, SSVCv2, SSVCv2_1)
LATEST = VERSIONS[-1]

def main():
    for version in VERSIONS:
        print(version.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
