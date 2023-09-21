#!/usr/bin/env python
'''
file: supplier
author: adh
created_at: 9/21/23 11:41 AM
'''
from ssvc.decision_points.automatable import AUTOMATABLE_1 as AUTOMATABLE
from ssvc.decision_points.exploitation import EXPLOITATION_1 as EXPLOITATION
from ssvc.decision_points.public_safety_impact import PUBLIC_SAFETY_IMPACT_1 as PUBLIC_SAFETY_IMPACT
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1 as SAFETY_IMPACT
from ssvc.decision_points.technical_impact import TECHNICAL_IMPACT_1 as TECHNICAL_IMPACT
from ssvc.decision_points.utility import UTILITY_1_0_1 as UTILITY
from ssvc.decision_points.value_density import VALUE_DENSITY_1 as VALUE_DENSITY
from ssvc.dp_groups.base import SsvcDecisionPointGroup


def main():
    pass
    
if __name__=='__main__':
    main()
SUPPLIER_1 = SsvcDecisionPointGroup(
    name="Supplier",
    description="The decision points used by the supplier.",
    key="S",
    version="1.0.0",
    decision_points=[
        EXPLOITATION,
        UTILITY,
        AUTOMATABLE,
        VALUE_DENSITY,
        TECHNICAL_IMPACT,
        PUBLIC_SAFETY_IMPACT,
        SAFETY_IMPACT
    ],
)
