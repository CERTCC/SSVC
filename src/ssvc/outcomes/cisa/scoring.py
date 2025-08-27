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
"""
Provides the CISA Levels outcome group for use in SSVC.
"""

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cisa.base import CisaDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_TRACK = DecisionPointValue(
    name="Track",
    key="T",
    definition="The vulnerability does not require action at this time. "
    "The organization would continue to track the vulnerability and reassess it if new information becomes available. "
    "CISA recommends remediating Track vulnerabilities within standard update timelines.",
)

_TRACK_STAR = DecisionPointValue(
    name="Track*",
    key="T*",
    definition="The vulnerability contains specific characteristics that may require closer monitoring for changes. "
    "CISA recommends remediating Track* vulnerabilities within standard update timelines.",
)

_ATTEND = DecisionPointValue(
    name="Attend",
    key="AT",
    definition="The vulnerability requires attention from the organization's internal, supervisory-level individuals. "
    "Necessary actions may include requesting assistance or information about the vulnerability and may involve publishing a notification, either internally and/or externally, about the vulnerability. "
    "CISA recommends remediating Attend vulnerabilities sooner than standard update timelines.",
)

_ACT = DecisionPointValue(
    name="Act",
    key="AC",
    definition="The vulnerability requires attention from the organization's internal, supervisory-level and leadership-level individuals. "
    "Necessary actions include requesting assistance or information about the vulnerability, as well as publishing a notification either internally and/or externally. "
    "Typically, internal groups would meet to determine the overall response and then execute agreed upon actions. "
    "CISA recommends remediating Act vulnerabilities as soon as possible.",
)

CISA = CisaDecisionPoint(
    name="CISA Levels",
    key="CISA",
    definition="The CISA outcome group. "
    "CISA uses its own SSVC decision tree model to prioritize relevant vulnerabilities into four possible decisions: Track, Track*, Attend, and Act.",
    version="1.1.0",
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
