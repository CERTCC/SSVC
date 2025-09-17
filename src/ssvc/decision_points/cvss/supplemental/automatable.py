#!/usr/bin/env python
"""
Provides the CVSS supplemental metric Automatable
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
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

NO = DecisionPointValue(
    name="No",
    key="N",
    definition="Attackers cannot reliably automate all 4 steps of the kill chain for this vulnerability for "
    "some reason. These steps are reconnaissance, weaponization, delivery, and exploitation.",
)
YES = DecisionPointValue(
    name="Yes",
    key="Y",
    definition="Attackers can reliably automate all 4 steps of the kill chain. These steps are "
    "reconnaissance, weaponization, delivery, and exploitation (e.g., the vulnerability is "
    '"wormable").',
)
AUTOMATABLE_1 = CvssDecisionPoint(
    name="Automatable",
    definition='The "Automatable" metric captures the answer to the question "Can an attacker automate exploitation '
    'events for this vulnerability across multiple targets?" based on steps 1-4 of the kill chain.',
    key="AU",
    version="1.0.0",
    values=(
        NO,
        YES,
        NOT_DEFINED_X,
    ),
)

VERSIONS = (AUTOMATABLE_1,)
LATEST = AUTOMATABLE_1


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
