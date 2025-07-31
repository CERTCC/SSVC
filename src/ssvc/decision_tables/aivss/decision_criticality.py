#!/usr/bin/env python
"""
AIVSS Decision Criticality Decision Table
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

from ssvc.decision_points.aivss.decision_criticality import LATEST as DC
from ssvc.decision_points.aivss.financial_impact import LATEST as FI
from ssvc.decision_points.aivss.operational_disruption import LATEST as OD
from ssvc.decision_points.aivss.reputational_damage import LATEST as RD
from ssvc.decision_points.aivss.safety_critical import LATEST as SC
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

DECISION_CRITICALITY = DecisionTable(
    namespace=NameSpace.AIVSS,
    name="Decision Criticality",
    version="1.0.0",
    description="A decision table for assessing the criticality of decisions supported by AI systems.",
    decision_points={dp.id: dp for dp in [SC, FI, RD, OD, DC]},
    outcome=DC.id,
)


VERSIONS = [
    DECISION_CRITICALITY,
]
LATEST = VERSIONS[-1]


def main():

    print(LATEST.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
