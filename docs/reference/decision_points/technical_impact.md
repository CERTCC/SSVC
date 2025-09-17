# Technical Impact

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.technical_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

!!! tip "Gathering Information about Technical Impact"

      See this [HowTo](../../howto/gathering_info/technical_impact.md) for advice on gathering information about the Technical Impact decision point.

When evaluating *Technical Impact*, recall the scope definition in the [Scope Section](../../topics/scope.md).
Total control is relative to the affected component where the vulnerability resides.
If a vulnerability discloses authentication or authorization credentials to the system, this information disclosure should also be scored as “total” if those credentials give an adversary total control of the component.

As mentioned in [Current State of Practice](../../topics/state_of_practice.md), the scope of SSVC is just those situations in which there is a vulnerability.
Our definition of **vulnerability** is based on the determination that some security policy is violated.
We consider a security policy violation to be a technical impact—or at least, a security policy violation must have some technical instantiation.
Therefore, if there is a vulnerability then there must be some technical impact.
