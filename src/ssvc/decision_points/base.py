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


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPointValue(_Base, _Keyed):
    """
    Models a single value option for a decision point.
    """

    pass


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPoint(_Base, _Keyed, _Versioned, _Namespaced):
    """
    Models a single decision point as a list of values.
    """

    values: Tuple[SsvcDecisionPointValue]

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
    dp = SsvcDecisionPoint(
        _comment="This is an optional comment that will be included in the object.",
        name="Exploitation",
        description="Is there an exploit available?",
        key="E",
        version="1.0.0",
        values=(
            SsvcDecisionPointValue(
                name="None", key="N", description="No exploit available"
            ),
            SsvcDecisionPointValue(
                name="PoC",
                key="P",
                description="Proof of concept exploit available",
            ),
            SsvcDecisionPointValue(
                name="Active", key="A", description="Active exploitation observed"
            ),
        ),
    )
    print(dp.to_json(indent=2))


if __name__ == "__main__":
    main()
