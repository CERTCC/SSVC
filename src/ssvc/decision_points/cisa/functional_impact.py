#!/usr/bin/env python
"""
Provides the NCISS Functional Impact decision point and values.
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
from ssvc.decision_points.cisa.base import NcissDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

IMPACT_NONE = DecisionPointValue(
    key="N",
    name="No Impact",
    description="Organization has experienced no loss in ability to provide all services to all users.",
)

LOW = DecisionPointValue(
    key="L",
    name="Low",
    description="Organization has experienced a loss of efficiency, but can still provide all critical services to all users with minimal effect on performance.",
)

MEDIUM = DecisionPointValue(
    key="M",
    name="Medium",
    description="Organization has lost the ability to provide a critical service to a subset of system users.",
)

HIGH = DecisionPointValue(
    key="H",
    name="High",
    description="Organization has lost the ability to provide all critical services to all system users.",
)

## based on https://www.cisa.gov/sites/default/files/publications/Federal_Incident_Notification_Guidelines_2015.pdf
FUNCTIONAL_IMPACT_1 = NcissDecisionPoint(
    key="FI",
    name="Functional Impact",
    version="1.0.0",
    description="A measure of the impact to business functionality or ability to provide services.",
    values=(
        IMPACT_NONE,
        LOW,
        MEDIUM,
        HIGH,
    ),
)

NO_IMPACT = DecisionPointValue(
    key="N",
    name="No Impact",
    description="Event has no impact.",
)

NO_IMPACT_TO_SERVICES = DecisionPointValue(
    key="S",
    name="No Impact to Services",
    description="Event has no impact to any business or Industrial Control Systems (ICS) services or delivery to entity customers.",
)

MINIMAL_IMPACT_TO_NON_CRITICAL_SERVICES = DecisionPointValue(
    key="M",
    name="Minimal Impact to Non-Critical Services",
    description="Some small level of impact to non-critical systems and services.",
)

MINIMAL_IMPACT_TO_CRITICAL_SERVICES = DecisionPointValue(
    key="C",
    name="Minimal Impact to Critical Services",
    description="Minimal impact but to a critical system or service, such as email or active directory.",
)

SIGNIFICANT_IMPACT_TO_NON_CRITICAL_SERVICES = DecisionPointValue(
    key="I",
    name="Significant Impact to Non-Critical Services",
    description="A non-critical service or system has a significant impact.",
)

DENIAL_OF_NON_CRITICAL_SERVICES = DecisionPointValue(
    key="D",
    name="Denial of Non-Critical Services",
    description="A non-critical system is denied or destroyed.",
)

SIGNIFICANT_IMPACT_TO_CRITICAL_SERVICES = DecisionPointValue(
    key="T",
    name="Significant Impact to Critical Services",
    description="A critical system has a significant impact, such as local administrative account compromise.",
)

DENIAL_OF_CRITICAL_SERVICES_LOSS_OF_CONTROL = DecisionPointValue(
    key="L",
    name="Denial of Critical Services/Loss of Control",
    description="A critical system has been rendered unavailable.",
)

# based on https://www.cisa.gov/sites/default/files/publications/Federal_Incident_Notification_Guidelines.pdf
FUNCTIONAL_IMPACT_2 = NcissDecisionPoint(
    key="FI",
    name="Functional Impact",
    version="2.0.0",
    description="A measure of the impact to business functionality or ability to provide services.",
    values=(
        NO_IMPACT,
        NO_IMPACT_TO_SERVICES,
        MINIMAL_IMPACT_TO_NON_CRITICAL_SERVICES,
        MINIMAL_IMPACT_TO_CRITICAL_SERVICES,
        SIGNIFICANT_IMPACT_TO_NON_CRITICAL_SERVICES,
        DENIAL_OF_NON_CRITICAL_SERVICES,
        SIGNIFICANT_IMPACT_TO_CRITICAL_SERVICES,
        DENIAL_OF_CRITICAL_SERVICES_LOSS_OF_CONTROL,
    ),
)

VERSIONS = (
    FUNCTIONAL_IMPACT_1,
    FUNCTIONAL_IMPACT_2,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
