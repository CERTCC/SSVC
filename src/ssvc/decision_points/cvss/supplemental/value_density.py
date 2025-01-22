#!/usr/bin/env python
"""
Provides the CVSS supplemental metric Value Density
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
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

from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs


VALUE_DENSITY_1 = CvssDecisionPoint(
    name="Value Density",
    description="Value Density describes the resources that the attacker will gain control over with a single "
    "exploitation event. It has two possible values, diffuse and concentrated.",
    key="V",
    version="1.0.0",
    values=(
        NOT_DEFINED_X,
        SsvcDecisionPointValue(
            name="Diffuse",
            key="D",
            description="The vulnerable system has limited resources. That is, the resources that the attacker will "
            "gain control over with a single exploitation event are relatively small.",
        ),
        SsvcDecisionPointValue(
            name="Concentrated",
            key="C",
            description="The vulnerable system is rich in resources. Heuristically, such systems are often the direct "
            'responsibility of "system operators" rather than users.',
        ),
    ),
)


def main():
    versions = [
        VALUE_DENSITY_1,
    ]

    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
