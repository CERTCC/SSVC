#!/usr/bin/env python
"""
Provides an example decision table using EPSS probability as a decision point.
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

from ssvc.decision_points.basic.probability.five_weighted import (
    P5W as FIVE_WEIGHTED,
)
from ssvc.decision_points.cisa.in_kev import IN_KEV_1 as IN_KEV
from ssvc.decision_points.cvss.exploit_maturity import (
    EXPLOIT_MATURITY_2_NoX as EXPLOIT_MATURITY,
)
from ssvc.decision_points.ssvc.exploitation import (
    EXPLOITATION_1_1_0 as EXPLOITATION,
)
from ssvc.decision_tables.example.base import ExampleDecisionTable

EXAMPLE = ExampleDecisionTable(
    key="EXP",
    version="1.0.0",
    name="Exploitation Data Integration Example",
    definition="An example decision table that uses multiple exploitation-related decision points, including EPSS probability",
    decision_points={
        dp.id: dp
        for dp in (EXPLOIT_MATURITY, IN_KEV, FIVE_WEIGHTED, EXPLOITATION)
    },
    outcome=EXPLOITATION.id,
    mapping=[
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P0_30",
            "ssvc:E:1.1.0": "N",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P0_30",
            "ssvc:E:1.1.0": "P",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P0_30",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P30_55",
            "ssvc:E:1.1.0": "N",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P0_30",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P0_30",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P30_55",
            "ssvc:E:1.1.0": "P",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P30_55",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P55_75",
            "ssvc:E:1.1.0": "N",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P0_30",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P30_55",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P30_55",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P55_75",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P55_75",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P75_90",
            "ssvc:E:1.1.0": "P",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P30_55",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P55_75",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P55_75",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P75_90",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P75_90",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P90_100",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P55_75",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P75_90",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P75_90",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P90_100",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "U",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P90_100",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P75_90",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "N",
            "basic:P_5W:1.0.0": "P90_100",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "P",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P90_100",
            "ssvc:E:1.1.0": "A",
        },
        {
            "cvss:E_NoX:2.0.0": "A",
            "cisa:KEV:1.0.0": "Y",
            "basic:P_5W:1.0.0": "P90_100",
            "ssvc:E:1.1.0": "A",
        },
    ],
)


def fix_mapping():
    for row in EXAMPLE.mapping:
        # set the defaults based on CVSS
        if row["cvss:E_NoX:2.0.0"] == "U":
            row["ssvc:E:1.1.0"] = "N"
        elif row["cvss:E_NoX:2.0.0"] == "P":
            row["ssvc:E:1.1.0"] = "P"
        elif row["cvss:E_NoX:2.0.0"] == "A":
            row["ssvc:E:1.1.0"] = "A"

        # now override based on IN_KEV
        if row["cisa:KEV:1.0.0"] == "Y":
            row["ssvc:E:1.1.0"] = "A"

        # now update based on EPSS percentile
        if row["basic:P_5W:1.0.0"] == "P90_100":
            # force everything to A
            row["ssvc:E:1.1.0"] = "A"
        elif row["basic:P_5W:1.0.0"] == "P75_90":
            # bump N to P, P to A
            if row["ssvc:E:1.1.0"] == "P":
                row["ssvc:E:1.1.0"] = "A"
            elif row["ssvc:E:1.1.0"] == "N":
                row["ssvc:E:1.1.0"] = "P"
        elif row["basic:P_5W:1.0.0"] == "P55_75":
            # just bump P to A
            if row["ssvc:E:1.1.0"] == "P":
                row["ssvc:E:1.1.0"] = "A"


fix_mapping()


def main():
    print(EXAMPLE.model_dump_json(indent=2))

    print(EXAMPLE.mapping)


if __name__ == "__main__":
    main()
