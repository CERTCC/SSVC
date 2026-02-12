#!/usr/bin/env python
"""
Models an example to play or not to play decision table for SSVC.
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

from ssvc.decision_points.cisa.in_kev import LATEST as InKEV
from ssvc.decision_points.ssvc.system_exposure import LATEST as EXPOSURE
from ssvc.decision_points.ssvc.high_value_asset import LATEST as HVA
from ssvc.decision_tables.example.base import ExampleDecisionTable
from ssvc.outcomes.ssvc.dsoi import LATEST as OUTCOMES

dp_dict = {dp.id: dp for dp in [InKEV, EXPOSURE, HVA, OUTCOMES]}


BODs_1 = ExampleDecisionTable(
    key="BODs",
    version="1.0.0",
    name="CISA BODs",
    definition="combining several recent BODs",
    decision_points={dp.id: dp for dp in [InKEV, EXPOSURE, HVA, OUTCOMES]},
    outcome=OUTCOMES.id,
    mapping=[
        ]
    )

VERSIONS = [
    BODs_1,
]
LATEST = BODs_1


def main():

    print("## BODs Decision Table Object")
    print()
    print(BODs_1.model_dump_json(indent=2))

    print("## BODs Decision Table Longform DataFrame CSV")
    print()
    from ssvc.decision_tables.base import decision_table_to_longform_df

    print(decision_table_to_longform_df(BODs_1).to_csv(index=False))


if __name__ == "__main__":
    main()
