#!/usr/bin/env python
"""
Provides a decision point representing whether a vulnerability is in the CISA Known Exploited Vulnerabilities (KEV) list.
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

YES = SsvcDecisionPointValue(
    name="Yes",
    key="Y",
    description="Vulnerability is listed in KEV.",
)

NO = SsvcDecisionPointValue(
    name="No",
    key="N",
    description="Vulnerability is not listed in KEV.",
)

IN_KEV_1 = SsvcDecisionPoint(
    name="In KEV",
    description="Denotes whether a vulnerability is in the CISA Known Exploited Vulnerabilities (KEV) list.",
    key="KEV",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)


def main():
    print(IN_KEV_1.to_json(indent=2))


if __name__ == "__main__":
    main()
