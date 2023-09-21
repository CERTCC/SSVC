#!/usr/bin/env python
'''
file: deployer
author: adh
created_at: 9/21/23 11:40 AM
'''
from ssvc.decision_points.automatable import AUTOMATABLE_1 as AUTOMATABLE
from ssvc.decision_points.exploitation import EXPLOITATION_1 as EXPLOITATION
from ssvc.decision_points.exposure import EXPOSURE_1_0_1 as EXPOSURE
from ssvc.decision_points.human_impact import HUMAN_IMPACT_1 as HUMAN_IMPACT
from ssvc.decision_points.mission_impact import MISSION_IMPACT_1 as MISSION_IMPACT
from ssvc.decision_points.utility import UTILITY_1_0_1 as UTILITY
from ssvc.decision_points.value_density import VALUE_DENSITY_1 as VALUE_DENSITY
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.dp_groups.v2 import SITUATED_SAFETY_IMPACT


def main():
    pass
    
if __name__=='__main__':
    main()
DEPLOYER_1 = SsvcDecisionPointGroup(
    name="Deployer",
    description="The decision points used by the deployer.",
    key="D",
    version="1.0.0",
    decision_points=[
        EXPLOITATION,
        EXPOSURE,
        UTILITY,
        AUTOMATABLE,
        VALUE_DENSITY,
        HUMAN_IMPACT,
        SITUATED_SAFETY_IMPACT,
        MISSION_IMPACT,
    ],
)
