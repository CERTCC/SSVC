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

#  Copyright (c) 2023-2025 Carnegie Mellon University.
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

import argparse
import logging
import re
import sys

import pandas as pd
import sklearn.inspection
from sklearn.base import clone
from sklearn.tree import DecisionTreeClassifier

from ssvc.utils.toposort import graph_from_value_tuples

logger = logging.getLogger(__name__)

# set an option to avoid a deprecation warning
pd.set_option("future.no_silent_downcasting", True)


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
        pd.DataFrame(
            {"feature": column_names, "feature_importance": importances}
        )
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
    parser = argparse.ArgumentParser(
        description="Analyze an SSVC tree csv file"
    )
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


def check_topological_order(
    df: pd.DataFrame, target: str, target_value_order: list[str] = None
) -> list[dict]:
    # split df into features and target
    X, y = _prepare_data(df, target)

    if target_value_order is None:
        # convert outcome to numeric codes
        codes = list(enumerate(y.unique()))
    else:
        # use the provided order for the target values
        codes = list(enumerate(target_value_order))

    mapper = {v: k for (k, v) in codes}
    y = y.replace(mapper)

    node_tuples = []
    for col in X.columns:
        # get the unique values in the column, sort them, and convert to tuple
        vals = tuple(sorted(X[col].unique()))
        node_tuples.append(vals)
    logger.debug(f"Node tuples: {node_tuples}")
    # create a graph of the nodes, assign the outcome value to each node
    # and then check that the graph is topologically sorted
    # (i.e. no edges point backwards)

    G = graph_from_value_tuples(node_tuples)

    # create a dict to lookup node outcomes from nodes
    node_outcomes = {}
    for i, row in enumerate(X.iterrows()):
        rownum, rowval = row

        # cast the row to a tuple so we can use it as a node
        node = tuple(rowval)
        node_outcomes[node] = y.iloc[i]

    for u in G.nodes:
        # assign the outcome value to each node
        G.nodes[u]["outcome"] = node_outcomes.get(u, None)

    logger.debug(f"Graph has {len(G.nodes)} nodes with {len(G.edges)} edges")

    problems = []
    # check if the outcome is topologically sorted
    for u, v in G.edges:
        if G.nodes[u]["outcome"] > G.nodes[v]["outcome"]:
            problem = {
                "u": u,
                "v": v,
                "u_outcome": G.nodes[u]["outcome"],
                "v_outcome": G.nodes[v]["outcome"],
            }
            problems.append(problem)

    if len(problems) == 0:
        logger.info("No topological problems found")

    return problems


if __name__ == "__main__":
    main()
