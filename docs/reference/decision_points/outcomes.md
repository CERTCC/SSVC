# Outcome Decision Points

SSVC outcomes are just Decision Point objects.
The only distinction is that these Decision Points are usually intended to be used
as the *outputs* of a decision, whereas most other Decision Points are intended to serve as *inputs* to a decision.
However, there are use cases (e.g., [compound decision points](compound_decision_points.md))
where an outcome of one decision may feed into another decision, so the
distinction between *input* and *output* is somewhat arbitrary. Hence, we chose to use the same
data structure for both.

Following is a list of Decision Points often used as outcomes in SSVC decision models.

```python exec="true" idprefix=""
from ssvc.outcomes import ALL
from ssvc.doc_helpers import example_block

for dp in ALL:
    print(example_block(dp))
```
