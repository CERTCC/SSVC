#!/usr/bin/env python
"""
file: coordinator_publication
author: adh
created_at: 9/21/23 11:40 AM
"""
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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

from ssvc.decision_points.exploitation import EXPLOITATION_1
from ssvc.decision_points.public_value_added import PUBLIC_VALUE_ADDED_1
from ssvc.decision_points.supplier_involvement import SUPPLIER_INVOLVEMENT_1
from ssvc.dp_groups.base import SsvcDecisionPointGroup


COORDINATOR_PUBLICATION_1 = SsvcDecisionPointGroup(
    name="Coordinator Publication",
    description="The decision points used by the coordinator during publication.",
    version="1.0.0",
    decision_points=(
        SUPPLIER_INVOLVEMENT_1,
        EXPLOITATION_1,
        PUBLIC_VALUE_ADDED_1,
    ),
)
"""
Added in SSVC v2, the Coordinator Publication v1.0.0 decision points are used by the coordinator during the publication process.

It includes decision points:

- Supplier Involvement v1.0.0
- Exploitation v1.0.0
- Public Value Added v1.0.0
"""


def main():
    print(COORDINATOR_PUBLICATION_1.to_json(indent=2))


if __name__ == "__main__":
    main()
