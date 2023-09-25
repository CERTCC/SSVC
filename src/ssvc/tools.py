#!/usr/bin/env python
"""
file: tools
author: adh
created_at: 9/21/23 3:20 PM
"""
from ssvc.dp_groups.base import SsvcDecisionPointGroup


def group_to_jsonfiles(group: SsvcDecisionPointGroup, path: str = ".") -> None:
    for dp in group.decision_points:
        basename = dp.name.strip().lower().replace(" ", "_")

        json_fname = f"{path}/{basename}.json"
        with open(json_fname, "w") as f:
            print(f"Writing {json_fname}")
            f.write(dp.to_json(indent=2))
            f.write("\n")

        table_fname = f"{path}/{basename}.md"
        with open(table_fname, "w") as f:
            print(f"Writing {table_fname}")
            f.write(dp.to_table())
            f.write("\n")


def replace_in_list(lst, old, new):
    idx = lst.index(old)
    lst[idx] = new
    return lst
