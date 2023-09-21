#!/usr/bin/env python
"""
file: base
author: adh
created_at: 9/20/23 4:47 PM
"""
from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from ssvc._mixins import _Base, _Versioned
from ssvc.decision_points.base import SsvcDecisionPoint


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPointGroup(_Base, _Versioned):
    """
    Models a group of decision points.
    """

    decision_points: List[SsvcDecisionPoint]


def get_all_decision_points_from(
    glist: list[SsvcDecisionPointGroup],
) -> list[SsvcDecisionPoint]:
    """
    Given a list of SsvcDecisionPointGroup objects, return a list of all
    the unique SsvcDecisionPoint objects contained in those groups.

    Args:
        groups (list): A list of SsvcDecisionPointGroup objects.

    Returns:
        list: A list of SsvcDecisionPoint objects.
    """
    dps = []
    for group in glist:
        for dp in group.decision_points:
            if dp in dps:
                # skip duplicates
                continue
            # keep non-duplicates
            dps.append(dp)
    return dps


def group_to_jsonfiles(group: SsvcDecisionPointGroup, path: str = ".") -> None:
    for dp in group.decision_points:
        basename = dp.name.strip().lower().replace(" ", "_")
        fname = f"{path}/{basename}.json"
        with open(fname, "w") as f:
            print(f"Writing {fname}")
            f.write(dp.to_json(indent=2))


def main():
    pass


if __name__ == "__main__":
    main()
