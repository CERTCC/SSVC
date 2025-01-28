#!/usr/bin/env python
"""
file: value_density
author: adh
created_at: 9/21/23 10:01 AM
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

CONCENTRATED = SsvcDecisionPointValue(
    name="Concentrated",
    key="C",
    description="The system that contains the vulnerable component is rich in resources. Heuristically, such systems are often the direct responsibility of “system operators” rather than users.",
)

DIFFUSE = SsvcDecisionPointValue(
    name="Diffuse",
    key="D",
    description="The system that contains the vulnerable component has limited resources. That is, the resources that the adversary will gain control over with a single exploitation event are relatively small.",
)

VALUE_DENSITY_1 = SsvcDecisionPoint(
    name="Value Density",
    description="The concentration of value in the target",
    key="VD",
    version="1.0.0",
    values=(
        DIFFUSE,
        CONCENTRATED,
    ),
)


def main():
    print(VALUE_DENSITY_1.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
