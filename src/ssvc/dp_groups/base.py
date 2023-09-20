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


def main():
    pass


if __name__ == "__main__":
    main()
