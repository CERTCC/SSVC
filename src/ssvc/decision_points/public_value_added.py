#!/usr/bin/env python
'''
file: public_value_added
author: adh
created_at: 9/21/23 11:27 AM
'''

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

PUBLIC_VALUE_ADDED_1 = SsvcDecisionPoint(
    name="Public Value Added",
    description="How much value would a publication from the coordinator benefit the broader community?",
    key="PVA",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Precedence",
            key="P",
            description="The publication would be the first publicly available, or be coincident with the first publicly available.",
        ),
        SsvcValue(
            name="Ampliative",
            key="A",
            description="Amplifies and/or augments the existing public information about the vulnerability, for example, adds additional detail, addresses or corrects errors in other public information, draws further attention to the vulnerability, etc.",
        ),
        SsvcValue(
            name="Limited",
            key="L",
            description="Minimal value added to the existing public information because existing information is already high quality and in multiple outlets.",
        ),
    ],
)

def main():
    pass


if __name__ == '__main__':
    main()
