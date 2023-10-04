#!/usr/bin/env python
"""
Models the CVSS Collateral Damage Potential metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_NOT_DEFINED = SsvcDecisionPointValue(
    name="Not Defined",
    key="ND",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
)

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
        _NOT_DEFINED,
    ),
)
"""
Updates None description. Adds Low-Medium, Medium-High, and Not Defined value.
"""


def main():
    print(COLLATERAL_DAMAGE_POTENTIAL_1.to_json(indent=2))
    print(COLLATERAL_DAMAGE_POTENTIAL_2.to_json(indent=2))


if __name__ == "__main__":
    main()
