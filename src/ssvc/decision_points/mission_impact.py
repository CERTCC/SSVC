#!/usr/bin/env python
"""
file: mission_impact
author: adh
created_at: 9/21/23 10:20 AM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue


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
MISSION_IMPACT_2 = deepcopy(MISSION_IMPACT_1)
MISSION_IMPACT_2.version = "2.0.0"
MISSION_IMPACT_2.values = (DEGRADED, MEF_CRIPPLED, MEF_FAILURE, MISSION_FAILURE)


def main():
    print(MISSION_IMPACT_1.to_json(indent=2))
    print(MISSION_IMPACT_2.to_json(indent=2))


if __name__ == "__main__":
    main()
