#!/usr/bin/env python
"""
Provides the NCISS Functional Impact decision point and values.
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

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.nciss.base import NcissDecisionPoint

IMPACT_NONE = SsvcDecisionPointValue(
    key="N",
    name="No Impact",
    description="Organization has experienced no loss in ability to provide all services to all users.",
)

LOW = SsvcDecisionPointValue(
    key="L",
    name="Low",
    description="Organization has experienced a loss of efficiency, but can still provide all critical services to all users with minimal effect on performance.",
)

MEDIUM = SsvcDecisionPointValue(
    key="M",
    name="Medium",
    description="Organization has lost the ability to provide a critical service to a subset of system users.",
)

HIGH = SsvcDecisionPointValue(
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

NO_IMPACT = SsvcDecisionPointValue(
    key="N",
    name="No Impact",
    description="Event has no impact.",
)

NO_IMPACT_TO_SERVICES = SsvcDecisionPointValue(
    key="S",
    name="No Impact to Services",
    description="Event has no impact to any business or Industrial Control Systems (ICS) services or delivery to entity customers.",
)

MINIMAL_IMPACT_TO_NON_CRITICAL_SERVICES = SsvcDecisionPointValue(
    key="M",
    name="Minimal Impact to Non-Critical Services",
    description="Some small level of impact to non-critical systems and services.",
)

MINIMAL_IMPACT_TO_CRITICAL_SERVICES = SsvcDecisionPointValue(
    key="C",
    name="Minimal Impact to Critical Services",
    description="Minimal impact but to a critical system or service, such as email or active directory.",
)

SIGNIFICANT_IMPACT_TO_NON_CRITICAL_SERVICES = SsvcDecisionPointValue(
    key="I",
    name="Significant Impact to Non-Critical Services",
    description="A non-critical service or system has a significant impact.",
)

DENIAL_OF_NON_CRITICAL_SERVICES = SsvcDecisionPointValue(
    key="D",
    name="Denial of Non-Critical Services",
    description="A non-critical system is denied or destroyed.",
)

SIGNIFICANT_IMPACT_TO_CRITICAL_SERVICES = SsvcDecisionPointValue(
    key="T",
    name="Significant Impact to Critical Services",
    description="A critical system has a significant impact, such as local administrative account compromise.",
)

DENIAL_OF_CRITICAL_SERVICES_LOSS_OF_CONTROL = SsvcDecisionPointValue(
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
