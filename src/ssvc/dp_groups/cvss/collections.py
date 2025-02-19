#!/usr/bin/env python
"""
Models CVSS vectors as SSVC decision point groups
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
from ssvc.decision_points.cvss.authentication import (
    AUTHENTICATION_1,
    AUTHENTICATION_2,
)
from ssvc.decision_points.cvss.availability_impact import (
    AVAILABILITY_IMPACT_1,
    AVAILABILITY_IMPACT_2,
    AVAILABILITY_IMPACT_2_0_1,
)
from ssvc.decision_points.cvss.availability_requirement import (
    AVAILABILITY_REQUIREMENT_1,
    AVAILABILITY_REQUIREMENT_1_1,
    AVAILABILITY_REQUIREMENT_1_1_1,
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
    CONFIDENTIALITY_REQUIREMENT_1_1,
    CONFIDENTIALITY_REQUIREMENT_1_1_1,
)
from ssvc.decision_points.cvss.equivalence_set_1 import EQ1
from ssvc.decision_points.cvss.equivalence_set_2 import EQ2
from ssvc.decision_points.cvss.equivalence_set_3 import EQ3
from ssvc.decision_points.cvss.equivalence_set_4 import EQ4
from ssvc.decision_points.cvss.equivalence_set_5 import EQ5
from ssvc.decision_points.cvss.equivalence_set_6 import EQ6
from ssvc.decision_points.cvss.exploitability import (
    EXPLOITABILITY_1,
    EXPLOITABILITY_1_1,
    EXPLOIT_CODE_MATURITY_1_2,
    EXPLOIT_MATURITY_2,
)
from ssvc.decision_points.cvss.helpers import modify_3, modify_4
from ssvc.decision_points.cvss.impact_bias import IMPACT_BIAS_1
from ssvc.decision_points.cvss.integrity_impact import (
    INTEGRITY_IMPACT_1,
    INTEGRITY_IMPACT_2,
    INTEGRITY_IMPACT_2_0_1,
)
from ssvc.decision_points.cvss.integrity_requirement import (
    INTEGRITY_REQUIREMENT_1,
    INTEGRITY_REQUIREMENT_1_1,
    INTEGRITY_REQUIREMENT_1_1_1,
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
from ssvc.decision_points.cvss.supplemental.automatable import AUTOMATABLE_1
from ssvc.decision_points.cvss.supplemental.provider_urgency import (
    PROVIDER_URGENCY_1,
)
from ssvc.decision_points.cvss.supplemental.recovery import RECOVERY_1
from ssvc.decision_points.cvss.supplemental.safety import SAFETY_1
from ssvc.decision_points.cvss.supplemental.value_density import (
    VALUE_DENSITY_1,
)
from ssvc.decision_points.cvss.supplemental.vulnerability_response_effort import (
    VULNERABILITY_RESPONSE_EFFORT_1,
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

# Instantiate the CVSS v1 decision point group
_BASE_1 = [
    ACCESS_VECTOR_1,
    ACCESS_COMPLEXITY_1,
    AUTHENTICATION_1,
    CONFIDENTIALITY_IMPACT_1,
    INTEGRITY_IMPACT_1,
    AVAILABILITY_IMPACT_1,
    IMPACT_BIAS_1,
]
_TEMPORAL_1 = [
    EXPLOITABILITY_1,
    REMEDIATION_LEVEL_1,
    REPORT_CONFIDENCE_1,
]
_ENVIRONMENTAL_1 = [
    COLLATERAL_DAMAGE_POTENTIAL_1,
    TARGET_DISTRIBUTION_1,
]

CVSSv1_B = SsvcDecisionPointGroup(
    name="CVSS",
    version="1.0",
    description="CVSS v1 decision points",
    decision_points=tuple(_BASE_1),
)

CVSSv1_BT = SsvcDecisionPointGroup(
    name="CVSS",
    version="1.0",
    description="CVSS v1 decision points",
    decision_points=tuple(_BASE_1 + _TEMPORAL_1),
)

CVSSv1_BTE = SsvcDecisionPointGroup(
    name="CVSS",
    version="1.0",
    description="CVSS v1 decision points",
    decision_points=tuple(_BASE_1 + _TEMPORAL_1 + _ENVIRONMENTAL_1),
)

CVSSv1 = CVSSv1_BTE  # convenience alias

# CVSS v2 decision points

_BASE_2 = [
    ACCESS_VECTOR_2,
    ACCESS_COMPLEXITY_2,
    AUTHENTICATION_2,
    CONFIDENTIALITY_IMPACT_1,
    INTEGRITY_IMPACT_1,
    AVAILABILITY_IMPACT_1,
]
_TEMPORAL_2 = [
    EXPLOITABILITY_1_1,
    REMEDIATION_LEVEL_1_1,
    REPORT_CONFIDENCE_1_1,
]
_ENVIRONMENTAL_2 = [
    COLLATERAL_DAMAGE_POTENTIAL_2,
    TARGET_DISTRIBUTION_1_1,
    CONFIDENTIALITY_REQUIREMENT_1,
    INTEGRITY_REQUIREMENT_1,
    AVAILABILITY_REQUIREMENT_1,
]

CVSSv2_B = SsvcDecisionPointGroup(
    name="CVSS Version 2 Base Metrics",
    description="Base metrics for CVSS v2",
    version="2.0",
    decision_points=tuple(_BASE_2),
)

CVSSv2_BT = SsvcDecisionPointGroup(
    name="CVSS Version 2 Base and Temporal Metrics",
    description="Base and Temporal metrics for CVSS v2",
    version="2.0",
    decision_points=tuple(_BASE_2 + _TEMPORAL_2),
)

CVSSv2_BTE = SsvcDecisionPointGroup(
    name="CVSS Version 2 Base, Temporal, and Environmental Metrics",
    description="Base, Temporal, and Environmental metrics for CVSS v2",
    version="2.0",
    decision_points=tuple(_BASE_2 + _TEMPORAL_2 + _ENVIRONMENTAL_2),
)

CVSSv2 = CVSSv2_BTE  # convenience alias

# CVSS v3 decision points
_BASE_3 = [
    ATTACK_VECTOR_3,
    ATTACK_COMPLEXITY_3,
    PRIVILEGES_REQUIRED_1,
    USER_INTERACTION_1,
    SCOPE,
    CONFIDENTIALITY_IMPACT_2,
    INTEGRITY_IMPACT_2,
    AVAILABILITY_IMPACT_2,
]
_TEMPORAL_3 = [
    EXPLOIT_CODE_MATURITY_1_2,
    REMEDIATION_LEVEL_1_1,
    REPORT_CONFIDENCE_2,
]

_ENVIRONMENTAL_3 = [modify_3(dp) for dp in _BASE_3]
_ENVIRONMENTAL_3.extend(
    [
        CONFIDENTIALITY_REQUIREMENT_1_1,
        INTEGRITY_REQUIREMENT_1_1,
        AVAILABILITY_REQUIREMENT_1_1,
    ]
)

CVSSv3_B = SsvcDecisionPointGroup(
    name="CVSS Version 3 Base Metrics",
    description="Base metrics for CVSS v3",
    version="3.0",
    decision_points=tuple(_BASE_3),
)

CVSSv3_BT = SsvcDecisionPointGroup(
    name="CVSS Version 3 Base and Temporal Metrics",
    description="Base and Temporal metrics for CVSS v3",
    version="3.0",
    decision_points=tuple(_BASE_3 + _TEMPORAL_3),
)

CVSSv3_BTE = SsvcDecisionPointGroup(
    name="CVSS Version 3 Base, Temporal, and Environmental Metrics",
    description="Base, Temporal, and Environmental metrics for CVSS v3",
    version="3.0",
    decision_points=tuple(_BASE_3 + _TEMPORAL_3 + _ENVIRONMENTAL_3),
)

CVSSv3 = CVSSv3_BTE  # convenience alias

# CVSS v4 decision points

_EXPLOITABILITY_4 = [
    ATTACK_VECTOR_3_0_1,
    ATTACK_COMPLEXITY_3_0_1,
    ATTACK_REQUIREMENTS_1,
    PRIVILEGES_REQUIRED_1_0_1,
    USER_INTERACTION_2,
]
_IMPACT_4 = [
    CONFIDENTIALITY_IMPACT_2_0_1,
    INTEGRITY_IMPACT_2_0_1,
    AVAILABILITY_IMPACT_2_0_1,
    SUBSEQUENT_CONFIDENTIALITY_IMPACT_1,
    SUBSEQUENT_INTEGRITY_IMPACT_1,
    SUBSEQUENT_AVAILABILITY_IMPACT_1,
]
_BASE_4 = _EXPLOITABILITY_4 + _IMPACT_4

# note: CVSS v4 does more than just insert "modified" in front of the name and "M" in front of the key
_ENVIRONMENTAL_4 = [modify_4(dp) for dp in _BASE_4]
_ENVIRONMENTAL_4.extend(
    [
        CONFIDENTIALITY_REQUIREMENT_1_1_1,
        INTEGRITY_REQUIREMENT_1_1_1,
        AVAILABILITY_REQUIREMENT_1_1_1,
    ]
)
_THREAT_4 = [
    EXPLOIT_MATURITY_2,
]

_SUPPLEMENTAL_4 = [
    SAFETY_1,
    AUTOMATABLE_1,
    PROVIDER_URGENCY_1,
    RECOVERY_1,
    VALUE_DENSITY_1,
    VULNERABILITY_RESPONSE_EFFORT_1,
]
# CVSS-B	Base metrics
CVSSv4_B = SsvcDecisionPointGroup(
    name="CVSSv4 Base Metrics",
    description="Base metrics for CVSS v4",
    version="1.0.0",
    decision_points=tuple(_BASE_4),
)

# CVSS-BE	Base and Environmental metrics
CVSSv4_BE = SsvcDecisionPointGroup(
    name="CVSSv4 Base and Environmental Metrics",
    description="Base and Environmental metrics for CVSS v4",
    version="1.0.0",
    decision_points=tuple(_BASE_4 + _ENVIRONMENTAL_4),
)

# CVSS-BT	Base and Threat metrics
CVSSv4_BT = SsvcDecisionPointGroup(
    name="CVSSv4 Base and Threat Metrics",
    description="Base and Threat metrics for CVSS v4",
    version="1.0.0",
    decision_points=tuple(_BASE_4 + _THREAT_4),
)

# CVSS-BTE
CVSSv4_BTE = SsvcDecisionPointGroup(
    name="CVSSv4 Base, Threat, and Environmental Metrics",
    description="Base, Threat, and Environmental metrics for CVSS v4",
    version="1.0.0",
    decision_points=tuple(_BASE_4 + _THREAT_4 + _ENVIRONMENTAL_4),
)

CVSSv4 = SsvcDecisionPointGroup(
    name="CVSSv4",
    description="All decision points for CVSS v4 (including supplemental metrics)",
    version="1.0.0",
    decision_points=tuple(_BASE_4 + _THREAT_4 + _ENVIRONMENTAL_4 + _SUPPLEMENTAL_4),
)

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

CVSSv4_EQ = CVSSv4_Equivalence_Sets  # convenience alias


def main():
    for group in [
        CVSSv1_B,
        CVSSv1_BT,
        CVSSv1_BTE,
        CVSSv2_B,
        CVSSv2_BT,
        CVSSv2_BTE,
        CVSSv3_B,
        CVSSv3_BT,
        CVSSv3_BTE,
        CVSSv4_B,
        CVSSv4_BE,
        CVSSv4_BT,
        CVSSv4_BTE,
        CVSSv4_Equivalence_Sets,
        CVSSv4,
    ]:
        print(f"## {group.name} v{group.version}")
        print(group.model_dump_json(indent=2))
        print()


if __name__ == "__main__":
    main()
