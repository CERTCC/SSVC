#!/usr/bin/env python
"""
Provides the Deployer Patch Application Priority decision table for SSVC.
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

from ssvc.decision_points.ssvc.automatable import AUTOMATABLE_2 as Automatable
from ssvc.decision_points.ssvc.exploitation import (
    EXPLOITATION_1_1_0 as Exploitation,
)
from ssvc.decision_points.ssvc.human_impact import (
    HUMAN_IMPACT_2_0_2 as HumanImpact,
)
from ssvc.decision_points.ssvc.system_exposure import (
    SYSTEM_EXPOSURE_1_0_1 as Exposure,
)
from ssvc.decision_tables.base import (
    DecisionTable,
    decision_table_to_longform_df,
)
from ssvc.namespaces import NameSpace
from ssvc.outcomes.ssvc.dsoi import DSOI as DSOI

DEPLOYER_1 = DecisionTable(
    namespace=NameSpace.SSVC,
    key="DP",
    version="1.0.0",
    name="Deployer Patch Application Priority",
    definition="Decision table for evaluating deployer's patch application priority in SSVC",
    decision_points={
        dp.id: dp
        for dp in [Exploitation, Exposure, Automatable, HumanImpact, DSOI]
    },
    outcome=DSOI.id,
    mapping=[
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "D",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "D",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "D",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "D",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "D",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "D",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "D",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "S",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "C",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "N",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "L",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "M",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "H",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:EXP:1.0.1": "O",
            "ssvc:A:2.0.0": "Y",
            "ssvc:HI:2.0.2": "VH",
            "ssvc:DSOI:1.0.0": "I",
        },
    ],
)

VERSIONS = (DEPLOYER_1,)
LATEST = VERSIONS[-1]


def main():
    print("Deployer Decision Table")
    print()
    print(DEPLOYER_1.model_dump_json(indent=2))

    print("Longform DataFrame CSV")
    print()
    print(decision_table_to_longform_df(DEPLOYER_1).to_csv(index=False))


if __name__ == "__main__":
    main()
