# Utility

!!! note "Utility"

    The Usefulness of the Exploit to the Adversary
    
    | *Automatable* | *Value Density* | *Utility* |
    | ----------- | --------------- |       --: |
    | *no*  | *diffuse*   | laborious |
    | *no*  | *concentrated* | efficient |
    | *yes* | *diffuse*   | efficient |
    | *yes* | *concentrated* | super effective |

{== TODO note that this is a compound decision point, therefore it is a notational convenience ==}

[*Utility*](#utility) estimates an adversary's benefit compared to their effort based on the assumption that they can exploit the vulnerability.
[*Utility*](#utility) is independent from the state of [*Exploitation*](#exploitation), which measures whether a set of adversaries have ready access to exploit code or are in fact exploiting the vulnerability.
In economic terms, [*Exploitation*](#exploitation) measures whether the **capital cost** of producing reliable exploit code has been paid or not.
[*Utility*](#utility) estimates the **marginal cost** of each exploitation event.
More plainly, [*Utility*](#utility) is about how much an adversary might benefit from a campaign using the vulnerability in question, whereas [*Exploitation*](#exploitation) is about how easy it would be to start such a campaign or if one is already underway.

Heuristically, we base Utility on a combination of the value density of vulnerable components and whether potential exploitation is automatable.
This framing makes it easier to analytically derive these categories from a description of the vulnerability and the affected component.
[*Automatable*](#automatable) as ([*no*](#automatable) or [*yes*](#automatable)) and [*Value Density*](#value-density) as ([*diffuse*](#value-density) or [*concentrated*](#value-density)) define those decision points.

Roughly, [*Utility*](#utility) is a combination of two things: (1) the value of each exploitation event and (2) the ease and speed with which the adversary can cause exploitation events. We define [*Utility*](#utility) as laborious, efficient, or super effective, as described in [Utility Decision Values](#table-utility). [The next table](#table-utility-2) is an equivalent expression of [*Utility*](#utility) that resembles a lookup table in a program.



## Alternative Utility Outputs

Alternative heuristics can plausibly be used as proxies for adversary utility.
One example is the value of the vulnerability if it were sold on the open market.
Some firms, such as [Zerodium](https://zerodium.com/program.html), make such pricing structures public.
The valuable exploits track the [*Automatable*](#automatable) and [*Value Density*](#value-density) heuristics for the most part.
Within a single system—whether it is Apache, Windows, iOS or WhatsApp—more successfully automated steps in the kill lead to higher exploit value.
Remote code execution with sandbox escape and without user interaction are the most valuable exploits, and these features describe automation of the relevant kill chain steps.

How equivalently [*Automatable*](#automatable) exploits for different systems are priced relative to each other is more idiosyncratic.
Price does not only track the [*Value Density*](#value-density) of the system, but presumably also the existing supply of exploits and the installation distribution among the targets of Zerodium’s customers.
Currently, we simplify the analysis and ignore these factors.
However, future work should look for and prevent large mismatches between the outputs of the [*Utility*](#utility) decision point and the exploit markets.
