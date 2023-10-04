#!/usr/bin/env python
"""
Models the CVSS Access Vector metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_NETWORK = SsvcDecisionPointValue(
    name="Network",
    key="N",
    description="A vulnerability exploitable with network access means the vulnerable software is bound to the network stack and the attacker does not require local network access or local access. Such a vulnerability is often termed 'remotely exploitable'. An example of a network attack is an RPC buffer overflow.",
)

_ADJACENT = SsvcDecisionPointValue(
    name="Adjacent Network",
    key="A",
    description="A vulnerability exploitable with adjacent network access requires the attacker to have access to either the broadcast or collision domain of the vulnerable software.  Examples of local networks include local IP subnet, Bluetooth, IEEE 802.11, and local Ethernet segment.",
)

_LOCAL_2 = SsvcDecisionPointValue(
    name="Local",
    key="L",
    description="A vulnerability exploitable with only local access requires the attacker to have either physical access to the vulnerable system or a local (shell) account. Examples of locally exploitable vulnerabilities are peripheral attacks such as Firewire/USB DMA attacks, and local privilege escalations (e.g., sudo).",
)

_REMOTE = SsvcDecisionPointValue(
    name="Remote",
    key="R",
    description="The vulnerability is exploitable remotely.",
)

_LOCAL = SsvcDecisionPointValue(
    name="Local",
    key="L",
    description="The vulnerability is only exploitable locally (i.e., it requires physical access or authenticated login to the target system)",
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


def main():
    print(ACCESS_VECTOR_1.to_json(indent=2))
    print(ACCESS_VECTOR_2.to_json(indent=2))


if __name__ == "__main__":
    main()
