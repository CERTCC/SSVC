#!/usr/bin/env python
"""
Models the Human Impact decision table for SSVC.
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

from ssvc.decision_points.ssvc.human_impact import (
    HUMAN_IMPACT_2_0_2 as HumanImpact,
)
from ssvc.decision_points.ssvc.mission_impact import (
    MISSION_IMPACT_2 as MissionImpact,
)
from ssvc.decision_points.ssvc.safety_impact import (
    SAFETY_IMPACT_2 as SituatedSafetyImpact,
)
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

dp_dict = {
    dp.id: dp for dp in [SituatedSafetyImpact, MissionImpact, HumanImpact]
}

HUMAN_IMPACT_1 = DecisionTable(
    namespace=NameSpace.SSVC,
    key="HI",
    version="1.0.0",
    name="Human Impact",
    definition="Human Impact decision table for SSVC",
    decision_points={
        dp.id: dp for dp in [SituatedSafetyImpact, MissionImpact, HumanImpact]
    },
    outcome=HumanImpact.id,
    mapping=[
        {"ssvc:SI:2.0.0": "N", "ssvc:MI:2.0.0": "D", "ssvc:HI:2.0.2": "L"},
        {"ssvc:SI:2.0.0": "N", "ssvc:MI:2.0.0": "MSC", "ssvc:HI:2.0.2": "L"},
        {"ssvc:SI:2.0.0": "N", "ssvc:MI:2.0.0": "MEF", "ssvc:HI:2.0.2": "M"},
        {"ssvc:SI:2.0.0": "N", "ssvc:MI:2.0.0": "MF", "ssvc:HI:2.0.2": "VH"},
        {"ssvc:SI:2.0.0": "M", "ssvc:MI:2.0.0": "D", "ssvc:HI:2.0.2": "L"},
        {"ssvc:SI:2.0.0": "M", "ssvc:MI:2.0.0": "MSC", "ssvc:HI:2.0.2": "L"},
        {"ssvc:SI:2.0.0": "M", "ssvc:MI:2.0.0": "MEF", "ssvc:HI:2.0.2": "M"},
        {"ssvc:SI:2.0.0": "M", "ssvc:MI:2.0.0": "MF", "ssvc:HI:2.0.2": "VH"},
        {"ssvc:SI:2.0.0": "R", "ssvc:MI:2.0.0": "D", "ssvc:HI:2.0.2": "M"},
        {"ssvc:SI:2.0.0": "R", "ssvc:MI:2.0.0": "MSC", "ssvc:HI:2.0.2": "H"},
        {"ssvc:SI:2.0.0": "R", "ssvc:MI:2.0.0": "MEF", "ssvc:HI:2.0.2": "H"},
        {"ssvc:SI:2.0.0": "R", "ssvc:MI:2.0.0": "MF", "ssvc:HI:2.0.2": "VH"},
        {"ssvc:SI:2.0.0": "C", "ssvc:MI:2.0.0": "D", "ssvc:HI:2.0.2": "VH"},
        {"ssvc:SI:2.0.0": "C", "ssvc:MI:2.0.0": "MSC", "ssvc:HI:2.0.2": "VH"},
        {"ssvc:SI:2.0.0": "C", "ssvc:MI:2.0.0": "MEF", "ssvc:HI:2.0.2": "VH"},
        {"ssvc:SI:2.0.0": "C", "ssvc:MI:2.0.0": "MF", "ssvc:HI:2.0.2": "VH"},
    ],
)

VERSIONS = [
    HUMAN_IMPACT_1,
]
LATEST = HUMAN_IMPACT_1


def main():

    print("## Human Impact Decision Table Object")
    print()
    print(HUMAN_IMPACT_1.model_dump_json(indent=2))

    print("## Human Impact Decision Table Longform DataFrame CSV")
    print()
    from ssvc.decision_tables.base import decision_table_to_longform_df

    print(decision_table_to_longform_df(HUMAN_IMPACT_1).to_csv(index=False))


if __name__ == "__main__":
    main()
