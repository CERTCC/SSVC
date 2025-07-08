#!/usr/bin/env python
"""
Provides a decision point for assessing the pervasiveness of predisposing conditions based on Table F-5 from NIST SP 800-30 Revision 1.
ASSESSMENT SCALE – PERVASIVENESS OF PREDISPOSING CONDITIONS
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

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.nist.base import NistDecisionPoint

VERY_LOW = DecisionPointValue(
    name="Very Low",
    description="Applies to few organizational missions/business functions (Tier 1), mission/business processes (Tier 2), or information systems (Tier 3)",
    key="VL",
)
LOW = DecisionPointValue(
    name="Low",
    description="Applies to some organizational missions/business functions (Tier 1), mission/business processes (Tier 2), or information systems (Tier 3).",
    key="L",
)
MODERATE = DecisionPointValue(
    name="Moderate",
    description="Applies to many organizational missions/business functions (Tier 1), mission/business processes (Tier 2), or information systems (Tier 3).",
    key="M",
)
HIGH = DecisionPointValue(
    name="High",
    description="Applies to most organizational missions/business functions (Tier 1), mission/business processes (Tier 2), or information systems (Tier 3).",
    key="H",
)
VERY_HIGH = DecisionPointValue(
    name="Very High",
    description="Applies to all organizational missions/business functions (Tier 1), mission/business processes (Tier 2), or information systems (Tier 3).",
    key="VH",
)

CONDITION_PERVASIVENESS = NistDecisionPoint(
    name="Condition Pervasiveness",
    description="Pervasiveness of predisposing conditions",
    key="CP",
    version="1.0.0",
    values=(
        VERY_LOW,
        LOW,
        MODERATE,
        HIGH,
        VERY_HIGH,
    ),
)

VERSIONS = [
    CONDITION_PERVASIVENESS,
]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
