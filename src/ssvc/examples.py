#!/usr/bin/env python
"""
Example SSVC object instances
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

import datetime

from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.selection import (
    MinimalDecisionPointValue,
    Reference,
    Selection,
    SelectionList,
)

EXAMPLE_DECISION_POINT_1 = DecisionPoint(
    namespace="example",
    key="KEY1",
    version="1.0.0",
    name="Example Decision Point",
    definition="This is a sample decision point for demonstration purposes. Values must be an ordered list.",
    values=(
        DecisionPointValue(
            key="V1",
            name="Value One",
            definition="Value One definition.",
        ),
        DecisionPointValue(
            key="V2",
            name="Value Two",
            definition="Value Two definition.",
        ),
    ),
    registered=False,
)

EXAMPLE_DECISION_POINT_2 = DecisionPoint(
    namespace="example",
    key="KEY2",
    version="1.0.0",
    name="Example Decision Point 2",
    definition="This is another sample decision point for demonstration purposes. Values must be an ordered list.",
    values=(
        DecisionPointValue(
            key="A",
            name="Value A",
            definition="Value A definition.",
        ),
        DecisionPointValue(
            key="B",
            name="Value B",
            definition="Value B definition.",
        ),
    ),
    registered=False,
)
EXAMPLE_OUTCOME_DECISION_POINT = DecisionPoint(
    namespace="example",
    key="OUTCOME",
    version="1.0.0",
    name="Example Outcome Decision Point",
    definition="This is a sample outcome decision point for demonstration purposes. Values must be an ordered list.",
    values=(
        DecisionPointValue(
            key="O1",
            name="Outcome One",
            definition="Outcome One definition.",
        ),
        DecisionPointValue(
            key="O2",
            name="Outcome Two",
            definition="Outcome Two definition.",
        ),
        DecisionPointValue(
            key="O3",
            name="Outcome Three",
            definition="Outcome Three definition.",
        ),
    ),
    registered=False,
)

EXAMPLE_DECISION_TABLE = DecisionTable(
    namespace="example",
    key="DT1",
    version="1.0.0",
    name="Example Decision Table",
    definition="This is a sample decision table for demonstration purposes.",
    decision_points={
        dp.id: dp
        for dp in [
            EXAMPLE_DECISION_POINT_1,
            EXAMPLE_DECISION_POINT_2,
            EXAMPLE_OUTCOME_DECISION_POINT,
        ]
    },
    outcome=EXAMPLE_OUTCOME_DECISION_POINT.id,
    registered=False,
)
EXAMPLE_SELECTION_1 = Selection.from_decision_point(
    decision_point=EXAMPLE_DECISION_POINT_1
)
EXAMPLE_SELECTION_1.values = [
    EXAMPLE_SELECTION_1.values[0],
]


EXAMPLE_SELECTION_2 = Selection.from_decision_point(
    decision_point=EXAMPLE_DECISION_POINT_2
)
EXAMPLE_SELECTION_LIST = SelectionList(
    target_ids=["VU#9999999", "CVE-1900-0001"],
    selections=[EXAMPLE_SELECTION_1, EXAMPLE_SELECTION_2],
    timestamp=datetime.datetime.now(tz=datetime.timezone.utc),
    references=[
        Reference(uri="https://example.com", summary="Example reference"),
    ],
)

EXAMPLE_MINIMAL_DECISION_POINT_VALUE = MinimalDecisionPointValue(
    key="KEY_REQUIRED",
)
