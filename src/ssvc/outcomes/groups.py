#!/usr/bin/env python
"""
Provides a set of outcome groups for use in SSVC.
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

from ssvc.outcomes.base import OutcomeGroup, OutcomeValue

# Note: Outcome Groups must be defined in ascending order.


DSOI = OutcomeGroup(
    name="Defer, Scheduled, Out-of-Cycle, Immediate",
    description="The original SSVC outcome group.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(name="Defer", key="D", description="Defer"),
        OutcomeValue(name="Scheduled", key="S", description="Scheduled"),
        OutcomeValue(name="Out-of-Cycle", key="O", description="Out-of-Cycle"),
        OutcomeValue(name="Immediate", key="I", description="Immediate"),
    ),
)
"""
The original SSVC outcome group.
"""

PUBLISH = OutcomeGroup(
    name="Publish, Do Not Publish",
    description="The publish outcome group.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(
            name="Do Not Publish", key="N", description="Do Not Publish"
        ),
        OutcomeValue(name="Publish", key="P", description="Publish"),
    ),
)
"""
The publish outcome group.
"""

COORDINATE = OutcomeGroup(
    name="Decline, Track, Coordinate",
    description="The coordinate outcome group.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(name="Decline", key="D", description="Decline"),
        OutcomeValue(name="Track", key="T", description="Track"),
        OutcomeValue(name="Coordinate", key="C", description="Coordinate"),
    ),
)
"""
The coordinate outcome group.
"""

MOSCOW = OutcomeGroup(
    name="Must, Should, Could, Won't",
    description="The Moscow outcome group.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(name="Won't", key="W", description="Won't"),
        OutcomeValue(name="Could", key="C", description="Could"),
        OutcomeValue(name="Should", key="S", description="Should"),
        OutcomeValue(name="Must", key="M", description="Must"),
    ),
)
"""
The MoSCoW outcome group.
"""

EISENHOWER = OutcomeGroup(
    name="Do, Schedule, Delegate, Delete",
    description="The Eisenhower outcome group.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(name="Delete", key="D", description="Delete"),
        OutcomeValue(name="Delegate", key="G", description="Delegate"),
        OutcomeValue(name="Schedule", key="S", description="Schedule"),
        OutcomeValue(name="Do", key="O", description="Do"),
    ),
)
"""
The Eisenhower outcome group.
"""

CVSS = OutcomeGroup(
    name="CVSS Levels",
    description="The CVSS outcome group.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(name="Low", key="L", description="Low"),
        OutcomeValue(name="Medium", key="M", description="Medium"),
        OutcomeValue(name="High", key="H", description="High"),
        OutcomeValue(name="Critical", key="C", description="Critical"),
    ),
)
"""
The CVSS outcome group.
"""

CISA = OutcomeGroup(
    name="CISA Levels",
    description="The CISA outcome group. "
    "CISA uses its own SSVC decision tree model to prioritize relevant vulnerabilities into four possible decisions: Track, Track*, Attend, and Act.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(
            name="Track",
            key="T",
            description="The vulnerability does not require action at this time. "
            "The organization would continue to track the vulnerability and reassess it if new information becomes available. "
            "CISA recommends remediating Track vulnerabilities within standard update timelines.",
        ),
        OutcomeValue(
            name="Track*",
            key="T*",
            description="The vulnerability contains specific characteristics that may require closer monitoring for changes. "
            "CISA recommends remediating Track* vulnerabilities within standard update timelines.",
        ),
        OutcomeValue(
            name="Attend",
            key="A",
            description="The vulnerability requires attention from the organization's internal, supervisory-level individuals. "
            "Necessary actions may include requesting assistance or information about the vulnerability and may involve publishing a notification, either internally and/or externally, about the vulnerability. "
            "CISA recommends remediating Attend vulnerabilities sooner than standard update timelines.",
        ),
        OutcomeValue(
            name="Act",
            key="A",
            description="The vulnerability requires attention from the organization's internal, supervisory-level and leadership-level individuals. "
            "Necessary actions include requesting assistance or information about the vulnerability, as well as publishing a notification either internally and/or externally. "
            "Typically, internal groups would meet to determine the overall response and then execute agreed upon actions. "
            "CISA recommends remediating Act vulnerabilities as soon as possible.",
        ),
    ),
)
"""
The CISA outcome group. Based on CISA's customizations of the SSVC model.
See https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc
"""

YES_NO = OutcomeGroup(
    name="Yes, No",
    description="The Yes/No outcome group.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(name="No", key="N", description="No"),
        OutcomeValue(name="Yes", key="Y", description="Yes"),
    ),
)
"""
The Yes/No outcome group.
"""

VALUE_COMPLEXITY = OutcomeGroup(
    name="Value, Complexity",
    description="The Value/Complexity outcome group.",
    version="1.0.0",
    outcomes=(
        # drop, reconsider later, easy win, do first
        OutcomeValue(name="Drop", key="D", description="Drop"),
        OutcomeValue(
            name="Reconsider Later", key="R", description="Reconsider Later"
        ),
        OutcomeValue(name="Easy Win", key="E", description="Easy Win"),
        OutcomeValue(name="Do First", key="F", description="Do First"),
    ),
)
"""
The Value/Complexity outcome group.
"""

THE_PARANOIDS = OutcomeGroup(
    name="theParanoids",
    description="PrioritizedRiskRemediation outcome group based on TheParanoids.",
    version="1.0.0",
    outcomes=(
        OutcomeValue(name="Track 5", key="5", description="Track"),
        OutcomeValue(
            name="Track Closely 4", key="4", description="Track Closely"
        ),
        OutcomeValue(name="Attend 3", key="3", description="Attend"),
        OutcomeValue(name="Attend 2", key="2", description="Attend"),
        OutcomeValue(name="Act 1", key="1", description="Act"),
        OutcomeValue(name="Act ASAP 0", key="0", description="Act ASAP"),
    ),
)
"""
Outcome group based on TheParanoids' PrioritizedRiskRemediation.
Their model is a 6-point scale, with 0 being the most urgent and 5 being the least.
See https://github.com/theparanoids/PrioritizedRiskRemediation
"""


def main():
    pass


if __name__ == "__main__":
    main()
