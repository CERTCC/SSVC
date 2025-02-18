#!/usr/bin/env python
"""
Provides the CVSS supplemental metric Automatable
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

from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

NO = SsvcDecisionPointValue(name="No", key="N",
                               description="Attackers cannot reliably automate all 4 steps of the kill chain for this vulnerability for " \
                                           "some reason. These steps are reconnaissance, weaponization, delivery, and exploitation.", )
YES = SsvcDecisionPointValue(name="Yes", key="Y",
                               description="Attackers can reliably automate all 4 steps of the kill chain. These steps are " \
                                           "reconnaissance, weaponization, delivery, and exploitation (e.g., the vulnerability is " \
                                           '"wormable").', )
AUTOMATABLE_1 = CvssDecisionPoint(
    name="Automatable",
    description='The "Automatable" metric captures the answer to the question "Can an attacker automate exploitation '
    'events for this vulnerability across multiple targets?" based on steps 1-4 of the kill chain.',
    key="AU",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)

VERSIONS = (AUTOMATABLE_1,)
LATEST = AUTOMATABLE_1

def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
