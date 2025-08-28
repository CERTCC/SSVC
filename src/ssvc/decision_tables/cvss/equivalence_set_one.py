#!/usr/bin/env python
"""
Provides a decision table modeling equivalence set 1 from CVSS v4"""

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

# https://www.first.org/cvss/v4-0/specification-document
#  Table 24: EQ1 MacroVectors
# Levels	Constraints	Highest Severity Vector(s)
# 0	AV:N and PR:N and UI:N	AV:N/PR:N/UI:N
# 1	(AV:N or PR:N or UI:N) and not (AV:N and PR:N and UI:N) and not AV:P	AV:A/PR:N/UI:N or AV:N/PR:L/UI:N or AV:N/PR:N:/UI:P
# 2	AV:P or not(AV:N or PR:N or UI:N)	AV:P/PR:N/UI:N or AV:A/PR:L/UI:P

from ssvc.decision_points.cvss.attack_vector import ATTACK_VECTOR_3_0_1 as AV
from ssvc.decision_points.cvss.equivalence_set_1 import EQ1
from ssvc.decision_points.cvss.privileges_required import (
    PRIVILEGES_REQUIRED_1_0_1 as PR,
)
from ssvc.decision_points.cvss.user_interaction import USER_INTERACTION_2 as UI
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace


V1_0_0 = DecisionTable(
    namespace=NameSpace.CVSS,
    key="CVSS4_EQ1",
    version="1.0.0",
    name="CVSS v4 Equivalence Set 1",
    definition="This decision table models equivalence set 1 from CVSS v4. Factors include Attack Vector (AV), Privileges Required (PR), and User Interaction (UI).",
    decision_points={dp.id: dp for dp in (AV, PR, UI, EQ1)},
    outcome=EQ1.id,
    mapping=[
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "P",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "L",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "A",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "H",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "L",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "P",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "L",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "A",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "M",
        },
        {
            "cvss:AV:3.0.1": "N",
            "cvss:PR:1.0.1": "N",
            "cvss:UI:2.0.0": "N",
            "cvss:EQ1:1.0.0": "H",
        },
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version

    print_dt_version(LATEST, longform=False)


if __name__ == "__main__":
    main()
