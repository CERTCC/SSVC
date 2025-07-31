#!/usr/bin/env python
"""
AIVSS Adaptability Decision Table
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

from ssvc.decision_points.aivss.adaptability import LATEST as AD
from ssvc.decision_points.aivss.adversarial_training import LATEST as AT
from ssvc.decision_points.aivss.continuous_monitoring import LATEST as CM
from ssvc.decision_points.aivss.retraining_capabilities import LATEST as RT
from ssvc.decision_points.aivss.threat_intelligence_integration import LATEST as TI
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

V1_0_0 = DecisionTable(
    namespace=NameSpace.AIVSS,
    name="Adaptability",
    version="1.0.0",
    description="A decision table for assessing the adaptability of AI systems.",
    decision_points={dp.id: dp for dp in [CM, RT, TI, AT, AD]},
    outcome=AD.id,
)


VERSIONS = [
    V1_0_0,
]
LATEST = VERSIONS[-1]


def main():

    print(LATEST.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
