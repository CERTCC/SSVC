#!/usr/bin/env python
"""
Models the CVSS Attack Vector (formerly known as Access Vector) metric as an SSVC decision point.
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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

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
    "vulnerability is often termed 'remotely exploitable'.",
)

_ADJACENT = SsvcDecisionPointValue(
    name="Adjacent Network",
    key="A",
    description="A vulnerability exploitable with adjacent network access requires the attacker to have access to "
    "either the broadcast or collision domain of the vulnerable software.",
)

_LOCAL_2 = SsvcDecisionPointValue(
    name="Local",
    key="L",
    description="A vulnerability exploitable with only local access requires the attacker to have either physical "
    "access to the vulnerable system or a local (shell) account.",
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
    "or persistent.",
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


# CVSS v4 Attack Vector
_NETWORK_3 = SsvcDecisionPointValue(
    name="Network",
    key="N",
    description="The vulnerable system is bound to the network stack and the set of possible attackers extends beyond "
    "the other options listed below, up to and including the entire Internet. Such a vulnerability is "
    "often termed “remotely exploitable” and can be thought of as an attack being exploitable at the "
    "protocol level one or more network hops away (e.g., across one or more routers).",
)

_ADJACENT_3 = SsvcDecisionPointValue(
    name="Adjacent",
    key="A",
    description="The vulnerable system is bound to a protocol stack, but the attack is limited at the protocol level "
    "to a logically adjacent topology. This can mean an attack must be launched from the same shared "
    "proximity (e.g., Bluetooth, NFC, or IEEE 802.11) or logical network (e.g., local IP subnet), or from "
    "within a secure or otherwise limited administrative domain (e.g., MPLS, secure VPN within an "
    "administrative network zone).",
)

_LOCAL_4 = SsvcDecisionPointValue(
    name="Local",
    key="L",
    description="The vulnerable system is not bound to the network stack and the attacker’s path is via "
    "read/write/execute capabilities. Either: the attacker exploits the vulnerability by accessing the "
    "target system locally (e.g., keyboard, console), or through terminal emulation (e.g., SSH); or the "
    "attacker relies on User Interaction by another person to perform actions required to exploit the "
    "vulnerability (e.g., using social engineering techniques to trick a legitimate user into opening a "
    "malicious document).",
)

_PHYSICAL_3 = SsvcDecisionPointValue(
    name="Physical",
    key="P",
    description="The attack requires the attacker to physically touch or manipulate the vulnerable system. Physical "
    "interaction may be brief (e.g., evil maid attack1) or persistent.",
)

# updates descriptions of NETWORK, ADJACENT, LOCAL, and PHYSICAL values for CVSS Attack Vector
ATTACK_VECTOR_3_0_1 = CvssDecisionPoint(
    name="Attack Vector",
    description="This metric reflects the context by which vulnerability exploitation is possible. This metric value "
    "(and consequently the resulting severity) will be larger the more remote (logically, and physically) "
    "an attacker can be in order to exploit the vulnerable system. The assumption is that the number of "
    "potential attackers for a vulnerability that could be exploited from across a network is larger than "
    "the number of potential attackers that could exploit a vulnerability requiring physical access to a "
    "device, and therefore warrants a greater severity.",
    key="AV",
    version="3.0.1",
    values=(
        _PHYSICAL_3,
        _LOCAL_4,
        _ADJACENT_3,
        _NETWORK_3,
    ),
)

versions = [ACCESS_VECTOR_1, ACCESS_VECTOR_2, ATTACK_VECTOR_3, ATTACK_VECTOR_3_0_1]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
