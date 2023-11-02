#!/usr/bin/env python
"""
file: virulence
author: adh
created_at: 9/21/23 9:58 AM
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


def main():
    print(VIRULENCE_1.to_json(indent=2))


if __name__ == "__main__":
    main()
