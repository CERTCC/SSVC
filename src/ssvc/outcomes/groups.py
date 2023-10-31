#!/usr/bin/env python
"""
Provides a set of outcome groups for use in SSVC.
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

from ssvc.outcomes.base import OutcomeGroup, OutcomeValue

# Note: Outcome Groups must be defined in ascending order.


DSOI = OutcomeGroup(
    name="Defer, Scheduled, Out-of-Cycle, Immediate",
    description="The original SSVC outcome group.",
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
    outcomes=(
        OutcomeValue(name="Do Not Publish", key="N", description="Do Not Publish"),
        OutcomeValue(name="Publish", key="P", description="Publish"),
    ),
)
"""
The publish outcome group.
"""

COORDINATE = OutcomeGroup(
    name="Decline, Track, Coordinate",
    description="The coordinate outcome group.",
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

YES_NO = OutcomeGroup(
    name="Yes, No",
    description="The Yes/No outcome group.",
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
    outcomes=(
        # drop, reconsider later, easy win, do first
        OutcomeValue(name="Drop", key="D", description="Drop"),
        OutcomeValue(name="Reconsider Later", key="R", description="Reconsider Later"),
        OutcomeValue(name="Easy Win", key="E", description="Easy Win"),
        OutcomeValue(name="Do First", key="F", description="Do First"),
    ),
)
"""
The Value/Complexity outcome group.
"""


def main():
    pass


if __name__ == "__main__":
    main()
