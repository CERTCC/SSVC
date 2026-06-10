#!/usr/bin/env python
"""
Creates a decision table for CISA Binding Operational Directive 26-04.
"""
#  Copyright (c) 2026 Carnegie Mellon University.
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

from ssvc.decision_points.cisa.asset_exposure import (
    ASSET_EXPOSURE_1 as PUBLICLY_EXPOSED,
)
from ssvc.decision_points.cisa.in_kev import IN_KEV_1 as InKEV
from ssvc.decision_points.ssvc.automatable import AUTOMATABLE_2 as AUTOMATABLE
from ssvc.decision_points.ssvc.technical_impact import (
    TECHNICAL_IMPACT_1 as TECHNICAL_IMPACT,
)
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace
from ssvc.outcomes.cisa.bod2604 import BOD_26_04 as OUTCOMES

BOD_26_04 = DecisionTable(
    key="BOD2604",
    version="1.0.0",
    namespace=NameSpace.CISA,
    name="CISA BOD 26-04",
    definition="Decision table for CISA BOD 26-04.",
    decision_points={
        dp.id: dp
        for dp in [
            PUBLICLY_EXPOSED,
            InKEV,
            AUTOMATABLE,
            TECHNICAL_IMPACT,
            OUTCOMES,
        ]
    },
    outcome=OUTCOMES.id,
    mapping=[
        {
            "cisa:KEV:1.0.0": "N",
            "cisa:AE:1.0.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "cisa:BOD2604:1.0.0": "FSU",
        },
        {
            "cisa:KEV:1.0.0": "Y",
            "cisa:AE:1.0.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "cisa:BOD2604:1.0.0": "14D",
        },
        {
            "cisa:KEV:1.0.0": "N",
            "cisa:AE:1.0.0": "Y",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "cisa:BOD2604:1.0.0": "60D",
        },
        {
            "cisa:KEV:1.0.0": "N",
            "cisa:AE:1.0.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "cisa:BOD2604:1.0.0": "60D",
        },
        {
            "cisa:KEV:1.0.0": "N",
            "cisa:AE:1.0.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "cisa:BOD2604:1.0.0": "FSU",
        },
        {
            "cisa:KEV:1.0.0": "Y",
            "cisa:AE:1.0.0": "Y",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            "cisa:BOD2604:1.0.0": "14D",
        },
        {
            "cisa:KEV:1.0.0": "Y",
            "cisa:AE:1.0.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "cisa:BOD2604:1.0.0": "14D",
        },
        {
            "cisa:KEV:1.0.0": "N",
            "cisa:AE:1.0.0": "Y",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "cisa:BOD2604:1.0.0": "14D",
        },
        {
            "cisa:KEV:1.0.0": "Y",
            "cisa:AE:1.0.0": "N",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "cisa:BOD2604:1.0.0": "14D",
        },
        {
            "cisa:KEV:1.0.0": "N",
            "cisa:AE:1.0.0": "Y",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "cisa:BOD2604:1.0.0": "14D",
        },
        {
            "cisa:KEV:1.0.0": "N",
            "cisa:AE:1.0.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "cisa:BOD2604:1.0.0": "60D",
        },
        {
            "cisa:KEV:1.0.0": "Y",
            "cisa:AE:1.0.0": "Y",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "P",
            "cisa:BOD2604:1.0.0": "3D",
        },
        {
            "cisa:KEV:1.0.0": "Y",
            "cisa:AE:1.0.0": "Y",
            "ssvc:A:2.0.0": "N",
            "ssvc:TI:1.0.0": "T",
            "cisa:BOD2604:1.0.0": "3DF",
        },
        {
            "cisa:KEV:1.0.0": "Y",
            "cisa:AE:1.0.0": "N",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "cisa:BOD2604:1.0.0": "3DF",
        },
        {
            "cisa:KEV:1.0.0": "N",
            "cisa:AE:1.0.0": "Y",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "cisa:BOD2604:1.0.0": "3D",
        },
        {
            "cisa:KEV:1.0.0": "Y",
            "cisa:AE:1.0.0": "Y",
            "ssvc:A:2.0.0": "Y",
            "ssvc:TI:1.0.0": "T",
            "cisa:BOD2604:1.0.0": "3DF",
        },
    ],
)

VERSIONS = [
    BOD_26_04,
]
LATEST = BOD_26_04


def main():

    print("## BODs Decision Table Object")
    print()
    print(BOD_26_04.model_dump_json(indent=2))

    print("## BODs Decision Table Longform DataFrame CSV")
    print()
    from ssvc.decision_tables.base import decision_table_to_longform_df

    print(decision_table_to_longform_df(BOD_26_04).to_csv(index=False))


if __name__ == "__main__":
    main()
