#!/usr/bin/env python
"""
Provides a decision point to represent the recoverability of a system.
Based on the [National Cybersecurity Incident Scoring System (NCISS)](https://www.cisa.gov/sites/default/files/2023-01/cisa_national_cyber_incident_scoring_system_s508c.pdf)
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
    description="Recovery from the incident is not possible.",
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
