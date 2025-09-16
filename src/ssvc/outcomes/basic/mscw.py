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
Provides the MoSCoW (Must, Should, Could, Won't) outcome group for the `basic` namespace
"""

from ssvc.decision_points.base import (
    DecisionPoint,
    DecisionPointValue as DecisionPointValue,
)
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.namespaces import NameSpace

_WONT = DecisionPointValue(name="Won't", key="W", definition="Won't")

_COULD = DecisionPointValue(name="Could", key="C", definition="Could")

_SHOULD = DecisionPointValue(name="Should", key="S", definition="Should")

_MUST = DecisionPointValue(name="Must", key="M", definition="Must")

MSCW = DecisionPoint(
    name="MoSCoW",
    key="MSCW",
    definition="The MoSCoW (Must, Should, Could, Won't) outcome group.",
    version="1.0.0",
    namespace=NameSpace.BASIC,
    values=(
        _WONT,
        _COULD,
        _SHOULD,
        _MUST,
    ),
)
"""
The MoSCoW outcome group.
"""

VERSIONS = (MSCW,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
