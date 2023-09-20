#!/usr/bin/env python
'''
file: decisionpoints
author: adh
created_at: 9/20/23 10:07 AM
'''

from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

## notes
# based on https://gist.githubusercontent.com/sei-vsarvepalli/de2cd7dae33e1e1dc906d50846becb45/raw/2a85d08a4028f6dd3cc162d4ace3509e0458426f/Exploitation.json
# TODO: "Options" should be "Values"
# TODO: "label" should be "name"
# TODO: "key" should be namespaced (add a namespace field?)

@dataclass_json
@dataclass
class SsvcOption:
    label: str
    key: str
    description: str = None

@dataclass_json
@dataclass
class SsvcDecisionPoint:
    options: List[SsvcOption]
    label: str
    description: str
    key: str
    version: str

@dataclass_json
@dataclass
class SsvcDecisionPointGroup:
    label: str
    description: str
    key: str
    version: str
    decision_points: List[SsvcDecisionPoint]


def main():
    opt_none = SsvcOption(label="None", key="N", description="No exploit available")
    opt_poc = SsvcOption(label="PoC", key="P", description="Proof of concept exploit available")
    opt_active= SsvcOption(label="Active", key="A", description="Active exploitation observed")
    opts = [opt_none, opt_poc, opt_active]

    dp = SsvcDecisionPoint(options=opts, label="Exploitation", description="Is there an exploit available?", key="E", version="1.0.0")

    dpg = SsvcDecisionPointGroup(label="DPgroup", description="A group of decision points", key="DPG1", version="1.0.0", decision_points=[dp])
    print(dpg.to_json(indent=2))

if __name__ == '__main__':
    main()
