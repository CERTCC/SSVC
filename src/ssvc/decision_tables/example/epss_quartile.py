#!/usr/bin/env python
"""
Provides an example decision table using EPSS quartiles for probability.
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

from ssvc.decision_points.basic.quantiles.quartiles import (
    LATEST as QUARTILES_LATEST,
)
from ssvc.decision_points.example.base import ExampleDecisionPoint
from ssvc.decision_tables.example.base import ExampleDecisionTable
from ssvc.decision_tables.ssvc.deployer_dt import DEPLOYER_1

outcome_in = DEPLOYER_1.decision_points[DEPLOYER_1.outcome]


outcome_out = ExampleDecisionPoint(
    key=outcome_in.key,
    version=outcome_in.version,
    name=outcome_in.name,
    definition=outcome_in.definition,
    values=outcome_in.values,
)

EXAMPLE = ExampleDecisionTable(
    name="Example EPSS Quartile Decision Table",
    definition="An example decision table using EPSS quartiles to adjust the SSVC Deployer Table outcome.",
    key="EPSS_QRT",
    decision_points={
        dp.id: dp for dp in (QUARTILES_LATEST, outcome_in, outcome_out)
    },
    outcome=outcome_out.id,
)

UPDATE_MAP = {
    "Q1": {"D": "D", "S": "D", "O": "S", "I": "O"},
    "Q2": {"D": "D", "S": "S", "O": "O", "I": "I"},
    "Q3": {"D": "S", "S": "O", "O": "I", "I": "I"},
    "Q4": {"D": "O", "S": "I", "O": "I", "I": "I"},
}


def update_map_doc():
    s = {"Q1": "-1", "Q2": "0", "Q3": "+1", "Q4": "+2"}

    lines = [
        "| EPSS Quartile | Amplification Factor | Deployer Outcome Change |",
        "|:--------------|:-------------------:|:-----------------------|",
    ]
    for quartile, mapping in UPDATE_MAP.items():
        line = f"| {quartile} | {s[quartile]} | "
        parts = []
        for outcome_in, outcome_out in mapping.items():
            parts.append(f"{outcome_in} &rarr; {outcome_out}")
        line += ", ".join(parts)
        line += " |"
        lines.append(line)
    return "\n".join(lines)


def fix_mapping(dt: ExampleDecisionTable):
    for row in dt.mapping:
        row[outcome_out.id] = UPDATE_MAP[row.get("basic:QUARTILES:1.0.0")][
            row.get(outcome_in.id)
        ]


fix_mapping(EXAMPLE)


def main():
    print(EXAMPLE.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
