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
import pandas as pd

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
    dt: DecisionTable,
    longform: bool = True,
) -> str:
    """
    Convert a decision table to a DataFrame.
    Args:
        decision_table (DecisionTable): The decision table to convert.
        longform (bool): Whether to return the longform or shortform DataFrame.
    Returns:
        str: A string representation of the DataFrame in text/markdown format.
    """
    if longform:
        df = decision_table_to_longform_df(dt)
    else:
        df = decision_table_to_shortform_df(dt)

    df.index.rename("Row", inplace=True)
    return df.to_markdown(index=True)


def dt2df_html(dt: DecisionTable, longform: bool = True) -> str:
    """
    Converts a Decision Tree and represent it in friendly HTML Code
    Args:
        decision_table (DecisionTable): The decision table to convert.
        longform (bool): Whether to return the longform or shortform DataFram, defaults to true
    Returns:
        str: A string representation of the DataFrame in HTML format.
    """

    if longform:
        df = decision_table_to_longform_df(dt)
    else:
        df = decision_table_to_shortform_df(dt)

    df = decision_table_to_longform_df(dt)
    ncols = len(df.columns)
    nrows = len(df)

    # Precompute rowspan info for every cell
    # rowspan[i][j] = number of rows this cell should span; 0 means skip (because merged above)
    rowspan = [[1] * ncols for _ in range(nrows)]

    for col in range(ncols):
        r = 0
        while r < nrows:
            start = r
            val = df.iat[r, col]  # data_rows[r][col]
            # Count how many subsequent rows have same value
            while (
                r + 1 < nrows and df.iat[r + 1, col] == val
            ):  # data_rows[r + 1][col] == val:
                r += 1
            span = r - start + 1
            if span > 1:
                # Assign span to first, mark rest as 0 (skip)
                rowspan[start][col] = span
                for k in range(start + 1, start + span):
                    rowspan[k][col] = 0
            r += 1

    # Build HTML
    html = [
        """<style>
    table,th,td,tr { border-spacing: 0px; border: 1px solid cyan; padding: 0px; font-family: verdana,courier }
    .decision_table th { font-weight: bold; }
    td.decision_point { vertical-align: middle}
    td.outcome { font-style: italic; font-weight: bold}
</style>"""
    ]
    html.append('<table class="decision_table">')
    html.append(
        "  <tr>" + "".join(f"<th>{h}</th>" for h in df.columns) + "</tr>"
    )

    for i, row in df.iterrows():  # for i, row in enumerate(df):
        cells = []
        j = 0
        for _, val in row.items():  # enumerate(row):
            tdtype = "decision_point"
            if j == len(row) - 1:
                tdtype = "outcome"
            if rowspan[i][j] > 0:
                span = rowspan[i][j]
                if span > 1:
                    cells.append(
                        f'<td rowspan="{span}" class="{tdtype}">{val}</td>'
                    )
                else:
                    cells.append(f'<td class="{tdtype}">{val}</td>')
            j = j + 1
        html.append("  <tr>" + "".join(cells) + "</tr>")

    html.append("</table>")
    return "".join(html)


def build_tree(
    df: pd.DataFrame, columns: pd.Index | list[str]
) -> dict[str, dict[str, str] | list[str]] | list[str]:
    """
    Helper function recursively build a nested dict:
    {feature_value: subtree_or_list_of_outcomes}
    This tree should preserve the original row order of the DataFrame.
    """
    # Base case: if only one column is left, it's the outcome.
    if len(columns) == 1:
        # Last column: return a list of outcomes.
        return df[columns[0]].astype(str).tolist()

    # Get the first feature column and the rest of the columns.
    first, rest = columns[0], columns[1:]
    tree = {}

    # Iterate through the unique values of the first column in the order they appear.
    # This is the key change to preserve the original CSV order.
    for val in df[first].unique():
        # Filter the DataFrame to get the group for the current value.
        group = df[df[first] == val]
        # Recursively build the subtree for this group.
        tree[str(val)] = build_tree(group, rest)

    return tree


def draw_tree(
    node: dict | list, prefix: str = "", lines: list | None = None
) -> list:
    """
    Pretty-print nested dict/list as a tree.
    """
    if lines is None:
        lines = []

    if isinstance(node, dict):
        items = list(node.items())
        for i, (k, v) in enumerate(items):
            # Determine the branch characters for the tree.
            branch = "└── " if i == len(items) - 1 else "├── "
            lines.append(prefix + branch + k + " " * 4)

            # Calculate the prefix for the next level of the tree.
            next_prefix = prefix + (
                " " * 16 if i == len(items) - 1 else "│" + " " * 15
            )
            # Recursively draw the subtree.
            draw_tree(v, next_prefix, lines)
    else:  # list of outcomes
        for i, leaf in enumerate(node):
            # Determine the branch characters for the leaves.
            branch = "└── " if i == len(node) - 1 else "├── "
            lines.append(prefix + branch + f"[{leaf}]")

    return lines


def ascii_tree(dt: DecisionTable, df: pd.DataFrame | None = None) -> str:
    """
    Reads a Pandas data frame, builds a decision tree, and returns its ASCII representation.
    """
    # Check for the optional 'row' column and drop it if it exists.
    if df == None:
        df = decision_table_to_longform_df(dt)

    if "row" in df.columns:
        df.drop(columns="row", inplace=True)

    # Separate feature columns from the outcome column.
    feature_cols = list(df.columns[:-1])
    outcome_col = df.columns[-1]

    # Build the tree structure.
    tree = build_tree(df, feature_cols + [outcome_col])
    # Draw the tree into a list of strings.
    lines = draw_tree(tree)

    # Generate the header line.
    header = ""
    for item in df.columns:
        if len(item) > 14:
            header = header + item[0:12] + ".." + " | "
        else:
            header = header + item + " " * (14 - len(item)) + " | "

    # Generate the separator line.
    sep = "-" * len(header)

    # Combine the header, separator, and tree lines into a single string.
    return "\n".join([header, sep] + lines)


def main():
    pass


if __name__ == "__main__":
    main()
