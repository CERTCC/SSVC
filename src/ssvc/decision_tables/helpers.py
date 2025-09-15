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


import logging

from ssvc.decision_tables.base import (
    DecisionTable,
    decision_table_to_longform_df,
    decision_table_to_shortform_df,
)

logger = logging.getLogger(__name__)

EDGE_LIMIT = 500


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
    assert os.path.exists(
        target_dir
    ), f"Target directory {target_dir} does not exist."

    csv_path = os.path.join(target_dir, csvfile)

    with open(csv_path, "w") as fp:
        fp.write(
            decision_table_to_longform_df(decision_table).to_csv(index=index)
        )


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

    lines.extend(["graph LR", "subgraph inputs[Inputs]", "n1(( ))"])
    columns = list(mapping[0].keys())

    node_ids = {}  # (col_idx, path_tuple) -> node_id
    seen_edges = set()  # (parent_id, child_id)

    # Build subgraphs + nodes
    for col_idx, col in enumerate(columns):
        # if it's the last column, close the Inputs subgraph and start the Outputs subgraph
        if col_idx == len(columns) - 1:
            lines.append("end")
            lines.append("subgraph outputs[Outcome]")

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
    lines.append("end")  # close the outputs subgraph

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


def mermaid_title_from_dt(dt: "DecisionTable") -> str:
    return f"{dt.name} Decision Table ({dt.namespace}:{dt.key}:{dt.version})"


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
        return _mapping2mermaid(rows, title=title)
    except ValueError as e:
        # graph is too big, split it into smaller graphs
        # one graph per value in the first column
        first_col = list(rows[0].keys())[0]
        diagrams = []

        # find unique values but keep them in order of appearance
        _uniq_set = set()
        uniq_values = []
        for row in rows:
            if row[first_col] in _uniq_set:
                continue
            _uniq_set.add(row[first_col])
            uniq_values.append(row[first_col])

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
                logger.error(f"Skipping {title} {value} due to error: {e}")

        return (
            "\n\n".join(diagrams)
            if diagrams
            else "No valid diagrams generated."
        )


def dt2df_md(
    dt: "DecisionTable",
    longform: bool = True,
) -> str:
    """
    Convert a decision table to a DataFrame.
    Args:
        decision_table (DecisionTable): The decision table to convert.
        longform (bool): Whether to return the longform or shortform DataFrame.
    Returns:
        str: A string representation of the DataFrame in CSV format.
    """
    if longform:
        df = decision_table_to_longform_df(dt)
    else:
        df = decision_table_to_shortform_df(dt)

    df.index.rename("Row", inplace=True)
    return df.to_markdown(index=True)


def main():
    pass


if __name__ == "__main__":
    main()
