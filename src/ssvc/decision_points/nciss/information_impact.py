#!/usr/bin/env python
"""
Provides the NCISS Information Impact Decision Point.
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

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.nciss.base import NcissDecisionPoint

IMPACT_NONE = SsvcDecisionPointValue(
    key="N",
    name="None",
    description="No information was exfiltrated, modified, deleted, or otherwise compromised.",
)

INTEGRITY = SsvcDecisionPointValue(
    key="I",
    name="Integrity",
    description="The necessary integrity of information was modified without authorization.",
)

PRIVACY = SsvcDecisionPointValue(
    key="P",
    name="Privacy",
    description="The confidentiality of personally identifiable information (PII) "
    "or personal health information (PHI) was compromised.",
)

PROPRIETARY = SsvcDecisionPointValue(
    key="R",
    name="Proprietary",
    description="The confidentiality of unclassified proprietary information, such as "
    "protected critical infrastructure information (PCII), intellectual property, or "
    "trade secrets was compromised.",
)

CLASSIFIED = SsvcDecisionPointValue(
    key="C",
    name="Classified",
    description="The confidentiality of classified information was compromised.",
)

# based on https://www.cisa.gov/sites/default/files/publications/Federal_Incident_Notification_Guidelines_2015.pdf
INFORMATION_IMPACT_1 = NcissDecisionPoint(
    key="II",
    name="Information Impact",
    version="1.0.0",
    description="Describes the type of information lost, compromised, or corrupted.",
    values=(IMPACT_NONE, INTEGRITY, PRIVACY, PROPRIETARY, CLASSIFIED),
)


NO_IMPACT = SsvcDecisionPointValue(
    key="N",
    name="No Impact",
    description="No known data impact.",
)

SUSPECTED_BUT_NOT_IDENTIFIED = SsvcDecisionPointValue(
    key="S",
    name="Suspected But Not Identified",
    description="A data loss or impact to availability is suspected, but no direct confirmation exists.",
)

PROPRIETARY_INFORMATION_BREACH = SsvcDecisionPointValue(
    key="R",
    name="Proprietary Information Breach",
    description="The confidentiality of unclassified proprietary information, such as protected critical infrastructure information (PCII), intellectual property, or trade secrets was compromised.",
)

PRIVACY_DATA_BREACH = SsvcDecisionPointValue(
    key="P",
    name="Privacy Data Breach",
    description="The confidentiality of personally identifiable information (PII) or personal health information (PHI) was compromised.",
)


CRITICAL_SYSTEMS_DATA_BREACH = SsvcDecisionPointValue(
    key="C",
    name="Critical Systems Data Breach",
    description="Data pertaining to a critical system has been exfiltrated.",
)

DESTRUCTION_OF_NON_CRITICAL_SYSTEMS = SsvcDecisionPointValue(
    key="D",
    name="Destruction of Non-Critical Systems",
    description="Destructive techniques, such as master boot record (MBR) overwrite; have been used against a non-critical system.",
)


CORE_CREDENTIAL_COMPROMISE = SsvcDecisionPointValue(
    key="O",
    name="Core Credential Compromise",
    description="Core system credentials (such as domain or enterprise administrative credentials) or credentials for critical systems have been exfiltrated.",
)

DESTRUCTION_OF_CRITICAL_SYSTEM = SsvcDecisionPointValue(
    key="E",
    name="Destruction of Critical System",
    description="Destructive techniques, such as MBR overwrite; have been used against a critical system.",
)

# based on https://www.cisa.gov/sites/default/files/publications/Federal_Incident_Notification_Guidelines.pdf
INFORMATION_IMPACT_2 = NcissDecisionPoint(
    key="II",
    name="Information Impact",
    version="2.0.0",
    description="Describes the type of information lost, compromised, or corrupted.",
    values=(
        NO_IMPACT,
        SUSPECTED_BUT_NOT_IDENTIFIED,
        PRIVACY_DATA_BREACH,
        PROPRIETARY_INFORMATION_BREACH,
        DESTRUCTION_OF_NON_CRITICAL_SYSTEMS,
        CRITICAL_SYSTEMS_DATA_BREACH,
        CORE_CREDENTIAL_COMPROMISE,
        DESTRUCTION_OF_CRITICAL_SYSTEM,
    ),
)

VERSIONS = (
    INFORMATION_IMPACT_1,
    INFORMATION_IMPACT_2,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
