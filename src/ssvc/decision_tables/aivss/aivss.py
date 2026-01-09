#!/usr/bin/env python

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

"""
Provides TODO writeme
"""
from ssvc.decision_points.aivss.agentic_impact import AGENTIC_IMPACT_LEVEL_01
from ssvc.decision_points.aivss.base import AIVSS_NS
from ssvc.decision_points.aivss.systemic_impact import SYSTEMIC_IMPACT_01
from ssvc.decision_points.ssvc.exploitation import EXPLOITATION_1_1_0
from ssvc.decision_tables.base import DecisionTable
from ssvc.outcomes.ssvc.dsoi import DSOI

V1_0_0 = DecisionTable(
    key="AIVSS",
    name="AIVSS Decision Table",
    namespace=AIVSS_NS,
    version="1.0.0",
    definition="Decision table for the AIVSS framework.",
    decision_points={
        dp.id: dp
        for dp in [
            EXPLOITATION_1_1_0,
            AGENTIC_IMPACT_LEVEL_01,
            SYSTEMIC_IMPACT_01,
            DSOI,
        ]
    },
    outcome=DSOI.id,
    mapping=[
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "D",
        },
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "N",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "S",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "P",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "C",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "O",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "S",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "C",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "S",
            "ssvc:DSOI:1.0.0": "I",
        },
        {
            "ssvc:E:1.1.0": "A",
            "aivss:AIL:1.0.0": "P",
            "aivss:SI:1.0.0": "R",
            "ssvc:DSOI:1.0.0": "I",
        },
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_tables.helpers import print_dt_version

    print_dt_version(V1_0_0)


if __name__ == "__main__":
    main()
