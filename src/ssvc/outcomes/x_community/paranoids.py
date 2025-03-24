#!/usr/bin/env python

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

"""
Provides a decision point for the `x_community` namespace.
"""

from ssvc.decision_points.base import (
    DecisionPoint,
    DecisionPointValue as DecisionPointValue,
)
from ssvc.decision_points.helpers import print_versions_and_diffs

_TRACK_5 = DecisionPointValue(name="Track 5", key="5", description="Track")

_TRACK_CLOSELY_4 = DecisionPointValue(
    name="Track Closely 4", key="4", description="Track Closely"
)

_ATTEND_3 = DecisionPointValue(name="Attend 3", key="3", description="Attend")

_ATTEND_2 = DecisionPointValue(name="Attend 2", key="2", description="Attend")

_ACT_1 = DecisionPointValue(name="Act 1", key="1", description="Act")

_ACT_ASAP_0 = DecisionPointValue(name="Act ASAP 0", key="0", description="Act ASAP")

THE_PARANOIDS = DecisionPoint(
    name="theParanoids",
    key="PARANOIDS",
    description="PrioritizedRiskRemediation outcome group based on TheParanoids.",
    namespace="x_community",
    version="1.0.0",
    values=(
        _TRACK_5,
        _TRACK_CLOSELY_4,
        _ATTEND_3,
        _ATTEND_2,
        _ACT_1,
        _ACT_ASAP_0,
    ),
)
"""
Outcome group based on TheParanoids' PrioritizedRiskRemediation.
Their model is a 6-point scale, with 0 being the most urgent and 5 being the least.
See https://github.com/theparanoids/PrioritizedRiskRemediation
"""

VERSIONS = (THE_PARANOIDS,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
