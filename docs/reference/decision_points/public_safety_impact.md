# Public Safety Impact

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.public_safety_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

{% include-markdown "../../_includes/safety_cvss_ssvc.md" %}


Suppliers necessarily have a rather coarse-grained perspective on the broadly defined [Safety Impact](safety_impact.md) Decision Point.
Therefore we simplify the above into a binary categorization:

- *Significant* is when any impact meets the criteria for an impact of Marginal, Critical, or Catastrophic in the
  [Safety Impact](safety_impact.md) table.
- *Minimal* is when none do.

The mapping is shown in the diagram and table below.

```python exec="true" idprefix=""
from ssvc.decision_tables.ssvc.public_safety_impact import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

```python exec="true" idprefix=""

from ssvc.decision_tables.ssvc.public_safety_impact import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```


## Prior Versions

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.public_safety_impact import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\n---\n")
```
