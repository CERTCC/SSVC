## Automatable

[*Automatable*](#automatable) captures the answer to the question “Can an attacker reliably automate creating exploitation events for this vulnerability?” This metric can take the values *no* or *yes*:

  - [*no*](#automatable): Attackers cannot reliably automate steps 1-4 of the kill chain
    [@hutchins2011intelligence] for this vulnerability. These
    steps are (1) reconnaissance, (2) weaponization, (3) delivery, and (4) exploitation.
    Reasons why a step may not be reliably automatable could include the following:
    1. the vulnerable component is not searchable or enumerable on the network,
    2. weaponization may require human direction for each target,
    3. delivery may require channels that widely deployed network security configurations block, and
    4. exploitation is not reliable, due to exploit-prevention techniques enabled by default; ASLR is an example of an exploit-prevention tool.

  - [*yes*](#automatable): Attackers can reliably automate steps 1-4 of the kill chain.
    If the vulnerability allows remote code execution or command injection, the expected response should be yes.

Due to vulnerability chaining, there is some nuance as to whether reconnaissance can be automated. For example, consider a vulnerability A.
If the systems vulnerable to A are usually not openly connected to incoming traffic (that is, [*Exposure*](#exposure) is [small](#exposure) or [controlled](#exposure)), reconnaissance probably cannot be automated (scans would be blocked, etc.). This would make Automatable equal to [no](#automatable) for vulnerability A.
However, suppose that another vulnerability B where Automatable is equal to [yes](#automatiability) can be reliably used to chain to vulnerability A.
This automates the _reconnaissance_ of vulnerable systems.
In this situation, the analyst should continue to analyze vulnerability A to understand whether the remaining steps in the kill chain can be automated.

### Gathering Information About Automatable

An analyst should be able to sketch the automation scenario and how it either does or does not satisfy each of the four kill chain steps.
Once one step is not satisfied, the analyst can stop and select [*no*](#automatable).
Code that demonstrably automates all four kill chain steps certainly satisfies as a sketch.
We say sketch to indicate that plausible arguments, such as convincing psuedocode of an automation pathway for each step, are also adequate evidence in favor of a [*yes*](#automatable) to [*Automatable*](#automatable).

Like all SSVC decision points, [*Automatable*](#automatable) should capture the analyst's best understanding of plausible scenarios at the time of the analysis.
An answer of *no* does not mean that it is absolutely inconceivable to automate exploitation in any scenario.
It means the analyst is not able to sketch a plausible path through all four kill chain steps.
“Plausible” sketches should account for widely deployed network and host-based defenses.
Liveness of Internet-connected services means quite a few overlapping things [@bano2018scanning].
For most vulnerabilities, an open port does not automatically mean that reconnaissance, weaponization, and delivery are automatable.
Furthermore, discovery of a vulnerable service is not automatable in a situation where only two hosts are misconfigured to expose the service out of 2 million hosts that are properly configured.
As discussed in in [Reasoning Steps Forward](#reasoning-steps-forward), the analyst should consider *credible* effects based on *known* use cases of the software system to be pragmatic about scope and providing values to decision points.

