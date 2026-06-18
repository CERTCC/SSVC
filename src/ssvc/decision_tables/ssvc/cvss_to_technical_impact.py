#!/usr/bin/env python

#  Copyright (c) 2026 Carnegie Mellon University.
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

from ssvc.decision_points.cvss.confidentiality_impact import (
    CONFIDENTIALITY_IMPACT_3_0_0,
)
from ssvc.decision_points.cvss.integrity_impact import INTEGRITY_IMPACT_3_0_0
from ssvc.decision_points.cvss.privileges_required import (
    PRIVILEGES_REQUIRED_1_0_1,
)
from ssvc.decision_points.ssvc.technical_impact import TECHNICAL_IMPACT_1
from ssvc.decision_tables.base import DecisionTable
from ssvc.namespaces import NameSpace

V1_0_0 = DecisionTable(
    namespace=NameSpace.SSVC,
    key="CVSS4_TO_TI",
    name="CVSSv4 to Technical Impact",
    definition="Maps CVSS v4 vector elements to SSVC Technical Impact",
    version="1.0.0",
    decision_points={
        dp.id: dp
        for dp in [
            PRIVILEGES_REQUIRED_1_0_1,
            CONFIDENTIALITY_IMPACT_3_0_0,
            INTEGRITY_IMPACT_3_0_0,
            TECHNICAL_IMPACT_1,
        ]
    },
    outcome=TECHNICAL_IMPACT_1.id,
    mapping=[
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "N",
            "ssvc:TI:1.0.0": "P",
            # TODO: See comment thread on Issue #195 about this row.
            # It could be either "P" or "T" depending on how that thread resolves.
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "N",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "P",
            # TODO: See comment thread on Issue #195 about this row.
            # It could be either "P" or "T" depending on how that thread resolves.
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "P",
        },
        {
            "cvss:PR:1.0.1": "H",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "T",
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "L",
            "ssvc:TI:1.0.0": "T",
            # TODO: See comment thread on Issue #195 about this row.
            # It could be either "P" or "T" depending on how that thread resolves.
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "L",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "T",
            # TODO: See comment thread on Issue #195 about this row.
            # It could be either "P" or "T" depending on how that thread resolves.
        },
        {
            "cvss:PR:1.0.1": "L",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "T",
        },
        {
            "cvss:PR:1.0.1": "N",
            "cvss:VC:3.0.0": "H",
            "cvss:VI:3.0.0": "H",
            "ssvc:TI:1.0.0": "T",
        },
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version

    print_dt_version(LATEST)


if __name__ == "__main__":
    main()
