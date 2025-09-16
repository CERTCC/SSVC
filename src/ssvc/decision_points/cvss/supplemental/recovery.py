#!/usr/bin/env python
"""
Provides the CVSS supplemental metric Recovery
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

AUTOMATIC = DecisionPointValue(
    name="Automatic",
    key="A",
    definition="The system recovers services automatically after an attack has been performed.",
)
USER = DecisionPointValue(
    name="User",
    key="U",
    definition="The system requires manual intervention by the user to recover services, after an attack has "
    "been performed.",
)
IRRECOVERABLE = DecisionPointValue(
    name="Irrecoverable",
    key="I",
    definition="The system services are irrecoverable by the user, after an attack has been performed.",
)
RECOVERY_1 = CvssDecisionPoint(
    name="Recovery",
    definition="The Recovery metric describes the resilience of a system to recover services, in terms of performance "
    "and availability, after an attack has been performed.",
    key="R",
    version="1.0.0",
    values=(
        NOT_DEFINED_X,
        AUTOMATIC,
        USER,
        IRRECOVERABLE,
    ),
)

VERSIONS = (RECOVERY_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
