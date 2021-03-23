#!/usr/bin/env python
'''
file: ssvc_v2
author: adh
created_at: 3/23/21 3:23 PM
'''

import os
import pandas as pd

DATAPATH="../data/v2/csv"

PATHS = {
    'coord_pub': os.path.join(DATAPATH,"ssvc_2_coord-publish.csv"),
    'coord_triage': os.path.join(DATAPATH,"ssvc_2_coord-triage.csv"),
    'deployer': os.path.join(DATAPATH,"ssvc_2_deployer.csv"),
    'supplier': os.path.join(DATAPATH,"ssvc_2_supplier.csv"),
}

def load_csvs(path_dict):
    data = {}
    for key,path in path_dict.items():
        df = pd.read_csv(path)
        data[key] = df
    return data

DATA = load_csvs(PATHS)

def lookup(key, query_dict):
    # get the full table
    df = DATA[key]

    # with each pass, slice the table
    for k,v in query_dict.items():
        df = df.loc[df[k] == v]
    return df

def outcome_dist(df):
    '''
    Given a dataframe representing an SSVC tree fragment,
    compute and return the distribution of outcomes
    '''
    return df['Outcome'].value_counts(normalize=True)

def main():
    for key,df in DATA.items():
        print(key, df.columns)

    query = {
        "Utility": "laborious",
        "PublicSafetyImpact": "minor",
        "Credible":"Yes"
    }
    df = lookup('coord_triage',query)
    print(df)
    print(outcome_dist(df))

    query = {'Value added': "precedence"}
    df = lookup('coord_pub',query)
    print(df)
    print(outcome_dist(df))

    query = {"PublicSafetyImpact": "minimal"}
    df = lookup('supplier',query)
    print(df)
    print(outcome_dist(df))

if __name__ == '__main__':
    main()
