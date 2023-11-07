#!/usr/bin/env python
"""
Models the CVSS Attack Complexity (formerly known as Access Complexity) metric as an SSVC decision point.
"""
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_HIGH_3 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="A successful attack depends on conditions beyond the attacker's control.",
)

_LOW_3 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Specialized access conditions or extenuating circumstances do not exist. An attacker can expect "
    "repeatable success against the vulnerable component.",
)


_HIGH_2 = SsvcDecisionPointValue(
    name="High", key="H", description="Specialized access conditions exist."
)
_MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="The access conditions are somewhat specialized.",
)
_LOW_2 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Specialized access conditions or extenuating circumstances do not exist.",
)
_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Specialized access conditions exist; for example: the system is exploitable during specific windows "
    "of time (a race condition), the system is exploitable under specific circumstances (nondefault "
    "configurations), or the system is exploitable with victim interaction (vulnerability exploitable "
    "only if user opens e-mail)",
)
_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Specialized access conditions or extenuating circumstances do not exist; the system is always "
    "exploitable.",
)
ACCESS_COMPLEXITY_1 = CvssDecisionPoint(
    name="Access Complexity",
    description="This metric measures the complexity of the attack required to exploit the vulnerability once an "
    "attacker has gained access to the target system.",
    key="AC",
    version="1.0.0",
    values=(
        _LOW,
        _HIGH,
    ),
)

ACCESS_COMPLEXITY_2 = CvssDecisionPoint(
    name="Access Complexity",
    description="This metric measures the complexity of the attack required to exploit the vulnerability once an "
    "attacker has gained access to the target system.",
    key="AC",
    version="2.0.0",
    values=(
        _LOW_2,
        _MEDIUM,
        _HIGH_2,
    ),
)

ATTACK_COMPLEXITY_3 = CvssDecisionPoint(
    name="Attack Complexity",
    description="This metric describes the conditions beyond the attacker's control that must exist in order to "
    "exploit the vulnerability.",
    key="AC",
    version="3.0.0",
    values=(
        _LOW_3,
        _HIGH_3,
    ),
)
"""
Defines LOW and HIGH values for CVSS Attack Complexity.
"""


def main():
    print(ACCESS_COMPLEXITY_1.to_json(indent=2))
    print(ACCESS_COMPLEXITY_2.to_json(indent=2))
    print(ATTACK_COMPLEXITY_3.to_json(indent=2))


if __name__ == "__main__":
    main()
