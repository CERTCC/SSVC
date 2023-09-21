#!/usr/bin/env python
"""
file: decisionpoints
author: adh
created_at: 9/20/23 10:07 AM
"""

from dataclasses import dataclass
from typing import Tuple

from dataclasses_json import dataclass_json

from ssvc._mixins import _Base, _Namespaced, _Versioned


## notes
# based on https://gist.githubusercontent.com/sei-vsarvepalli/de2cd7dae33e1e1dc906d50846becb45/raw/2a85d08a4028f6dd3cc162d4ace3509e0458426f/Exploitation.json


@dataclass_json
@dataclass(kw_only=True)
class SsvcValue(_Base):
    """
    Models a single value option for a decision point.
    """

    pass


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPoint(_Base, _Versioned, _Namespaced):
    """
    Models a single decision point as a list of values.
    """

    values: Tuple[SsvcValue]


def main():
    opt_none = SsvcValue(name="None", key="N", description="No exploit available")
    opt_poc = SsvcValue(
        name="PoC", key="P", description="Proof of concept exploit available"
    )
    opt_active = SsvcValue(
        name="Active", key="A", description="Active exploitation observed"
    )
    opts = [opt_none, opt_poc, opt_active]

    dp = SsvcDecisionPoint(
        values=opts,
        name="Exploitation",
        description="Is there an exploit available?",
        key="E",
        version="1.0.0",
    )

    print(dp.to_json(indent=2))


if __name__ == "__main__":
    main()
