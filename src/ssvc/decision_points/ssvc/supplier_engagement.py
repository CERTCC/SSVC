#!/usr/bin/env python

"""
Provides the Supplier Engagement decision point and its values.
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
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

UNRESPONSIVE = DecisionPointValue(
    name="Unresponsive",
    key="U",
    definition="The supplier is not responding to the reporter’s contact effort and not actively participating in the coordination effort.",
)

ACTIVE = DecisionPointValue(
    name="Active",
    key="A",
    definition="The supplier is responding to the reporter’s contact effort and actively participating in the coordination effort.",
)

SUPPLIER_ENGAGEMENT_1 = SsvcDecisionPoint(
    name="Supplier Engagement",
    definition="Is the supplier responding to the reporter’s contact effort and actively participating in the coordination effort?",
    key="SE",
    version="1.0.0",
    values=(
        ACTIVE,
        UNRESPONSIVE,
    ),
)

VERSIONS = (SUPPLIER_ENGAGEMENT_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
