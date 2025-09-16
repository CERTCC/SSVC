#!/usr/bin/env python

"""
Provides the Automatable decision point and its values.
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
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

RAPID = DecisionPointValue(
    name="Rapid",
    key="R",
    definition="Steps 1-4 of the of the kill chain can be reliably automated. If the vulnerability allows remote "
    "code execution or command injection, the default response should be rapid.",
)
SLOW = DecisionPointValue(
    name="Slow",
    key="S",
    definition="Steps 1-4 of the kill chain cannot be reliably automated for this vulnerability for some reason. "
    "These steps are reconnaissance, weaponization, delivery, and exploitation.",
)

VIRULENCE_1 = SsvcDecisionPoint(
    name="Virulence",
    definition="The speed at which the vulnerability can be exploited.",
    key="V",
    version="1.0.0",
    values=(
        SLOW,
        RAPID,
    ),
)


AUT_NO = DecisionPointValue(
    name="No",
    key="N",
    definition="Attackers cannot reliably automate steps 1-4 of the kill chain for this vulnerability. "
    "These steps are (1) reconnaissance, (2) weaponization, (3) delivery, and (4) exploitation.",
)
AUT_YES = DecisionPointValue(
    name="Yes",
    key="Y",
    definition="Attackers can reliably automate steps 1-4 of the kill chain.",
)


AUTOMATABLE_2 = SsvcDecisionPoint(
    name="Automatable",
    definition="Can an attacker reliably automate creating exploitation events for this vulnerability?",
    key="A",
    version="2.0.0",
    values=(AUT_NO, AUT_YES),
)

# always append new VERSIONS to this list, do not remove old ones
VERSIONS = (VIRULENCE_1, AUTOMATABLE_2)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
