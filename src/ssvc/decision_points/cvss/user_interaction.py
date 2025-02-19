#!/usr/bin/env python
"""
Models CVSS User Interaction as an SSVC decision point.
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

_REQUIRED = SsvcDecisionPointValue(
    name="Required",
    key="R",
    description="Successful exploitation of this vulnerability requires a user to take some action before the "
    "vulnerability can be exploited.",
)

_UI_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="The vulnerable system can be exploited without interaction from any user.",
)


USER_INTERACTION_1 = CvssDecisionPoint(
    name="User Interaction",
    description="This metric captures the requirement for a user, other than the attacker, to participate in the "
    "successful compromise of the vulnerable component.",
    key="UI",
    version="1.0.0",
    values=(
        _REQUIRED,
        _UI_NONE,
    ),
)
"""
Defines None and Required values for CVSS User Interaction.
"""

_UI_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="The vulnerable system can be exploited without interaction from any human user, other than the "
    "attacker.",
)

_PASSIVE = SsvcDecisionPointValue(
    name="Passive",
    key="P",
    description="Successful exploitation of this vulnerability requires limited interaction by the targeted user with "
    "the vulnerable system and the attacker’s payload. These interactions would be considered involuntary "
    "and do not require that the user actively subvert protections built into the vulnerable system.",
)

_ACTIVE = SsvcDecisionPointValue(
    name="Active",
    key="A",
    description="Successful exploitation of this vulnerability requires a targeted user to perform specific, "
    "conscious interactions with the vulnerable system and the attacker’s payload, or the user’s "
    "interactions would actively subvert protection mechanisms which would lead to exploitation of the "
    "vulnerability.",
)

USER_INTERACTION_2 = CvssDecisionPoint(
    name="User Interaction",
    key="UI",
    description="This metric captures the requirement for a human user, other than the attacker, to participate "
    "in the successful compromise of the vulnerable system. This metric determines whether the "
    "vulnerability can be exploited solely at the will of the attacker, or whether a separate user "
    "(or user-initiated process) must participate in some manner. The resulting score is greatest "
    "when no user interaction is required.",
    version="2.0.0",
    values=(
        _ACTIVE,
        _PASSIVE,
        _UI_NONE_2,
    ),
)

VERSIONS = (USER_INTERACTION_1, USER_INTERACTION_2)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
