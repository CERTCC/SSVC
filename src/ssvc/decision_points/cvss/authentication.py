#!/usr/bin/env python
"""
Models the CVSS Authentication metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_AUTH_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="Authentication is not required to exploit the vulnerability.",
)

_SINGLE = SsvcDecisionPointValue(
    name="Single",
    key="S",
    description="The vulnerability requires an attacker to be logged into the system (such as at a command line or via a desktop session or web interface).",
)

_MULTIPLE = SsvcDecisionPointValue(
    name="Multiple",
    key="M",
    description="Exploiting the vulnerability requires that the attacker authenticate two or more times, even if the same credentials are used each time.",
)

_REQUIRED = SsvcDecisionPointValue(
    name="Required",
    key="R",
    description="Authentication is required to access and exploit the vulnerability.",
)

_NOT_REQUIRED = SsvcDecisionPointValue(
    name="Not Required",
    key="N",
    description="Authentication is not required to access or exploit the vulnerability.",
)

AUTHENTICATION_1 = CvssDecisionPoint(
    name="Authentication",
    description="This metric measures whether or not an attacker needs to be authenticated to the target system in order to exploit the vulnerability.",
    key="Au",
    version="1.0.0",
    values=(
        _NOT_REQUIRED,
        _REQUIRED,
    ),
)
"""
Includes NOT_REQUIRED and REQUIRED values for CVSS Authentication.
"""

AUTHENTICATION_2 = CvssDecisionPoint(
    name="Authentication",
    description="This metric measures the number of times an attacker must authenticate to a target in order to exploit a vulnerability. This metric does not gauge the strength or complexity of the authentication process, only that an attacker is required to provide credentials before an exploit may occur.  The possible values for this metric are listed in Table 3. The fewer authentication instances that are required, the higher the vulnerability score.",
    key="Au",
    version="2.0.0",
    values=(
        _MULTIPLE,
        _SINGLE,
        _AUTH_NONE,
    ),
)
"""
Includes MULTIPLE, SINGLE, and AUTH_NONE values for CVSS Authentication.
"""


def main():
    print(AUTHENTICATION_1.to_json(indent=2))
    print(AUTHENTICATION_2.to_json(indent=2))


if __name__ == "__main__":
    main()
