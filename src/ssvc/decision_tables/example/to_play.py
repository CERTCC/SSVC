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

from ssvc.decision_points.example.weather import LATEST as WEATHER
from ssvc.decision_points.example.humidity import LATEST as HUMIDITY
from ssvc.outcomes.basic.yn import LATEST as YESNO


from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

dp_dict = {
    dp.id: dp for dp in [WEATHER, HUMIDITY, YESNO]
}


TOPLAY_1 = DecisionTable(
    namespace="x_example.test#play",
    key="TP",
    version="1.0.0",
    name="To Play",
    definition="To play or not to play that is the question",
    decision_points={
        dp.id: dp for dp in [WEATHER, HUMIDITY, YESNO]
    },
    outcome=YESNO.id,
    mapping=[
    {
      "x_example.test#forecast:W:1.0.0": "R",
      "x_example.test#forecast:H:1.0.0": "H",
      "basic:YN:1.0.0": "N"
    },
    {
      "x_example.test#forecast:W:1.0.0": "O",
      "x_example.test#forecast:H:1.0.0": "H",
      "basic:YN:1.0.0": "N"
    },
    {
      "x_example.test#forecast:W:1.0.0": "R",
      "x_example.test#forecast:H:1.0.0": "L",
      "basic:YN:1.0.0": "N"
    },
    {
      "x_example.test#forecast:W:1.0.0": "S",
      "x_example.test#forecast:H:1.0.0": "H",
      "basic:YN:1.0.0": "N"
    },
    {
      "x_example.test#forecast:W:1.0.0": "O",
      "x_example.test#forecast:H:1.0.0": "L",
      "basic:YN:1.0.0": "Y"
    },
    {
      "x_example.test#forecast:W:1.0.0": "S",
      "x_example.test#forecast:H:1.0.0": "L",
      "basic:YN:1.0.0": "Y"
    }
    ],
)

VERSIONS = [
    TOPLAY_1,
]
LATEST = TOPLAY_1


def main():

    print("## To Play Decision Table Object")
    print()
    print(TOPLAY_1.model_dump_json(indent=2))

    print("## To Play Decision Table Longform DataFrame CSV")
    print()
    from ssvc.decision_tables.base import decision_table_to_longform_df

    print(decision_table_to_longform_df(TOPLAY_1).to_csv(index=False))


if __name__ == "__main__":
    main()
