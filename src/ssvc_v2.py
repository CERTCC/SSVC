#!/usr/bin/env python
'''
file: ssvc_v2
author: adh
created_at: 3/23/21 3:23 PM
'''

import os
import pandas as pd

DATAPATH="../data/csvs"

PATHS = {
    'coord_pub': os.path.join(DATAPATH,"coord-publish-options.csv"),
    'coord_triage': os.path.join(DATAPATH,"coord-triage-options.csv"),
    'deployer': os.path.join(DATAPATH,"deployer-options.csv"),
    'supplier': os.path.join(DATAPATH,"supplier-options.csv"),
}

DEFAULTS = {
    'coord_pub': {
        # An analyst should feel comfortable selecting none if they (or their search scripts) have performed searches
        # in the appropriate places for public PoCs and active exploitation (as described above) and found none.
        "Exploitation": "none",
    },
    'coord_triage': {

    },
    'deployer': {
        # An analyst should feel comfortable selecting none if they (or their search scripts) have performed searches
        # in the appropriate places for public PoCs and active exploitation (as described above) and found none.
        "Exploitation": "none",
        "Exposure": "unavoidable"
    },
    'supplier': {
        # An analyst should feel comfortable selecting none if they (or their search scripts) have performed searches
        # in the appropriate places for public PoCs and active exploitation (as described above) and found none.
        "Exploitation": "none",
    },
}

# confirm that PATHS and DEFAULTS keys match
assert(set(PATHS.keys()) == set(DEFAULTS.keys()))

def _load_csvs(path_dict):
    data = {}
    for key,path in path_dict.items():
        df = pd.read_csv(path)
        data[key] = df
    return data

DATA = _load_csvs(PATHS)

# confirm that PATHS and DATA keys match
assert(set(PATHS.keys()) == set(DATA.keys()))


def lookup(key, query_dict,use_defaults=True):
    # get the full table
    df = DATA[key]

    if use_defaults:
        # copy the defaults before we use them
        defaults = DEFAULTS.get(key,{})
        q = dict(defaults)
    else:
        q = {}

    q.update(query_dict)

    # with each pass, slice the table
    for k,v in q.items():

        df = df.loc[df[k] == v]
    return df

def outcome_dist(df,normalize=True):
    '''
    Given a dataframe representing an SSVC tree fragment,
    compute and return the distribution of outcomes
    '''
    return df['Priority'].value_counts(normalize=normalize)


def main():
    for key,df in DATA.items():
        print(key, df.columns)

    print()
    query = {
        "Utility": "laborious",
        "Public_Safety_Impact": "minimal",
    }
    df = lookup('coord_triage',query)
    print(query)
    print(df)
    print(outcome_dist(df).round(decimals=3).to_dict())

    print()
    query = {'Value added': "precedence"}
    df = lookup('coord_pub',query)
    print(query)
    print(df)
    print(outcome_dist(df).round(decimals=3).to_dict())

    print()
    query = {"Public-Safety Impact": "minimal"}
    df = lookup('supplier',query)
    print(query)
    print(df)
    print(outcome_dist(df).round(decimals=3).to_dict())

if __name__ == '__main__':
    main()
