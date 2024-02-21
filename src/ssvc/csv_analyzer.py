#!/usr/bin/env python
"""
This module provides a script for analyzing an SSVC tree csv file.

```shell
usage: csv_analyzer.py [-h] [--outcol OUTCOL] [--permutation] csvfile

Analyze an SSVC tree csv file

positional arguments:
  csvfile          the csv file to analyze

options:
  -h, --help       show this help message and exit
  --outcol OUTCOL  the name of the outcome column
  --permutation    use permutation importance instead of drop column importance
```

Example:
    Given a `test.csv` file like this:
    ```csv
    row,Exploitation,Exposure,Automatable,Human Impact,Priority
    1,none,small,no,low,defer
    2,none,small,no,medium,defer
    3,none,small,no,high,scheduled
    ...
    ```
    Analyze the csv file:
    ```shell
    $ python csv_analyzer.py test.csv

    Feature Importance after Dropping Each Feature in test.csv
             feature  feature_importance
    0  exploitation_            0.347222
    1  human_impact_            0.291667
    2   automatable_            0.180556
    3      exposure_            0.166667
    ```

    Higher values imply more important features.
    """

#  Copyright (c) 2023-2024 Carnegie Mellon University and Contributors.
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

import argparse
import logging
import re
import sys
from itertools import product

import networkx as nx
import pandas as pd
import sklearn.inspection
from sklearn.base import clone
from sklearn.tree import DecisionTreeClassifier

logger = logging.getLogger(__name__)


def _col_norm(c: str) -> str:
    """
    Normalize a column name

    Args:
        c: the column name to normalize

    Returns:
        the normalized column name
    """
    new_col = re.sub("[^0-9a-zA-Z]+", "_", c)
    new_col = new_col.lower()
    return new_col


def _imp_df(column_names: list, importances: list) -> pd.DataFrame:
    """
    Create a dataframe of feature importances

    Args:
        column_names: the names of the columns
        importances: the feature importances

    Returns:
        a dataframe of feature importances
    """
    df = (
        pd.DataFrame({"feature": column_names, "feature_importance": importances})
        .sort_values("feature_importance", ascending=False)
        .reset_index(drop=True)
    )
    return df


def _drop_col_feat_imp(
    model: DecisionTreeClassifier,
    X_train: pd.DataFrame,
    y_train: pd.DataFrame,
    random_state: int = 99,
) -> pd.DataFrame:
    # based on https://gist.github.com/erykml/6854134220276b1a50862aa486a44192#file-drop_col_feat_imp-py
    # clone the model to have the exact same specification as the one initially trained
    model_clone = clone(model)
    # set random_state for comparability
    model_clone.random_state = random_state
    # training and scoring the benchmark model
    model_clone.fit(X_train, y_train)

    benchmark_score = model_clone.score(X_train, y_train)
    # list for storing feature importances
    importances = []

    # iterating over all columns and storing feature importance (difference between benchmark and new model)
    for col in X_train.columns:
        model_clone = clone(model)
        model_clone.random_state = random_state
        model_clone.fit(X_train.drop(col, axis=1), y_train)
        drop_col_score = model_clone.score(X_train.drop(col, axis=1), y_train)
        importances.append(benchmark_score - drop_col_score)

    importances_df = _imp_df(X_train.columns, importances)
    return importances_df


def _split_data(df: pd.DataFrame, target: str) -> (pd.DataFrame, pd.DataFrame):
    """
    Split a dataframe into features and target

    Args:
        df: the dataframe to split
        target: the name of the target column

    Returns:
        a tuple of (features, target)
    """

    # construct feature list
    features = [c for c in df.columns if c != target]
    y = df[target]
    X = df[features]
    return X, y


def _clean_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean up a dataframe, normalizing column names and dropping columns we don't need

    Args:
        df: the dataframe to clean

    Returns:
        the cleaned dataframe
    """
    # normalize data
    df = df.rename(columns=_col_norm)
    # drop columns we don't need
    drop_cols = [
        "row",
    ]
    df = df.drop(columns=drop_cols, errors="ignore")
    return df


def _perm_feat_imp(model, x, y):
    model.random_state = 99
    model.fit(x, y)
    # analyze tree
    results = sklearn.inspection.permutation_importance(model, x, y)
    imp = results["importances_mean"]

    imp = _imp_df(x.columns, imp)
    return imp


def _parse_args(args) -> argparse.Namespace:
    # parse command line
    parser = argparse.ArgumentParser(description="Analyze an SSVC tree csv file")
    parser.add_argument(
        "csvfile", metavar="csvfile", type=str, help="the csv file to analyze"
    )
    parser.add_argument(
        "--outcol",
        dest="outcol",
        type=str,
        help="the name of the outcome column",
        default="priority",
    )
    # use permutation or drop column importance?
    # default is drop column
    parser.add_argument(
        "--permutation",
        dest="permutation",
        action="store_true",
        help="use permutation importance instead of drop column importance",
        default=False,
    )
    return parser.parse_args(args)


def main():
    # set up root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    hdlr = logging.StreamHandler()
    logger.addHandler(hdlr)

    args = _parse_args(sys.argv[1:])

    csvfile = args.csvfile
    # read csv
    df = pd.read_csv(csvfile)

    print("Checking for valid topological order...")

    problems = check_topological_order(df, args.outcol)

    if len(problems):
        print("Not topologically sorted!")

    for problem in problems:
        print(
            f"Problem: {problem['u']} ({problem['u_outcome']}) is greater than {problem['v']} ({problem['v_outcome']})"
        )
        sys.exit(1)

    if args.permutation:
        imp = permute_feature_importance(df, args.outcol)
        print(f"Feature Permutation Importance for {df.columns}")
    else:
        imp = drop_col_feature_importance(df, args.outcol)
        print(f"Drop Column Feature Importance for {df.columns}")

    print(imp)


def _prepare_data(
    df: pd.DataFrame, target: str, permute: bool = False
) -> (pd.DataFrame, pd.DataFrame):
    """
    Compute feature importance two different ways for a dataframe

    Args:
        df: the dataframe to analyze
        target: the name of the target column to analyze against
        permute: use permutation importance instead of drop column importance

    Returns:
        a tuple of (the cleaned dataframe, the feature importance dataframe)
    """

    df = _clean_table(df)
    # check for target column
    if target not in df.columns:
        raise KeyError(f"Column '{target}' not found in {list(df.columns)}")

    X, y = _split_data(df, target)
    # turn features into ordinals
    # this assumes that every column is an ordinal label
    # and that the ordinals are sorted in ascending order
    cols = []
    for c in X.columns:
        newcol = f"{c}_"
        cols.append(newcol)
        codes = list(enumerate(X[c].unique()))
        mapper = {v: k for (k, v) in codes}
        X[newcol] = X[c].replace(mapper)
    X2 = X[cols]

    return X2, y


def drop_col_feature_importance(df: pd.DataFrame, target: str) -> pd.DataFrame:
    """
    Compute feature importance using drop column feature importance

    Args:
        df: the dataframe to analyze
        target: the name of the target column to analyze against

    Returns:
        a dataframe of feature importances
    """
    X2, y = _prepare_data(df, target)
    # construct tree
    dt = DecisionTreeClassifier(random_state=99, criterion="entropy")

    imp = _drop_col_feat_imp(dt, X2, y)
    return imp


def permute_feature_importance(df: pd.DataFrame, target: str) -> pd.DataFrame:
    """
    Compute feature importance using permutation feature importance

    Args:
        df: the dataframe to analyze
        target: the name of the target column to analyze against

    Returns:
        a dataframe of feature importances
    """
    X2, y = _prepare_data(df, target)
    # construct tree
    dt = DecisionTreeClassifier(random_state=99, criterion="entropy")

    imp = _perm_feat_imp(dt, X2, y)
    return imp


def check_topological_order(df, target):
    # split df into features and target
    X, y = _prepare_data(df, target)

    # convert outcome to numeric codes
    codes = list(enumerate(y.unique()))
    mapper = {v: k for (k, v) in codes}
    y = y.replace(mapper)

    # create a graph of the nodes, assign the outcome value to each node
    # and then check that the graph is topologically sorted
    # (i.e. no edges point backwards)
    G = nx.DiGraph()
    # each row of X is a single node
    for i, row in enumerate(X.iterrows()):
        rownum, rowval = row

        # cast the row to a tuple so we can use it as a node
        node = tuple(rowval)
        G.add_node(node, outcome=y.iloc[i])

    # add edges
    for u, v in product(G.nodes, G.nodes):
        # skip self edges
        if u == v:
            continue

        # u is less than v if all elements of u are less than or equal to v
        if all(u[i] <= v[i] for i in range(len(u))):
            # and at least one element of u is less than v
            if any(u[i] < v[i] for i in range(len(u))):
                # add edge if not already there
                if not G.has_edge(u, v):
                    G.add_edge(u, v)

        # v is less than u if all elements of v are less than or equal to u
        if all(v[i] <= u[i] for i in range(len(v))):
            # and at least one element of v is less than u
            if any(v[i] < u[i] for i in range(len(v))):
                # add edge if not already there
                if not G.has_edge(v, u):
                    G.add_edge(v, u)

    # take the transitive reduction of G to remove redundant edges
    # this will remove all edges that are implied by other edges
    # and leave only the minimal set of edges
    # H is thus a Hasse diagram of G
    H = nx.transitive_reduction(G)

    # networkx transitive reduction doesn't copy the node data
    # so we need to copy it from G to H
    for u in H.nodes:
        H.nodes[u]["outcome"] = G.nodes[u]["outcome"]

    logger.debug(f"Original graph: {len(G.nodes)} nodes with {len(G.edges)} edges")
    logger.debug(f"Reduced graph: {len(H.nodes)} nodes with {len(H.edges)} edges")

    problems = []
    # check if the outcome is topologically sorted
    for u, v in H.edges:
        if H.nodes[u]["outcome"] > H.nodes[v]["outcome"]:
            problem = {
                "u": u,
                "v": v,
                "u_outcome": H.nodes[u]["outcome"],
                "v_outcome": H.nodes[v]["outcome"],
            }
            problems.append(problem)

    if len(problems) == 0:
        logger.info("No topological problems found")

    return problems


if __name__ == "__main__":
    main()
