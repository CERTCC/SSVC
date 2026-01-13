# AIVSS Agentic Impact Level

The Agentic Impact Level (AIL) is...

!!! info "Agentic Impact Level supports the AIVSS framework"

    The Agentic Impact Level (AIL) is one of the decision points used in the
    [AIVSS framework](./index.md) to help organizations prioritize AI-related
    vulnerabilities. The AIL describes the degree of autonomy and influence
    the AI system has in its operational environment, which can impact the
    potential risk associated with vulnerabilities in the system.

!!! tip "Assessing Agentic Impact Level"

    The Agentic Impact Level (AIL) is not intended to be assessed for every
    individual vulnerability reported. Instead, it is intended to be assessed
    for the system as a whole, or for significant changes to the system that
    may affect the AIL. Because of this, we recommend that organizations
    assess the AIL periodically, such as during major system updates or
    architecture changes.

## Outcome

The outcome set for AIVSS Agentic Impact Level describes the degree of
autonomy and influence the AI system has in its operational environment.

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.agentic_impact import LATEST as DT
from ssvc.doc_helpers import example_block

dp = DT.decision_points[DT.outcome]
print(example_block(dp))
```

## Decision Points

The Decision Points for AIVSS Agentic Impact Level are divided into three
supporting decision tables. The examples below show the outcomes for each
of those decision tables that are used to determine the overall Agentic Impact Level.

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.agentic_impact import LATEST as DT
from ssvc.doc_helpers import example_block

for dp in [v for k,v in DT.decision_points.items() if k != DT.outcome]:
    print(example_block(dp))
```

!!! info "See documentation for the supporting decision tables"

    Although the Agentic Impact Level (AIL) can be assessed directly, we recommend
    it be assessed by combining the results of a few supporting decision tables.
    See the documentation for 
    [Execution Power](exec_power.md), 
    [Environment & Adaptation](env_adapt.md), and 
    [Predictability & Influence](predict_influence.md)
    for more details.

## Decision Table

### Decision Model Visualization

```python exec="true" idprefix=""
from ssvc.decision_tables.aivss.agentic_impact import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

### Table of Values

The table below shows the values for the decision model.
Each row of the table corresponds to a path through the decision model diagram above.

```python exec="true" idprefix=""

from ssvc.decision_tables.aivss.agentic_impact import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```
