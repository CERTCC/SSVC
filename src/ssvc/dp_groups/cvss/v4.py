#!/usr/bin/env python
"""
file: v4
author: adh
created_at: 11/6/23 11:48 AM
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

from ssvc.decision_points.cvss.eq_sets import EQ1, EQ2, EQ3, EQ4, EQ5, EQ6
from ssvc.dp_groups.base import SsvcDecisionPointGroup


EquivalenceSetsV4 = SsvcDecisionPointGroup(
    name="CVSSv4 EQ Sets",
    description="Equivalence Sets for CVSS v4",
    version="1.0.0",
    decision_points=[
        EQ1,
        EQ2,
        EQ3,
        EQ4,
        EQ5,
        EQ6,
    ],
)


def main():
    print(EquivalenceSetsV4.to_json(indent=2))


if __name__ == "__main__":
    main()
