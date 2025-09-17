# Gathering Information About Technical Impact

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.technical_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

Assessing *Technical Impact* amounts to assessing the degree of control over the vulnerable component the attacker stands to gain by exploiting the vulnerability.
One way to approach this analysis is to ask whether the control gained is *total* or not.
If it is not total, it is *partial*.
If an answer to one of the following questions is *yes*, then control is *total*.
After exploiting the vulnerability,

- can the attacker install and run arbitrary software?
- can the attacker trigger all the actions that the vulnerable component can perform?
- does the attacker get an account with full privileges to the vulnerable component (administrator or root user accounts, for example)?

This list is an evolving set of heuristics.

{% include-markdown "../../_includes/question_callout.md" heading-offset=1 %}
