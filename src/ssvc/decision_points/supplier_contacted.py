#!/usr/bin/env python
"""
Provides the Supplier Engagement decision point and its values.
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
from ssvc.decision_points.helpers import print_versions_and_diffs

YES = SsvcDecisionPointValue(
    name="Yes",
    key="Y",
    description="The supplier has been contacted.",
)

NO = SsvcDecisionPointValue(
    name="No",
    key="N",
    description="The supplier has not been contacted.",
)

SUPPLIER_CONTACTED_1 = SsvcDecisionPoint(
    name="Supplier Contacted",
    description="Has the reporter made a good-faith effort to contact the supplier of the vulnerable component using a quality contact method?",
    key="SC",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)

VERSIONS = (SUPPLIER_CONTACTED_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
