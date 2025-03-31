#!/usr/bin/env python
"""
file: ssvc_v2
author: adh
created_at: 3/23/21 3:23 PM
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

import os

import pandas as pd

DATAPATH = "../data/csvs"

PATHS = {
    "coord_pub": os.path.join(DATAPATH, "coord-publish-options.csv"),
    "coord_triage": os.path.join(DATAPATH, "coord-triage-options.csv"),
    "deployer": os.path.join(DATAPATH, "deployer-options.csv"),
    "supplier": os.path.join(DATAPATH, "supplier-options.csv"),
}

DEFAULTS = {
    "coord_pub": {
        # An analyst should feel comfortable selecting none if they (or their search scripts) have performed searches
        # in the appropriate places for public PoCs and active exploitation (as described above) and found none.
        "Exploitation": "none",
    },
    "coord_triage": {},
    "deployer": {
        # An analyst should feel comfortable selecting none if they (or their search scripts) have performed searches
        # in the appropriate places for public PoCs and active exploitation (as described above) and found none.
        "Exploitation": "none",
        "Exposure": "unavoidable",
    },
    "supplier": {
        # An analyst should feel comfortable selecting none if they (or their search scripts) have performed searches
        # in the appropriate places for public PoCs and active exploitation (as described above) and found none.
        "Exploitation": "none",
    },
}

# confirm that PATHS and DEFAULTS keys match
assert set(PATHS.keys()) == set(DEFAULTS.keys())


def _load_csvs(path_dict):
    data = {}
    for key, path in path_dict.items():
        df = pd.read_csv(path)
        data[key] = df
    return data


DATA = _load_csvs(PATHS)

# confirm that PATHS and DATA keys match
assert set(PATHS.keys()) == set(DATA.keys())


def lookup(key, query_dict, use_defaults=True):
    # get the full table
    df = DATA[key]

    if use_defaults:
        # copy the defaults before we use them
        defaults = DEFAULTS.get(key, {})
        q = dict(defaults)
    else:
        q = {}

    q.update(query_dict)

    # with each pass, slice the table
    for k, v in q.items():

        df = df.loc[df[k] == v]
    return df


def outcome_dist(df, normalize=True):
    """
    Given a dataframe representing an SSVC tree fragment,
    compute and return the distribution of outcomes
    """
    return df["Priority"].value_counts(normalize=normalize)


def main():
    for key, df in DATA.items():
        print(key, df.columns)

    print()
    query = {
        "Utility": "laborious",
        "Public_Safety_Impact": "minimal",
    }
    df = lookup("coord_triage", query)
    print(query)
    print(df)
    print(outcome_dist(df).round(decimals=3).model_dump())

    print()
    query = {"Value added": "precedence"}
    df = lookup("coord_pub", query)
    print(query)
    print(df)
    print(outcome_dist(df).round(decimals=3).model_dump())

    print()
    query = {"Public-Safety Impact": "minimal"}
    df = lookup("supplier", query)
    print(query)
    print(df)
    print(outcome_dist(df).round(decimals=3).model_dump())


if __name__ == "__main__":
    main()
