#!/usr/bin/env python
"""
Provides the CVSS supplemental metric Recovery
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

AUTOMATIC = SsvcDecisionPointValue(name="Automatic", key="A",
                               description="The system recovers services automatically after an attack has been performed.", )
USER = SsvcDecisionPointValue(name="User", key="U",
                               description="The system requires manual intervention by the user to recover services, after an attack has " \
                                           "been performed.", )
IRRECOVERABLE = SsvcDecisionPointValue(name="Irrecoverable", key="I",
                               description="The system services are irrecoverable by the user, after an attack has been performed.", )
RECOVERY_1 = CvssDecisionPoint(
    name="Recovery",
    description="The Recovery metric describes the resilience of a system to recover services, in terms of performance "
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
