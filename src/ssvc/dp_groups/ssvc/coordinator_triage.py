#!/usr/bin/env python
"""
file: coordinator_triage
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
from ssvc.decision_points.ssvc.public_safety_impact import (
    PUBLIC_SAFETY_IMPACT_2,
)
from ssvc.decision_points.ssvc.report_credibility import REPORT_CREDIBILITY_1
from ssvc.decision_points.ssvc.report_public import REPORT_PUBLIC_1
from ssvc.decision_points.ssvc.safety_impact import SAFETY_IMPACT_1
from ssvc.decision_points.ssvc.supplier_cardinality import (
    SUPPLIER_CARDINALITY_1,
)
from ssvc.decision_points.ssvc.supplier_contacted import SUPPLIER_CONTACTED_1
from ssvc.decision_points.ssvc.supplier_engagement import SUPPLIER_ENGAGEMENT_1
from ssvc.decision_points.ssvc.utility import UTILITY_1_0_1
from ssvc.decision_points.ssvc.value_density import VALUE_DENSITY_1
from ssvc.dp_groups.base import DecisionPointGroup

COORDINATOR_TRIAGE_1 = DecisionPointGroup(
    name="Coordinator Triage",
    definition="The decision points used by the coordinator during triage.",
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

VERSIONS = (COORDINATOR_TRIAGE_1,)
LATEST = VERSIONS[-1]


def main():
    for version in VERSIONS:
        print(version.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
