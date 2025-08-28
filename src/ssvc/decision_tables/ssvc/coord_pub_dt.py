#!/usr/bin/env python
"""
Provides the Coordinator Publish Decision Table for SSVC.
"""


#  Copyright (c) 2025 Carnegie Mellon University.
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

from ssvc.decision_points.ssvc.exploitation import LATEST as Exploitation
from ssvc.decision_points.ssvc.public_value_added import (
    LATEST as PublicValueAdded,
)
from ssvc.decision_points.ssvc.supplier_involvement import (
    LATEST as SupplierInvolvement,
)
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace
from ssvc.outcomes.ssvc.publish import LATEST as Priority

V1_0_0 = DecisionTable(
    namespace=NameSpace.SSVC,
    key="COORD_PUBLISH",
    version="1.0.0",
    name="Coordinator Publish Decision Table",
    definition="This decision table is used to determine the priority of a coordinator publish.",
    decision_points={
        dp.id: dp
        for dp in [
            SupplierInvolvement,
            Exploitation,
            PublicValueAdded,
            Priority,
        ]
    },
    outcome=Priority.id,
    mapping=[
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "N",
        },
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "L",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "N",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "FR",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "A",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "P",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "C",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
        {
            "ssvc:SINV:1.0.0": "UU",
            "ssvc:E:1.1.0": "A",
            "ssvc:PVA:1.0.0": "P",
            "ssvc:PUBLISH:1.0.0": "P",
        },
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version

    print_dt_version(LATEST)


if __name__ == "__main__":
    main()
