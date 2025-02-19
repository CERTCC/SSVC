#!/usr/bin/env python

"""
Provides the Technical Impact decision point and its values.
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

TOTAL = SsvcDecisionPointValue(
    name="Total",
    key="T",
    description="The exploit gives the adversary total control over the behavior of the software, or it gives total disclosure of all information on the system that contains the vulnerability.",
)

PARTIAL = SsvcDecisionPointValue(
    name="Partial",
    key="P",
    description="The exploit gives the adversary limited control over, or information exposure about, the behavior of the software that contains the vulnerability. Or the exploit gives the adversary an importantly low stochastic opportunity for total control.",
)

TECHNICAL_IMPACT_1 = SsvcDecisionPoint(
    name="Technical Impact",
    description="The technical impact of the vulnerability.",
    key="TI",
    version="1.0.0",
    values=(
        PARTIAL,
        TOTAL,
    ),
)

VERSIONS = (TECHNICAL_IMPACT_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
