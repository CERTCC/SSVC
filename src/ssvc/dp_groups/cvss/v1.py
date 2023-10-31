#!/usr/bin/env python
"""
file: v1
author: adh
created_at: 9/20/23 12:39 PM
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

from ssvc.decision_points.cvss.attack_complexity import ACCESS_COMPLEXITY_1
from ssvc.decision_points.cvss.attack_vector import ACCESS_VECTOR_1
from ssvc.decision_points.cvss.authentication import AUTHENTICATION_1
from ssvc.decision_points.cvss.availability_impact import (
    AVAILABILITY_IMPACT_1,
)
from ssvc.decision_points.cvss.collateral_damage_potential import (
    COLLATERAL_DAMAGE_POTENTIAL_1,
)
from ssvc.decision_points.cvss.confidentiality_impact import (
    CONFIDENTIALITY_IMPACT_1,
)
from ssvc.decision_points.cvss.exploitability import (
    EXPLOITABILITY_1,
)
from ssvc.decision_points.cvss.impact_bias import IMPACT_BIAS_1
from ssvc.decision_points.cvss.integrity_impact import (
    INTEGRITY_IMPACT_1,
)
from ssvc.decision_points.cvss.remediation_level import (
    REMEDIATION_LEVEL_1,
)
from ssvc.decision_points.cvss.report_confidence import (
    REPORT_CONFIDENCE_1,
)
from ssvc.decision_points.cvss.target_distribution import (
    TARGET_DISTRIBUTION_1,
)
from ssvc.dp_groups.base import SsvcDecisionPointGroup

# Instantiate the CVSS v1 decision point group
CVSSv1 = SsvcDecisionPointGroup(
    name="CVSS",
    version="1.0",
    description="CVSS v1 decision points",
    decision_points=(
        ACCESS_VECTOR_1,
        ACCESS_COMPLEXITY_1,
        AUTHENTICATION_1,
        CONFIDENTIALITY_IMPACT_1,
        INTEGRITY_IMPACT_1,
        AVAILABILITY_IMPACT_1,
        IMPACT_BIAS_1,
        EXPLOITABILITY_1,
        REMEDIATION_LEVEL_1,
        REPORT_CONFIDENCE_1,
        COLLATERAL_DAMAGE_POTENTIAL_1,
        TARGET_DISTRIBUTION_1,
    ),
)


def main():
    print(CVSSv1.to_json(indent=2))


if __name__ == "__main__":
    main()
