#!/usr/bin/env python
"""
CVSS Subsequent System Integrity Impact Decision Point
"""
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

SI_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is a total loss of integrity, or a complete loss of protection. For example, the attacker is able "
    "to modify any/all files protected by the Subsequent System. Alternatively, only some files can be "
    "modified, but malicious modification would present a direct, serious consequence to the Subsequent "
    "System.",
)

SI_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Modification of data is possible, but the attacker does not have control over the consequence of a "
    "modification, or the amount of modification is limited. The data modification does not have a direct, "
    "serious impact to the Subsequent System.",
)

SI_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no loss of integrity within the Subsequent System or all integrity impact is constrained to "
    "the Vulnerable System.",
)

SUBSEQUENT_INTEGRITY_IMPACT_1 = CvssDecisionPoint(
    name="Integrity Impact to the Subsequent System",
    key="SI",
    description="This metric measures the impact to integrity of a successfully exploited vulnerability. Integrity "
    "refers to the trustworthiness and veracity of information. Integrity of a system is impacted when "
    "an attacker causes unauthorized modification of system data. Integrity is also impacted when a "
    "system user can repudiate critical actions taken in the context of the system (e.g. due to "
    "insufficient logging). The resulting score is greatest when the consequence to the system is "
    "highest.",
    version="1.0.0",
    values=(
        SI_NONE,
        SI_LOW,
        SI_HIGH,
    ),
)

versions = [
    SUBSEQUENT_INTEGRITY_IMPACT_1,
]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
