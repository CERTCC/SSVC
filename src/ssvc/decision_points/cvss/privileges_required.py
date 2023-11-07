#!/usr/bin/env python
"""
Models the CVSS Privileges Required metric as an SSVC decision point.
"""
from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="The attacker is authorized with (i.e. requires) privileges that provide significant (e.g. administrative) control over the vulnerable component that could affect component-wide settings and files.",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="The attacker is authorized with (i.e. requires) privileges that provide basic user capabilities that could normally affect only settings and files owned by a user. Alternatively, an attacker with Low privileges may have the ability to cause an impact only to non-sensitive resources.",
)

_PR_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="The attacker is unauthorized prior to attack, and therefore does not require any access to settings or files to carry out an attack.",
)

PRIVILEGES_REQUIRED_1 = CvssDecisionPoint(
    name="Privileges Required",
    description="This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability.",
    key="PR",
    version="1.0.0",
    values=(
        _PR_NONE,
        _LOW,
        _HIGH,
    ),
)
"""
Defines None, Low, and High values for CVSS Privileges Required.
"""


def main():
    print(PRIVILEGES_REQUIRED_1.to_json(indent=2))


if __name__ == "__main__":
    main()
