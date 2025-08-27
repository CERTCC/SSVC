#!/usr/bin/env python

"""
This module provides the Public Value Added decision point for the Stakeholder Specific Vulnerability Categorization (SSVC) framework.
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

LIMITED = DecisionPointValue(
    name="Limited",
    key="L",
    definition="Minimal value added to the existing public information because existing information is already high quality and in multiple outlets.",
)

AMPLIATIVE = DecisionPointValue(
    name="Ampliative",
    key="A",
    definition="Amplifies and/or augments the existing public information about the vulnerability, for example, adds additional detail, addresses or corrects errors in other public information, draws further attention to the vulnerability, etc.",
)

PRECEDENCE = DecisionPointValue(
    name="Precedence",
    key="P",
    definition="The publication would be the first publicly available, or be coincident with the first publicly available.",
)

PUBLIC_VALUE_ADDED_1 = SsvcDecisionPoint(
    name="Public Value Added",
    definition="How much value would a publication from the coordinator benefit the broader community?",
    key="PVA",
    version="1.0.0",
    values=(LIMITED, AMPLIATIVE, PRECEDENCE),
)


VERSIONS = (PUBLIC_VALUE_ADDED_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
