#!/usr/bin/env python
'''
file: coordinator_triage
author: adh
created_at: 9/21/23 11:40 AM
'''
from ssvc.decision_points.public_safety_impact import PUBLIC_SAFETY_IMPACT_1 as PUBLIC_SAFETY_IMPACT
from ssvc.decision_points.report_credibility import REPORT_CREDIBILITY_1 as REPORT_CREDIBILITY
from ssvc.decision_points.report_public import REPORT_PUBLIC_1 as REPORT_PUBLIC
from ssvc.decision_points.supplier_cardinality import SUPPLIER_CARDINALITY_1 as SUPPLIER_CARDINALITY
from ssvc.decision_points.supplier_contacted import SUPPLIER_CONTACTED_1 as SUPPLIER_CONTACTED
from ssvc.decision_points.supplier_engagement import SUPPLIER_ENGAGEMENT_1 as SUPPLIER_ENGAGEMENT
from ssvc.decision_points.utility import UTILITY_1_0_1 as UTILITY
from ssvc.dp_groups.base import SsvcDecisionPointGroup


def main():
    pass
    
if __name__=='__main__':
    main()
COORDINATOR_TRIAGE_1 = SsvcDecisionPointGroup(
    name="Coordinator Triage",
    description="The decision points used by the coordinator during triage.",
    key="CT",
    version="1.0.0",
    decision_points=[
        REPORT_PUBLIC,
        SUPPLIER_CONTACTED,
        REPORT_CREDIBILITY,
        SUPPLIER_CARDINALITY,
        SUPPLIER_ENGAGEMENT,
        UTILITY,
        PUBLIC_SAFETY_IMPACT,
    ],
)
