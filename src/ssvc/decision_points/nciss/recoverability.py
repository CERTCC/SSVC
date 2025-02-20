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

# RECOVERABILITY
# Recoverability represents the scope of resources needed to recover from the incident. In many cases, an
# entity’s internal computer network defense staff will be able to handle an incident without external support,
# resulting in a recoverability classification of Regular. An example of a Regular recovery would be a phishing
# email that was automatically blocked by a mail server. In Extended recoverability cases, significant efforts
# such as a multi-agency, multi-organizational response task force may be needed for recovery. For example, if
# an entity requests support from CISA, the incident is by its nature an Extended recovery. Lastly, it may not be
# feasible to recover from some types of incidents, such as significant confidentiality or privacy compromises.
# REGULAR
# Time to recovery is predictable with existing resources.

REGULAR = SsvcDecisionPointValue(
    name="Regular",
    key="R",
    description="Time to recovery is predictable with existing resources.",
)

# SUPPLEMENTED
# Time to recover is predictable with additional resources.

SUPPLEMENTED = SsvcDecisionPointValue(
    name="Supplemented",
    key="S",
    description="Time to recover is predictable with additional resources.",
)

# EXTENDED
# Time to recovery is unpredictable; additional resources and outside assistance may be required.

EXTENDED = SsvcDecisionPointValue(
    name="Extended",
    key="E",
    description="Time to recovery is unpredictable; additional resources and outside assistance may be required.",
)

# NOT RECOVERABLE
# Recovery from the incident is not possible (e.g., sensitive data was exfiltrated and posted publicly,
# investigation launched).

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
