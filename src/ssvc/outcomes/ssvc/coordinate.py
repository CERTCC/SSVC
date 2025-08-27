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
from ssvc.decision_points.base import DecisionPointValue as DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

_DECLINE = DecisionPointValue(name="Decline", key="D", definition="Decline")

_TRACK = DecisionPointValue(name="Track", key="T", definition="Track")

_COORDINATE = DecisionPointValue(
    name="Coordinate", key="C", definition="Coordinate"
)

_DECLINE_2 = DecisionPointValue(
    name="Decline", key="D", definition="Do not act on the report."
)
_TRACK_2 = DecisionPointValue(
    name="Track",
    key="T",
    definition="Receive information about the vulnerability and monitor for status changes but do not take any overt actions.",
)

_COORDINATE_2 = DecisionPointValue(
    name="Coordinate",
    key="C",
    definition="Take action on the report.",
)

COORDINATE = SsvcDecisionPoint(
    name="Decline, Track, Coordinate",
    key="COORDINATE",
    definition="The coordinate outcome group.",
    version="1.0.0",
    values=(
        _DECLINE,
        _TRACK,
        _COORDINATE,
    ),
)
"""
The coordinate outcome group.
"""


COORDINATE_1_0_1 = SsvcDecisionPoint(
    name="Decline, Track, Coordinate",
    key="COORDINATE",
    definition="The coordinate outcome group.",
    version="1.0.1",
    values=(
        _DECLINE_2,
        _TRACK_2,
        _COORDINATE_2,
    ),
)


VERSIONS = (COORDINATE, COORDINATE_1_0_1)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
