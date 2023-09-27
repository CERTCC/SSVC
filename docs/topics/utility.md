# Utility

!!! note "Utility"

    <a name="table-utility"></a>
    The Usefulness of the Exploit to the Adversary
    
    | *Automatable* | *Value Density* | *Utility* |
    | ----------- | --------------- |       --: |
    | *no*  | *diffuse*   | laborious |
    | *no*  | *concentrated* | efficient |
    | *yes* | *diffuse*   | efficient |
    | *yes* | *concentrated* | super effective |

{== TODO note that this is a compound decision point, therefore it is a notational convenience ==}

[*Utility*](#utility) estimates an adversary's benefit compared to their effort based on the assumption that they can exploit the vulnerability.
[*Utility*](#utility) is independent from the state of [*Exploitation*](../reference/decision_points/exploitation.md), which measures whether a set of adversaries have ready access to exploit code or are in fact exploiting the vulnerability.
In economic terms, [*Exploitation*](../reference/decision_points/exploitation.md) measures whether the **capital cost** of producing reliable exploit code has been paid or not.
[*Utility*](#utility) estimates the **marginal cost** of each exploitation event.
More plainly, [*Utility*](#utility) is about how much an adversary might benefit from a campaign using the vulnerability in question, whereas [*Exploitation*](../reference/decision_points/exploitation.md) is about how easy it would be to start such a campaign or if one is already underway.

Heuristically, we base Utility on a combination of the value density of vulnerable components and whether potential exploitation is automatable.
This framing makes it easier to analytically derive these categories from a description of the vulnerability and the affected component.
[*Automatable*](../reference/decision_points/automatable.md) as ([*no*](../reference/decision_points/automatable.md) or [*yes*](../reference/decision_points/automatable.md)) and [*Value Density*](../reference/decision_points/value_density.md) as ([*diffuse*](../reference/decision_points/value_density.md) or [*concentrated*](../reference/decision_points/value_density.md)) define those decision points.

Roughly, [*Utility*](#utility) is a combination of two things: (1) the value of each exploitation event and (2) the ease and speed with which the adversary can cause exploitation events.
We define [*Utility*](#utility) as laborious, efficient, or super effective, as described in the [table](#table-utility) above.


## Alternative Utility Outputs

Alternative heuristics can plausibly be used as proxies for adversary utility.
One example is the value of the vulnerability if it were sold on the open market.
Some firms, such as [Zerodium](https://zerodium.com/program.html), make such pricing structures public.
The valuable exploits track the [*Automatable*](../reference/decision_points/automatable.md) and [*Value Density*](../reference/decision_points/value_density.md) heuristics for the most part.
Within a single system—whether it is Apache, Windows, iOS or WhatsApp—more successfully automated steps in the kill lead to higher exploit value.
Remote code execution with sandbox escape and without user interaction are the most valuable exploits, and these features describe automation of the relevant kill chain steps.

How equivalently [*Automatable*](../reference/decision_points/automatable.md) exploits for different systems are priced relative to each other is more idiosyncratic.
Price does not only track the [*Value Density*](../reference/decision_points/value_density.md) of the system, but presumably also the existing supply of exploits and the installation distribution among the targets of Zerodium’s customers.
Currently, we simplify the analysis and ignore these factors.
However, future work should look for and prevent large mismatches between the outputs of the [*Utility*](#utility) decision point and the exploit markets.
