#!/usr/bin/env python
"""
Provides a decision table modeling equivalence set 3 from CVSS v4"""

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
# Table 26: EQ3 - MacroVectors
#
# Levels	Constraints	Highest Severity Vector(s)
# 0	VC:H and VI:H	VC:H/VI:H/VA:H
# 1	not (VC:H and VI:H) and (VC:H or VI:H or VA:H)	VC:L/VI:H/VA:H or VC:H/VI:L/VA:H
# 2	not (VC:H or VI:H or VA:H)	VC:L/VI:L/VA:L

from ssvc.decision_points.cvss.availability_impact import (
    AVAILABILITY_IMPACT_3_0_0 as VA,
)
from ssvc.decision_points.cvss.confidentiality_impact import (
    CONFIDENTIALITY_IMPACT_3_0_0 as VC,
)
from ssvc.decision_points.cvss.equivalence_set_3 import EQ3
from ssvc.decision_points.cvss.integrity_impact import (
    INTEGRITY_IMPACT_3_0_0 as VI,
)
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

V1_0_0 = DecisionTable(
    namespace=NameSpace.CVSS,
    key="CVSS4_EQ3",
    version="1.0.0",
    name="CVSS v4 Equivalence Set 3",
    definition="This decision table models equivalence set 3 from CVSS v4.",
    decision_points={dp.id: dp for dp in (VC, VI, VA, EQ3)},
    outcome=EQ3.id,
    mapping=[
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "L",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "L",
        },
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "L",
        },
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "L",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "L",
        },
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "L",
        },
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "L",
        },
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "L",
        },
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "N",
            "cvss:EQ3:1.0.0": "H",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "N",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "L",
            "cvss:EQ3:1.0.0": "H",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "L",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "M",
        },
        {
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "H",
            "cvss:VA:3.0.0": "H",
            "cvss:EQ3:1.0.0": "H",
        },
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version

    print_dt_version(LATEST, longform=False)


if __name__ == "__main__":
    main()
