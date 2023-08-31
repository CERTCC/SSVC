!!! note "System Exposure"

    The Accessible Attack Surface of the Affected System or Service

    | Value       | Description |
    | :---        | :------------ |
    | Small       | Local service or program; highly controlled network       |
    | Controlled  | Networked service with some access restrictions or mitigations already in place (whether locally or on the network). A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable both reliably and quickly enough to respond. *Controlled* covers the situation in which a vulnerability can be exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably execute it, then *exposure* should be *small*. |
    | Open        | Internet or another widely accessible network where access cannot plausibly be restricted or controlled (e.g., DNS servers, web servers, VOIP servers, email servers)  |

Measuring the attack surface precisely is difficult, and we do not propose to perfectly delineate between small and controlled access.
Exposure should be judged against the system in its deployed context, which may differ from how it is commonly expected to be deployed.
For example, the exposure of a device on a vehicle's CAN bus will vary depending on the presence of a cellular telemetry device on the same bus.

If a vulnerability cannot be remediated, other mitigations may be used.
Usually, the effect of these mitigations is to reduce exposure of the vulnerable component.
Therefore, a deployer’s response to Exposure may change if such mitigations are put in place.
If a mitigation changes exposure and thereby reduces the priority of a vulnerability, that mitigation can be considered a success.
Whether that mitigation allows the deployer to defer further action varies according to each case.


### Gathering Information About System Exposure

[*System Exposure*](#system-exposure) is primarily used by Deployers, so the question is about whether some specific system is in fact exposed, not a hypothetical or aggregate question about systems of that type.
Therefore, it generally has a concrete answer, even though it may vary from vulnerable component to vulnerable component, based on their respective configurations.

[*System Exposure*](#system-exposure) can be readily informed by network scanning techniques.
For example, if the vulnerable component is visible on [Shodan](www.shodan.io) or by some other external scanning service, then it is [*open*](#system-exposure).
Network policy or diagrams are also useful information sources, especially for services intentionally open to the Internet such as public web servers.
An analyst should also choose [*open*](#system-exposure) for a phone or PC that connects to the web or email without the usual protections (IP and URL blocking, updated firewalls, etc.).

Distinguishing between [*small*](#system-exposure) and [*controlled*](#system-exposure) is more nuanced.
If [*open*](#system-exposure) has been ruled out, some suggested heuristics for differentiating the other two are as follows.
Apply these heuristics in order and stop when one of them applies.
 - If the system's networking and communication interfaces have been physically removed or disabled, choose [*small*](#system-exposure).
 - If [*Automatable*](#automatable) is [*yes*](#automatable), then choose [*controlled*](#system-exposure). The reasoning behind this heuristic is that if reconnaissance through exploitation is automatable, then the usual deployment scenario exposes the system sufficiently that access can be automated, which contradicts the expectations of [*small*](#system-exposure).
 - If the vulnerable component is on a network where other hosts can browse the web or receive email, choose [*controlled*](#system-exposure).
 - If the vulnerable component is in a third party library that is unreachable because the feature is unused in the surrounding product, choose [*small*](#system-exposure).

The unreachable vulnerable component scenario may be a point of concern for stakeholders like patch suppliers who often find it more cost-effective to simply update the included library to an existing fixed version rather than try to explain to customers why the vulnerable code is unreachable in their own product.
In those cases, we suggest the stakeholder reviews the decision outcomes of the tree to ensure the appropriate action is taken (paying attention to [_defer_](#supplier-tree) vs [_scheduled_](#supplier-tree), for example).

If you have suggestions for further heuristics, or potential counterexamples to these,  please describe the example and reasoning in an issue on the [SSVC GitHub](https://github.com/CERTCC/SSVC/issues).
