#!/usr/bin/env python
"""
file: authentication
author: adh
created_at: 9/20/23 1:39 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

AUTHENTICATION_1 = CvssDecisionPoint(
    name="Authentication",
    description="This metric measures whether or not an attacker needs to be authenticated to the target system in order to exploit the vulnerability.",
    key="AU",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Not Required",
            key="N",
            description="Authentication is not required to access or exploit the vulnerability.",
        ),
        SsvcValue(
            name="Required",
            key="R",
            description="Authentication is required to access and exploit the vulnerability.",
        ),
    ],
)

AUTHENTICATION_2 = deepcopy(AUTHENTICATION_1)
AUTHENTICATION_2.version = "2.0.0"
AUTHENTICATION_2.description = "This metric measures the number of times an attacker must authenticate to a target in order to exploit a vulnerability. This metric does not gauge the strength or complexity of the authentication process, only that an attacker is required to provide credentials before an exploit may occur.  The possible values for this metric are listed in Table 3. The fewer authentication instances that are required, the higher the vulnerability score."
AUTHENTICATION_2.values = [
    SsvcValue(
        name="Multiple",
        key="M",
        description="Exploiting the vulnerability requires that the attacker authenticate two or more times, even if the same credentials are used each time.",
    ),
    SsvcValue(
        name="Single",
        key="S",
        description="The vulnerability requires an attacker to be logged into the system (such as at a command line or via a desktop session or web interface).",
    ),
    SsvcValue(
        name="None",
        key="N",
        description="Authentication is not required to exploit the vulnerability.",
    ),
]


def main():
    print(AUTHENTICATION_1.to_json(indent=2))
    print(AUTHENTICATION_2.to_json(indent=2))


if __name__ == "__main__":
    main()
