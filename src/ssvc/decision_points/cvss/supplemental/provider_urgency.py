#!/usr/bin/env python
"""
Provides the CVSS supplemental metric Provider Urgency as a SSVC decision point.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
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

from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

RED = SsvcDecisionPointValue(name="Red", key="R",
                               description="Provider has assessed the impact of this vulnerability as having the highest urgency.", )
AMBER = SsvcDecisionPointValue(name="Amber", key="A",
                               description="Provider has assessed the impact of this vulnerability as having a moderate urgency.", )
GREEN = SsvcDecisionPointValue(name="Green", key="G",
                               description="Provider has assessed the impact of this vulnerability as having a reduced urgency.", )
CLEAR = SsvcDecisionPointValue(name="Clear", key="C",
                               description="Provider has assessed the impact of this vulnerability as having no urgency (Informational).", )
PROVIDER_URGENCY_1 = CvssDecisionPoint(
    name="Provider Urgency",
    description="Many vendors currently provide supplemental severity ratings to consumers via product security "
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
