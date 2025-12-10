#!/usr/bin/env python

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

"""
Provides TODO writeme
"""

from ssvc.decision_points.aivss.autonomy import AUTONOMY
from ssvc.decision_points.aivss.base import AIVSS_NS
from ssvc.decision_points.aivss.execution_power import EXECUTION_POWER
from ssvc.decision_points.aivss.goal_driven_planning import (
    GOAL_DRIVEN_PLANNING,
)
from ssvc.decision_points.aivss.self_modification import (
    SELF_MODIFICATION_1_1_0 as SELF_MODIFICATION,
)
from ssvc.decision_points.aivss.tool_use import TOOL_USE
from ssvc.decision_tables.base import DecisionTable

V1_0_0 = DecisionTable(
    key="EP",
    name="Execution Power",
    definition="Determines the level of execution power granted to an AI agent, influencing its ability to perform actions autonomously and interact with external systems.",
    version="1.0.0",
    namespace=AIVSS_NS,
    decision_points={
        dp.id: dp
        for dp in [
            AUTONOMY,
            TOOL_USE,
            SELF_MODIFICATION,
            GOAL_DRIVEN_PLANNING,
            EXECUTION_POWER,
        ]
    },
    outcome=EXECUTION_POWER.id,
    mapping=[
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "G",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "C",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "S",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "V",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "CA",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "O",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "F",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "T",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "R",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "A",
            "aivss:EP:1.0.0": "H",
        },
        {
            "aivss:AA:1.0.0": "F",
            "aivss:TU:1.0.0": "A",
            "aivss:SM:1.1.0": "M",
            "aivss:GDP:1.0.0": "U",
            "aivss:EP:1.0.0": "H",
        },
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version
    from ssvc.decision_tables.aivss.utils import Rule, RuleSet, rules_mapping

    print_dt_version(V1_0_0)

    ruleset = RuleSet(
        rules=[
            # Highest severity first
            Rule(value=2, value_count=2, outcome=2),
            Rule(value=2, value_count=1, outcome=1),
            Rule(value=1, value_count=2, outcome=1),
            Rule(value=0, value_count=0, outcome=0),
        ]
    )

    print(rules_mapping(V1_0_0, ruleset))


if __name__ == "__main__":
    main()
