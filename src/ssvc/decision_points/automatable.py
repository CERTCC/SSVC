#!/usr/bin/env python
"""
file: automatable
author: adh
created_at: 9/21/23 10:37 AM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue


AUT_NO = SsvcDecisionPointValue(
    name="No",
    key="N",
    description="Attackers cannot reliably automate steps 1-4 of the kill chain for this vulnerability. "
    "These steps are (1) reconnaissance, (2) weaponization, (3) delivery, and (4) exploitation.",
)
AUT_YES = SsvcDecisionPointValue(
    name="Yes",
    key="Y",
    description="Attackers can reliably automate steps 1-4 of the kill chain.",
)


AUTOMATABLE_1 = SsvcDecisionPoint(
    name="Automatable",
    description="Can an attacker reliably automate creating exploitation events for this vulnerability?",
    key="A",
    version="1.0.0",
    values=(AUT_NO, AUT_YES),
)


def main():
    print(AUTOMATABLE_1.to_json(indent=2))


if __name__ == "__main__":
    main()
