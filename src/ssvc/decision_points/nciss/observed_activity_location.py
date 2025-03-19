#!/usr/bin/env python
"""
Provides a decision point for the location of observed activity.
Based on [National Cybersecurity Incident Scoring System (NCISS)](https://www.cisa.gov/sites/default/files/2023-01/cisa_national_cyber_incident_scoring_system_s508c.pdf)
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


LEVEL_0 = SsvcDecisionPointValue(
    name="Unsuccessful",
    key="0",
    description="Existing network defenses repelled all observed activity.",
)


LEVEL_1 = SsvcDecisionPointValue(
    name="Business Demilitarized Zone",
    key="1",
    description="Activity was observed in the business network’s demilitarized zone (DMZ). These systems are generally untrusted and are designed to be exposed to the Internet.",
)


LEVEL_2 = SsvcDecisionPointValue(
    name="Business Network",
    key="2",
    description="Activity was observed in the business or corporate network of the victim. These systems would be corporate user workstations, application servers, and other non-core management systems.",
)


LEVEL_3 = SsvcDecisionPointValue(
    name="Business Network Management",
    key="3",
    description="Activity was observed in business network management systems such as administrative user workstations, active directory servers, or other trust stores.",
)

LEVEL_4 = SsvcDecisionPointValue(
    name="Critical System DMZ",
    key="4",
    description="Activity was observed in the DMZ that exists between the business network and a critical system network. These systems may be internally facing services such as SharePoint sites, financial systems, or relay “jump” boxes into more critical systems.",
)

LEVEL_5 = SsvcDecisionPointValue(
    name="Critical System Management",
    key="5",
    description="Activity was observed in high-level critical systems management such as human-machine interfaces (HMIs) in industrial control systems.",
)

LEVEL_6 = SsvcDecisionPointValue(
    name="Critical Systems",
    key="6",
    description="Activity was observed in the critical systems that operate critical processes, such as programmable logic controllers in industrial control system environments.",
)

LEVEL_7 = SsvcDecisionPointValue(
    name="Safety Systems",
    key="7",
    description="Activity was observed in critical safety systems that ensure the safe operation of an environment. One example of a critical safety system is a fire suppression system.",
)

UNKNOWN = SsvcDecisionPointValue(
    name="Unknown",
    key="U",
    description="Activity was observed, but the network segment could not be identified.",
)

OBSERVED_ACTIVITY_LOCATION = NcissDecisionPoint(
    name="Observed Activity Location",
    description="The location of observed activity describes where the observed activity was detected in the network. ",
    key="OAL",
    version="1.0.0",
    values=(
        LEVEL_0,
        LEVEL_1,
        LEVEL_2,
        LEVEL_3,
        LEVEL_4,
        LEVEL_5,
        LEVEL_6,
        LEVEL_7,
        UNKNOWN,
    ),
)

VERSIONS = (OBSERVED_ACTIVITY_LOCATION,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
