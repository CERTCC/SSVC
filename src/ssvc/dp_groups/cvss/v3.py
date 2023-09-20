#!/usr/bin/env python
"""
file: v3
author: adh
created_at: 9/20/23 2:30 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.decision_points.cvss.attack_complexity import (
    ATTACK_COMPLEXITY_1 as ATTACK_COMPLEXITY,
)
from ssvc.decision_points.cvss.attack_vector import ATTACK_VECTOR_1 as ATTACK_VECTOR
from ssvc.decision_points.cvss.availability_impact import (
    AVAILABILITY_IMPACT_2 as AVAILABILITY_IMPACT,
)
from ssvc.decision_points.cvss.availability_requirement import (
    AVAILABILITY_REQUIREMENT_1 as AVAILABILITY_REQUIREMENT,
)
from ssvc.decision_points.cvss.confidentiality_impact import (
    CONFIDENTIALITY_IMPACT_2 as CONFIDENTIALITY_IMPACT,
)
from ssvc.decision_points.cvss.confidentiality_requirement import (
    CONFIDENTIALITY_REQUIREMENT_1 as CONFIDENTIALITY_REQUIREMENT,
)
from ssvc.decision_points.cvss.exploitability import (
    EXPLOIT_CODE_MATURITY_1_1_1 as EXPLOIT_CODE_MATURITY,
)
from ssvc.decision_points.cvss.integrity_impact import (
    INTEGRITY_IMPACT_2 as INTEGRITY_IMPACT,
)
from ssvc.decision_points.cvss.integrity_requirement import (
    INTEGRITY_REQUIREMENT_1 as INTEGRITY_REQUIREMENT,
)
from ssvc.decision_points.cvss.privileges_required import (
    PRIVILEGES_REQUIRED_1 as PRIVILEGES_REQUIRED,
)
from ssvc.decision_points.cvss.remediation_level import (
    REMEDIATION_LEVEL_1_1 as REMEDIATION_LEVEL,
)
from ssvc.decision_points.cvss.report_confidence import (
    REPORT_CONFIDENCE_2 as REPORT_CONFIDENCE,
)
from ssvc.decision_points.cvss.scope import SCOPE_1 as SCOPE
from ssvc.decision_points.cvss.user_interaction import (
    USER_INTERACTION_1 as USER_INTERACTION,
)


def _modify(obj):
    """
    Prepends "Modified " to the name and "M" to the key of the given object. Also adds a value of "Not Defined" to the
    values list.
    :param obj: the object to modify
    :return: the object
    """
    o = deepcopy(obj)
    o.name = "Modified " + o.name
    o.key = "M" + o.key
    nd = SsvcValue(name="Not Defined", key="ND", description="Ignore this value")
    o.values.append(nd)
    return o


MODIFIED_ATTACK_VECTOR = _modify(ATTACK_VECTOR)
MODIFIED_ATTACK_COMPLEXITY = _modify(ATTACK_COMPLEXITY)
MODIFIED_PRIVILEGES_REQUIRED = _modify(PRIVILEGES_REQUIRED)
MODIFIED_USER_INTERACTION = _modify(USER_INTERACTION)
MODIFIED_SCOPE = _modify(SCOPE)
MODIFIED_CONFIDENTIALITY_IMPACT = _modify(CONFIDENTIALITY_IMPACT)
MODIFIED_INTEGRITY_IMPACT = _modify(INTEGRITY_IMPACT)
MODIFIED_AVAILABILITY_IMPACT = _modify(AVAILABILITY_IMPACT)


CVSSv3 = SsvcDecisionPointGroup(
    name="CVSS Version 3",
    description="The Common Vulnerability Scoring System (CVSS) is a free and open industry standard for assessing the severity of computer system security vulnerabilities. CVSS attempts to assign severity scores to vulnerabilities, allowing responders to prioritize responses and resources according to threat. Scores are calculated based on a formula that depends on several metrics that approximate ease of exploit and the impact of exploit. Scores range from 0 to 10, with 10 being the most severe.",
    key="CVSSv3",
    version="3.0",
    decision_points=[
        ATTACK_VECTOR,
        ATTACK_COMPLEXITY,
        PRIVILEGES_REQUIRED,
        USER_INTERACTION,
        SCOPE,
        CONFIDENTIALITY_IMPACT,
        INTEGRITY_IMPACT,
        AVAILABILITY_IMPACT,
        EXPLOIT_CODE_MATURITY,
        REMEDIATION_LEVEL,
        REPORT_CONFIDENCE,
        CONFIDENTIALITY_REQUIREMENT,
        INTEGRITY_REQUIREMENT,
        AVAILABILITY_REQUIREMENT,
        MODIFIED_ATTACK_VECTOR,
        MODIFIED_ATTACK_COMPLEXITY,
        MODIFIED_PRIVILEGES_REQUIRED,
        MODIFIED_USER_INTERACTION,
        MODIFIED_SCOPE,
        MODIFIED_CONFIDENTIALITY_IMPACT,
        MODIFIED_INTEGRITY_IMPACT,
        MODIFIED_AVAILABILITY_IMPACT,
    ],
)


def main():
    print(CVSSv3.to_json(indent=2))


if __name__ == "__main__":
    main()
