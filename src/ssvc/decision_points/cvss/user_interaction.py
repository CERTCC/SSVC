#!/usr/bin/env python
"""
Models CVSS User Interaction as an SSVC decision point.
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

_REQUIRED = DecisionPointValue(
    name="Required",
    key="R",
    definition="Successful exploitation of this vulnerability requires a user to take some action before the "
    "vulnerability can be exploited.",
)

_UI_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="The vulnerable system can be exploited without interaction from any user.",
)


USER_INTERACTION_1 = CvssDecisionPoint(
    name="User Interaction",
    definition="This metric captures the requirement for a user, other than the attacker, to participate in the "
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

_UI_NONE_2 = DecisionPointValue(
    name="None",
    key="N",
    definition="The vulnerable system can be exploited without interaction from any human user, other than the "
    "attacker.",
)

_PASSIVE = DecisionPointValue(
    name="Passive",
    key="P",
    definition="Successful exploitation of this vulnerability requires limited interaction by the targeted user with "
    "the vulnerable system and the attacker’s payload. These interactions would be considered involuntary "
    "and do not require that the user actively subvert protections built into the vulnerable system.",
)

_ACTIVE = DecisionPointValue(
    name="Active",
    key="A",
    definition="Successful exploitation of this vulnerability requires a targeted user to perform specific, "
    "conscious interactions with the vulnerable system and the attacker’s payload, or the user’s "
    "interactions would actively subvert protection mechanisms which would lead to exploitation of the "
    "vulnerability.",
)

USER_INTERACTION_2 = CvssDecisionPoint(
    name="User Interaction",
    key="UI",
    definition="This metric captures the requirement for a human user, other than the attacker, to participate "
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
