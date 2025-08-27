#!/usr/bin/env python
"""
CVSS Equivalence Set 5 Decision Table
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

# Table 28: EQ5 - MacroVectors
#
# Levels	Constraints	Highest Severity Vector(s)
# 0	E:A	E:A
# 1	E:P	E:P
# 2	E:U	E:U


from ssvc.decision_points.cvss.equivalence_set_5 import EQ5
from ssvc.decision_points.cvss.exploit_maturity import (
    EXPLOIT_MATURITY_2_NoX as E,
)
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

V1_0_0 = DecisionTable(
    namespace=NameSpace.CVSS,
    key="CVSS_EQ5",
    version="1.0.0",
    name="CVSS v4 Equivalence Set 5",
    definition="CVSS Equivalence Set 5 Decision Table",
    decision_points={dp.id: dp for dp in [E, EQ5]},
    outcome=EQ5.id,
    mapping=[
        {"cvss:E_NoX:2.0.0": "U", "cvss:EQ5:1.0.0": "L"},
        {"cvss:E_NoX:2.0.0": "P", "cvss:EQ5:1.0.0": "M"},
        {"cvss:E_NoX:2.0.0": "A", "cvss:EQ5:1.0.0": "H"},
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version

    print_dt_version(LATEST, longform=False)


if __name__ == "__main__":
    main()
