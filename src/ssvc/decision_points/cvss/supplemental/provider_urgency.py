#!/usr/bin/env python
"""
Provides the CVSS supplemental metric Provider Urgency as a SSVC decision point.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
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
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

RED = DecisionPointValue(
    name="Red",
    key="R",
    definition="Provider has assessed the impact of this vulnerability as having the highest urgency.",
)
AMBER = DecisionPointValue(
    name="Amber",
    key="A",
    definition="Provider has assessed the impact of this vulnerability as having a moderate urgency.",
)
GREEN = DecisionPointValue(
    name="Green",
    key="G",
    definition="Provider has assessed the impact of this vulnerability as having a reduced urgency.",
)
CLEAR = DecisionPointValue(
    name="Clear",
    key="C",
    definition="Provider has assessed the impact of this vulnerability as having no urgency (Informational).",
)
PROVIDER_URGENCY_1 = CvssDecisionPoint(
    name="Provider Urgency",
    definition="Many vendors currently provide supplemental severity ratings to consumers via product security "
    "advisories. Other vendors publish Qualitative Severity Ratings from the CVSS Specification Document "
    "in their advisories. To facilitate a standardized method to incorporate additional provider-supplied "
    'assessment, an optional "pass-through" Supplemental Metric called Provider Urgency is available.',
    key="U",
    version="1.0.0",
    values=(
        NOT_DEFINED_X,
        CLEAR,
        GREEN,
        AMBER,
        RED,
    ),
)

VERSIONS = (PROVIDER_URGENCY_1,)
LATEST = PROVIDER_URGENCY_1


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
