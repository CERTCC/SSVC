#!/usr/bin/env python
"""
Models the CVSS Attack Vector (formerly known as Access Vector) metric as an SSVC decision point.
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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_REMOTE = DecisionPointValue(
    name="Remote",
    key="R",
    definition="The vulnerability is exploitable remotely.",
)

_LOCAL = DecisionPointValue(
    name="Local",
    key="L",
    definition="The vulnerability is only exploitable locally (i.e., it requires physical access or authenticated "
    "login to the target system)",
)

ACCESS_VECTOR_1 = CvssDecisionPoint(
    name="Access Vector",
    definition="This metric measures whether or not the vulnerability is exploitable locally or remotely.",
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

_NETWORK = DecisionPointValue(
    name="Network",
    key="N",
    definition="A vulnerability exploitable with network access means the vulnerable software is bound to the "
    "network stack and the attacker does not require local network access or local access. Such a "
    "vulnerability is often termed 'remotely exploitable'.",
)

_ADJACENT = DecisionPointValue(
    name="Adjacent Network",
    key="A",
    definition="A vulnerability exploitable with adjacent network access requires the attacker to have access to "
    "either the broadcast or collision domain of the vulnerable software.",
)

_LOCAL_2 = DecisionPointValue(
    name="Local",
    key="L",
    definition="A vulnerability exploitable with only local access requires the attacker to have either physical "
    "access to the vulnerable system or a local (shell) account.",
)


ACCESS_VECTOR_2 = CvssDecisionPoint(
    name="Access Vector",
    definition="This metric reflects the context by which vulnerability exploitation is possible.",
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


_NETWORK_2 = DecisionPointValue(
    name="Network",
    key="N",
    definition="A vulnerability exploitable with network access means the vulnerable component is bound to the "
    "network stack and the attacker's path is through OSI layer 3 (the network layer). Such a "
    "vulnerability is often termed 'remotely exploitable' and can be thought of as an attack being "
    "exploitable one or more network hops away (e.g. across layer 3 boundaries from routers).",
)

_ADJACENT_2 = DecisionPointValue(
    name="Adjacent",
    key="A",
    definition="A vulnerability exploitable with adjacent network access means the vulnerable component is bound to "
    "the network stack, however the attack is limited to the same shared physical (e.g. Bluetooth, "
    "IEEE 802.11), or logical (e.g. local IP subnet) network, and cannot be performed across an OSI layer "
    "3 boundary (e.g. a router).",
)

_LOCAL_3 = DecisionPointValue(
    name="Local",
    key="L",
    definition="A vulnerability exploitable with Local access means that the vulnerable component is not bound to "
    "the network stack, and the attacker's path is via read/write/execute capabilities. In some cases, "
    "the attacker may be logged in locally in order to exploit the vulnerability, otherwise, she may rely "
    "on User Interaction to execute a malicious file.",
)

_PHYSICAL_2 = DecisionPointValue(
    name="Physical",
    key="P",
    definition="A vulnerability exploitable with Physical access requires the attacker to physically touch or "
    "manipulate the vulnerable component. Physical interaction may be brief (e.g. evil maid attack [1]) "
    "or persistent.",
)

ATTACK_VECTOR_3 = CvssDecisionPoint(
    name="Attack Vector",
    definition="This metric reflects the context by which vulnerability exploitation is possible. ",
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
_NETWORK_3 = DecisionPointValue(
    name="Network",
    key="N",
    definition="The vulnerable system is bound to the network stack and the set of possible attackers extends beyond "
    "the other options listed below, up to and including the entire Internet. Such a vulnerability is "
    "often termed “remotely exploitable” and can be thought of as an attack being exploitable at the "
    "protocol level one or more network hops away (e.g., across one or more routers).",
)

_ADJACENT_3 = DecisionPointValue(
    name="Adjacent",
    key="A",
    definition="The vulnerable system is bound to a protocol stack, but the attack is limited at the protocol level "
    "to a logically adjacent topology. This can mean an attack must be launched from the same shared "
    "proximity (e.g., Bluetooth, NFC, or IEEE 802.11) or logical network (e.g., local IP subnet), or from "
    "within a secure or otherwise limited administrative domain (e.g., MPLS, secure VPN within an "
    "administrative network zone).",
)

_LOCAL_4 = DecisionPointValue(
    name="Local",
    key="L",
    definition="The vulnerable system is not bound to the network stack and the attacker’s path is via "
    "read/write/execute capabilities. Either: the attacker exploits the vulnerability by accessing the "
    "target system locally (e.g., keyboard, console), or through terminal emulation (e.g., SSH); or the "
    "attacker relies on User Interaction by another person to perform actions required to exploit the "
    "vulnerability (e.g., using social engineering techniques to trick a legitimate user into opening a "
    "malicious document).",
)

_PHYSICAL_3 = DecisionPointValue(
    name="Physical",
    key="P",
    definition="The attack requires the attacker to physically touch or manipulate the vulnerable system. Physical "
    "interaction may be brief (e.g., evil maid attack1) or persistent.",
)

# updates descriptions of NETWORK, ADJACENT, LOCAL, and PHYSICAL values for CVSS Attack Vector
ATTACK_VECTOR_3_0_1 = CvssDecisionPoint(
    name="Attack Vector",
    definition="This metric reflects the context by which vulnerability exploitation is possible. This metric value "
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

VERSIONS = (
    ACCESS_VECTOR_1,
    ACCESS_VECTOR_2,
    ATTACK_VECTOR_3,
    ATTACK_VECTOR_3_0_1,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
