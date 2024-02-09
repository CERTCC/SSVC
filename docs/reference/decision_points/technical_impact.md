# Technical Impact

{% include-markdown "../../_generated/decision_points/technical_impact.md" %}

When evaluating [*Technical Impact*](technical_impact.md), recall the scope definition in the [Scope Section](../../topics/scope.md).
Total control is relative to the affected component where the vulnerability resides.
If a vulnerability discloses authentication or authorization credentials to the system, this information disclosure should also be scored as “total” if those credentials give an adversary total control of the component.

As mentioned in [Current State of Practice](../../topics/state_of_practice.md), the scope of SSVC is just those situations in which there is a vulnerability.
Our definition of **vulnerability** is based on the determination that some security policy is violated.
We consider a security policy violation to be a technical impact—or at least, a security policy violation must have some technical instantiation.
Therefore, if there is a vulnerability then there must be some technical impact.


!!! tip "Gathering Information About Technical Impact"

    Assessing [*Technical Impact*](technical_impact.md) amounts to assessing the degree of control over the vulnerable component the attacker stands to gain by exploiting the vulnerability.
    One way to approach this analysis is to ask whether the control gained is *total* or not.
    If it is not total, it is *partial*.
    If an answer to one of the following questions is _yes_, then control is *total*.
    After exploiting the vulnerability,
 
    - can the attacker install and run arbitrary software?
    - can the attacker trigger all the actions that the vulnerable component can perform?
    - does the attacker get an account with full privileges to the vulnerable component (administrator or root user accounts, for example)?

    This list is an evolving set of heuristics.
    If you find a vulnerability that should have [*total*](technical_impact.md)  [*Technical Impact*](technical_impact.md) but that does not answer yes to any of these questions, please describe the example and what question we might add to this list in an issue on the [SSVC GitHub](https://github.com/CERTCC/SSVC/issues).

