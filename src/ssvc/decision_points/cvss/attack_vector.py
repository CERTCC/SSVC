#!/usr/bin/env python
"""
Models the CVSS Attack Vector (formerly known as Access Vector) metric as an SSVC decision point.
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

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_REMOTE = SsvcDecisionPointValue(
    name="Remote",
    key="R",
    description="The vulnerability is exploitable remotely.",
)

_LOCAL = SsvcDecisionPointValue(
    name="Local",
    key="L",
    description="The vulnerability is only exploitable locally (i.e., it requires physical access or authenticated "
    "login to the target system)",
)

ACCESS_VECTOR_1 = CvssDecisionPoint(
    name="Access Vector",
    description="This metric measures whether or not the vulnerability is exploitable locally or remotely.",
    key="AV",
    version="1.0.0",
    values=(
        _LOCAL,
        _REMOTE,
    ),
)
"""
Defines LOCAL and REMOTE values for CVSS Access Vector.
"""

_NETWORK = SsvcDecisionPointValue(
    name="Network",
    key="N",
    description="A vulnerability exploitable with network access means the vulnerable software is bound to the "
    "network stack and the attacker does not require local network access or local access. Such a "
    "vulnerability is often termed 'remotely exploitable'. An example of a network attack is an RPC "
    "buffer overflow.",
)

_ADJACENT = SsvcDecisionPointValue(
    name="Adjacent Network",
    key="A",
    description="A vulnerability exploitable with adjacent network access requires the attacker to have access to "
    "either the broadcast or collision domain of the vulnerable software.  Examples of local networks "
    "include local IP subnet, Bluetooth, IEEE 802.11, and local Ethernet segment.",
)

_LOCAL_2 = SsvcDecisionPointValue(
    name="Local",
    key="L",
    description="A vulnerability exploitable with only local access requires the attacker to have either physical "
    "access to the vulnerable system or a local (shell) account. Examples of locally exploitable "
    "vulnerabilities are peripheral attacks such as Firewire/USB DMA attacks, and local privilege "
    "escalations (e.g., sudo).",
)


ACCESS_VECTOR_2 = CvssDecisionPoint(
    name="Access Vector",
    description="This metric reflects the context by which vulnerability exploitation is possible.",
    key="AV",
    version="2.0.0",
    values=(
        _LOCAL_2,
        _ADJACENT,
        _NETWORK,
    ),
)
"""
Updates LOCAL definition for CVSS Access Vector. Adds ADJACENT and NETWORK values. Removes REMOTE value.
"""


_NETWORK_2 = SsvcDecisionPointValue(
    name="Network",
    key="N",
    description="A vulnerability exploitable with network access means the vulnerable component is bound to the "
    "network stack and the attacker's path is through OSI layer 3 (the network layer). Such a "
    "vulnerability is often termed 'remotely exploitable' and can be thought of as an attack being "
    "exploitable one or more network hops away (e.g. across layer 3 boundaries from routers).",
)

_ADJACENT_2 = SsvcDecisionPointValue(
    name="Adjacent",
    key="A",
    description="A vulnerability exploitable with adjacent network access means the vulnerable component is bound to "
    "the network stack, however the attack is limited to the same shared physical (e.g. Bluetooth, "
    "IEEE 802.11), or logical (e.g. local IP subnet) network, and cannot be performed across an OSI layer "
    "3 boundary (e.g. a router).",
)

_LOCAL_3 = SsvcDecisionPointValue(
    name="Local",
    key="L",
    description="A vulnerability exploitable with Local access means that the vulnerable component is not bound to "
    "the network stack, and the attacker's path is via read/write/execute capabilities. In some cases, "
    "the attacker may be logged in locally in order to exploit the vulnerability, otherwise, she may rely "
    "on User Interaction to execute a malicious file.",
)

_PHYSICAL_2 = SsvcDecisionPointValue(
    name="Physical",
    key="P",
    description="A vulnerability exploitable with Physical access requires the attacker to physically touch or "
    "manipulate the vulnerable component. Physical interaction may be brief (e.g. evil maid attack [1]) "
    "or persistent. An example of such an attack is a cold boot attack which allows an attacker to access "
    "to disk encryption keys after gaining physical access to the system, or peripheral attacks such as "
    "Firewire/USB Direct Memory Access attacks.",
)

ATTACK_VECTOR_3 = CvssDecisionPoint(
    name="Attack Vector",
    description="This metric reflects the context by which vulnerability exploitation is possible. ",
    key="AV",
    version="3.0.0",
    values=(
        _PHYSICAL_2,
        _LOCAL_3,
        _ADJACENT_2,
        _NETWORK_2,
    ),
)
"""
Defines PHYSICAL, LOCAL, ADJACENT, and NETWORK values for CVSS Attack Vector.
"""


def main():
    print(ACCESS_VECTOR_1.to_json(indent=2))
    print(ACCESS_VECTOR_2.to_json(indent=2))
    print(ATTACK_VECTOR_3.to_json(indent=2))


if __name__ == "__main__":
    main()
