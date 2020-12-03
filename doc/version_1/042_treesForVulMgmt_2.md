## Likely Decision Points and Relevant Data

We propose the following decision points and associated values should be a factor when making decisions about vulnerability prioritization. Each decision point is tagged with the stakeholder it is relevant to: deployers, suppliers, or both. We emphasize that these descriptions are hypotheses to be further tested and validated. We made every effort to put forward informed and useful decision frameworks with wide applicability, but the goal of this paper is more to solicit feedback than make a declaration. We welcome questions, constructive criticism, refuting evidence, or supporting evidence about any aspect of this proposal.

One important omission from the values for each category is an “unknown” option. Instead, we recommend explicitly identifying an option that is a reasonable assumption based on prior events. Such an option requires reliable historical evidence for what tends to be the case; of course, future events may require changes to these assumptions over time.  Therefore, our assumptions require evidence and are open to debate in light of new evidence. Different risk tolerance or risk discounting postures are not addressed in the current work; accommodating such tolerance or discounting explicitly is an area for future work. This flexibility fits into our overall goal of supplying a decision-making framework that is both transparent and fits the needs of different communities. Resisting an “unknown” option discourages the modeler from silently embedding these assumptions in their choices for how the decision tree flows below the selection of any “unknown” option.

We propose satisfactory decision points for vulnerability management in the next sections, in no particular order.

### Exploitation (Supplier, Deployer)
> Evidence of Active Exploitation of a Vulnerability

The intent of this measure is the present state of exploitation of the vulnerability. The intent is not to predict future exploitation but only to acknowledge the current state of affairs. Predictive systems, such as EPSS, could be used to augment this decision or to notify stakeholders of likely changes [@jacobs2019exploit].

| | Table 4: Exploitation Decision Values |
| --- | --------------------------------- |
| None | There is no evidence of active exploitation and no public proof of concept (PoC) of how to exploit the vulnerability. |
| PoC <br /> (Proof of Concept) | One of the following cases is true: (1) exploit code sold or traded on underground or restricted fora; (2) typical public PoC in places such as Metasploit or ExploitDB; or (3) the vulnerability has a well-known method of exploitation. Some examples of condition (3) are open-source web proxies serve as the PoC code for how to exploit any vulnerability in the vein of improper validation of TLS certificates. As another example, Wireshark serves as a PoC for packet replay attacks on ethernet or WiFi networks. |
| Active | Shared, observable, reliable evidence that the exploit is being used in the wild by real attackers; there is credible public reporting. |

### Technical Impact (Supplier)
> Technical Impact of Exploiting the Vulnerability

When evaluating *Technical Impact*, recall the scope definition above.
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

### Utility (Supplier, Deployer)
> The Usefulness of the Exploit to the Adversary

Heuristically, we base *utility* on a combination of value density of vulnerable components and automatability of potential exploitation. This framing makes it easier to analytically derive these categories from a description of the vulnerability and the affected component. Automatability (slow or rapid) and value density (diffuse or concentrated) are defined in Sections 4.4.3.1 and 4.4.3.2. Deployers currently use this feature only as a suggested constraint on the values for *Mission Impact*.
main

Roughly, *utility* is a combination of two things: (1) the value of each exploitation event and (2) the ease and speed with which the adversary can cause exploitation events. We define *utility* as laborious, efficient, or super effective, as described in Table 6.

|  | Table 6: Utility Decision Values |
| --------------- | ------------------------------------------------------------------------------ |
| Laborious       | Slow automatability and diffuse value                                               |
| Efficient       | {Rapid automatability and diffuse value} OR {Slow automatability and concentrated value} |
| Super Effective | Rapid automatability and concentrated value                                         |

#### Automatability

*Automatability* is described as slow or rapid:

  - **Slow**. Attackers cannot reliably automate steps 1-4 of the kill chain
    [@hutchins2011intelligence] for this vulnerability for some reason. These
    steps are reconnaissance, weaponization, delivery, and exploitation. Example
    reasons for why a step may not be reliably automatable include (1)
    the vulnerable component is not searchable or enumerable on the
    network, (2) weaponization may require human direction for each
    target, (3) delivery may require channels that widely deployed
    network security configurations block, and (3) exploitation may be
    frustrated by adequate exploit-prevention techniques enabled by
    default; ASLR is an example of an exploit-prevention tool.

  - **Rapid**. Attackers can reliably automate steps 1-4 of the of the kill
    chain. If the vulnerability allows remote code execution or command
    injection, the default response should be rapid.

Due to vulnerability chaining, there is some nuance as to whether reconnaissance can be automated. For example, consider a vulnerability A. If the systems vulnerable to A are usually not openly connected to incoming traffic ([*Exposure*](#exposure) is [small](#exposure) or [controlled](#exposure)), reconnaissance probably cannot be automated (as scans should be blocked, etc.). This fact would make automatability [slow](#automatability). However, if another vulnerability B with [rapid](#automatiability) automatability can be reliably used to chain to vulnerability A, then that automates reconnaissance of vulnerable systems. In such a situation, the analyst should continue to analyze vulnerability A to understand whether the remaining steps in the kill chain can be automated.

#### Value Density

*Value density* is described as diffuse or concentrated:

  - **Diffuse**. The system that contains the vulnerable component has
    limited resources. That is, the resources that the adversary will
    gain control over with a single exploitation event are relatively
    small. Examples of systems with diffuse value are email accounts,
    most consumer online banking accounts, common cell phones, and most
    personal computing resources owned and maintained by users. (A
    “user” is anyone whose professional task is something other than
    the maintenance of the system or component. As with *safety impact*,
    a “system operator” is anyone who is professionally responsible for
    the proper operation or maintenance of a system.)

  - **Concentrated**. The system that contains the vulnerable component
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

The output for the *Utility* decision point is visualized in Table 7.

Table 7: Utility to the Adversary, as a Combination of Automatability and Value Density

| *Automatability* | *Value Density* | *Utility* |
| ----------- | --------------- |       --: |
| **slow**  | **diffuse**   | laborious |
| **slow**  | **concentrated** | efficient |
| **rapid** | **diffuse**   | efficient |
| **rapid** | **concentrated** | super effective |


Alternative heuristics for proxying adversary utility are plausible. One such example is the value the vulnerability would have were it sold on the open market. Some firms, such as [Zerodium](https://zerodium.com/program.html), make such pricing structures public. The valuable exploits track the automatability and value density heuristics for the most part. Within a single system—whether it is Apache, Windows, iOS or WhatsApp—more automated kill chain steps successfully leads to higher exploit value. Remote code execution with sandbox escape and without user interaction are the most valuable exploits, and those features describe automation of the relevant kill chain steps. How equivalently virulent exploits for different systems are priced relative to each other is more idiosyncratic. Price does not only track value density of the system, but presumably also the existing supply of exploits and the installation distribution among the targets of Zerodium’s customers. Currently, we simplify the analysis and ignore these factors. However, future work should look for and prevent large mismatches between the outputs of the *utility* decision point and the exploit markets.
