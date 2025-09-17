#!/usr/bin/env python
"""
Provides CVSS v4 Supplemental Metric for Safety
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

PRESENT = DecisionPointValue(
    name="Present",
    key="P",
    definition="Consequences of the vulnerability meet definition of IEC 61508 consequence categories of "
    '"marginal," "critical," or "catastrophic."',
)
NEGLIGIBLE = DecisionPointValue(
    name="Negligible",
    key="N",
    definition="Consequences of the vulnerability meet definition of IEC 61508 consequence category "
    '"negligible."',
)
SAFETY_1 = CvssDecisionPoint(
    name="Safety",
    definition="The Safety decision point is a measure of the potential for harm to humans or the environment.",
    key="SF",
    version="1.0.0",
    values=(
        NOT_DEFINED_X,
        PRESENT,
        NEGLIGIBLE,
    ),
)

VERSIONS = (SAFETY_1,)
LATEST = SAFETY_1


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
