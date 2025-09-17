#!/usr/bin/env python
"""
Models the CVSS Privileges Required metric as an SSVC decision point.
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

_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="The attacker is authorized with (i.e. requires) privileges that provide significant (e.g. "
    "administrative) control over the vulnerable component that could affect component-wide settings and "
    "files.",
)

_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="The attacker is authorized with (i.e. requires) privileges that provide basic user capabilities that "
    "could normally affect only settings and files owned by a user. Alternatively, an attacker with Low "
    "privileges may have the ability to cause an impact only to non-sensitive resources.",
)

_PR_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="The attacker is unauthorized prior to attack, and therefore does not require any access to settings "
    "or files to carry out an attack.",
)


# NOTE: values must be listed from "least bad" to "most bad" for sorting to work properly
# therefore High < Low < None
PRIVILEGES_REQUIRED_1 = CvssDecisionPoint(
    name="Privileges Required",
    definition="This metric describes the level of privileges an attacker must possess before successfully "
    "exploiting the vulnerability.",
    key="PR",
    version="1.0.0",
    values=(
        _HIGH,
        _LOW,
        _PR_NONE,
    ),
)
"""
Defines None, Low, and High values for CVSS Privileges Required.
"""


_PR_NONE_2 = DecisionPointValue(
    name="None",
    key="N",
    definition="The attacker is unauthorized prior to attack, and therefore does not require any access to settings "
    "or files to carry out an attack.",
)

_LOW_2 = DecisionPointValue(
    name="Low",
    key="L",
    definition="The attacker is authorized with (i.e., requires) privileges that provide basic capabilities that "
    "are typically limited to settings and resources owned by a single low-privileged user. Alternatively, "
    "an attacker with Low privileges has the ability to access only non-sensitive resources.",
)

_HIGH_2 = DecisionPointValue(
    name="High",
    key="H",
    definition="The attacker is authorized with (i.e., requires) privileges that provide significant (e.g., "
    "administrative) control over the vulnerable system allowing full access to the vulnerable system’s "
    "settings and files.",
)

PRIVILEGES_REQUIRED_1_0_1 = CvssDecisionPoint(
    name="Privileges Required",
    definition="This metric describes the level of privileges an attacker must possess prior to successfully "
    "exploiting the vulnerability. The method by which the attacker obtains privileged credentials "
    "prior to the attack (e.g., free trial accounts), is outside the scope of this metric. Generally, "
    "self-service provisioned accounts do not constitute a privilege requirement if the attacker can "
    "grant themselves privileges as part of the attack.",
    key="PR",
    version="1.0.1",
    values=(
        _HIGH_2,
        _LOW_2,
        _PR_NONE_2,
    ),
)

VERSIONS = (PRIVILEGES_REQUIRED_1, PRIVILEGES_REQUIRED_1_0_1)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
