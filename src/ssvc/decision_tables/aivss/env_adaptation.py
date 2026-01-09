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

from ssvc.decision_points.aivss.base import AIVSS_NS
from ssvc.decision_points.aivss.contextual_awareness import (
    CONTEXTUAL_AWARENESS_01,
)
from ssvc.decision_points.aivss.dynamic_identity import DYNAMIC_IDENTITY_01
from ssvc.decision_points.aivss.env_adaptation import ENV_ADAPT_01
from ssvc.decision_points.aivss.memory import MEMORY_01
from ssvc.decision_points.aivss.multi_agent_interactions import (
    MULTI_AGENT_INTERACTIONS_01,
)
from ssvc.decision_tables.base import DecisionTable

V1_0_0 = DecisionTable(
    key="EA",
    name="Environmental Adaptation",
    definition=ENV_ADAPT_01.definition,
    version="1.0.0",
    namespace=AIVSS_NS,
    decision_points={
        dp.id: dp
        for dp in [
            MEMORY_01,
            CONTEXTUAL_AWARENESS_01,
            DYNAMIC_IDENTITY_01,
            MULTI_AGENT_INTERACTIONS_01,
            ENV_ADAPT_01,
        ]
    },
    outcome=ENV_ADAPT_01.id,
    mapping=[
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "I",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "I",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "I",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "I",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "S",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "I",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "L",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "I",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "C",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "T",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "F",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "S",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "S",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "R",
            "aivss:EA:1.0.0": "P",
        },
        {
            "aivss:MU:1.0.0": "M",
            "aivss:CA:1.0.0": "A",
            "aivss:DI:1.0.0": "A",
            "aivss:MAI:1.0.0": "O",
            "aivss:EA:1.0.0": "P",
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
