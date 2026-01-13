# AIVSS Environment and Adaptation

Some text

## Outcome

The outcome of the *Environment and Adaptation* decision table is defined by
the [Environment and Adaptation Level](../../reference/decision_points/aivss/environment_and_adaptation.md) decision point.

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.env_adaptation import LATEST as DT
from ssvc.doc_helpers import example_block

dp = DT.decision_points[DT.outcome]
print(example_block(dp))
```

## Decision Points

The *Environment and Adaptation* decision table has the following decision points:

- [Memory Usage Level](../../reference/decision_points/aivss/memory_level.md)
- [Contextual Awareness](../../reference/decision_points/aivss/contextual_awareness_level.md)
- [Dynamic Identity](../../reference/decision_points/aivss/dynamic_identity_level.md)
- [Multi-Agent Interactions](../../reference/decision_points/aivss/multi_agent_interactions_level.md)

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.env_adaptation import LATEST as DT
from ssvc.doc_helpers import example_block

for dp in [v for k,v in DT.decision_points.items() if k != DT.outcome]:
    print(example_block(dp))
```

## Decision Table

### Decision Model Visualization

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.env_adaptation import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

### Table of Values

The table below shows the values for the decision model.
Each row of the table corresponds to a path through the decision model diagram above.

```python exec="true" idprefix=""

from ssvc.decision_tables.aivss.env_adaptation import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```
