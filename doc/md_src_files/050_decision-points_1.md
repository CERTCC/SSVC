# Likely Decision Points and Relevant Data

We propose the following decision points and associated values should be a factor when making decisions about vulnerability prioritization. Each decision point is tagged with the stakeholder it is relevant to: deployers, suppliers, or both. We emphasize that these descriptions are hypotheses to be further tested and validated. We made every effort to put forward informed and useful decision frameworks with wide applicability, but the goal of this paper is more to solicit feedback than make a declaration. We welcome questions, constructive criticism, refuting evidence, or supporting evidence about any aspect of this proposal.

One important omission from the values for each category is an “unknown” option. Instead, we recommend explicitly identifying an option that is a reasonable assumption based on prior events. Such an option requires reliable historical evidence for what tends to be the case; of course, future events may require changes to these assumptions over time.  Therefore, our assumptions require evidence and are open to debate in light of new evidence. Different risk tolerance or risk discounting postures are not addressed in the current work; accommodating such tolerance or discounting explicitly is an area for future work. This flexibility fits into our overall goal of supplying a decision-making framework that is both transparent and fits the needs of different communities. Resisting an “unknown” option discourages the modeler from silently embedding these assumptions in their choices for how the decision tree flows below the selection of any “unknown” option.

We propose satisfactory decision points for vulnerability management in the next sections, in no particular order.

## Exploitation
> Evidence of Active Exploitation of a Vulnerability

The intent of this measure is the present state of exploitation of the vulnerability. The intent is not to predict future exploitation but only to acknowledge the current state of affairs. Predictive systems, such as EPSS, could be used to augment this decision or to notify stakeholders of likely changes [@jacobs2019exploit].

| | Table 4: Exploitation Decision Values |
| --- | --------------------------------- |
| None | There is no evidence of active exploitation and no public proof of concept (PoC) of how to exploit the vulnerability. |
| PoC <br /> (Proof of Concept) | One of the following cases is true: (1) exploit code sold or traded on underground or restricted fora; (2) typical public PoC in places such as Metasploit or ExploitDB; or (3) the vulnerability has a well-known method of exploitation. Some examples of condition (3) are open-source web proxies serve as the PoC code for how to exploit any vulnerability in the vein of improper validation of TLS certificates. As another example, Wireshark serves as a PoC for packet replay attacks on ethernet or WiFi networks. |
| Active | Shared, observable, reliable evidence that the exploit is being used in the wild by real attackers; there is credible public reporting. |


### Gathering Information About Exploitation
[@householder2020historical] presents a method for searching the GitHub repositories of open-source exploit databases.
This method could be leveraged to provide some information about whether [PoC](#exploitation) is true.
However, part (3) of [PoC](#exploitation) would not be represented in such a search, so more information gathering would be needed.
For part (3), perhaps we could construct a mapping of CWE-IDs which always represent vulnerabilities with well-known methods of exploitation.
For example, CWE-295, [Improper Certificate Validation
](https://cwe.mitre.org/data/definitions/295.html), and its child CWEs, describe improper validation of TLS certificates.
These CWE-IDs could always be marked as [PoC](#exploitation) since that meets condition (3) in the definition.
A comprehensive set of suggested CWE-IDs for this purpose is future work.

Gathering information for [active](#exploitation) is a bit harder.
If the vulnerability has a name or public identifier such as a CVE-ID, a search of news websites, twitter, the vendor's vulnerability description, and public vulnerability databases for mentions of exploitation is generally adequate.
However, if the organization has the ability to detect exploitation attempts -- say through reliable and precise IDS signatures based on a public PoC -- then detection of exploitation attempts also signals that [active](#exploitation) is the right choice.

The description for [none](#exploitation) says there is no **evidence** of exploitation.
This framing admits that an analyst may not be able to detect or know about every attack.
An analyst should feel comfortable selecting [none](#exploitation) if they (or their search scripts) have performed searches in the appropriate places for public PoCs and active exploitation (as described above) and found none.
Acknowledging that [*Exploitation*](#exploitation) values can change relatively quickly, we recommend conducting these searches frequently -- if they can be automated to the organization's satisfaction, perhaps once a day (see also [Guidance on Communicating Results](#guidance-on-communicating-results)).  

## Technical Impact
> Technical Impact of Exploiting the Vulnerability

When evaluating [*Technical Impact*](#technical-impact), recall the scope definition in the [Scope Section](#scope).
Total control is relative to the affected component where the vulnerability resides.
If a vulnerability discloses authentication or authorization credentials to the system, this information disclosure should also be scored as “total” if those credentials give an adversary total control of the component.

As mentioned in [Section 2](#current-state-of-practice), the scope of SSVC is just those situations in which there is a vulnerability.
The definition of **vulnerability** we go by is based on the determination that some security policy is violated.
We consider a security policy violation to be a technical impact -- or at least, a security policy violation must have some technical instantiation.
Therefore, if there is a vulnerability then there must be some technical impact.


|  |  Table 5: Technical Impact Decision Values |
| ------- | -------------- |
| Partial | The exploit gives the adversary *limited* control over, or information exposure about, the behavior of the software that contains the vulnerability. Or the exploit gives the adversary an importantly low stochastic opportunity for total control. In this context, “low” means that the attacker cannot reasonably make enough attempts to overcome the low chance of each attempt not working. Denial of service is a form of limited control over the behavior of the vulnerable component. |
| Total   | The exploit gives the adversary *total* control over the behavior of the software, or it gives total disclosure of all information on the system that contains the vulnerability       |


### Gathering Information About Technical Impact

Assessing [*Technical Impact*](#technical-impact) amounts to assessing the degree of control the vulnerability gives an attacker over the vulnerable component.
One way to approach this analyiss is to ask whether the control gained is *total* or not.
If it is not total, it is *partial*.
If an answer to one of the following questions is yes, then control is *total*:
 - Can the attacker install and run arbitrary software?
 - Can the attacker trigger all the actions that the vulnerable component can perform?
 - Does the attacker get an account with full privileges to the vulnerable component (administrator or root user accounts, for example)?

This list is an evolving set of heuristics.
If you find a vulnerability that should have [*total*](#technical-impact)  [*Technical Impact*](#technical-impact) but that does not answer yes to any of these questions, please describe the example and what question we might add to this list in an issue on the [SSVC GitHub](https://github.com/CERTCC/SSVC/issues). 

## Utility
> The Usefulness of the Exploit to the Adversary

[*Utility*](#utility) estimates an adversary's benefit compared to their effort based on the assumption that they can exploit the vulnerability.
[*Utility*](#utility) is independent from the state of [*Exploitation*](#exploitation), which measures whether a set of adversaries have ready access exploit code to or are in fact exploiting the vulnerability.
In economics terms, [*Exploitation*](#exploitation) measures whether the **capital cost** of producing reliable exploit code has been paid or not.
[*Utility*](#utility) estimates the **marginal cost** of each exploitation event.
More plainly, [*Utility*](#utility) is about how much an adversary might benefit from a campaign using the vulnerability in question, whereas [*Exploitation*](#exploitation) is about how easy it would be to start such a campaign or if one is already underway.


Heuristically, we base [*Utility*](#utility) on a combination of value density of vulnerable components and whether potential exploitation is automatable.
This framing makes it easier to analytically derive these categories from a description of the vulnerability and the affected component.
[*Automatable*](#automatable) as ([*no*](#automatable) or [*yes*](#automatable)) and [*Value Density*](#value-density) as ([*diffuse*](#value-density) or [*concentrated*](#value-density)) are defined in Sections 4.4.3.1 and 4.4.3.2.

Roughly, [*Utility*](#utility) is a combination of two things: (1) the value of each exploitation event and (2) the ease and speed with which the adversary can cause exploitation events. We define [*Utility*](#utility) as laborious, efficient, or super effective, as described in Table 6. Table 7 is an equivalent expression of [*Utility*](#utility) more like a lookup table a program might use.

|  | Table 6: Utility Decision Values |
| --------------- | ------------------------------------------------------------------------------ |
| Laborious       | *No* to automatable and diffuse value                                               |
| Efficient       | {*Yes* to automatable and diffuse value} OR {*No* to automatable and concentrated value} |
| Super Effective | *Yes* to automatable and concentrated value                                         |

Table 7: Utility to the Adversary, as a Combination of automatable and Value Density

| *Automatable* | *Value Density* | *Utility* |
| ----------- | --------------- |       --: |
| *no*  | *diffuse*   | laborious |
| *no*  | *concentrated* | efficient |
| *yes* | *diffuse*   | efficient |
| *yes* | *concentrated* | super effective |



### Automatable

[*Automatable*](#automatable) captures the answer to the question "Can an attacker reliably automate creating exploitation events for this vulnerability?" The metric can take the values *no* or *yes*:

  - [*no*](#automatable): Attackers cannot reliably automate steps 1-4 of the kill chain
    [@hutchins2011intelligence] for this vulnerability for some reason. These
    steps are reconnaissance, weaponization, delivery, and exploitation. Example
    reasons for why a step may not be reliably automatable include
    - (1) the vulnerable component is not searchable or enumerable on the network,
    - (2) weaponization may require human direction for each target,
    - (3) delivery may require channels that widely deployed network security configurations block, and
    - (4) exploitation is not reliable, due to exploit-prevention techniques enabled by default; ASLR is an example of an exploit-prevention tool.

  - [*yes*](#automatable): Attackers can reliably automate steps 1-4 of the of the kill chain.
    If the vulnerability allows remote code execution or command injection, the expected response should be yes.

Due to vulnerability chaining, there is some nuance as to whether reconnaissance can be automated. For example, consider a vulnerability A. If the systems vulnerable to A are usually not openly connected to incoming traffic ([*Exposure*](#exposure) is [small](#exposure) or [controlled](#exposure)), reconnaissance probably cannot be automated (as scans should be blocked, etc.). This fact would make automatable [no](#automatable). However, if another vulnerability B with a [yes](#automatiability) to automatable can be reliably used to chain to vulnerability A, then that automates reconnaissance of vulnerable systems. In such a situation, the analyst should continue to analyze vulnerability A to understand whether the remaining steps in the kill chain can be automated.

#### Gathering Information About Automatable


Like all SSVC decision points, [*Automatable*](#automatable) should capture the analyst's best understanding of plausible scenarios at the time of the analysis.
An answer of *no* does not mean that it is absolutely inconceivable to automate exploitation in any scenario.
It means the analyst is not able to sketch a plausible path through all four kill chain steps.  
Code that demonstrably automates all four kill chain steps certainly satisfies as a sketch.
We say sketch to indicate that plausible arguments, such as convincing psuedocode of an automation pathway for each step, are also adequate evidence in favor of a *yes* to  [*Automatable*](#automatable).


### Value Density

[*Value Density*](#value-density) is described as diffuse or concentrated:

  - [*diffuse*](#value-density): The system that contains the vulnerable component has
    limited resources. That is, the resources that the adversary will
    gain control over with a single exploitation event are relatively
    small. Examples of systems with diffuse value are email accounts,
    most consumer online banking accounts, common cell phones, and most
    personal computing resources owned and maintained by users. (A
    “user” is anyone whose professional task is something other than
    the maintenance of the system or component. As with [*Safety Impact*](#safety-impact),
    a “system operator” is anyone who is professionally responsible for
    the proper operation or maintenance of a system.)

  - [*concentrated*](#value-density): The system that contains the vulnerable component
    is rich in resources. Heuristically, such systems are often the
    direct responsibility of “system operators” rather than users.
    Examples of concentrated value are database systems, Kerberos
    servers, web servers hosting login pages, and cloud service
    providers. However, usefulness and uniqueness of the resources on
    the vulnerable system also inform value density. For example,
    encrypted mobile messaging platforms may have concentrated value,
    not because each phone’s messaging history has a particularly large
    amount of data, but because it is uniquely valuable to law
    enforcement.

#### Gathering Information About Value Density

### Alternative Utility Outputs

Alternative heuristics for proxying adversary utility are plausible. One such example is the value the vulnerability would have were it sold on the open market. Some firms, such as [Zerodium](https://zerodium.com/program.html), make such pricing structures public. The valuable exploits track the automatable and value density heuristics for the most part. Within a single system—whether it is Apache, Windows, iOS or WhatsApp—more automated kill chain steps successfully leads to higher exploit value. Remote code execution with sandbox escape and without user interaction are the most valuable exploits, and those features describe automation of the relevant kill chain steps. How equivalently virulent exploits for different systems are priced relative to each other is more idiosyncratic. Price does not only track value density of the system, but presumably also the existing supply of exploits and the installation distribution among the targets of Zerodium’s customers. Currently, we simplify the analysis and ignore these factors.
However, future work should look for and prevent large mismatches between the outputs of the [*Utility*](#utility) decision point and the exploit markets.
