#!/usr/bin/env python
"""
Models the CVSS Attack Complexity (formerly known as Access Complexity) metric as an SSVC decision point.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_HIGH_3 = DecisionPointValue(
    name="High",
    key="H",
    definition="A successful attack depends on conditions beyond the attacker's control.",
)

_LOW_3 = DecisionPointValue(
    name="Low",
    key="L",
    definition="Specialized access conditions or extenuating circumstances do not exist. An attacker can expect "
    "repeatable success against the vulnerable component.",
)


_HIGH_2 = DecisionPointValue(
    name="High", key="H", definition="Specialized access conditions exist."
)
_MEDIUM = DecisionPointValue(
    name="Medium",
    key="M",
    definition="The access conditions are somewhat specialized.",
)
_LOW_2 = DecisionPointValue(
    name="Low",
    key="L",
    definition="Specialized access conditions or extenuating circumstances do not exist.",
)
_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="Specialized access conditions exist; for example: the system is exploitable during specific windows "
    "of time (a race condition), the system is exploitable under specific circumstances (nondefault "
    "configurations), or the system is exploitable with victim interaction (vulnerability exploitable "
    "only if user opens e-mail)",
)
_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="Specialized access conditions or extenuating circumstances do not exist; the system is always "
    "exploitable.",
)
ACCESS_COMPLEXITY_1 = CvssDecisionPoint(
    name="Access Complexity",
    definition="This metric measures the complexity of the attack required to exploit the vulnerability once an "
    "attacker has gained access to the target system.",
    key="AC",
    version="1.0.0",
    values=(
        _HIGH,
        _LOW,
    ),
)

ACCESS_COMPLEXITY_2 = CvssDecisionPoint(
    name="Access Complexity",
    definition="This metric measures the complexity of the attack required to exploit the vulnerability once an "
    "attacker has gained access to the target system.",
    key="AC",
    version="2.0.0",
    values=(
        _HIGH_2,
        _MEDIUM,
        _LOW_2,
    ),
)

ATTACK_COMPLEXITY_3 = CvssDecisionPoint(
    name="Attack Complexity",
    definition="This metric describes the conditions beyond the attacker's control that must exist in order to "
    "exploit the vulnerability.",
    key="AC",
    version="3.0.0",
    values=(
        _HIGH_3,
        _LOW_3,
    ),
)
"""
Defines LOW and HIGH values for CVSS Attack Complexity.
"""

LOW_4 = DecisionPointValue(
    name="Low",
    key="L",
    definition="The attacker must take no measurable action to exploit the vulnerability. The attack requires no "
    "target-specific circumvention to exploit the vulnerability. An attacker can expect repeatable "
    "success against the vulnerable system. ",
)

HIGH_4 = DecisionPointValue(
    name="High",
    key="H",
    definition="The successful attack depends on the evasion or circumvention of security-enhancing "
    "techniques in place that would otherwise hinder the attack. These include: Evasion of exploit "
    "mitigation techniques. The attacker must have additional methods available to bypass security "
    "measures in place.",
)

ATTACK_COMPLEXITY_3_0_1 = CvssDecisionPoint(
    name="Attack Complexity",
    definition="This metric captures measurable actions that must be taken by the attacker to actively evade or "
    "circumvent existing built-in security-enhancing conditions in order to obtain a working exploit. ",
    key="AC",
    version="3.0.1",
    values=(
        HIGH_4,
        LOW_4,
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
