#!/usr/bin/env python
"""
file: v1
author: adh
created_at: 9/21/23 9:52 AM
"""
from ssvc.decision_points.exploitation import EXPLOITATION_1 as EXPLOITATION
from ssvc.decision_points.technical_impact import TECHNICAL_IMPACT_1 as TECHNICAL_IMPACT
from ssvc.decision_points.virulence import VIRULENCE_1 as VIRULENCE
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.decision_points.utility import UTILITY_1 as UTILITY

SSVCv1 = SsvcDecisionPointGroup(
    name="SSVCv1",
    description="The first version of the SSVC.",
    key="SSVCv1",
    version="1.0.0",
    decision_points=[
        EXPLOITATION,
        TECHNICAL_IMPACT,
        UTILITY,
        VIRULENCE,
    ],
)


def main():
    print(SSVCv1.to_json(indent=2))


if __name__ == "__main__":
    main()
