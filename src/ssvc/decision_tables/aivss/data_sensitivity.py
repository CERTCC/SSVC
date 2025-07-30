#!/usr/bin/env python
"""
AIVSS Data Sensitivity Decision Table
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

from ssvc.decision_points.aivss.data_confidentiality import LATEST as DC
from ssvc.decision_points.aivss.data_integrity import LATEST as DI
from ssvc.decision_points.aivss.data_provenance import LATEST as DP
from ssvc.decision_points.aivss.data_sensitivity import LATEST as DS
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

DATA_SENSITIVITY = DecisionTable(
    namespace=NameSpace.AIVSS,
    name="Data Sensitivity",
    version="1.0.0",
    description="A decision table for assessing the sensitivity of data used in AI systems.",
    decision_points={dp.id: dp for dp in [DS, DI, DP, DC]},
    outcome=DS.id,
)


VERSIONS = [
    DATA_SENSITIVITY,
]
LATEST = VERSIONS[-1]


def main():

    print(LATEST.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
