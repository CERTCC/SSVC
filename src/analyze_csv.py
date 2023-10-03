#!/usr/bin/env python
"""
This module provides a script for analyzing an SSVC tree csv file.

```shell
usage: analyze_csv.py [-h] [--outcol OUTCOL] [--permutation] csvfile

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
    $ python analyze_csv.py test.csv

    Feature Importance after Dropping Each Feature in test.csv
             feature  feature_importance
    0  exploitation_            0.347222
    1  human_impact_            0.291667
    2   automatable_            0.180556
    3      exposure_            0.166667
    ```

    Higher values imply more important features.
    """

import argparse
import sys

import pandas as pd
import re
from sklearn.tree import DecisionTreeClassifier
import sklearn.inspection
from sklearn.base import clone


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
    args = _parse_args(sys.argv[1:])

    # read csv
    df = pd.read_csv(args.csvfile)
    df = _clean_table(df)

    # check for target column
    target = args.outcol
    if target not in df.columns:
        print(
            f"Column '{target}' not found in {list(df.columns)}.\nPlease specify --outcol=<col> and try again."
        )
        exit(1)

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

    # construct tree
    dt = DecisionTreeClassifier(random_state=99, criterion="entropy")

    if args.permutation:
        imp = _perm_feat_imp(dt, X2, y)
        print(f"Feature Permutation Importance for {args.csvfile}")
    else:
        # drop columns and re-run
        imp = _drop_col_feat_imp(dt, X2, y)
        print(f"Drop Column Feature Importance for {args.csvfile}")

    print(imp)


if __name__ == "__main__":
    main()
