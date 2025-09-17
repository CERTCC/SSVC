#!/usr/bin/env python
"""
Models the Utility decision table for SSVC.
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

from ssvc.decision_points.ssvc.automatable import LATEST as Automatable
from ssvc.decision_points.ssvc.utility import LATEST as Utility
from ssvc.decision_points.ssvc.value_density import LATEST as ValueDensity
from ssvc.decision_tables.base import (
    DecisionTable,
    decision_table_to_longform_df,
)
from ssvc.decision_tables.helpers import write_csv
from ssvc.namespaces import NameSpace

UTILITY_1 = DecisionTable(
    namespace=NameSpace.SSVC,
    key="U",
    version="1.0.0",
    name="Utility",
    definition="Utility decision table for SSVC",
    decision_points={dp.id: dp for dp in [Automatable, ValueDensity, Utility]},
    outcome=Utility.id,
    mapping=[
        {"ssvc:A:2.0.0": "N", "ssvc:VD:1.0.0": "D", "ssvc:U:1.0.1": "L"},
        {"ssvc:A:2.0.0": "N", "ssvc:VD:1.0.0": "C", "ssvc:U:1.0.1": "E"},
        {"ssvc:A:2.0.0": "Y", "ssvc:VD:1.0.0": "D", "ssvc:U:1.0.1": "E"},
        {"ssvc:A:2.0.0": "Y", "ssvc:VD:1.0.0": "C", "ssvc:U:1.0.1": "S"},
    ],
)

VERSIONS = (UTILITY_1,)
LATEST = VERSIONS[-1]


def main():
    print("## Utility Decision Table Object")
    print()
    print(UTILITY_1.model_dump_json(indent=2))

    print("## Utility Decision Table Longform DataFrame CSV")
    print()
    print(decision_table_to_longform_df(UTILITY_1).to_csv(index=False))

    csvfile = "utility.csv"
    write_csv(UTILITY_1, csvfile)


if __name__ == "__main__":
    main()
