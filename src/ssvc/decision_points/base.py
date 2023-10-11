#!/usr/bin/env python
"""
file: decisionpoints
author: adh
created_at: 9/20/23 10:07 AM
"""

from dataclasses import dataclass
from typing import Tuple

from dataclasses_json import dataclass_json

from ssvc._mixins import _Base, _Keyed, _Namespaced, _Versioned


## notes
# based on https://gist.githubusercontent.com/sei-vsarvepalli/de2cd7dae33e1e1dc906d50846becb45/raw/2a85d08a4028f6dd3cc162d4ace3509e0458426f/Exploitation.json


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPointValue(_Base, _Keyed):
    """
    Models a single value option for a decision point.
    """
    def schemaprops(root=False):
        props = {"description": "Decision Point Values are valid results from a Decision Point",
                 "uniqueItems": True
                 }
        return props
    pass


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPoint(_Base, _Keyed, _Versioned, _Namespaced):
    """
    Models a single decision point as a list of values.
    """

    values: Tuple[SsvcDecisionPointValue]

    def schemaprops(root=True):
        props = {"$schema": "https://json-schema.org/draft/2020-12/schema",
                 "title":"Decision Point schema definition",
                 "$id": "https://certcc.github.io/SSVC/data/schema/dp.json",
                 "description": "Decision points are the basic building blocks of SSVC decision functions. Individual decision points describe a single aspect of the input to a decision function.",
                 "type": "object",
                 "additionalProperties": False
                 }
        if not root:
            for d in ['$schema','$id','title','type']:
                del props[d]
        return props

    def to_table(self):
        rows = []
        rows.append(f"{self.description}")
        rows.append("")

        headings = ["Value", "Key", "Description"]

        def make_row(items):
            return "| " + " | ".join(items) + " |"

        rows.append(make_row(headings))
        rows.append(make_row(["---" for _ in headings]))

        for value in self.values:
            rows.append(make_row([value.name, value.key, value.description]))

        return "\n".join(rows)


def main():
    opt_none = SsvcDecisionPointValue(
        name="None", key="N", description="No exploit available"
    )
    opt_poc = SsvcDecisionPointValue(
        name="PoC", key="P", description="Proof of concept exploit available"
    )
    opt_active = SsvcDecisionPointValue(
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
