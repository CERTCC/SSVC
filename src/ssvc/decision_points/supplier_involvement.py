#!/usr/bin/env python
"""
file: supplier_involvement
author: adh
created_at: 9/21/23 11:28 AM
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

UNCOOPERATIVE = SsvcDecisionPointValue(
    name="Uncooperative/Unresponsive",
    key="UU",
    description="The supplier has not responded, declined to generate a remediation, or no longer exists.",
)

COOPERATIVE = SsvcDecisionPointValue(
    name="Cooperative",
    key="C",
    description="The supplier is actively generating a patch or fix; they may or may not have provided a mitigation or work-around in the mean time.",
)

FIX_READY = SsvcDecisionPointValue(
    name="Fix Ready",
    key="FR",
    description="The supplier has provided a patch or fix.",
)

SUPPLIER_INVOLVEMENT_1 = SsvcDecisionPoint(
    name="Supplier Involvement",
    description="What is the state of the supplier’s work on addressing the vulnerability?",
    key="SI",
    version="1.0.0",
    values=(
        FIX_READY,
        COOPERATIVE,
        UNCOOPERATIVE,
    ),
)


def main():
    print(SUPPLIER_INVOLVEMENT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
