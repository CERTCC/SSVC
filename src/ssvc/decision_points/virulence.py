#!/usr/bin/env python
"""
file: virulence
author: adh
created_at: 9/21/23 9:58 AM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

RAPID = SsvcDecisionPointValue(
    name="Rapid",
    key="R",
    description="Steps 1-4 of the of the kill chain can be reliably automated. If the vulnerability allows remote code execution or command injection, the default response should be rapid.",
)

SLOW = SsvcDecisionPointValue(
    name="Slow",
    key="S",
    description="Steps 1-4 of the kill chain cannot be reliably automated for this vulnerability for some reason. These steps are reconnaissance, weaponization, delivery, and exploitation. Example reasons for why a step may not be reliably automatable include (1) the vulnerable component is not searchable or enumerable on the network, (2) weaponization may require human direction for each target, (3) delivery may require channels that widely deployed network security configurations block, and (3) exploitation may be frustrated by adequate exploit-prevention techniques enabled by default; ASLR is an example of an exploit-prevention tool.",
)

VIRULENCE_1 = SsvcDecisionPoint(
    name="Virulence",
    description="The speed at which the vulnerability can be exploited.",
    key="V",
    version="1.0.0",
    values=(
        SLOW,
        RAPID,
    ),
)


def main():
    print(VIRULENCE_1.to_json(indent=2))


if __name__ == "__main__":
    main()
