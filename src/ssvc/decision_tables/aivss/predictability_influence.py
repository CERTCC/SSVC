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
from ssvc.decision_points.aivss.deceptiveness_potential import (
    DECEPTIVENESS_POTENTIAL_01,
)
from ssvc.decision_points.aivss.non_determinism import NON_DETERMINISM_01
from ssvc.decision_points.aivss.opacity_reflexivity import (
    OPACITY_REFLEXIVITY_01,
)
from ssvc.decision_points.aivss.predictability_influence import (
    PREDICTABILITY_INFLUENCE_01,
)
from ssvc.decision_points.aivss.verification_capability import (
    VERIFICATION_CAPABILITY_01,
)
from ssvc.decision_tables.base import DecisionTable

V1_0_0 = DecisionTable(
    key="PI",
    version="1.0.0",
    namespace=AIVSS_NS,
    name="Predictability and Influence",
    definition="TODO writeme",
    decision_points={
        dp.id: dp
        for dp in [
            NON_DETERMINISM_01,
            OPACITY_REFLEXIVITY_01,
            VERIFICATION_CAPABILITY_01,
            DECEPTIVENESS_POTENTIAL_01,
            PREDICTABILITY_INFLUENCE_01,
        ]
    },
    outcome=PREDICTABILITY_INFLUENCE_01.id,
    mapping=[
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "V",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "V",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "V",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "V",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "D",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "V",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "B",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "T",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "U",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "F",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "P",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "K",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "P",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "F",
            "x_org.owasp#aivss:PI:1.0.0": "O",
        },
        {
            "x_org.owasp#aivss:ND:1.0.0": "H",
            "x_org.owasp#aivss:OR:1.0.0": "O",
            "x_org.owasp#aivss:VC:1.0.0": "U",
            "x_org.owasp#aivss:DP:1.0.0": "S",
            "x_org.owasp#aivss:PI:1.0.0": "O",
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
