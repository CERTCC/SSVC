#!/usr/bin/env python
"""
file: utility
author: adh
created_at: 9/21/23 9:55 AM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

SUPER_EFFECTIVE_2 = SsvcValue(
    name="Super Effective",
    key="S",
    description="Yes to automatable and concentrated value",
)

EFFICIENT_2 = SsvcValue(
    name="Efficient",
    key="E",
    description="Yes to automatable and diffuse value OR No to automatable and concentrated value",
)

LABORIOUS_2 = SsvcValue(
    name="Laborious", key="L", description="No to automatable and diffuse value"
)

SUPER_EFFECTIVE = SsvcValue(
    name="Super Effective",
    key="S",
    description="Rapid virulence and concentrated value",
)

EFFICIENT = SsvcValue(
    name="Efficient",
    key="E",
    description="Rapid virulence and diffuse value OR Slow virulence and concentrated value",
)

LABORIOUS = SsvcValue(
    name="Laborious", key="L", description="Slow virulence and diffuse value"
)

UTILITY_1 = SsvcDecisionPoint(
    name="Utility",
    description="The Usefulness of the Exploit to the Adversary",
    key="U",
    version="1.0.0",
    values=(
        LABORIOUS,
        EFFICIENT,
        SUPER_EFFECTIVE,
    ),
)

UTILITY_1_0_1 = SsvcDecisionPoint(
    name="Utility",
    description="The Usefulness of the Exploit to the Adversary",
    key="U",
    version="1.0.1",
    values=(
        LABORIOUS_2,
        EFFICIENT_2,
        SUPER_EFFECTIVE_2,
    ),
)


def main():
    print(UTILITY_1.to_json(indent=2))
    print(UTILITY_1_0_1.to_json(indent=2))


if __name__ == "__main__":
    main()
