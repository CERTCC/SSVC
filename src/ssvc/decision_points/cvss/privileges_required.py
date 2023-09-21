#!/usr/bin/env python
"""
file: privileges_required
author: adh
created_at: 9/20/23 2:38 PM
"""
from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

HIGH = SsvcValue(
    name="High",
    key="H",
    description="The attacker is authorized with (i.e. requires) privileges that provide significant (e.g. administrative) control over the vulnerable component that could affect component-wide settings and files.",
)

LOW = SsvcValue(
    name="Low",
    key="L",
    description="The attacker is authorized with (i.e. requires) privileges that provide basic user capabilities that could normally affect only settings and files owned by a user. Alternatively, an attacker with Low privileges may have the ability to cause an impact only to non-sensitive resources.",
)

PR_NONE = SsvcValue(
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
        PR_NONE,
        LOW,
        HIGH,
    ),
)


def main():
    print(PRIVILEGES_REQUIRED_1.to_json(indent=2))


if __name__ == "__main__":
    main()
