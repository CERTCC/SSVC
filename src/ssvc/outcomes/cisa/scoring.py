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
"""
Provides the CISA Levels outcome group for use in SSVC.
"""

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cisa.base import CisaDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_TRACK = DecisionPointValue(
    name="Track",
    key="T",
    description="The vulnerability does not require action at this time. "
    "The organization would continue to track the vulnerability and reassess it if new information becomes available. "
    "CISA recommends remediating Track vulnerabilities within standard update timelines.",
)

_TRACK_STAR = DecisionPointValue(
    name="Track*",
    key="T*",
    description="The vulnerability contains specific characteristics that may require closer monitoring for changes. "
    "CISA recommends remediating Track* vulnerabilities within standard update timelines.",
)

_ATTEND = DecisionPointValue(
    name="Attend",
    key="A",
    description="The vulnerability requires attention from the organization's internal, supervisory-level individuals. "
    "Necessary actions may include requesting assistance or information about the vulnerability and may involve publishing a notification, either internally and/or externally, about the vulnerability. "
    "CISA recommends remediating Attend vulnerabilities sooner than standard update timelines.",
)

_ACT = DecisionPointValue(
    name="Act",
    key="A",
    description="The vulnerability requires attention from the organization's internal, supervisory-level and leadership-level individuals. "
    "Necessary actions include requesting assistance or information about the vulnerability, as well as publishing a notification either internally and/or externally. "
    "Typically, internal groups would meet to determine the overall response and then execute agreed upon actions. "
    "CISA recommends remediating Act vulnerabilities as soon as possible.",
)

CISA = CisaDecisionPoint(
    name="CISA Levels",
    key="CISA",
    description="The CISA outcome group. "
    "CISA uses its own SSVC decision tree model to prioritize relevant vulnerabilities into four possible decisions: Track, Track*, Attend, and Act.",
    version="1.0.0",
    values=(
        _TRACK,
        _TRACK_STAR,
        _ATTEND,
        _ACT,
    ),
)
"""
The CISA outcome group. Based on CISA's customizations of the SSVC model.
See https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc
"""


VERSIONS = (CISA,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
