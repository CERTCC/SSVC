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
from ssvc.decision_points.base import DecisionPointValue as DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc_.base import SsvcDecisionPoint

_DECLINE = DecisionPointValue(name="Decline", key="D", description="Decline")

_TRACK = DecisionPointValue(name="Track", key="T", description="Track")

_COORDINATE = DecisionPointValue(name="Coordinate", key="C", description="Coordinate")

COORDINATE = SsvcDecisionPoint(
    name="Decline, Track, Coordinate",
    key="COORDINATE",
    description="The coordinate outcome group.",
    version="1.0.0",
    values=(
        _DECLINE,
        _TRACK,
        _COORDINATE,
    ),
)
"""
The coordinate outcome group.
"""

VERSIONS = (COORDINATE,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
