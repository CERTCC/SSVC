#!/usr/bin/env python
"""
Models the CVSS Privileges Required metric as an SSVC decision point.
"""
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="The attacker is authorized with (i.e. requires) privileges that provide significant (e.g. "
    "administrative) control over the vulnerable component that could affect component-wide settings and "
    "files.",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="The attacker is authorized with (i.e. requires) privileges that provide basic user capabilities that "
    "could normally affect only settings and files owned by a user. Alternatively, an attacker with Low "
    "privileges may have the ability to cause an impact only to non-sensitive resources.",
)

_PR_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="The attacker is unauthorized prior to attack, and therefore does not require any access to settings "
    "or files to carry out an attack.",
)


# NOTE: values must be listed from "least bad" to "most bad" for sorting to work properly
# therefore High < Low < None
PRIVILEGES_REQUIRED_1 = CvssDecisionPoint(
    name="Privileges Required",
    description="This metric describes the level of privileges an attacker must possess before successfully "
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


_PR_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="The attacker is unauthorized prior to attack, and therefore does not require any access to settings "
    "or files to carry out an attack.",
)

_LOW_2 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="The attacker is authorized with (i.e., requires) privileges that provide basic capabilities that "
    "are typically limited to settings and resources owned by a single low-privileged user. Alternatively, "
    "an attacker with Low privileges has the ability to access only non-sensitive resources.",
)

_HIGH_2 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="The attacker is authorized with (i.e., requires) privileges that provide significant (e.g., "
    "administrative) control over the vulnerable system allowing full access to the vulnerable system’s "
    "settings and files.",
)

PRIVILEGES_REQUIRED_1_0_1 = CvssDecisionPoint(
    name="Privileges Required",
    description="This metric describes the level of privileges an attacker must possess prior to successfully "
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

versions = [PRIVILEGES_REQUIRED_1, PRIVILEGES_REQUIRED_1_0_1]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
