# CVSS v4 Equivalence Set EQ3

Here we describe an example decision model for an analyst assessing the CVSS v4
equivalence set EQ3.

## Analyst Units of Work

!!! info inline end "Analyst Unit of Work"

    The unit of work for an Analyst is a single vulnerability report.

Analysts are usually tasked with assessing the CVSS score for an individual
vulnerability report.

## Analyst Decision Outcomes

The analyst's decision is to choose the appropriate level for CVSS v4 EQ3.

```python exec="true" idprefix=""
from ssvc.decision_tables.cvss.equivalence_set_three import LATEST as DT
from ssvc.doc_helpers import example_block

dp = DT.decision_points[DT.outcome]
print(example_block(dp))
```

## Analyst Decision Points

```python exec="true" idprefix=""
from ssvc.decision_tables.cvss.equivalence_set_three import LATEST as DT
from ssvc.doc_helpers import example_block

for dp in [v for k,v in DT.decision_points.items() if k != DT.outcome]:
    print(example_block(dp))
```

## Analyst Decision Model

Below we provide an example deployer prioritization policy that maps the decision points just listed to the outcomes described above.

### Decision Model Visualization

The following diagram shows the decision model for the EQ3 decision.

```python exec="true" idprefix=""
from ssvc.decision_tables.cvss.equivalence_set_three import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

### Table of Values

The table below shows the values for the decision model.
Each row of the table corresponds to a path through the decision model diagram above.

```python exec="true" idprefix=""

from ssvc.decision_tables.cvss.equivalence_set_three import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```
