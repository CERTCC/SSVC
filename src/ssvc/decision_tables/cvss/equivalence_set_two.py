#!/usr/bin/env python
"""
Provides a decision table modeling equivalence set 2 from CVSS v4"""

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

# https://www.first.org/cvss/v4-0/specification-document
# Table 25: EQ2 - MacroVectors
#
# Levels	Constraints	Highest Severity Vector(s)
# 0	AC:L and AT:N	AC:L/AT:N
# 1	not (AC:L and AT:N)	AC:L/AT:P or AC:H/AT:N

from ssvc.decision_points.cvss.attack_complexity import (
    ATTACK_COMPLEXITY_3_0_1 as AC,
)
from ssvc.decision_points.cvss.attack_requirements import (
    ATTACK_REQUIREMENTS_1 as AT,
)

from ssvc.decision_points.cvss.equivalence_set_2 import EQ2
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

V1_0_0 = DecisionTable(
    namespace=NameSpace.CVSS,
    key="CVSS4_EQ2",
    version="1.0.0",
    name="CVSS v4 Equivalence Set 2",
    definition="This decision table models equivalence set 2 from CVSS v4. Factors include Attack Complexity (AC) and Attack Requirements (AT).",
    decision_points={dp.id: dp for dp in (AC, AT, EQ2)},
    outcome=EQ2.id,
    mapping=[
        {"cvss:AC:3.0.1": "H", "cvss:AT:1.0.0": "P", "cvss:EQ2:1.0.0": "L"},
        {"cvss:AC:3.0.1": "L", "cvss:AT:1.0.0": "P", "cvss:EQ2:1.0.0": "L"},
        {"cvss:AC:3.0.1": "H", "cvss:AT:1.0.0": "N", "cvss:EQ2:1.0.0": "L"},
        {"cvss:AC:3.0.1": "L", "cvss:AT:1.0.0": "N", "cvss:EQ2:1.0.0": "H"},
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version

    print_dt_version(LATEST, longform=False)


if __name__ == "__main__":
    main()
