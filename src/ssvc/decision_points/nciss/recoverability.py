#!/usr/bin/env python
"""
Provides a decision point to represent the recoverability of a system.
Based on the [National Cybersecurity Incident Scoring System (NCISS)](https://www.cisa.gov/sites/default/files/2023-01/cisa_national_cyber_incident_scoring_system_s508c.pdf)
"""
#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
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
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.nciss.base import NcissDecisionPoint


REGULAR = SsvcDecisionPointValue(
    name="Regular",
    key="R",
    description="Time to recovery is predictable with existing resources.",
)

SUPPLEMENTED = SsvcDecisionPointValue(
    name="Supplemented",
    key="S",
    description="Time to recover is predictable with additional resources.",
)

EXTENDED = SsvcDecisionPointValue(
    name="Extended",
    key="E",
    description="Time to recovery is unpredictable; additional resources and outside assistance may be required.",
)

NOT_RECOVERABLE = SsvcDecisionPointValue(
    name="Not Recoverable",
    key="N",
    description="Recovery from the incident is not possible (e.g., sensitive data was exfiltrated and posted publicly, investigation launched).",
)

RECOVERABILITY = NcissDecisionPoint(
    name="Recoverability",
    description="Represents the scope of resources needed to recover from the incident.",
    key="RECOVERABILITY",
    version="1.0.0",
    values=(REGULAR, SUPPLEMENTED, EXTENDED, NOT_RECOVERABLE),
)

VERSIONS = (RECOVERABILITY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
