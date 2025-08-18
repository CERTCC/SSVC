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

    node_ids = {}  # (col_idx, path_tuple) -> node_id
    seen_edges = set()  # (parent_id, child_id)

    # Build subgraphs + nodes
    for col_idx, col in enumerate(columns):
        subgraph_name = f's{col_idx+1}["{col}"]'
        lines.append(f"subgraph {subgraph_name}")
        seen_paths = set()
        for row in rows:
            path = tuple(row[columns[i]] for i in range(col_idx + 1))
            if path in seen_paths:
                continue
            seen_paths.add(path)
            node_id = "_".join(path) + f"_L{col_idx}"
            # future: if you want to label the nodes, do that here
            label = row[columns[col_idx]]
            lines.append(f"{node_id}([{label}])")
            node_ids[(col_idx, path)] = node_id
        lines.append("end")

    # Root → level 0
    for row in rows:
        path = (row[columns[0]],)
        child_id = node_ids[(0, path)]
        edge = ("n1", child_id)
        if edge not in seen_edges:
            lines.append(f"{edge[0]} --- {edge[1]}")
            seen_edges.add(edge)

    # Level k-1 → level k
    for row in rows:
        for col_idx in range(1, len(columns)):
            parent_path = tuple(row[columns[i]] for i in range(col_idx))
            child_path = parent_path + (row[columns[col_idx]],)
            parent_id = node_ids[(col_idx - 1, parent_path)]
            child_id = node_ids[(col_idx, child_path)]
            edge = (parent_id, child_id)
            if edge not in seen_edges:
                # future: if you want to label the links, do that here
                lines.append(f"{parent_id} --- {child_id}")
                seen_edges.add(edge)

    return "\n".join(lines)


# Example

if __name__ == "__main__":
    from ssvc.decision_tables.ssvc.coord_pub_dt import LATEST as CP

    rows = CP.mapping
    print(dicts_to_mermaid_subgraphs(rows))
