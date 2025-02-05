#!/usr/bin/env python
"""
file: exposure
author: adh
created_at: 9/21/23 10:16 AM
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

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

EXP_UNAVOIDABLE = SsvcDecisionPointValue(
    name="Unavoidable",
    key="U",
    description="Internet or another widely accessible network where access cannot plausibly be restricted or "
    "controlled (e.g., DNS servers, web servers, VOIP servers, email servers)",
)

EXP_CONTROLLED = SsvcDecisionPointValue(
    name="Controlled",
    key="C",
    description="Networked service with some access restrictions or mitigations already in place (whether locally or on the network). "
    "A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable "
    "both reliably and quickly enough to respond. Controlled covers the situation in which a vulnerability can be "
    "exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the "
    "attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably "
    "execute it, then exposure should be small.",
)

EXP_SMALL = SsvcDecisionPointValue(
    name="Small",
    key="S",
    description="Local service or program; highly controlled network",
)


SYSTEM_EXPOSURE_1 = SsvcDecisionPoint(
    name="System Exposure",
    description="The Accessible Attack Surface of the Affected System or Service",
    key="EXP",
    version="1.0.0",
    values=(
        EXP_SMALL,
        EXP_CONTROLLED,
        EXP_UNAVOIDABLE,
    ),
)

# EXP_OPEN is just a rename of EXP_UNAVOIDABLE
EXP_OPEN = SsvcDecisionPointValue(
    name="Open",
    key="O",
    description="Internet or another widely accessible network where access cannot plausibly be restricted or "
    "controlled (e.g., DNS servers, web servers, VOIP servers, email servers)",
)


SYSTEM_EXPOSURE_1_0_1 = SsvcDecisionPoint(
    name="System Exposure",
    description="The Accessible Attack Surface of the Affected System or Service",
    key="EXP",
    version="1.0.1",
    values=(
        EXP_SMALL,
        EXP_CONTROLLED,
        EXP_OPEN,
    ),
)


def main():
    print(SYSTEM_EXPOSURE_1.model_dump_json(indent=2))
    print(SYSTEM_EXPOSURE_1_0_1.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
