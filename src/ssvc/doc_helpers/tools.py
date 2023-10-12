#!/usr/bin/env python
"""
file: tools
author: adh
created_at: 9/21/23 3:20 PM
"""
from ssvc.decision_points.base import SsvcDecisionPoint
from ssvc.dp_groups.base import SsvcDecisionPointGroup, get_all_decision_points_from

_DISCLAIMER = "This file is auto-generated. Do not edit."


def _html_comment(s: str) -> str:
    return f"<!-- {s} -->\n"


def write_file(fname: str, blob: str) -> None:
    with open(fname, "w") as f:
        print(f"Writing {fname}")
        f.write(blob)
        f.write("\n")


def dump_dp(dp: SsvcDecisionPoint, path: str = None) -> None:
    dp._comment = _DISCLAIMER
    json_blob = dp.to_json(indent=2)

    if path is None:
        # act like we're in a json list
        lines = [f"  {line}" for line in json_blob.split("\n")]
        print("\n".join(lines) + ",")
    else:
        basename = dp.name.strip().lower().replace(" ", "_")
        basename += f"_{dp.version.replace('.', '_')}"

        json_fname = f"{path}/{basename}.json"
        write_file(json_fname, json_blob)

        table_fname = f"{path}/{basename}.md"
        md_str = _html_comment(_DISCLAIMER)
        md_str += dp.to_table()
        write_file(table_fname, md_str)


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
