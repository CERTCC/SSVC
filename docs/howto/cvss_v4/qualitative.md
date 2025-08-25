# CVSS v4  Qualitative Severity Rating

Here we describe an example decision model for an analyst assessing the CVSS v4
Qualitative Severity Rating.
In our decision model, we assume that the analyst has already assessed the
vulnerability report against the CVSS v4 Equivalence Sets:

- EQ1: [CVSS v4 Equivalence Set 1](eq1.md)
- EQ2: [CVSS v4 Equivalence Set 2](eq2.md)
- EQ3: [CVSS v4 Equivalence Set 3](eq3.md)
- EQ4: [CVSS v4 Equivalence Set 4](eq4.md)
- EQ5: [CVSS v4 Equivalence Set 5](eq5.md)
- EQ6: [CVSS v4 Equivalence Set 6](eq6.md)

and is now ready to assign a qualitative severity rating based on the outcomes
of those equivalence sets.

!!! info "How we modeled the CVSS v4 Qualitative Severity Rating"

    The CVSS v4 specification provides a 
    [mapping](https://github.com/FIRSTdotorg/cvss-v4-calculator/blob/main/cvss_lookup.js)
    from each CVSS v4 *MacroVector* (made up of the six equivalence set selections)
    to a numerical score between 0.0 and 10.0.
    CVSS has traditionally provided the following mapping from numerical score
    ranges to qualitative severity ratings:

    | Numerical Score | Qualitative Severity Rating |
    |------------------|-----------------------------|
    | 0.0              | None                        |
    | 0.1 - 3.9        | Low                         |
    | 4.0 - 6.9        | Medium                      |
    | 7.0 - 8.9        | High                        |

    In our implementation, we just skip the numerical score step and go directly
    from the equivalence set outcomes to the qualitative severity rating that
    corresponds to the numerical score in the lookup table linked above.

## Analyst Units of Work

!!! info inline end "Analyst Unit of Work"

    The unit of work for an Analyst is a single vulnerability report.

Analysts are usually tasked with assessing the CVSS score for an individual
vulnerability report.

## Analyst Decision Outcomes

The analyst's decision is to choose the appropriate level for the CVSS v4 Qualitative Severity Rating.

```python exec="true" idprefix=""
from ssvc.decision_tables.cvss.qualitative_severity import LATEST as DT
from ssvc.doc_helpers import example_block

dp = DT.decision_points[DT.outcome]
print(example_block(dp))
```

## Analyst Decision Points

Each of these decision points corresponds to the outcome of one of the six equivalence set
decision tables.

```python exec="true" idprefix=""
from ssvc.decision_tables.cvss.qualitative_severity import LATEST as DT
from ssvc.doc_helpers import example_block

for dp in [v for k,v in DT.decision_points.items() if k != DT.outcome]:
    print(example_block(dp))
```

## Analyst Decision Model

Below we provide an example deployer prioritization decision table that maps the decision points just listed to the outcomes described above.

### Decision Model Visualization

The following diagram shows the decision model for the Qualitative Severity Rating decision.

```python exec="true" idprefix=""
from ssvc.decision_tables.cvss.qualitative_severity import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)

# filter rows for invalid
def invalid(row):
    if row["cvss:EQ3:1.0.0"] == "L" and row["cvss:EQ6:1.0.0"] == "H":
        return True
    return False

rows = [row for row in rows if not invalid(row)]
print(mapping2mermaid(rows, title=title))
```

### Table of Values

The table below shows the values for the decision model.
Each row of the table corresponds to a path through the decision model diagram above.

```python exec="true" idprefix=""

from ssvc.decision_tables.cvss.qualitative_severity import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

# filter rows for invalid (these don't affect the outcome because they're
# unreachable from valid CVSS vectors)
def invalid(row):
    if row["cvss:EQ3:1.0.0"] == "L" and row["cvss:EQ6:1.0.0"] == "H":
        return True
    return False

DT.mapping = [row for row in DT.mapping if not invalid(row)]

print(dt2df_md(DT))
```
