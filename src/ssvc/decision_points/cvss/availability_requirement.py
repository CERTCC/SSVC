#!/usr/bin/env python
"""
Models the CVSS Availability Requirement metric as an SSVC decision point.
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
from ssvc.decision_points.cvss._not_defined import (
    NOT_DEFINED_ND,
    NOT_DEFINED_X,
)
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.cvss.helpers import no_x
from ssvc.decision_points.helpers import print_versions_and_diffs


_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="Loss of availability is likely to have a catastrophic adverse effect on the organization or "
    "individuals associated with the organization (e.g., employees, customers).",
)

_MEDIUM = DecisionPointValue(
    name="Medium",
    key="M",
    definition="Loss of availability is likely to have a serious adverse effect on the organization or individuals "
    "associated with the organization (e.g., employees, customers).",
)

_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="Loss of availability is likely to have only a limited adverse effect on the organization or "
    "individuals associated with the organization (e.g., employees, customers).",
)


AVAILABILITY_REQUIREMENT_1 = CvssDecisionPoint(
    name="Availability Requirement",
    definition="This metric measures the impact to the availability of a successfully exploited vulnerability.",
    key="AR",
    version="1.0.0",
    values=(
        _LOW,
        _MEDIUM,
        _HIGH,
        NOT_DEFINED_ND,
    ),
)
"""
Defines Low, Medium, High, and Not Defined values for CVSS Availability Requirement.
"""

AVAILABILITY_REQUIREMENT_1_1 = CvssDecisionPoint(
    name="Availability Requirement",
    definition="This metric measures the impact to the availability of a successfully exploited vulnerability.",
    key="AR",
    version="1.1.0",
    values=(
        _LOW,
        _MEDIUM,
        _HIGH,
        NOT_DEFINED_X,
    ),
)


_HIGH_2 = DecisionPointValue(
    name="High",
    key="H",
    definition="Loss of availability is likely to have a catastrophic adverse effect on the organization or "
    "individuals associated with the organization (e.g., employees, customers).",
)

_MEDIUM_2 = DecisionPointValue(
    name="Medium",
    key="M",
    definition="Loss of availability is likely to have a serious adverse effect on the organization or "
    "individuals associated with the organization (e.g., employees, customers).",
)

_LOW_2 = DecisionPointValue(
    name="Low",
    key="L",
    definition="Loss of availability is likely to have only a limited adverse effect on the organization or "
    "individuals associated with the organization (e.g., employees, customers).",
)

AVAILABILITY_REQUIREMENT_1_1_1 = CvssDecisionPoint(
    name="Availability Requirement",
    definition="This metric enables the consumer to customize the assessment depending on the importance of the "
    "affected IT asset to the analyst’s organization, measured in terms of Availability.",
    key="AR",
    version="1.1.1",
    values=(
        _LOW_2,
        _MEDIUM_2,
        _HIGH_2,
        NOT_DEFINED_X,
    ),
)

AR_NoX = no_x(AVAILABILITY_REQUIREMENT_1_1_1)
"""A version of the Availability Requirement decision point without the Not Defined (X) option."""

VERSIONS = (
    AVAILABILITY_REQUIREMENT_1,
    AVAILABILITY_REQUIREMENT_1_1,
    AVAILABILITY_REQUIREMENT_1_1_1,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
