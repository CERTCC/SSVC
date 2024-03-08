#!/usr/bin/env python
"""
file: automatable
author: adh
created_at: 9/21/23 10:37 AM
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

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

RAPID = SsvcDecisionPointValue(
    name="Rapid",
    key="R",
    description="Steps 1-4 of the of the kill chain can be reliably automated. If the vulnerability allows remote "
    "code execution or command injection, the default response should be rapid.",
)
SLOW = SsvcDecisionPointValue(
    name="Slow",
    key="S",
    description="Steps 1-4 of the kill chain cannot be reliably automated for this vulnerability for some reason. "
    "These steps are reconnaissance, weaponization, delivery, and exploitation.",
)

VIRULENCE_1 = SsvcDecisionPoint(
    name="Virulence",
    description="The speed at which the vulnerability can be exploited.",
    key="V",
    version="1.0.0",
    values=(
        SLOW,
        RAPID,
    ),
)


AUT_NO = SsvcDecisionPointValue(
    name="No",
    key="N",
    description="Attackers cannot reliably automate steps 1-4 of the kill chain for this vulnerability. "
    "These steps are (1) reconnaissance, (2) weaponization, (3) delivery, and (4) exploitation.",
)
AUT_YES = SsvcDecisionPointValue(
    name="Yes",
    key="Y",
    description="Attackers can reliably automate steps 1-4 of the kill chain.",
)


AUTOMATABLE_2 = SsvcDecisionPoint(
    name="Automatable",
    description="Can an attacker reliably automate creating exploitation events for this vulnerability?",
    key="A",
    version="2.0.0",
    values=(AUT_NO, AUT_YES),
)


def main():
    versions = (VIRULENCE_1, AUTOMATABLE_2)

    print_versions_and_diffs(versions)

if __name__ == "__main__":
    main()
