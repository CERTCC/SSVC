#!/usr/bin/python3
from ssvc.outcomes import groups
from ssvc.outcomes.base import OutcomeGroup

for x in dir(groups):
 outcome = getattr(groups,x);
 if type(outcome) == OutcomeGroup:
  with open(f"../data/json/outcomes/{x}.json","w") as f:
   f.write(outcome.to_json())

 
