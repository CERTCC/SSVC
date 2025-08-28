#!/usr/bin/env python
"""
Models CVSS vectors as SSVC decision point groups
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
    AVAILABILITY_IMPACT_3_0_0,
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
    CONFIDENTIALITY_IMPACT_3_0_0,
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
from ssvc.decision_points.cvss.exploit_maturity import (
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
    INTEGRITY_IMPACT_3_0_0,
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
from ssvc.dp_groups.base import DecisionPointGroup

# Instantiate the CVSS v1 decision point group
BASE_1 = [
    ACCESS_VECTOR_1,
    ACCESS_COMPLEXITY_1,
    AUTHENTICATION_1,
    CONFIDENTIALITY_IMPACT_1,
    INTEGRITY_IMPACT_1,
    AVAILABILITY_IMPACT_1,
    IMPACT_BIAS_1,
]
"""List of CVSS v1 Base decision points"""

TEMPORAL_1 = [
    EXPLOITABILITY_1,
    REMEDIATION_LEVEL_1,
    REPORT_CONFIDENCE_1,
]
"""List of CVSS v1 Temporal decision points"""

ENVIRONMENTAL_1 = [
    COLLATERAL_DAMAGE_POTENTIAL_1,
    TARGET_DISTRIBUTION_1,
]
"""List of CVSS v1 Environmental decision points"""

CVSSv1_B = DecisionPointGroup(
    name="CVSS",
    version="1.0.0",
    definition="CVSS v1 decision points",
    decision_points=tuple(BASE_1),
)
"""CVSS v1 Base Metrics"""

CVSSv1_BT = DecisionPointGroup(
    name="CVSS",
    version="1.0.0",
    definition="CVSS v1 decision points",
    decision_points=tuple(BASE_1 + TEMPORAL_1),
)
"""CVSS v1 Base and Temporal Metrics"""

CVSSv1_BTE = DecisionPointGroup(
    name="CVSS",
    version="1.0.0",
    definition="CVSS v1 decision points",
    decision_points=tuple(BASE_1 + TEMPORAL_1 + ENVIRONMENTAL_1),
)
"""CVSS v1 Base, Temporal, and Environmental Metrics"""

CVSSv1 = CVSSv1_BTE  # convenience alias

# CVSS v2 decision points

BASE_2 = [
    ACCESS_VECTOR_2,
    ACCESS_COMPLEXITY_2,
    AUTHENTICATION_2,
    CONFIDENTIALITY_IMPACT_1,
    INTEGRITY_IMPACT_1,
    AVAILABILITY_IMPACT_1,
]
"""List of CVSS v2 Base decision points"""

TEMPORAL_2 = [
    EXPLOITABILITY_1_1,
    REMEDIATION_LEVEL_1_1,
    REPORT_CONFIDENCE_1_1,
]
"""List of CVSS v2 Temporal decision points"""

ENVIRONMENTAL_2 = [
    COLLATERAL_DAMAGE_POTENTIAL_2,
    TARGET_DISTRIBUTION_1_1,
    CONFIDENTIALITY_REQUIREMENT_1,
    INTEGRITY_REQUIREMENT_1,
    AVAILABILITY_REQUIREMENT_1,
]
"""List of CVSS v2 Environmental decision points"""

CVSSv2_B = DecisionPointGroup(
    name="CVSS Version 2 Base Metrics",
    definition="Base metrics for CVSS v2",
    version="2.0.0",
    decision_points=tuple(BASE_2),
)
"""CVSS v2 Base Metrics"""

CVSSv2_BT = DecisionPointGroup(
    name="CVSS Version 2 Base and Temporal Metrics",
    definition="Base and Temporal metrics for CVSS v2",
    version="2.0.0",
    decision_points=tuple(BASE_2 + TEMPORAL_2),
)
"""CVSS v2 Base and Temporal Metrics"""

CVSSv2_BTE = DecisionPointGroup(
    name="CVSS Version 2 Base, Temporal, and Environmental Metrics",
    definition="Base, Temporal, and Environmental metrics for CVSS v2",
    version="2.0.0",
    decision_points=tuple(BASE_2 + TEMPORAL_2 + ENVIRONMENTAL_2),
)
"""CVSS v2 Base, Temporal, and Environmental Metrics"""

CVSSv2 = CVSSv2_BTE  # convenience alias

# CVSS v3 decision points
BASE_3 = [
    ATTACK_VECTOR_3,
    ATTACK_COMPLEXITY_3,
    PRIVILEGES_REQUIRED_1,
    USER_INTERACTION_1,
    SCOPE,
    CONFIDENTIALITY_IMPACT_2,
    INTEGRITY_IMPACT_2,
    AVAILABILITY_IMPACT_2,
]
"""List of CVSS v3 Base decision points"""

TEMPORAL_3 = [
    EXPLOIT_CODE_MATURITY_1_2,
    REMEDIATION_LEVEL_1_1,
    REPORT_CONFIDENCE_2,
]
"""List of CVSS v3 Temporal decision points"""

ENVIRONMENTAL_3 = [modify_3(dp) for dp in BASE_3] + [
    CONFIDENTIALITY_REQUIREMENT_1_1,
    INTEGRITY_REQUIREMENT_1_1,
    AVAILABILITY_REQUIREMENT_1_1,
]
"""List of CVSS v3 Environmental decision points"""


CVSSv3_B = DecisionPointGroup(
    name="CVSS Version 3 Base Metrics",
    definition="Base metrics for CVSS v3",
    version="3.0.0",
    decision_points=tuple(BASE_3),
)
"""CVSS v3 Base Metrics"""

CVSSv3_BT = DecisionPointGroup(
    name="CVSS Version 3 Base and Temporal Metrics",
    definition="Base and Temporal metrics for CVSS v3",
    version="3.0.0",
    decision_points=tuple(BASE_3 + TEMPORAL_3),
)
"""CVSS v3 Base and Temporal Metrics"""

CVSSv3_BTE = DecisionPointGroup(
    name="CVSS Version 3 Base, Temporal, and Environmental Metrics",
    definition="Base, Temporal, and Environmental metrics for CVSS v3",
    version="3.0.0",
    decision_points=tuple(BASE_3 + TEMPORAL_3 + ENVIRONMENTAL_3),
)
"""CVSS v3 Base, Temporal, and Environmental Metrics"""

CVSSv3 = CVSSv3_BTE  # convenience alias

# CVSS v4 decision points

EXPLOITABILITY_4 = [
    ATTACK_VECTOR_3_0_1,
    ATTACK_COMPLEXITY_3_0_1,
    ATTACK_REQUIREMENTS_1,
    PRIVILEGES_REQUIRED_1_0_1,
    USER_INTERACTION_2,
]
"""List of CVSS v4 Exploitability decision points"""

IMPACT_4 = [
    CONFIDENTIALITY_IMPACT_3_0_0,
    INTEGRITY_IMPACT_3_0_0,
    AVAILABILITY_IMPACT_3_0_0,
    SUBSEQUENT_CONFIDENTIALITY_IMPACT_1,
    SUBSEQUENT_INTEGRITY_IMPACT_1,
    SUBSEQUENT_AVAILABILITY_IMPACT_1,
]
"""List of CVSS v4 Impact decision points"""

BASE_4 = EXPLOITABILITY_4 + IMPACT_4
"""List of CVSS v4 Base decision points"""

# note: CVSS v4 does more than just insert "modified" in front of the name and "M" in front of the key
ENVIRONMENTAL_4 = [modify_4(dp) for dp in BASE_4] + [
    CONFIDENTIALITY_REQUIREMENT_1_1_1,
    INTEGRITY_REQUIREMENT_1_1_1,
    AVAILABILITY_REQUIREMENT_1_1_1,
]
"""List of CVSS v4 Environmental decision points"""

THREAT_4 = [
    EXPLOIT_MATURITY_2,
]
"""List of CVSS v4 Threat decision points"""

SUPPLEMENTAL_4 = [
    SAFETY_1,
    AUTOMATABLE_1,
    PROVIDER_URGENCY_1,
    RECOVERY_1,
    VALUE_DENSITY_1,
    VULNERABILITY_RESPONSE_EFFORT_1,
]
"""List of CVSS v4 Supplemental decision points"""

# CVSS-B	Base metrics
CVSSv4_B = DecisionPointGroup(
    name="CVSSv4 Base Metrics",
    definition="Base metrics for CVSS v4",
    version="4.0.0",
    decision_points=tuple(BASE_4),
)
"""CVSS v4 Base Metrics"""

# CVSS-BE	Base and Environmental metrics
CVSSv4_BE = DecisionPointGroup(
    name="CVSSv4 Base and Environmental Metrics",
    definition="Base and Environmental metrics for CVSS v4",
    version="4.0.0",
    decision_points=tuple(BASE_4 + ENVIRONMENTAL_4),
)
"""CVSS v4 Base and Environmental Metrics"""

# CVSS-BT	Base and Threat metrics
CVSSv4_BT = DecisionPointGroup(
    name="CVSSv4 Base and Threat Metrics",
    definition="Base and Threat metrics for CVSS v4",
    version="4.0.0",
    decision_points=tuple(BASE_4 + THREAT_4),
)
"""CVSS v4 Base and Threat Metrics"""

# CVSS-BTE
CVSSv4_BTE = DecisionPointGroup(
    name="CVSSv4 Base, Threat, and Environmental Metrics",
    definition="Base, Threat, and Environmental metrics for CVSS v4",
    version="4.0.0",
    decision_points=tuple(BASE_4 + THREAT_4 + ENVIRONMENTAL_4),
)
"""CVSS v4 Base, Threat, and Environmental Metrics"""

CVSSv4 = DecisionPointGroup(
    name="CVSSv4",
    definition="All decision points for CVSS v4 (including supplemental metrics)",
    version="4.0.0",
    decision_points=tuple(
        BASE_4 + THREAT_4 + ENVIRONMENTAL_4 + SUPPLEMENTAL_4
    ),
)
"""CVSS v4 All Metrics"""

CVSSv4_Equivalence_Sets = DecisionPointGroup(
    name="CVSSv4 EQ Sets",
    definition="Equivalence Sets for CVSS v4",
    version="4.0.0",
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
