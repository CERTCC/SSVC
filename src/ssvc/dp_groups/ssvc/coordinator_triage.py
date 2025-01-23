#!/usr/bin/env python
"""
file: coordinator_triage
author: adh
created_at: 9/21/23 11:40 AM
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

from ssvc.decision_points.automatable import AUTOMATABLE_2
from ssvc.decision_points.public_safety_impact import PUBLIC_SAFETY_IMPACT_2
from ssvc.decision_points.report_credibility import REPORT_CREDIBILITY_1
from ssvc.decision_points.report_public import REPORT_PUBLIC_1
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1
from ssvc.decision_points.supplier_cardinality import SUPPLIER_CARDINALITY_1
from ssvc.decision_points.supplier_contacted import SUPPLIER_CONTACTED_1
from ssvc.decision_points.supplier_engagement import SUPPLIER_ENGAGEMENT_1
from ssvc.decision_points.utility import UTILITY_1_0_1
from ssvc.decision_points.value_density import VALUE_DENSITY_1
from ssvc.dp_groups.base import SsvcDecisionPointGroup


COORDINATOR_TRIAGE_1 = SsvcDecisionPointGroup(
    name="Coordinator Triage",
    description="The decision points used by the coordinator during triage.",
    version="1.0.0",
    decision_points=(
        REPORT_PUBLIC_1,
        SUPPLIER_CONTACTED_1,
        REPORT_CREDIBILITY_1,
        SUPPLIER_CARDINALITY_1,
        SUPPLIER_ENGAGEMENT_1,
        UTILITY_1_0_1,
        AUTOMATABLE_2,
        VALUE_DENSITY_1,
        PUBLIC_SAFETY_IMPACT_2,
        SAFETY_IMPACT_1,
    ),
)
"""
Added in SSVC v2, the Coordinator Triage v1.0.0 decision points are used by the coordinator during the intake and triage process.

It includes decision points:

- Report Public v1.0.0
- Supplier Contacted v1.0.0
- Report Credibility v1.0.0
- Supplier Cardinality v1.0.0
- Supplier Engagement v1.0.0
- Utility v1.0.1, which depends on
    - Value Density v1.0.0
    - Automatable v1.0.0
- Public Safety Impact v1.0.0. which depends on
    - Safety Impact v1.0.0
"""


def main():
    print(COORDINATOR_TRIAGE_1.to_json(indent=2))


if __name__ == "__main__":
    main()
