#!/usr/bin/env python
"""
file: utility
author: adh
created_at: 9/21/23 9:55 AM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

UTILITY_1 = SsvcDecisionPoint(
    name="Utility",
    description="The Usefulness of the Exploit to the Adversary",
    key="U",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Laborious", key="L", description="Slow virulence and diffuse value"
        ),
        SsvcValue(
            name="Efficient",
            key="E",
            description="Rapid virulence and diffuse value OR Slow virulence and concentrated value",
        ),
        SsvcValue(
            name="Super Effective",
            key="S",
            description="Rapid virulence and concentrated value",
        ),
    ],
)

# SSVC v2 keeps same options but changes descriptions
UTILITY_1_0_1 = deepcopy(UTILITY_1)
UTILITY_1_0_1.version = "1.0.1"
UTILITY_1_0_1.values = [
    SsvcValue(
        name="Laborious", key="L", description="No to automatable and diffuse value"
    ),
    SsvcValue(
        name="Efficient",
        key="E",
        description="Yes to automatable and diffuse value OR No to automatable and concentrated value",
    ),
    SsvcValue(
        name="Super Effective",
        key="S",
        description="Yes to automatable and concentrated value",
    ),
]


def main():
    print(UTILITY_1.to_json(indent=2))
    print(UTILITY_1_0_1.to_json(indent=2))


if __name__ == "__main__":
    main()
