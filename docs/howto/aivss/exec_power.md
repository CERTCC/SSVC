# AIVSS Execution Power

Some text

## Outcome

The outcome of the *Execution Power* decision table is defined by
the [Execution Power Level](../../reference/decision_points/aivss/execution_power.md) decision point.

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.execution_power import LATEST as DT
from ssvc.doc_helpers import example_block

dp = DT.decision_points[DT.outcome]
print(example_block(dp))
```

## Decision Points

The *Execution Power* decision table has the following decision points:

- [Autonomy](../../reference/decision_points/aivss/autonomy_level.md)
- [Tool Use](../../reference/decision_points/aivss/tool_use.md)
- [Self-Modification](../../reference/decision_points/aivss/self_modification.md)
- [Goal-Driven Planning](../../reference/decision_points/aivss/goal_driven_planning.md)

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.execution_power import LATEST as DT
from ssvc.doc_helpers import example_block

for dp in [v for k,v in DT.decision_points.items() if k != DT.outcome]:
    print(example_block(dp))
```

## Decision Table

### Decision Model Visualization

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.execution_power import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

### Table of Values

The table below shows the values for the decision model.
Each row of the table corresponds to a path through the decision model diagram above.

```python exec="true" idprefix=""

from ssvc.decision_tables.aivss.execution_power import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```
