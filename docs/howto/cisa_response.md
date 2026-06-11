# HOW TO USE THE CISA RESPONSE TIMELINE SSVC DECISION TREE

The CISA Response Timeline SSVC Decision Tree is a tool support implementers
of [CISA BOD 26-04](<https://www.cisa>.
gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk).
Readers should consult the directive for more details about how to use the
decision table below. What follows is just a brief introduction to the
outcomes, decision points, and decision table structure.

## Outcomes and Decision Points

The CISA Response Timeline has 4 binary decision points:

1. InKEV
2. Publicly Exposed
3. Automatable
4. Technical Impact

More information about each of these will be at the bottom of this page.

These 4 decision points are combined to yield 4 outcomes for vulnerability
response timelines:

```python exec="true" idprefix=""
from ssvc.outcomes.cisa.bod2604 import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

InKEV, Automatable, and Technical Impact address the vulnerability whereas
Publicly Exposed questions the state of the asset.

```python exec="true" idprefix=""
from ssvc.decision_points.cisa.in_kev import IN_KEV_1
from ssvc.decision_points.cisa.publicly_exposed import PUBLICLY_EXPOSED_1
from ssvc.decision_points.ssvc.automatable import AUTOMATABLE_2
from ssvc.decision_points.ssvc.technical_impact import TECHNICAL_IMPACT_1
from ssvc.doc_helpers import example_block

print(example_block(IN_KEV_1))
print(example_block(PUBLICLY_EXPOSED_1))
print(example_block(AUTOMATABLE_2))
print(example_block(TECHNICAL_IMPACT_1))
```

## CISA BOD 26-04 Decision Model

```python exec="true" idprefix=""
from ssvc.decision_tables.cisa.bod_2604_dt import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

### Table of Values

The table below shows the values for the decision model.
Each row of the table corresponds to a path through the decision model diagram above.

{% include-markdown "../_includes/_scrollable_table.md" heading-offset=1 %}

```python exec="true" idprefix=""

from ssvc.decision_tables.cisa.bod_2604_dt import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```
