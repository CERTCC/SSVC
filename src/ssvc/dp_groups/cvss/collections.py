#!/usr/bin/env python
"""
Models CVSS vectors as SSVC decision point groups
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

from ssvc.decision_points.cvss.attack_complexity import (
    ACCESS_COMPLEXITY_1,
    ACCESS_COMPLEXITY_2,
    ATTACK_COMPLEXITY_3,
    ATTACK_COMPLEXITY_3_0_1,
)
from ssvc.decision_points.cvss.attack_requirements import ATTACK_REQUIREMENTS_1
from ssvc.decision_points.cvss.attack_vector import (
    ACCESS_VECTOR_1,
    ACCESS_VECTOR_2,
    ATTACK_VECTOR_3,
    ATTACK_VECTOR_3_0_1,
)
from ssvc.decision_points.cvss.authentication import AUTHENTICATION_1, AUTHENTICATION_2
from ssvc.decision_points.cvss.availability_impact import (
    AVAILABILITY_IMPACT_1,
    AVAILABILITY_IMPACT_2,
    AVAILABILITY_IMPACT_2_0_1,
)
from ssvc.decision_points.cvss.availability_requirement import (
    AVAILABILITY_REQUIREMENT_1,
    AVAILABILITY_REQUIREMENT_1_0_1,
)
from ssvc.decision_points.cvss.collateral_damage_potential import (
    COLLATERAL_DAMAGE_POTENTIAL_1,
    COLLATERAL_DAMAGE_POTENTIAL_2,
)
from ssvc.decision_points.cvss.confidentiality_impact import (
    CONFIDENTIALITY_IMPACT_1,
    CONFIDENTIALITY_IMPACT_2,
    CONFIDENTIALITY_IMPACT_2_0_1,
)
from ssvc.decision_points.cvss.confidentiality_requirement import (
    CONFIDENTIALITY_REQUIREMENT_1,
    CONFIDENTIALITY_REQUIREMENT_1_0_1,
)
from ssvc.decision_points.cvss.eq_sets import EQ1, EQ2, EQ3, EQ4, EQ5, EQ6
from ssvc.decision_points.cvss.exploitability import (
    EXPLOITABILITY_1,
    EXPLOITABILITY_1_1,
    EXPLOIT_CODE_MATURITY_1_2,
    EXPLOIT_MATURITY_2,
)
from ssvc.decision_points.cvss.impact_bias import IMPACT_BIAS_1
from ssvc.decision_points.cvss.integrity_impact import (
    INTEGRITY_IMPACT_1,
    INTEGRITY_IMPACT_2,
    INTEGRITY_IMPACT_2_0_1,
)
from ssvc.decision_points.cvss.integrity_requirement import (
    INTEGRITY_REQUIREMENT_1,
    INTEGRITY_REQUIREMENT_1_0_1,
)
from ssvc.decision_points.cvss.privileges_required import (
    PRIVILEGES_REQUIRED_1,
    PRIVILEGES_REQUIRED_1_0_1,
)
from ssvc.decision_points.cvss.remediation_level import (
    REMEDIATION_LEVEL_1,
    REMEDIATION_LEVEL_1_1,
)
from ssvc.decision_points.cvss.report_confidence import (
    REPORT_CONFIDENCE_1,
    REPORT_CONFIDENCE_1_1,
    REPORT_CONFIDENCE_2,
)
from ssvc.decision_points.cvss.scope import SCOPE_1 as SCOPE
from ssvc.decision_points.cvss.subsequent_availability_impact import (
    SUBSEQUENT_AVAILABILITY_IMPACT_1,
)
from ssvc.decision_points.cvss.subsequent_confidentiality_impact import (
    SUBSEQUENT_CONFIDENTIALITY_IMPACT_1,
)
from ssvc.decision_points.cvss.subsequent_integrity_impact import (
    SUBSEQUENT_INTEGRITY_IMPACT_1,
)
from ssvc.decision_points.cvss.target_distribution import (
    TARGET_DISTRIBUTION_1,
    TARGET_DISTRIBUTION_1_1,
)
from ssvc.decision_points.cvss.user_interaction import (
    USER_INTERACTION_1,
    USER_INTERACTION_2,
)
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.dp_groups.cvss.helpers import modify


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

# CVSS v2 decision points
CVSSv2 = SsvcDecisionPointGroup(
    name="CVSS Version 2",
    description="The Common Vulnerability Scoring System (CVSS) is a free and open industry standard for assessing the severity of computer system security vulnerabilities. CVSS attempts to assign severity scores to vulnerabilities, allowing responders to prioritize responses and resources according to threat. Scores are calculated based on a formula that depends on several metrics that approximate ease of exploit and the impact of exploit. Scores range from 0 to 10, with 10 being the most severe.",
    version="2.0",
    decision_points=(
        ACCESS_VECTOR_2,
        ACCESS_COMPLEXITY_2,
        AUTHENTICATION_2,
        CONFIDENTIALITY_IMPACT_1,
        INTEGRITY_IMPACT_1,
        AVAILABILITY_IMPACT_1,
        EXPLOITABILITY_1_1,
        REMEDIATION_LEVEL_1_1,
        REPORT_CONFIDENCE_1_1,
        COLLATERAL_DAMAGE_POTENTIAL_2,
        TARGET_DISTRIBUTION_1_1,
        CONFIDENTIALITY_REQUIREMENT_1,
        INTEGRITY_REQUIREMENT_1,
        AVAILABILITY_REQUIREMENT_1,
    ),
)

# CVSS v3 decision points
MODIFIED_ATTACK_VECTOR = modify(ATTACK_VECTOR_3)
MODIFIED_ATTACK_COMPLEXITY = modify(ATTACK_COMPLEXITY_3)
MODIFIED_PRIVILEGES_REQUIRED = modify(PRIVILEGES_REQUIRED_1)
MODIFIED_USER_INTERACTION = modify(USER_INTERACTION_1)
MODIFIED_SCOPE = modify(SCOPE)
MODIFIED_CONFIDENTIALITY_IMPACT = modify(CONFIDENTIALITY_IMPACT_2)
MODIFIED_INTEGRITY_IMPACT = modify(INTEGRITY_IMPACT_2)
MODIFIED_AVAILABILITY_IMPACT = modify(AVAILABILITY_IMPACT_2)

CVSSv3 = SsvcDecisionPointGroup(
    name="CVSS Version 3",
    description="The Common Vulnerability Scoring System (CVSS) is a free and open industry standard for assessing the severity of computer system security vulnerabilities. CVSS attempts to assign severity scores to vulnerabilities, allowing responders to prioritize responses and resources according to threat. Scores are calculated based on a formula that depends on several metrics that approximate ease of exploit and the impact of exploit. Scores range from 0 to 10, with 10 being the most severe.",
    version="3.0",
    decision_points=(
        ATTACK_VECTOR_3,
        ATTACK_COMPLEXITY_3,
        PRIVILEGES_REQUIRED_1,
        USER_INTERACTION_1,
        SCOPE,
        CONFIDENTIALITY_IMPACT_2,
        INTEGRITY_IMPACT_2,
        AVAILABILITY_IMPACT_2,
        EXPLOIT_CODE_MATURITY_1_2,
        REMEDIATION_LEVEL_1_1,
        REPORT_CONFIDENCE_2,
        CONFIDENTIALITY_REQUIREMENT_1,
        INTEGRITY_REQUIREMENT_1,
        AVAILABILITY_REQUIREMENT_1,
        MODIFIED_ATTACK_VECTOR,
        MODIFIED_ATTACK_COMPLEXITY,
        MODIFIED_PRIVILEGES_REQUIRED,
        MODIFIED_USER_INTERACTION,
        MODIFIED_SCOPE,
        MODIFIED_CONFIDENTIALITY_IMPACT,
        MODIFIED_INTEGRITY_IMPACT,
        MODIFIED_AVAILABILITY_IMPACT,
    ),
)

# CVSS v4 decision points

_EXPLOITABILITY = [
    ATTACK_VECTOR_3_0_1,
    ATTACK_COMPLEXITY_3_0_1,
    ATTACK_REQUIREMENTS_1,
    PRIVILEGES_REQUIRED_1_0_1,
    USER_INTERACTION_2,
]
_IMPACT = [
    CONFIDENTIALITY_IMPACT_2_0_1,
    INTEGRITY_IMPACT_2_0_1,
    AVAILABILITY_IMPACT_2_0_1,
    SUBSEQUENT_CONFIDENTIALITY_IMPACT_1,
    SUBSEQUENT_INTEGRITY_IMPACT_1,
    SUBSEQUENT_AVAILABILITY_IMPACT_1,
]
_BASE = _EXPLOITABILITY + _IMPACT
_ENVIRONMENTAL = [modify(base_metric) for base_metric in _BASE]
_ENVIRONMENTAL.extend(
    [
        CONFIDENTIALITY_REQUIREMENT_1_0_1,
        INTEGRITY_REQUIREMENT_1_0_1,
        AVAILABILITY_REQUIREMENT_1_0_1,
    ]
)
_THREAT = [
    EXPLOIT_MATURITY_2,
]

# CVSS-B	Base metrics
CVSSv4_B = SsvcDecisionPointGroup(
    name="CVSSv4 Base Metrics",
    description="Base metrics for CVSS v4",
    version="1.0.0",
    decision_points=tuple(_BASE),
)

# CVSS-BE	Base and Environmental metrics
CVSSv4_BE = SsvcDecisionPointGroup(
    name="CVSSv4 Base and Environmental Metrics",
    description="Base and Environmental metrics for CVSS v4",
    version="1.0.0",
    decision_points=tuple(_BASE + _ENVIRONMENTAL),
)

# CVSS-BT	Base and Threat metrics
CVSSv4_BT = SsvcDecisionPointGroup(
    name="CVSSv4 Base and Threat Metrics",
    description="Base and Threat metrics for CVSS v4",
    version="1.0.0",
    decision_points=tuple(_BASE + _THREAT),
)

# CVSS-BTE
CVSSv4_BTE = SsvcDecisionPointGroup(
    name="CVSSv4 Base, Threat, and Environmental Metrics",
    description="Base, Threat, and Environmental metrics for CVSS v4",
    version="1.0.0",
    decision_points=tuple(_BASE + _THREAT + _ENVIRONMENTAL),
)

CVSSv4 = CVSSv4_BTE  # convenience alias

CVSSv4_Equivalence_Sets = SsvcDecisionPointGroup(
    name="CVSSv4 EQ Sets",
    description="Equivalence Sets for CVSS v4",
    version="1.0.0",
    decision_points=(
        EQ1,
        EQ2,
        EQ3,
        EQ4,
        EQ5,
        EQ6,
    ),
)


def main():
    for group in [
        CVSSv1,
        CVSSv2,
        CVSSv3,
        CVSSv4_B,
        CVSSv4_BE,
        CVSSv4_BT,
        CVSSv4_BTE,
        CVSSv4_Equivalence_Sets,
    ]:
        print(group.to_json(indent=2))
        print()


if __name__ == "__main__":
    main()
