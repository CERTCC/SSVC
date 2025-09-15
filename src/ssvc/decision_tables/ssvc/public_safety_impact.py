#!/usr/bin/env python
"""
Public Safety Impact Decision Table
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

from ssvc.decision_points.ssvc.public_safety_impact import (
    PUBLIC_SAFETY_IMPACT_2_0_1 as PSI,
)
from ssvc.decision_points.ssvc.safety_impact import SAFETY_IMPACT_2 as SI
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

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

V1_0_0 = DecisionTable(
    namespace=NameSpace.SSVC,
    key="DT_PSI",
    version="1.0.0",
    name="Public Safety Impact",
    definition="Public Safety Impact Decision Table",
    decision_points={dp.id: dp for dp in [SI, PSI]},
    outcome=PSI.id,
    mapping=[
        {"ssvc:SI:2.0.0": "N", "ssvc:PSI:2.0.1": "M"},
        {"ssvc:SI:2.0.0": "M", "ssvc:PSI:2.0.1": "S"},
        {"ssvc:SI:2.0.0": "R", "ssvc:PSI:2.0.1": "S"},
        {"ssvc:SI:2.0.0": "C", "ssvc:PSI:2.0.1": "S"},
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version

    print_dt_version(LATEST, longform=False)


if __name__ == "__main__":
    main()
