#!/usr/bin/env python
"""
Models the CVSS Attack Complexity (formerly known as Access Complexity) metric as an SSVC decision point.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
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
from ssvc.decision_points.helpers import print_versions_and_diffs

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

LOW_4 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="The attacker must take no measurable action to exploit the vulnerability. The attack requires no "
    "target-specific circumvention to exploit the vulnerability. An attacker can expect repeatable "
    "success against the vulnerable system. ",
)

HIGH_4 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="The successful attack depends on the evasion or circumvention of security-enhancing "
    "techniques in place that would otherwise hinder the attack. These include: Evasion of exploit "
    "mitigation techniques. The attacker must have additional methods available to bypass security "
    "measures in place.",
)

ATTACK_COMPLEXITY_3_0_1 = CvssDecisionPoint(
    name="Attack Complexity",
    description="This metric captures measurable actions that must be taken by the attacker to actively evade or "
    "circumvent existing built-in security-enhancing conditions in order to obtain a working exploit. ",
    key="AC",
    version="3.0.1",
    values=(
        LOW_4,
        HIGH_4,
    ),
)
"""
Defines LOW and HIGH values for CVSS Attack Complexity.
"""


VERSIONS = (
    ACCESS_COMPLEXITY_1,
    ACCESS_COMPLEXITY_2,
    ATTACK_COMPLEXITY_3,
    ATTACK_COMPLEXITY_3_0_1,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
