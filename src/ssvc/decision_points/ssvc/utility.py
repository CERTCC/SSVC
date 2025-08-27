#!/usr/bin/env python

"""
Provides the Utility decision point and its values.
"""

#  Copyright (c) 2024-2025 Carnegie Mellon University.
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

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

SUPER_EFFECTIVE_2 = DecisionPointValue(
    name="Super Effective",
    key="S",
    definition="Automatable:Yes AND Value Density:Concentrated",
)

EFFICIENT_2 = DecisionPointValue(
    name="Efficient",
    key="E",
    definition="(Automatable:Yes AND Value Density:Diffuse) OR (Automatable:No AND Value Density:Concentrated)",
)

LABORIOUS_2 = DecisionPointValue(
    name="Laborious",
    key="L",
    definition="Automatable:No AND Value Density:Diffuse",
)

SUPER_EFFECTIVE = DecisionPointValue(
    name="Super Effective",
    key="S",
    definition="Virulence:Rapid and Value Density:Concentrated",
)

EFFICIENT = DecisionPointValue(
    name="Efficient",
    key="E",
    definition="Virulence:Rapid and Value Density:Diffuse OR Virulence:Slow and Value Density:Concentrated",
)

LABORIOUS = DecisionPointValue(
    name="Laborious",
    key="L",
    definition="Virulence:Slow and Value Density:Diffuse",
)

UTILITY_1 = SsvcDecisionPoint(
    name="Utility",
    definition="The Usefulness of the Exploit to the Adversary",
    key="U",
    version="1.0.0",
    values=(
        LABORIOUS,
        EFFICIENT,
        SUPER_EFFECTIVE,
    ),
)

UTILITY_1_0_1 = SsvcDecisionPoint(
    name="Utility",
    definition="The Usefulness of the Exploit to the Adversary",
    key="U",
    version="1.0.1",
    values=(
        LABORIOUS_2,
        EFFICIENT_2,
        SUPER_EFFECTIVE_2,
    ),
)

VERSIONS = (UTILITY_1, UTILITY_1_0_1)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
