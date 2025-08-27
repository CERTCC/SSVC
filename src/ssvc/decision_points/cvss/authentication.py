#!/usr/bin/env python
"""
Models the CVSS Authentication metric as an SSVC decision point.
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

_AUTH_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="Authentication is not required to exploit the vulnerability.",
)

_SINGLE = DecisionPointValue(
    name="Single",
    key="S",
    definition="The vulnerability requires an attacker to be logged into the system (such as at a command line or via a desktop session or web interface).",
)

_MULTIPLE = DecisionPointValue(
    name="Multiple",
    key="M",
    definition="Exploiting the vulnerability requires that the attacker authenticate two or more times, even if the same credentials are used each time.",
)

_REQUIRED = DecisionPointValue(
    name="Required",
    key="R",
    definition="Authentication is required to access and exploit the vulnerability.",
)

_NOT_REQUIRED = DecisionPointValue(
    name="Not Required",
    key="N",
    definition="Authentication is not required to access or exploit the vulnerability.",
)

AUTHENTICATION_1 = CvssDecisionPoint(
    name="Authentication",
    definition="This metric measures whether or not an attacker needs to be authenticated to the target system in order to exploit the vulnerability.",
    key="Au",
    version="1.0.0",
    values=(
        _NOT_REQUIRED,
        _REQUIRED,
    ),
)
"""
Includes NOT_REQUIRED and REQUIRED values for CVSS Authentication.
"""

AUTHENTICATION_2 = CvssDecisionPoint(
    name="Authentication",
    definition="This metric measures the number of times an attacker must authenticate to a target in order to exploit a vulnerability. This metric does not gauge the strength or complexity of the authentication process, only that an attacker is required to provide credentials before an exploit may occur.  The possible values for this metric are listed in Table 3. The fewer authentication instances that are required, the higher the vulnerability score.",
    key="Au",
    version="2.0.0",
    values=(
        _MULTIPLE,
        _SINGLE,
        _AUTH_NONE,
    ),
)
"""
Includes MULTIPLE, SINGLE, and AUTH_NONE values for CVSS Authentication.
"""

VERSIONS = (AUTHENTICATION_1, AUTHENTICATION_2)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
