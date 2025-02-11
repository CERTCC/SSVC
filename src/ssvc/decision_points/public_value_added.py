#!/usr/bin/env python

"""
This module provides the Public Value Added decision point for the Stakeholder Specific Vulnerability Categorization (SSVC) framework.
"""

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

LIMITED = SsvcDecisionPointValue(
    name="Limited",
    key="L",
    description="Minimal value added to the existing public information because existing information is already high quality and in multiple outlets.",
)

AMPLIATIVE = SsvcDecisionPointValue(
    name="Ampliative",
    key="A",
    description="Amplifies and/or augments the existing public information about the vulnerability, for example, adds additional detail, addresses or corrects errors in other public information, draws further attention to the vulnerability, etc.",
)

PRECEDENCE = SsvcDecisionPointValue(
    name="Precedence",
    key="P",
    description="The publication would be the first publicly available, or be coincident with the first publicly available.",
)

PUBLIC_VALUE_ADDED_1 = SsvcDecisionPoint(
    name="Public Value Added",
    description="How much value would a publication from the coordinator benefit the broader community?",
    key="PVA",
    version="1.0.0",
    values=(LIMITED, AMPLIATIVE, PRECEDENCE),
)


def main():
    versions = (PUBLIC_VALUE_ADDED_1,)

    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
