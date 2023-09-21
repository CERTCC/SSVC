#!/usr/bin/env python
"""
file: base
author: adh
created_at: 9/21/23 2:07 PM
"""
from ssvc.decision_points.base import SsvcDecisionPoint


@dataclasses_json
@dataclass(kw_only=True)
class OssfDecisionPoint(SsvcDecisionPoint):
    namespace: str = "ossf"


def main():
    pass


if __name__ == "__main__":
    main()
