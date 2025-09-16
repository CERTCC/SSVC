# Value Density (SSVC)

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.value_density import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

!!! tip "Gathering Information about Value Density"

      See this [HowTo](../../howto/gathering_info/value_density.md) for advice on gathering information about the Value Density decision point.

!!! tip "See also"

    Value Density combines with [Automatability](./automatable.md) to inform 
    [Utility](./utility.md).

{% include-markdown "../../_includes/value_density_cvss_ssvc.md" %}

!!! info "User vs. System Operator"

    A “user” is anyone whose professional task is something other than the maintenance of the system or component.
    As with [*Safety Impact*](safety_impact.md), a “system operator” is anyone who is professionally responsible for
    the proper operation or maintenance of a system.

!!! example "Diffuse"

    Examples of systems with diffuse value are email accounts, most consumer online banking accounts, common cell
    phones, and most personal computing resources owned and maintained by users.

!!! example "Concentrated"

    Examples of concentrated value are database systems, Kerberos
    servers, web servers hosting login pages, and cloud service
    providers. However, usefulness and uniqueness of the resources on
    the vulnerable system also inform value density. For example,
    encrypted mobile messaging platforms may have concentrated value,
    not because each phone’s messaging history has a particularly large
    amount of data, but because it is uniquely valuable to law
    enforcement.
