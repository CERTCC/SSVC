# Gathering Information About System Exposure

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.system_exposure import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

{% include-markdown "../../_includes/default_system_exposure_values.md" %}

*System Exposure* is primarily used by [Deployers](../../deployer_tree), so the question is about whether some specific system is in fact exposed, not a hypothetical or aggregate question about systems of that type.
Therefore, it generally has a concrete answer, even though it may vary from vulnerable component to vulnerable component, based on their respective configurations.

*System Exposure* can be readily informed by network scanning techniques.
For example, if the vulnerable component is visible on [Shodan](https://www.shodan.io) or by some other external scanning service, then it is *open*.
Network policy or diagrams are also useful information sources, especially for services intentionally open to the Internet such as public web servers.
An analyst should also choose *open* for a phone or PC that connects to the web or email without the usual protections (IP and URL blocking, updated firewalls, etc.).

## *Small* versus *Controlled* System Exposure

Distinguishing between *small* and *controlled* is more nuanced.
If *open* has been ruled out, some suggested heuristics for differentiating the other two are as follows.
Apply these heuristics in order and stop when one of them applies.

- If the system's networking and communication interfaces have been physically removed or disabled, choose *small*.
- If [*Automatable*](automatable.md) is [*yes*](automatable.md), then choose *controlled*. The reasoning behind this heuristic is that if reconnaissance through exploitation is automatable, then the usual deployment scenario exposes the system sufficiently that access can be automated, which contradicts the expectations of *small*.
- If the vulnerable component is on a network where other hosts can browse the web or receive email, choose *controlled*.
- If the vulnerable component is in a third party library that is unreachable because the feature is unused in the surrounding product, choose *small*.

The unreachable vulnerable component scenario may be a point of concern for stakeholders like [patch suppliers](../../howto/supplier_tree.md) who often find it more cost-effective to simply update the included library to an existing fixed version rather than try to explain to customers why the vulnerable code is unreachable in their own product.
In those cases, we suggest the stakeholder reviews the decision outcomes of the tree to ensure the appropriate action is taken (paying attention to [*defer*](../../howto/supplier_tree.md) vs [*scheduled*](../../howto/supplier_tree.md), for example).


{% include-markdown "../../_includes/question_callout.md" heading-offset=1 %}
