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

    def schemaprops(root=True):
        props = {"$schema": "https://json-schema.org/draft/2020-12/schema",
                 "title":"Decision Points Group schema definition",
                 "$id": "https://certcc.github.io/SSVC/docs/reference/schema/Decision_Point_Group.schema.json",
                 "type": "object",
                 "additionalProperties": False
                 }
        if not root:
            for d in ['$schema','$id','title','type']:
                del props[d]
        return props
    
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
    for group in glist:
        for dp in group.decision_points:
            if dp in dps:
                # skip duplicates
                continue
            # keep non-duplicates
            dps.append(dp)

    return tuple(dps)


def main():
    pass


if __name__ == "__main__":
    main()
