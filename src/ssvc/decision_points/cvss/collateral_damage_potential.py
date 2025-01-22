#!/usr/bin/env python
"""
Models the CVSS Collateral Damage Potential metric as an SSVC decision point.
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

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_ND
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs


_MEDIUM_HIGH = SsvcDecisionPointValue(
    name="Medium-High",
    key="MH",
    description="A successful exploit of this vulnerability may result in significant physical or property damage or loss.",
)

_LOW_MEDIUM = SsvcDecisionPointValue(
    name="Low-Medium",
    key="LM",
    description="A successful exploit of this vulnerability may result in moderate physical or property damage or loss.",
)

_CDP_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no potential for loss of life, physical assets, productivity or revenue.",
)

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="A successful exploit of this vulnerability may result in catastrophic physical or property damage and loss. The range of effect may be over a wide area.",
)

_MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="A successful exploit of this vulnerability may result in significant physical or property damage or loss.",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="A successful exploit of this vulnerability may result in light physical or property damage or loss. The system itself may be damaged or destroyed.",
)

_CDP_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no potential for physical or property damage.",
)


COLLATERAL_DAMAGE_POTENTIAL_1 = CvssDecisionPoint(
    name="Collateral Damage Potential",
    description="This metric measures the potential for a loss in physical equipment, property damage or loss of life or limb.",
    key="CDP",
    version="1.0.0",
    values=(
        _CDP_NONE,
        _LOW,
        _MEDIUM,
        _HIGH,
    ),
)
"""
Defines None, Low, Medium, and High values for CVSS Collateral Damage Potential.
"""

COLLATERAL_DAMAGE_POTENTIAL_2 = CvssDecisionPoint(
    name="Collateral Damage Potential",
    description="This metric measures the potential for loss of life or physical assets.",
    key="CDP",
    version="2.0.0",
    values=(
        _CDP_NONE_2,
        _LOW_MEDIUM,
        _MEDIUM_HIGH,
        _HIGH,
        NOT_DEFINED_ND,
    ),
)
"""
Updates None description. Adds Low-Medium, Medium-High, and Not Defined value.
"""

versions = [COLLATERAL_DAMAGE_POTENTIAL_1, COLLATERAL_DAMAGE_POTENTIAL_2]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
