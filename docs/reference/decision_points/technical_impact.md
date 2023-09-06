!!! note "Technical Impact"

    Technical Impact of Exploiting the Vulnerability

    | Value | Definition |
    | :--- | :-------------  |
    | Partial | The exploit gives the adversary *limited* control over, or information exposure about, the behavior of the software that contains the vulnerability. Or the exploit gives the adversary an importantly low stochastic opportunity for total control. In this context, “low” means that the attacker cannot reasonably make enough attempts to overcome the low chance of each attempt not working. Denial of service is a form of limited control over the behavior of the vulnerable component. |
    | Total   | The exploit gives the adversary *total* control over the behavior of the software, or it gives total disclosure of all information on the system that contains the vulnerability       |

When evaluating [*Technical Impact*](#technical-impact), recall the scope definition in the [Scope Section](#scope).
Total control is relative to the affected component where the vulnerability resides.
If a vulnerability discloses authentication or authorization credentials to the system, this information disclosure should also be scored as “total” if those credentials give an adversary total control of the component.

As mentioned in [Current State of Practice](#current-state-of-practice), the scope of SSVC is just those situations in which there is a vulnerability.
Our definition of **vulnerability** is based on the determination that some security policy is violated.
We consider a security policy violation to be a technical impact—or at least, a security policy violation must have some technical instantiation.
Therefore, if there is a vulnerability then there must be some technical impact.


!!! tip "Gathering Information About Technical Impact"

    Assessing [*Technical Impact*](#technical-impact) amounts to assessing the degree of control over the vulnerable component the attacker stands to gain by exploiting the vulnerability.
    One way to approach this analysis is to ask whether the control gained is *total* or not.
    If it is not total, it is *partial*.
    If an answer to one of the following questions is _yes_, then control is *total*.
    After exploiting the vulnerability,
 
    - can the attacker install and run arbitrary software?
    - can the attacker trigger all the actions that the vulnerable component can perform?
    - does the attacker get an account with full privileges to the vulnerable component (administrator or root user accounts, for example)?

    This list is an evolving set of heuristics.
    If you find a vulnerability that should have [*total*](#technical-impact)  [*Technical Impact*](#technical-impact) but that does not answer yes to any of these questions, please describe the example and what question we might add to this list in an issue on the [SSVC GitHub](https://github.com/CERTCC/SSVC/issues).

