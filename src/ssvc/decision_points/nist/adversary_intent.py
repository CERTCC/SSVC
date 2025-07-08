#!/usr/bin/env python
"""
Provides a decision point for assessing adversary intent based on Table D-4 from NIST SP 800-30 Revision 1.
ASSESSMENT SCALE – CHARACTERISTICS OF ADVERSARY INTENT
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
    description="The adversary seeks to usurp, disrupt, or deface the organization’s cyber resources, and does so "
    "without concern about attack detection/disclosure of tradecraft.",
    key="VL",
)
LOW = DecisionPointValue(
    name="Low",
    description="The adversary actively seeks to obtain critical or sensitive information or to usurp/disrupt the "
    "organization’s cyber resources, and does so without concern about attack detection/disclosure of "
    "tradecraft.",
    key="L",
)
MODERATE = DecisionPointValue(
    name="Moderate",
    description="The adversary seeks to obtain or modify specific critical or sensitive information or usurp/disrupt "
    "the organization’s cyber resources by establishing a foothold in the organization’s information "
    "systems or infrastructure. The adversary is concerned about minimizing attack detection/disclosure "
    "of tradecraft, particularly when carrying out attacks over long time periods. The adversary is "
    "willing to impede aspects of the organization’s missions/business functions to achieve these ends.",
    key="M",
)
HIGH = DecisionPointValue(
    name="High",
    description="The adversary seeks to undermine/impede critical aspects of a core mission or business function, "
    "program, or enterprise, or place itself in a position to do so in the future, by maintaining a "
    "presence in the organization’s information systems or infrastructure. The adversary is very "
    "concerned about minimizing attack detection/disclosure of tradecraft, particularly while preparing "
    "for future attacks.",
    key="H",
)
VERY_HIGH = DecisionPointValue(
    name="Very High",
    description="The adversary seeks to undermine, severely impede, or destroy a core mission or business function, "
    "program, or enterprise by exploiting a presence in the organization’s information systems or "
    "infrastructure. The adversary is concerned about disclosure of tradecraft only to the extent that it "
    "would impede its ability to complete stated goals.",
    key="VH",
)

ADVERSARY_INTENT = NistDecisionPoint(
    name="Adversary Intent",
    description="Characteristics of adversary intent",
    key="AI",
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
    ADVERSARY_INTENT,
]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
