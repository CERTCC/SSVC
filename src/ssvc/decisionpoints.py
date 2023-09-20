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

@dataclass_json
@dataclass(kw_only=True)
class SsvcBase:
    name: str
    description: str
    key: str
    namespace: str="ssvc"

@dataclass_json
@dataclass(kw_only=True)
class SsvcVersionedBase(SsvcBase):
    version: str

@dataclass_json
@dataclass(kw_only=True)
class SsvcOption(SsvcBase):
    pass

@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPoint(SsvcVersionedBase):
    values: List[SsvcOption]

@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPointGroup(SsvcVersionedBase):
    decision_points: List[SsvcDecisionPoint]


def main():
    opt_none = SsvcOption(name="None", key="N", description="No exploit available")
    opt_poc = SsvcOption(name="PoC", key="P", description="Proof of concept exploit available")
    opt_active= SsvcOption(name="Active", key="A", description="Active exploitation observed")
    opts = [opt_none, opt_poc, opt_active]

    dp = SsvcDecisionPoint(values=opts, name="Exploitation", description="Is there an exploit available?", key="E", version="1.0.0")

    dpg = SsvcDecisionPointGroup(name="DPgroup", description="A group of decision points", key="DPG1", version="1.0.0", decision_points=[dp])
    print(dpg.to_json(indent=2))

if __name__ == '__main__':
    main()
