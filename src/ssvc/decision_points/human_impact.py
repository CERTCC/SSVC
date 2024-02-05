#!/usr/bin/env python
"""
file: human_impact
author: adh
created_at: 9/21/23 10:49 AM
"""
#  Copyright (c) 2023-2024 Carnegie Mellon University and Contributors.
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

LOW_1 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Mission Prevalence Minimal and Public Well-Being Impact Minimal",
)

MEDIUM_1 = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Mission Prevalence Support and Public Well-Being Impact Minimal or Material",
)

HIGH_1 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Mission Prevalence Essential or Public Well-Being Impact Irreversible",
)

VERY_HIGH_1 = SsvcDecisionPointValue(
    name="Very High",
    key="VH",
    description="Safety=Catastrophic OR Mission=Mission Failure",
)

HIGH_2 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Safety=Hazardous, Mission=None/Degraded/Crippled/MEF Failure OR Safety=Major, Mission=MEF Failure",
)

MEDIUM_2 = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Safety=None/Minor, Mission=MEF Failure OR Safety=Major, Mission=None/Degraded/Crippled",
)

LOW_2 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Safety=None/Minor, Mission=None/Degraded/Crippled",
)


MISSION_AND_WELL_BEING_IMPACT_1 = SsvcDecisionPoint(
    name="Mission and Well-Being Impact",
    description="Mission and Well-Being Impact is a combination of Mission Prevalence and Public Well-Being Impact.",
    key="MWI",
    version="1.0.0",
    values=(
        LOW_1,
        MEDIUM_1,
        HIGH_1,
    ),
)

HUMAN_IMPACT_2 = SsvcDecisionPoint(
    name="Human Impact",
    description="Human Impact is a combination of Safety and Mission impacts.",
    key="HI",
    version="2.0.0",
    values=(
        LOW_2,
        MEDIUM_2,
        HIGH_2,
        VERY_HIGH_1,
    ),
)


def main():
    versions = (MISSION_AND_WELL_BEING_IMPACT_1, HUMAN_IMPACT_2)

    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
