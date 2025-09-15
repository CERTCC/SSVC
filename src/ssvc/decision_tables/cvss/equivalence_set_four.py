#!/usr/bin/env python
"""
Provides CVSS v4 Equivalence Set 4 Decision Table
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
#
#
# https://www.first.org/cvss/v4-0/specification-document
# Table 27: EQ4 - MacroVectors
#
# Levels	Constraints	Highest Severity Vector(s)
# 0	MSI:S or MSA:S	SC:H/SI:S/SA:S
# 1	not (MSI:S or MSA:S) and (SC:H or SI:H or SA:H)	SC:H/SI:H/SA:H
# 2	not (MSI:S or MSA:S) and not (SC:H or SI:H or SA:H)	SC:L/SI:L/SA:L

from ssvc.decision_points.cvss.equivalence_set_4 import EQ4
from ssvc.decision_points.cvss.modified.modified_subsequent_availability_impact import (
    MSA_NoX as MSA,
)
from ssvc.decision_points.cvss.modified.modified_subsequent_integrity_impact import (
    MSI_NoX as MSI,
)
from ssvc.decision_points.cvss.subsequent_confidentiality_impact import (
    SUBSEQUENT_CONFIDENTIALITY_IMPACT_1 as SC,
)
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

V1_0_0 = DecisionTable(
    namespace=NameSpace.CVSS,
    key="CVSS4_EQ4",
    version="1.0.0",
    name="CVSS v4 Equivalence Set 4",
    definition="This decision table models equivalence set 4 from CVSS v4.",
    decision_points={dp.id: dp for dp in (SC, MSI, MSA, EQ4)},
    outcome=EQ4.id,
    mapping=[
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "L",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "L",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "L",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "L",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "L",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "L",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "L",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "L",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "N",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "N",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "L",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "M",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "L",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "N",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "H",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "H",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "L",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
        },
        {
            "cvss:SC:1.0.0": "H",
            "cvss:MSI_NoX:1.0.1": "S",
            "cvss:MSA_NoX:1.0.1": "S",
            "cvss:EQ4:1.0.0": "H",
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
