#!/usr/bin/env python
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

VERY_HIGH = SsvcDecisionPointValue(
    name="Very High",
    key="VH",
    description="Safety Impact:Catastrophic OR Mission Impact:Mission Failure",
)

HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="(Safety Impact:Hazardous AND Mission Impact:(None OR Degraded OR Crippled)) OR (Safety Impact:Major AND Mission Impact:MEF Failure)",
)

MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="(Safety Impact:(None OR Minor) AND Mission Impact:MEF Failure) OR (Safety Impact:Major AND Mission Impact:(None OR Degraded OR Crippled))",
)

LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Safety Impact:(None OR Minor) AND Mission Impact:(None OR Degraded OR Crippled)",
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
    versions = (HUMAN_IMPACT_1,)

    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
