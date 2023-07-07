#!/usr/bin/env python
'''
file: analyze_csv
author: adh
created_at: 3/18/21 2:30 PM
'''
import argparse
import pandas as pd
import re
from sklearn.tree import DecisionTreeClassifier
import sklearn.inspection


# normalize column names
def col_norm(c):
    new_col = re.sub('[^0-9a-zA-Z]+',"_",c)
    new_col = new_col.lower()
    return new_col

def main():
    # parse command line
    parser = argparse.ArgumentParser(description="Analyze an SSVC tree csv file")
    parser.add_argument('csvfile',metavar="csvfile",type=str,help="the csv file to analyze")
    parser.add_argument('--outcol',dest="outcol",type=str,help="the name of the outcome column",default="priority")
    args = parser.parse_args()

    # read csv
    df = pd.read_csv(args.csvfile)

    # normalize data
    df = df.rename(columns=col_norm)

    target = args.outcol
    if target not in df.columns:
        print(f"Column \'{target}\' not found in {list(df.columns)}.\nPlease specify --outcol=<col> and try again.")
        exit(1)

    # drop columns we don't need
    drop_cols = ['row',]
    df = df.drop(columns=drop_cols,errors="ignore")

    # construct feature list
    features = [c for c in df.columns if c != target]
    y = df[target]
    X = df[features]

    # turn features into ordinals
    # this assumes that every column is an ordinal label
    # and that the ordinals are sorted in ascending order
    encoded = {c: list(enumerate(X[c].unique())) for c in X.columns}
    cols = []
    for c in X.columns:
        newcol = f"{c}_"
        cols.append(newcol)
        codes = list(enumerate(X[c].unique()))
        mapper = {v:k for (k,v) in codes}
        X[newcol] = X[c].replace(mapper)
    X2 = X[cols]

    # construct tree
    dt = DecisionTreeClassifier(random_state=99,criterion="entropy")
    dt.fit(X2,y)

    # analyze tree
    results = sklearn.inspection.permutation_importance(dt,X2,y)

    imp = results['importances_mean']
    labels = [c.replace("_","") for c in cols]

    pairs = zip(labels,imp)
    pairs = sorted(pairs,key=lambda x: x[1],reverse=True)

    # print results
    print(f"Feature Permutation Importance for {args.csvfile}")

    for label,importance in pairs:
        print(f"{label:>25}: {importance:0.4f}")

if __name__ == '__main__':
    main()
