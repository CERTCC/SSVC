#!/usr/bin/env python
"""
file: tools
author: adh
created_at: 9/21/23 3:20 PM
"""
from ssvc.decision_points.base import SsvcDecisionPoint
from ssvc.dp_groups.base import SsvcDecisionPointGroup, get_all_decision_points_from


def write_json(fname: str, dp: SsvcDecisionPoint) -> None:
    with open(fname, "w") as f:
        print(f"Writing {fname}")
        f.write(dp.to_json(indent=2))
        f.write("\n")


def write_markdown_table(fname: str, dp: SsvcDecisionPoint) -> None:
    with open(fname, "w") as f:
        print(f"Writing {fname}")
        f.write(dp.to_table())
        f.write("\n")


def dump_dp(dp: SsvcDecisionPoint, path: str = None) -> None:
    if path is None:
        # act like we're in a json list
        lines = [f"  {line}" for line in dp.to_json(indent=2).split("\n")]
        print("\n".join(lines) + ",")
    else:
        basename = dp.name.strip().lower().replace(" ", "_")

        json_fname = f"{path}/{basename}.json"
        write_json(json_fname, dp)

        table_fname = f"{path}/{basename}.md"
        write_markdown_table(table_fname, dp)


def group_to_jsonfiles(group: SsvcDecisionPointGroup, path: str = None) -> None:
    for dp in group.decision_points:
        dump_dp(dp, path)


def main():
    from ssvc.dp_groups.v1 import SSVCv1
    from ssvc.dp_groups.v2 import SSVCv2
    from ssvc.dp_groups.v2_1 import SSVCv2_1
    from ssvc.dp_groups.cvss.v1 import CVSSv1
    from ssvc.dp_groups.cvss.v2 import CVSSv2
    from ssvc.dp_groups.cvss.v3 import CVSSv3

    # extract all decision points from the groups
    dps = get_all_decision_points_from(
        [SSVCv1, SSVCv2, SSVCv2_1, CVSSv1, CVSSv2, CVSSv3]
    )
    print("[")
    for dp in dps:
        dump_dp(dp, None)
    print("]")


if __name__ == "__main__":
    main()
