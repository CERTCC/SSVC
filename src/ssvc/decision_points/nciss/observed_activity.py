#!/usr/bin/env python
"""
Provides the NCISS Observed Activity Decision Point.
"""
#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
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
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.nciss.base import NcissDecisionPoint

PREPARE = SsvcDecisionPointValue(
    key="P",
    name="Prepare",
    description="Prepare actions are actions taken to establish objectives, intent, and strategy; "
                "identify potential targets and attack vectors; "
                "identify resource requirements; "
                "and develop capabilities.",
)

ENGAGE = SsvcDecisionPointValue(
    key="E",
    name="Engage",
    description="Engage activities are actions taken against a specific target or target set prior to gaining, "
                "but with the intent to gain access to the victim's physical or virtual computer or information systems, "
                "networks, and data stores.",
)

PRESENCE = SsvcDecisionPointValue(
    key="R",
    name="Presence",
        description="Presence is the set of actions taken by the threat actor once access to the target physical or "
                    "virtual computer or information system has been achieved. "
                    "These actions establish and maintain conditions for the threat actor to perform intended actions "
                    "or operate at will against the host physical or virtual computer or information system, network, "
                    "or data stores.",
)

EFFECT = SsvcDecisionPointValue(
    key="F",
    name="Effect",
    description="Effects are outcomes of a threat actor’s actions "
                "on a victim’s physical or virtual computer or information systems, networks, and data stores.",
)


OBSERVED_ACTIVITY = NcissDecisionPoint(
    key="OA",
    name="Observed Activity",
    description="Observed activity describes what is known about threat actor activity on the network.",
    values=(PREPARE, ENGAGE, PRESENCE, EFFECT),
)

VERSIONS = (OBSERVED_ACTIVITY,)
LATEST = VERSIONS[-1]

def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == '__main__':
    main()
