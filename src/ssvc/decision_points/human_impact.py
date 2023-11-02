#!/usr/bin/env python
"""
file: human_impact
author: adh
created_at: 9/21/23 10:49 AM
"""
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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

VERY_HIGH = SsvcDecisionPointValue(
    name="Very High",
    key="VH",
    description="Safety=Catastrophic OR Mission=Mission Failure",
)

HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Safety=Hazardous, Mission=None/Degraded/Crippled/MEF Failure OR Safety=Major, Mission=MEF Failure",
)

MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Safety=None/Minor, Mission=MEF Failure OR Safety=Major, Mission=None/Degraded/Crippled",
)

LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Safety=None/Minor, Mission=None/Degraded/Crippled",
)

HUMAN_IMPACT_1 = SsvcDecisionPoint(
    name="Human Impact",
    description="Human Impact is a combination of Safety and Mission impacts.",
    key="HI",
    version="1.0.0",
    values=(
        LOW,
        MEDIUM,
        HIGH,
        VERY_HIGH,
    ),
)


def main():
    print(HUMAN_IMPACT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
