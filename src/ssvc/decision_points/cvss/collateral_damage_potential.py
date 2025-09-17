#!/usr/bin/env python
"""
Models the CVSS Collateral Damage Potential metric as an SSVC decision point.
"""

#  Copyright (c) 2023-2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_ND
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs


_MEDIUM_HIGH = DecisionPointValue(
    name="Medium-High",
    key="MH",
    definition="A successful exploit of this vulnerability may result in significant physical or property damage or loss.",
)

_LOW_MEDIUM = DecisionPointValue(
    name="Low-Medium",
    key="LM",
    definition="A successful exploit of this vulnerability may result in moderate physical or property damage or loss.",
)

_CDP_NONE_2 = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no potential for loss of life, physical assets, productivity or revenue.",
)

_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="A successful exploit of this vulnerability may result in catastrophic physical or property damage and loss. The range of effect may be over a wide area.",
)

_MEDIUM = DecisionPointValue(
    name="Medium",
    key="M",
    definition="A successful exploit of this vulnerability may result in significant physical or property damage or loss.",
)

_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="A successful exploit of this vulnerability may result in light physical or property damage or loss. The system itself may be damaged or destroyed.",
)

_CDP_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no potential for physical or property damage.",
)


COLLATERAL_DAMAGE_POTENTIAL_1 = CvssDecisionPoint(
    name="Collateral Damage Potential",
    definition="This metric measures the potential for a loss in physical equipment, property damage or loss of life or limb.",
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
    definition="This metric measures the potential for loss of life or physical assets.",
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

VERSIONS = (COLLATERAL_DAMAGE_POTENTIAL_1, COLLATERAL_DAMAGE_POTENTIAL_2)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
