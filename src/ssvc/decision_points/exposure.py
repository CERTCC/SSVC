#!/usr/bin/env python
"""
file: exposure
author: adh
created_at: 9/21/23 10:16 AM
"""
from copy import deepcopy

# Exposure
# The Accessible Attack Surface of the Affected System or Service

# Small Local service or program; highly controlled network
# Controlled Networked service with some access restrictions or mitigations already in place (whether locally or on
# the network). A successful mitigation must reliably interrupt the adversary’s attack, which requires the
# attack is detectable both reliably and quickly enough to respond. Controlled covers the situation in
# which a vulnerability can be exploited through chaining it with other vulnerabilities. The assumption is
# that the number of steps in the attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably execute it, then exposure should be small.
# Unavoidable Internet or another widely accessible network where access cannot plausibly be restricted or controlled (e.g., DNS servers, web servers, VOIP servers, email servers)

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

EXPOSURE_1 = SsvcDecisionPoint(
    name="Exposure",
    description="The Accessible Attack Surface of the Affected System or Service",
    key="EXP",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Small",
            key="S",
            description="Local service or program; highly controlled network",
        ),
        SsvcValue(
            name="Controlled",
            key="C",
            description="Networked service with some access restrictions or mitigations already in place (whether locally or on the network). A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable both reliably and quickly enough to respond. Controlled covers the situation in which a vulnerability can be exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably execute it, then exposure should be small.",
        ),
        SsvcValue(
            name="Unavoidable",
            key="U",
            description="Internet or another widely accessible network where access cannot plausibly be restricted or controlled (e.g., DNS servers, web servers, VOIP servers, email servers)",
        ),
    ],
)

EXPOSURE_1_0_1 = deepcopy(EXPOSURE_1)
EXPOSURE_1_0_1.version = "1.0.1"
EXPOSURE_1_0_1.values = [
    SsvcValue(
        name="Small",
        key="S",
        description="Local service or program; highly controlled network",
    ),
    SsvcValue(
        name="Controlled",
        key="C",
        description="Networked service with some access restrictions or mitigations already in place (whether locally or on the network). A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable both reliably and quickly enough to respond. Controlled covers the situation in which a vulnerability can be exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably execute it, then exposure should be small.",
    ),
    SsvcValue(
        name="Open",
        key="O",
        description="Internet or another widely accessible network where access cannot plausibly be restricted or controlled (e.g., DNS servers, web servers, VOIP servers, email servers)",
    ),
]


def main():
    print(EXPOSURE_1.to_json(indent=2))
    print(EXPOSURE_1_0_1.to_json(indent=2))


if __name__ == "__main__":
    main()
