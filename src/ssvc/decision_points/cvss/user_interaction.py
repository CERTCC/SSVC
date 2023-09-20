#!/usr/bin/env python
"""
file: user_interaction
author: adh
created_at: 9/20/23 2:38 PM
"""

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint


USER_INTERACTION_1 = CvssDecisionPoint(
    name="User Interaction",
    description="This metric captures the requirement for a user, other than the attacker, to participate in the successful compromise of the vulnerable component.",
    key="UI",
    version="1.0.0",
    values=[
        SsvcValue(
            name="None",
            key="N",
            description="The vulnerable system can be exploited without interaction from any user.",
        ),
        SsvcValue(
            name="Required",
            key="R",
            description="Successful exploitation of this vulnerability requires a user to take some action before the vulnerability can be exploited.",
        ),
    ],
)


def main():
    print(USER_INTERACTION_1.to_json(indent=2))


if __name__ == "__main__":
    main()
