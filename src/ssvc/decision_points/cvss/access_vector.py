#!/usr/bin/env python
"""
file: access_vector
author: adh
created_at: 9/20/23 1:30 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

ACCESS_VECTOR_1 = CvssDecisionPoint(
    name="Access Vector",
    description="This metric measures whether or not the vulnerability is exploitable locally or remotely.",
    key="AV",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Local",
            key="L",
            description="The vulnerability is only exploitable locally (i.e., it requires physical access or authenticated login to the target system)",
        ),
        SsvcValue(
            name="Remote",
            key="R",
            description="The vulnerability is exploitable remotely.",
        ),
    ],
)

ACCESS_VECTOR_2 = deepcopy(ACCESS_VECTOR_1)
ACCESS_VECTOR_2.version = "2.0.0"
ACCESS_VECTOR_2.values = [
    SsvcValue(
        name="Local",
        key="L",
        description="A vulnerability exploitable with only local access requires the attacker to have either physical access to the vulnerable system or a local (shell) account. Examples of locally exploitable vulnerabilities are peripheral attacks such as Firewire/USB DMA attacks, and local privilege escalations (e.g., sudo).",
    ),
    SsvcValue(
        name="Adjacent Network",
        key="A",
        description="A vulnerability exploitable with adjacent network access requires the attacker to have access to either the broadcast or collision domain of the vulnerable software.  Examples of local networks include local IP subnet, Bluetooth, IEEE 802.11, and local Ethernet segment.",
    ),
    SsvcValue(
        name="Network",
        key="N",
        description="A vulnerability exploitable with network access means the vulnerable software is bound to the network stack and the attacker does not require local network access or local access. Such a vulnerability is often termed 'remotely exploitable'. An example of a network attack is an RPC buffer overflow.",
    ),
]


def main():
    print(ACCESS_VECTOR_1.to_json(indent=2))
    print(ACCESS_VECTOR_2.to_json(indent=2))


if __name__ == "__main__":
    main()
