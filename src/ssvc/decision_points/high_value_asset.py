#!/usr/bin/env python
"""
Models a high value asset as a decision point.
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
    description="System meets a high value asset definition.",
)

NO = SsvcDecisionPointValue(
    name="No",
    key="N",
    description="System does not meet a high value asset definition.",
)

HIGH_VALUE_ASSET_1 = SsvcDecisionPoint(
    name="High Value Asset",
    description="Denotes whether a system meets a high value asset definition.",
    key="HVA",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)


def main():
    print(HIGH_VALUE_ASSET_1.to_json(indent=2))


if __name__ == "__main__":
    main()
