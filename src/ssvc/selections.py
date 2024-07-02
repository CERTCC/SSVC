#!/usr/bin/env python
#  Copyright (c) 2024 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University
"""
file: selections
author: adh
created_at: 6/27/24 2:46 PM
"""
from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPointSelection:
    namespace: str
    name: str
    version: str
    values: List[str]


@dataclass_json
@dataclass(kw_only=True)
class SsvcDecisionPointGroupSelection:
    selections: List[SsvcDecisionPointSelection]


def main():
    from marshmallow_jsonschema import JSONSchema

    json_schema = JSONSchema()

    print("#####################################################")
    print("### Schema example for SsvcDecisionPointSelection ###")
    print("#####################################################")
    print(json_schema.dumps(SsvcDecisionPointSelection.schema(), indent=2))

    with open("../../data/schema/Decision_Point_Selection.schema.json", "w") as f:
        f.write(json_schema.dumps(SsvcDecisionPointSelection.schema(), indent=2))

    print()
    print()

    print("##########################################################")
    print("### Schema example for SsvcDecisionPointGroupSelection ###")
    print("##########################################################")
    print(json_schema.dumps(SsvcDecisionPointGroupSelection.schema(), indent=2))

    with open("../../data/schema/Decision_Point_Group_Selection.schema.json", "w") as f:
        f.write(json_schema.dumps(SsvcDecisionPointGroupSelection.schema(), indent=2))

    print()
    print()


if __name__ == "__main__":
    main()
