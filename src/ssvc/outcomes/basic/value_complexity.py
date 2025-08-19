#!/usr/bin/env python

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
Provides the Value/Complexity outcome group for the `basic` namespace.
"""

from ssvc.decision_points.base import (
    DecisionPoint,
    DecisionPointValue as DecisionPointValue,
)
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.namespaces import NameSpace

_DROP = DecisionPointValue(name="Drop", key="D", description="Drop")

_RECONSIDER = DecisionPointValue(
    name="Reconsider Later", key="R", description="Reconsider Later"
)

_EASY_WIN = DecisionPointValue(
    name="Easy Win", key="E", description="Easy Win"
)

_DO_FIRST = DecisionPointValue(
    name="Do First", key="F", description="Do First"
)

VALUE_COMPLEXITY = DecisionPoint(
    name="Value, Complexity",
    key="VALUE_COMPLEXITY",
    description="The Value/Complexity outcome group.",
    version="1.0.0",
    namespace=NameSpace.BASIC,
    values=(
        _DROP,
        _RECONSIDER,
        _EASY_WIN,
        _DO_FIRST,
    ),
)
"""
The Value/Complexity outcome group.
"""

VERSIONS = (VALUE_COMPLEXITY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
