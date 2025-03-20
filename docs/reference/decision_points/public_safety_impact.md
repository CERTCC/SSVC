# Public Safety Impact

```python exec="true" idprefix=""
from ssvc.decision_points.public_safety_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

{% include-markdown "../../_includes/safety_cvss_ssvc.md" %}

This is a compound decision point, therefore it is a notational convenience.

Suppliers necessarily have a rather coarse-grained perspective on the broadly defined [Safety Impact](safety_impact.md) Decision Point.
Therefore we simplify the above into a binary categorization:

- *Significant* is when any impact meets the criteria for an impact of Marginal, Critical, or Catastrophic in the
  [Safety Impact](safety_impact.md) table.
- *Minimal* is when none do.

## Prior Versions

```python exec="true" idprefix=""
from ssvc.decision_points.public_safety_impact import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\n---\n")
```
