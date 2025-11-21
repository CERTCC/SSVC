# AIVSS

AIVSS is... {== TODO WRITE ME ==}

## Outcome

The outcome set for AIVSS is the basic SSVC priority levels: Defer, Scheduled, Out-of-Cycle, and Immediate.

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.aivss import LATEST as DT
from ssvc.doc_helpers import example_block

dp = DT.decision_points[DT.outcome]
print(example_block(dp))
```

## Decision Points

The Decision Points for AIVSS include:

- [Exploitation](../reference/decision_points/exploitation.md)
- Agentic Impact Level
- Systemic Impact

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.aivss import LATEST as DT
from ssvc.doc_helpers import example_block

for dp in [v for k,v in DT.decision_points.items() if k != DT.outcome]:
    print(example_block(dp))
```

!!! info "Agentic Impact Level is a Composite Decision Point"

    Although the Agentic Impact Level (AIL) can be assessed directly, we recommend
    it be assessed by combining the results of a few supporting decision tables.
    See [AIVSS Agentic Impact Level](./agentic_impact.md) for more details.

## Decision Table

### Decision Model Visualization

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.aivss import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

### Table of Values

The table below shows the values for the decision model.
Each row of the table corresponds to a path through the decision model diagram above.

```python exec="true" idprefix=""

from ssvc.decision_tables.aivss.aivss import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```
