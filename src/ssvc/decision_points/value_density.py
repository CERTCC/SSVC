#!/usr/bin/env python
"""
file: value_density
author: adh
created_at: 9/21/23 10:01 AM
"""
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
    print(VALUE_DENSITY_1.to_json(indent=2))


if __name__ == "__main__":
    main()
