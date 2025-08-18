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

EDGE_LIMIT = 500


def _mapping2mermaid(mapping: list[dict[str:str]], title: str = None) -> str:
    """
    Convert a decision table mapping to a Mermaid graph.
    Args:
        mapping (list[dict[str:str]]): A list of dictionaries representing the decision table mapping.
            Each dictionary corresponds to a row in the table, with keys as column names and values as cell values.
            Each row should have the same keys, representing the columns of the decision table.
    Returns:
        str: A string containing a markdown Mermaid graph representation, including the code block markers.
    """
    lines = [
        "```mermaid",
    ]
    if title is not None:
        # add the yaml front matter for the title
        lines.extend(["---", f"title: {title}", "---"])

    lines.extend(["graph LR", "n1(( ))"])
    columns = list(mapping[0].keys())

    node_ids = {}  # (col_idx, path_tuple) -> node_id
    seen_edges = set()  # (parent_id, child_id)

    # Build subgraphs + nodes
    for col_idx, col in enumerate(columns):
        subgraph_name = f's{col_idx+1}["{col}"]'
        lines.append(f"subgraph {subgraph_name}")
        seen_paths = set()
        for row in mapping:
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
    for row in mapping:
        path = (row[columns[0]],)
        child_id = node_ids[(0, path)]
        edge = ("n1", child_id)
        if edge not in seen_edges:
            lines.append(f"{edge[0]} --- {edge[1]}")
            seen_edges.add(edge)

    # Level k-1 → level k
    for row in mapping:
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
                if len(seen_edges) > EDGE_LIMIT:
                    raise ValueError(
                        f"Too many edges in the graph: Limit={EDGE_LIMIT}."
                        "Consider filtering the mapping to reduce complexity."
                    )

    # Close the graph
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def mapping2mermaid(rows: list[dict[str:str]], title: str = None) -> str:
    """
    Convert a decision table mapping to a Mermaid graph.
    Args:
        rows (list[dict[str:str]]): A list of dictionaries representing the decision table mapping.
            Each dictionary corresponds to a row in the table, with keys as column names and values as cell values.
            Each row should have the same keys, representing the columns of the decision table.
    Returns:
        str: A string containing a markdown Mermaid graph representation, including the code block markers.
    """
    try:
        return _mapping2mermaid(rows)
    except ValueError as e:
        # graph is too big, split it into smaller graphs
        # one graph per value in the first column
        first_col = list(rows[0].keys())[0]
        diagrams = []
        uniq_values = set(row[first_col] for row in rows)
        for value in uniq_values:
            filtered_rows = [row for row in rows if row[first_col] == value]
            if not filtered_rows:
                continue
            try:
                diagram = _mapping2mermaid(
                    filtered_rows, title=f"{title} - {first_col}:{value}"
                )
                diagrams.append(diagram)
            except ValueError as e:
                print(f"Skipping {value} due to error: {e}")

        return "\n\n".join(diagrams) if diagrams else "No valid diagrams generated."


# Example

if __name__ == "__main__":

    from ssvc.decision_tables.cvss.qualitative_severity import LATEST as DT

    rows = DT.mapping

    # filter rows for invalid
    def invalid(row):
        if row["cvss:EQ3:1.0.0"] == "L" and row["cvss:EQ6:1.0.0"] == "H":
            return True
        return False

    rows = [row for row in rows if not invalid(row)]
    print(mapping2mermaid(rows))
