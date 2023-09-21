#!/usr/bin/env python
'''
file: coordinator_publication
author: adh
created_at: 9/21/23 11:40 AM
'''
from ssvc.decision_points.exploitation import EXPLOITATION_1 as EXPLOITATION
from ssvc.decision_points.public_value_added import PUBLIC_VALUE_ADDED_1 as PUBLIC_VALUE_ADDED
from ssvc.decision_points.supplier_involvement import SUPPLIER_INVOLVEMENT_1 as SUPPLIER_INVOLVEMENT
from ssvc.dp_groups.base import SsvcDecisionPointGroup


def main():
    pass
    
if __name__=='__main__':
    main()
COORDINATOR_PUBLICATION_1 = SsvcDecisionPointGroup(
    name="Coordinator Publication",
    description="The decision points used by the coordinator during publication.",
    key="CP",
    version="1.0.0",
    decision_points=[
        SUPPLIER_INVOLVEMENT,
        EXPLOITATION,
        PUBLIC_VALUE_ADDED,
    ],
)
