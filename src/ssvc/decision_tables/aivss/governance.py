#!/usr/bin/env python
"""
AIVSS Governance and Validation Decision Table
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

import logging

from ssvc.decision_points.aivss.auditing import LATEST as AU
from ssvc.decision_points.aivss.compliance import LATEST as CO
from ssvc.decision_points.aivss.ethical_framework_alignment import LATEST as EA
from ssvc.decision_points.aivss.governance import LATEST as GV
from ssvc.decision_points.aivss.human_oversight import LATEST as HO
from ssvc.decision_points.aivss.risk_management import LATEST as RM
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

V1_0_0 = DecisionTable(
    namespace=NameSpace.AIVSS,
    key="GV",
    version="1.0.0",
    name="Governance and Validation",
    description="A decision table for assessing the governance and validation of AI systems.",
    decision_points={dp.id: dp for dp in [CO, AU, RM, HO, EA, GV]},
    outcome=GV.id,
)


VERSIONS = [
    V1_0_0,
]
LATEST = VERSIONS[-1]


def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    print(LATEST.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
