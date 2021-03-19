#!/usr/bin/env python
'''
file: ssvc
author: adh
created_at: 12/2/19 2:23 PM
'''

import pandas as pd

_app_cols = ['Exploitation', 'Exposure', 'MissionImpact', 'SafetyImpact', 'Outcome']
_dev_cols = ['Exploitation', 'Utility', 'TechnicalImpact', 'SafetyImpact', 'Outcome']

_df_applier = pd.read_csv("../data/ssvc_1_applier.csv", usecols=_app_cols)
_df_developer = pd.read_csv("../data/ssvc_1_developer.csv", usecols=_dev_cols)

_app_lookup = _df_applier.to_dict(orient="records")
_dev_lookup = _df_developer.to_dict(orient="records")

defaults = {
    # In the case where no information is available or the organization has not yet
    # matured its initial situational analysis, we can suggest something like defaults
    # for some decision points. If the applier does not know their exposure, that means
    # they do not know where the devices are or how they are controlled, so they should
    # assume exposure is unavoidable.
    "exposure": "unavoidable",

    # If the decision maker knows nothing about the
    # environment in which the device is used, we suggest assuming a major safety impact.
    # This position is conservative, but software is thoroughly embedded in daily life now,
    # so we suggest that the decision maker provide evidence that no one’s well-being will
    # suffer. The reach of software exploits is no longer limited to a research network.
    "safety_impact": "major",

    # Similarly, with mission impact, the applier should assume that the software is in
    # use at the organization for a reason, and that it supports essential functions
    # unless they have evidence otherwise. With a total lack of information, assume
    # MEF support crippled as a default.
    "mission_impact": "MEF crippled",

    # Exploitation needs no special default; if
    # adequate searches are made for exploit code and none is found, the answer is
    # none.
    "exploitation": "none",

}

class SSVC_Error(Exception):
    pass

def applier_tree(exploitation=None, exposure=None, mission_impact=None, safety_impact=None):
    defaults_applied = []

    if exposure is None:
        exposure = defaults['exposure']
        defaults_applied.append('exposure')
    if safety_impact is None:
        safety_impact = defaults['safety_impact']
        defaults_applied.append('safety_impact')
    if mission_impact is None:
        mission_impact = defaults['mission_impact']
        defaults_applied.append('mission_impact')
    if exploitation is None:
        exploitation = defaults['exploitation']
        defaults_applied.append('exploitation')


    # This is a stupid linear search. Would make more sense if it was indexed.
    for item in _app_lookup:
        if exploitation.lower() != item['Exploitation'].lower():
            continue
        if exposure.lower() != item['Exposure'].lower():
            continue
        if mission_impact.lower() != item['MissionImpact'].lower():
            continue
        if safety_impact.lower() != item['SafetyImpact'].lower():
            continue
        # return the first thing that matches all four of the above
        item['defaults_applied'] = sorted(defaults_applied)
        return item

    # if you got here, you failed to match
    raise SSVC_Error("No match")

def developer_tree(exploitation=None, utility=None, technical_impact=None, safety_impact=None):
    defaults_applied = []

    if exploitation is None:
        exploitation = defaults['exploitation']
        defaults_applied.append('exploitation')
    if safety_impact is None:
        safety_impact = defaults['safety_impact']
        defaults_applied.append('safety_impact')
    if utility is None:
        raise SSVC_Error("utility value must be specified")
    if technical_impact is None:
        raise SSVC_Error("technical_impact value must be specified")

    for item in _dev_lookup:
        if exploitation.lower() != item['Exploitation'].lower():
            continue
        if utility.lower() != item['Utility'].lower():
            continue
        if technical_impact.lower() != item['TechnicalImpact'].lower():
            continue
        if safety_impact.lower() != item['SafetyImpact'].lower():
            continue
        # return the first thing that matches all four of the above
        item['defaults_applied'] = sorted(defaults_applied)

    # if you got here, you failed to match
    raise SSVC_Error("No match")





def main():
    print(_df_applier)
    print(_df_developer)


if __name__ == '__main__':
    main()