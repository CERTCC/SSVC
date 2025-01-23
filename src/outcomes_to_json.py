#!/usr/bin/python3
from ssvc.outcomes import groups
from ssvc.outcomes.base import OutcomeGroup

for x in dir(groups):
 outcome = getattr(groups,x);
 if type(outcome) == OutcomeGroup:
  f = open(f"../data/json/outcomes/{x}.json","w")
  f.write(outcome.to_json())
  f.close()
 
