#!/usr/bin/env python
"""
file: mission_impact
author: adh
created_at: 9/21/23 10:20 AM
"""
from copy import deepcopy

# Impact on Mission Essential Functions of the Organization

# None Little to no impact
# Non-Essential
# Degraded
# Degradation of non-essential functions; chronic degradation would eventually harm essential
# functions
# MEF Support
# Crippled
# Activities that directly support essential functions are crippled; essential functions continue for a
# time
# MEF Failure Any one mission essential function fails for period of time longer than acceptable; overall mission of the organization degraded but can still be accomplished for a time
# Mission Failure Multiple or all mission essential functions fail; ability to recover those functions degraded; organization’s ability to deliver its overall mission fails

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

MISSION_IMPACT_1 = SsvcDecisionPoint(
    name="Mission Impact",
    description="Impact on Mission Essential Functions of the Organization",
    key="MI",
    version="1.0.0",
    values=[
        SsvcValue(name="None", key="N", description="Little to no impact"),
        SsvcValue(
            name="Non-Essential Degraded",
            key="NED",
            description="Degradation of non-essential functions; chronic degradation would eventually harm essential functions",
        ),
        SsvcValue(
            name="MEF Support Crippled",
            key="MSC",
            description="Activities that directly support essential functions are crippled; essential functions continue for a time",
        ),
        SsvcValue(
            name="MEF Failure",
            key="MEF",
            description="Any one mission essential function fails for period of time longer than acceptable; overall mission of the organization degraded but can still be accomplished for a time",
        ),
        SsvcValue(
            name="Mission Failure",
            key="MF",
            description="Multiple or all mission essential functions fail; ability to recover those functions degraded; organization’s ability to deliver its overall mission fails",
        ),
    ],
)

# SSVC v2.1 combined None and Non-Essential Degraded into a single value
MISSION_IMPACT_2 = deepcopy(MISSION_IMPACT_1)
MISSION_IMPACT_2.version = "2.0.0"
MISSION_IMPACT_2.values = [
    SsvcValue(
        name="Degraded",
        key="D",
        description="Little to no impact up to degradation of non-essential functions; chronic degradation would eventually harm essential functions",
    ),
    SsvcValue(
        name="MEF Support Crippled",
        key="MSC",
        description="Activities that directly support essential functions are crippled; essential functions continue for a time",
    ),
    SsvcValue(
        name="MEF Failure",
        key="MEF",
        description="Any one mission essential function fails for period of time longer than acceptable; overall mission of the organization degraded but can still be accomplished for a time",
    ),
    SsvcValue(
        name="Mission Failure",
        key="MF",
        description="Multiple or all mission essential functions fail; ability to recover those functions degraded; organization’s ability to deliver its overall mission fails",
    ),
]

def main():
    print(MISSION_IMPACT_1.to_json(indent=2))
    print(MISSION_IMPACT_2.to_json(indent=2))


if __name__ == "__main__":
    main()
