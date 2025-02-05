#!/usr/bin/env python
#  Copyright (c) 2024-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

SUPER_EFFECTIVE_2 = SsvcDecisionPointValue(
    name="Super Effective",
    key="S",
    description="Automatable:Yes AND Value Density:Concentrated",
)

EFFICIENT_2 = SsvcDecisionPointValue(
    name="Efficient",
    key="E",
    description="(Automatable:Yes AND Value Density:Diffuse) OR (Automatable:No AND Value Density:Concentrated)",
)

LABORIOUS_2 = SsvcDecisionPointValue(
    name="Laborious",
    key="L",
    description="Automatable:No AND Value Density:Diffuse",
)

SUPER_EFFECTIVE = SsvcDecisionPointValue(
    name="Super Effective",
    key="S",
    description="Virulence:Rapid and Value Density:Concentrated",
)

EFFICIENT = SsvcDecisionPointValue(
    name="Efficient",
    key="E",
    description="Virulence:Rapid and Value Density:Diffuse OR Virulence:Slow and Value Density:Concentrated",
)

LABORIOUS = SsvcDecisionPointValue(
    name="Laborious",
    key="L",
    description="Virulence:Slow and Value Density:Diffuse",
)

UTILITY_1 = SsvcDecisionPoint(
    name="Utility",
    description="The Usefulness of the Exploit to the Adversary",
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
    description="The Usefulness of the Exploit to the Adversary",
    key="U",
    version="1.0.1",
    values=(
        LABORIOUS_2,
        EFFICIENT_2,
        SUPER_EFFECTIVE_2,
    ),
)


def main():
    versions = (UTILITY_1, UTILITY_1_0_1)

    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
