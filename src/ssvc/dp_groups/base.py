#!/usr/bin/env python
"""
file: base
author: adh
created_at: 9/20/23 4:47 PM
"""
from dataclasses import dataclass
from typing import Tuple

from dataclasses_json import dataclass_json

from ssvc._mixins import _Base, _Versioned
from ssvc.decision_points.base import SsvcDecisionPoint


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPointGroup(_Base, _Versioned):
    """
    Models a group of decision points.
    """

    decision_points: Tuple[SsvcDecisionPoint]

    def __iter__(self):
        return iter(self.decision_points)


def get_all_decision_points_from(
    glist: list[SsvcDecisionPointGroup],
) -> Tuple[SsvcDecisionPoint]:
    """
    Given a list of SsvcDecisionPointGroup objects, return a list of all
    the unique SsvcDecisionPoint objects contained in those groups.

    Args:
        groups (list): A list of SsvcDecisionPointGroup objects.

    Returns:
        list: A list of SsvcDecisionPoint objects.
    """
    dps = []
    seen = set()

    for group in glist:
        for dp in group.decision_points:
            if dp in dps:
                # skip duplicates
                continue
            key = (dp.name, dp.version)
            if key in seen:
                # skip duplicates
                continue
            # keep non-duplicates
            dps.append(dp)
            seen.add(key)

    return tuple(dps)


def main():
    pass


if __name__ == "__main__":
    main()
