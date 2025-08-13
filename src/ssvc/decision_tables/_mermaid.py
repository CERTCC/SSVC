#!/usr/bin/env python
"""
file: _mermaid
author: adh
created_at: 8/13/25 4:29 PM
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


def dicts_to_mermaid_subgraphs(rows):
    lines = ["graph LR", "n1(( ))"]
    columns = list(rows[0].keys())

    # Build subgraphs
    for col_idx, col in enumerate(columns):
        subgraph_name = f's{col_idx+1}["{col}"]'
        lines.append(f"subgraph {subgraph_name}")
        seen = set()
        for row in rows:
            node_id = "".join(
                row[columns[i]]
                + (f"s{col_idx+1}" if col_idx == len(columns) - 1 else "")
                for i in range(col_idx + 1)
            )
            label = row[columns[col_idx]]
            if node_id not in seen:
                lines.append(f"{node_id}([{label}])")
                seen.add(node_id)
        lines.append("end")

    # Add edges
    first_col_vals = {row[columns[0]] for row in rows}
    for val in first_col_vals:
        lines.append(f"n1 --- {val}")

    for row in rows:
        prev_id = row[columns[0]]
        for col_idx in range(1, len(columns)):
            node_id = "".join(
                row[columns[i]]
                + (f"s{col_idx+1}" if col_idx == len(columns) - 1 else "")
                for i in range(col_idx + 1)
            )
            lines.append(f"{prev_id} --- {node_id}")
            prev_id = node_id

    return "\n".join(lines)


# Example

if __name__ == "__main__":
    from ssvc.decision_tables.ssvc.coord_pub_dt import LATEST as CP

    rows = CP.mapping
    print(dicts_to_mermaid_subgraphs(rows))
