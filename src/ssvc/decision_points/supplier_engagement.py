#!/usr/bin/env python
"""
file: supplier_engagement
author: adh
created_at: 9/21/23 11:22 AM
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

UNRESPONSIVE = SsvcDecisionPointValue(
    name="Unresponsive",
    key="U",
    description="The supplier is not responding to the reporter’s contact effort and not actively participating in the coordination effort.",
)

ACTIVE = SsvcDecisionPointValue(
    name="Active",
    key="A",
    description="The supplier is responding to the reporter’s contact effort and actively participating in the coordination effort.",
)

SUPPLIER_ENGAGEMENT_1 = SsvcDecisionPoint(
    name="Supplier Engagement",
    description="Is the supplier responding to the reporter’s contact effort and actively participating in the coordination effort?",
    key="SE",
    version="1.0.0",
    values=(
        ACTIVE,
        UNRESPONSIVE,
    ),
)


def main():
    print(SUPPLIER_ENGAGEMENT_1.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
