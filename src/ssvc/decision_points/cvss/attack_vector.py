#!/usr/bin/env python
"""
Models the CVSS Attack Vector metric as an SSVC decision point.
"""
from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_NETWORK = SsvcDecisionPointValue(
    name="Network",
    key="N",
    description="A vulnerability exploitable with network access means the vulnerable component is bound to the network stack and the attacker's path is through OSI layer 3 (the network layer). Such a vulnerability is often termed 'remotely exploitable' and can be thought of as an attack being exploitable one or more network hops away (e.g. across layer 3 boundaries from routers).",
)

_ADJACENT = SsvcDecisionPointValue(
    name="Adjacent",
    key="A",
    description="A vulnerability exploitable with adjacent network access means the vulnerable component is bound to the network stack, however the attack is limited to the same shared physical (e.g. Bluetooth, IEEE 802.11), or logical (e.g. local IP subnet) network, and cannot be performed across an OSI layer 3 boundary (e.g. a router).",
)

_LOCAL = SsvcDecisionPointValue(
    name="Local",
    key="L",
    description="A vulnerability exploitable with Local access means that the vulnerable component is not bound to the network stack, and the attacker's path is via read/write/execute capabilities. In some cases, the attacker may be logged in locally in order to exploit the vulnerability, otherwise, she may rely on User Interaction to execute a malicious file.",
)

_PHYSICAL = SsvcDecisionPointValue(
    name="Physical",
    key="P",
    description="A vulnerability exploitable with Physical access requires the attacker to physically touch or manipulate the vulnerable component. Physical interaction may be brief (e.g. evil maid attack [1]) or persistent. An example of such an attack is a cold boot attack which allows an attacker to access to disk encryption keys after gaining physical access to the system, or peripheral attacks such as Firewire/USB Direct Memory Access attacks.",
)

ATTACK_VECTOR_1 = CvssDecisionPoint(
    name="Attack Vector",
    description="This metric reflects the context by which vulnerability exploitation is possible. ",
    key="AV",
    version="1.0.0",
    values=(
        _PHYSICAL,
        _LOCAL,
        _ADJACENT,
        _NETWORK,
    ),
)
"""
Defines PHYSICAL, LOCAL, ADJACENT, and NETWORK values for CVSS Attack Vector.
"""


def main():
    print(ATTACK_VECTOR_1.to_json(indent=2))


if __name__ == "__main__":
    main()
