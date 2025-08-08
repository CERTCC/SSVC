#!/usr/bin/env python
"""
Provides helper functions for decision tables in SSVC.
"""

#  Copyright (c) 2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278


from ssvc.decision_tables.base import (
    DecisionTable,
    decision_table_to_longform_df,
    decision_table_to_shortform_df,
)


def write_csv(
    decision_table: "DecisionTable",
    csvfile: str,
    child_tree: bool = False,
    index: bool = False,
):
    import os

    # write longform csv to file
    file_path = os.path.abspath(__file__)
    project_base_path = os.path.abspath(
        os.path.join(os.path.dirname(file_path), "..", "..", "..")
    )

    parts = ["data", "csvs"]
    if child_tree:
        parts.append("child_trees")

    target_dir = os.path.join(project_base_path, *parts)
    assert os.path.exists(target_dir), f"Target directory {target_dir} does not exist."

    csv_path = os.path.join(target_dir, csvfile)

    with open(csv_path, "w") as fp:
        fp.write(decision_table_to_longform_df(decision_table).to_csv(index=index))


def print_dt_version(dt: DecisionTable, longform=True) -> None:
    from ssvc.decision_tables.base import decision_table_to_longform_df

    print(f"# Decision Table: {dt.name} v{dt.version}")
    print()
    print("## Full Model Dump:")
    print()
    print(dt.model_dump_json(indent=2))
    print()
    print("## CSV Mapping:")
    print()
    if longform:
        df = decision_table_to_longform_df(dt)
    else:
        df = decision_table_to_shortform_df(dt)
    print(df.to_csv(index=False))


def main():
    pass


if __name__ == "__main__":
    main()

