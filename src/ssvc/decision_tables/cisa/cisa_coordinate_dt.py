#!/usr/bin/env python
"""
Provides the CISA coordinator decision table.
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
    MISSION_AND_WELL_BEING_IMPACT_1 as MissionAndWellBeingImpact,
)
from ssvc.decision_points.ssvc.technical_impact import (
    TECHNICAL_IMPACT_1 as TechnicalImpact,
)
from ssvc.decision_tables.base import (
    DecisionTable,
    decision_table_to_longform_df,
)
from ssvc.namespaces import NameSpace
from ssvc.outcomes.cisa.scoring import CISA as Priority

CISA_COORDINATE_1 = DecisionTable(
    namespace=NameSpace.CISA,
    key="CO",
    version="2.0.3",
    name="CISA Coordinator",
    definition="CISA Coordinator decision table for SSVC",
    outcome=Priority.id,
    decision_points={
        dp.id: dp
        for dp in [
            Exploitation,
            Automatable,
            TechnicalImpact,
            MissionAndWellBeingImpact,
            Priority,
        ]
    },
    mapping=[
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "T*",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "T*",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T*",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T*",
        },
        {
            "ssvc:E:1.1.0": "P",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "T",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AC",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AC",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "L",
            "cisa:CISA:1.1.0": "AT",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "M",
            "cisa:CISA:1.1.0": "AC",
        },
        {
            "ssvc:E:1.1.0": "A",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "ssvc:MWI:1.0.0": "H",
            "cisa:CISA:1.1.0": "AC",
        },
    ],
)

VERSIONS = (CISA_COORDINATE_1,)
LATEST = VERSIONS[-1]


def main():
    print("CISA Coordinator Decision Table (2.0.3)")
    print()
    print(CISA_COORDINATE_1.model_dump_json(indent=2))

    print("Longform DataFrame CSV")
    print()
    print(decision_table_to_longform_df(CISA_COORDINATE_1).to_csv(index=False))


if __name__ == "__main__":
    main()
