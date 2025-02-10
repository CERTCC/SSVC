#!/usr/bin/env python

"""
Provides the Mission Impact decision point and its values.
"""

#  Copyright (c) 2024-2025 Carnegie Mellon University and Contributors.
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

MISSION_FAILURE = SsvcDecisionPointValue(
    name="Mission Failure",
    key="MF",
    description="Multiple or all mission essential functions fail; ability to recover those functions degraded; organization’s ability to deliver its overall mission fails",
)

MEF_FAILURE = SsvcDecisionPointValue(
    name="MEF Failure",
    key="MEF",
    description="Any one mission essential function fails for period of time longer than acceptable; overall mission of the organization degraded but can still be accomplished for a time",
)

MEF_CRIPPLED = SsvcDecisionPointValue(
    name="MEF Support Crippled",
    key="MSC",
    description="Activities that directly support essential functions are crippled; essential functions continue for a time",
)


MI_NED = SsvcDecisionPointValue(
    name="Non-Essential Degraded",
    key="NED",
    description="Degradation of non-essential functions; chronic degradation would eventually harm essential functions",
)

MI_NONE = SsvcDecisionPointValue(
    name="None", key="N", description="Little to no impact"
)

# combine MI_NONE and MI_NED into a single value
DEGRADED = SsvcDecisionPointValue(
    name="Degraded",
    key="D",
    description="Little to no impact up to degradation of non-essential functions; chronic degradation would eventually harm essential functions",
)


MISSION_IMPACT_1 = SsvcDecisionPoint(
    name="Mission Impact",
    description="Impact on Mission Essential Functions of the Organization",
    key="MI",
    version="1.0.0",
    values=(
        MI_NONE,
        MI_NED,
        MEF_CRIPPLED,
        MEF_FAILURE,
        MISSION_FAILURE,
    ),
)

# SSVC v2.1 combined None and Non-Essential Degraded into a single value
MISSION_IMPACT_2 = SsvcDecisionPoint(
    name="Mission Impact",
    description="Impact on Mission Essential Functions of the Organization",
    key="MI",
    version="2.0.0",
    values=(DEGRADED, MEF_CRIPPLED, MEF_FAILURE, MISSION_FAILURE),
)


def main():
    versions = (MISSION_IMPACT_1, MISSION_IMPACT_2)

    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
