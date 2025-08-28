#!/usr/bin/env python
"""
CVSS Subsequent System Integrity Impact Decision Point
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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

SI_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="There is a total loss of integrity, or a complete loss of protection. For example, the attacker is able "
    "to modify any/all files protected by the Subsequent System. Alternatively, only some files can be "
    "modified, but malicious modification would present a direct, serious consequence to the Subsequent "
    "System.",
)

SI_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="Modification of data is possible, but the attacker does not have control over the consequence of a "
    "modification, or the amount of modification is limited. The data modification does not have a direct, "
    "serious impact to the Subsequent System.",
)

SI_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no loss of integrity within the Subsequent System or all integrity impact is constrained to "
    "the Vulnerable System.",
)

SUBSEQUENT_INTEGRITY_IMPACT_1 = CvssDecisionPoint(
    name="Integrity Impact to the Subsequent System",
    key="SI",
    definition="This metric measures the impact to integrity of a successfully exploited vulnerability. Integrity "
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

VERSIONS = (SUBSEQUENT_INTEGRITY_IMPACT_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
