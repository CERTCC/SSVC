#!/usr/bin/env python
"""
file: v1
author: adh
created_at: 9/20/23 12:39 PM
"""

from ssvc.decision_points.base import SsvcDecisionPointGroup
from ssvc.decision_points.cvss.access_complexity import (
    ACCESS_COMPLEXITY_1 as ACCESS_COMPLEXITY,
)
from ssvc.decision_points.cvss.access_vector import ACCESS_VECTOR_1 as ACCESS_VECTOR
from ssvc.decision_points.cvss.authentication import AUTHENTICATION_1 as AUTHENTICATION
from ssvc.decision_points.cvss.availability_impact import (
    AVAILABILITY_IMPACT_1 as AVAILABILITY_IMPACT,
)
from ssvc.decision_points.cvss.collateral_damage_potential import (
    COLLATERAL_DAMAGE_POTENTIAL_1 as COLLATERAL_DAMAGE_POTENTIAL,
)
from ssvc.decision_points.cvss.confidentiality_impact import (
    CONFIDENTIALITY_IMPACT_1 as CONFIDENTIALITY_IMPACT,
)
from ssvc.decision_points.cvss.exploitability import (
    EXPLOITABILITY_1 as EXPLOITABILITY,
)
from ssvc.decision_points.cvss.impact_bias import IMPACT_BIAS
from ssvc.decision_points.cvss.integrity_impact import (
    INTEGRITY_IMPACT_1 as INTEGRITY_IMPACT,
)
from ssvc.decision_points.cvss.remediation_level import (
    REMEDIATION_LEVEL_1 as REMEDIATION_LEVEL,
)
from ssvc.decision_points.cvss.report_confidence import (
    REPORT_CONFIDENCE_1 as REPORT_CONFIDENCE,
)
from ssvc.decision_points.cvss.target_distribution import (
    TARGET_DISTRIBUTION_1 as TARGET_DISTRIBUTION,
)


# Instantiate the CVSS v1 decision point group
CVSSv1 = SsvcDecisionPointGroup(
    name="CVSS",
    version="1.0",
    key="CVSSv1",
    description="CVSS v1 decision points",
    decision_points=[
        ACCESS_VECTOR,
        ACCESS_COMPLEXITY,
        AUTHENTICATION,
        CONFIDENTIALITY_IMPACT,
        INTEGRITY_IMPACT,
        AVAILABILITY_IMPACT,
        IMPACT_BIAS,
        EXPLOITABILITY,
        REMEDIATION_LEVEL,
        REPORT_CONFIDENCE,
        COLLATERAL_DAMAGE_POTENTIAL,
        TARGET_DISTRIBUTION,
    ],
)


def main():
    print(CVSSv1.to_json(indent=2))


if __name__ == "__main__":
    main()
