#!/usr/bin/env python
"""
file: analyze_csv
author: adh
created_at: 3/18/21 2:30 PM
"""
import argparse
import pandas as pd
import re
from sklearn.tree import DecisionTreeClassifier
import sklearn.inspection
from sklearn.base import clone


# normalize column names
def col_norm(c):
    new_col = re.sub("[^0-9a-zA-Z]+", "_", c)
    new_col = new_col.lower()
    return new_col


def imp_df(column_names, importances) -> pd.DataFrame:
    df = (
        pd.DataFrame({"feature": column_names, "feature_importance": importances})
        .sort_values("feature_importance", ascending=False)
        .reset_index(drop=True)
    )
    return df


def drop_col_feat_imp(model, X_train, y_train, random_state=42) -> pd.DataFrame:
    # from https://gist.github.com/erykml/6854134220276b1a50862aa486a44192#file-drop_col_feat_imp-py
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

    importances_df = imp_df(X_train.columns, importances)
    return importances_df


def main():
    args = parse_args()

    # read csv
    df = pd.read_csv(args.csvfile)
    df = clean_data(df)

    # check for target column
    target = args.outcol
    if target not in df.columns:
        print(
            f"Column '{target}' not found in {list(df.columns)}.\nPlease specify --outcol=<col> and try again."
        )
        exit(1)

    X, y = split_data(df, target)

    # turn features into ordinals
    # this assumes that every column is an ordinal label
    # and that the ordinals are sorted in ascending order
    encoded = {c: list(enumerate(X[c].unique())) for c in X.columns}
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
        perm_imp_feature(X2, args, cols, dt, y)
    else:
        drop_col_imp_feature(dt, X2, y)


def split_data(df: pd.DataFrame, target: str) -> (pd.DataFrame, pd.DataFrame):
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


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean up a dataframe, normalizing column names and dropping columns we don't need

    Args:
        df: the dataframe to clean

    Returns:
        the cleaned dataframe
    """
    # normalize data
    df = df.rename(columns=col_norm)
    # drop columns we don't need
    drop_cols = [
        "row",
    ]
    df = df.drop(columns=drop_cols, errors="ignore")
    return df


def drop_col_imp_feature(
    dt: DecisionTreeClassifier,
    x: pd.DataFrame,
    y: pd.DataFrame,
) -> None:
    # drop columns and re-run
    print("\nFeature Importance after Dropping Each Feature")
    imp = drop_col_feat_imp(dt, x, y)
    print(imp)


def perm_imp_feature(
    X2: pd.DataFrame, args, cols: list, dt: DecisionTreeClassifier, y: pd.DataFrame
) -> None:
    dt.fit(X2, y)
    # analyze tree
    results = sklearn.inspection.permutation_importance(dt, X2, y)
    imp = results["importances_mean"]
    labels = [c.replace("_", "") for c in cols]
    pairs = zip(labels, imp)
    pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
    # print results
    print(f"Feature Permutation Importance for {args.csvfile}")
    for label, importance in pairs:
        print(f"{label:>25}: {importance:0.4f}")


def parse_args():
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
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
