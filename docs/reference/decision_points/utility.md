# Utility

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.utility import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

!!! tip "See also"

    Utility is a combination of [Automatable](./automatable.md) and
    [Value Density](./value_density.md)

This is a compound decision point, therefore it is a notational convenience.

*Utility* estimates an adversary's benefit compared to their effort based on the assumption that they can exploit the vulnerability.
*Utility* is independent from the state of [*Exploitation*](exploitation.md), which measures whether a set of adversaries have ready access to exploit code or are in fact exploiting the vulnerability.
In economic terms, [*Exploitation*](exploitation.md) measures whether the **capital cost** of producing reliable exploit code has been paid or not.
*Utility* estimates the **marginal cost** of each exploitation event.

Whereas [*Exploitation*](exploitation.md) is about how easy it would be to start such a campaign or if one is already underway,
*Utility* is about how much an adversary might benefit from a campaign using the vulnerability in question.

Heuristically, we base Utility on a combination of the value density of vulnerable components and whether potential exploitation is automatable.
This framing makes it easier to analytically derive these categories from a description of the vulnerability and the affected component.
[*Automatable*](automatable.md) as ([*no*](automatable.md) or [*yes*](automatable.md)) and [*Value Density*](value_density.md) as ([*diffuse*](value_density.md) or [*concentrated*](value_density.md)) define those decision points.

Roughly, *Utility* is a combination of two things: (1) the value of each exploitation event and (2) the ease and speed with which the adversary can cause exploitation events.
We define *Utility* as laborious, efficient, or super effective, as described in the table above.

The mapping is shown in the diagram and table below.

```python exec="true" idprefix=""
from ssvc.decision_tables.ssvc.utility import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

```python exec="true" idprefix=""

from ssvc.decision_tables.ssvc.utility import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```


## Alternative Utility Outputs

Alternative heuristics can plausibly be used as proxies for adversary utility.
One example is the value of the vulnerability if it were sold on the open market.
Some firms, such as [Zerodium](https://zerodium.com/program.html), make such pricing structures public.
The valuable exploits track the [*Automatable*](automatable.md) and [*Value Density*](value_density.md) heuristics for the most part.
Within a single system—whether it is Apache, Windows, iOS or WhatsApp—more successfully automated steps in the kill lead to higher exploit value.
Remote code execution with sandbox escape and without user interaction are the most valuable exploits, and these features describe automation of the relevant kill chain steps.

How equivalently [*Automatable*](automatable.md) exploits for different systems are priced relative to each other is more idiosyncratic.
Price does not only track the [*Value Density*](value_density.md) of the system, but presumably also the existing supply of exploits and the installation distribution among the targets of Zerodium’s customers.
Currently, we simplify the analysis and ignore these factors.
However, future work should look for and prevent large mismatches between the outputs of the *Utility* decision point and the exploit markets.

## Previous Versions

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.utility import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\n---\n")
```

!!! tip "See also"

    Utility v1.0.0 was a combination of [Virulence](./automatable.md) and
    [Value Density](./value_density.md)
