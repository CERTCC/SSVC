# Automatable

{% include-markdown "../../_generated/decision_points/automatable.md" %}

!!! tip "See also"

    Automatable combines with [Value Density](./value_density.md) to inform 
    [Utility](./utility.md)


[*Automatable*](#automatable) captures the answer to the question “Can an attacker reliably automate creating exploitation events for this vulnerability?”

!!! question "What are Steps 1-4 of the Kill Chain?"

    These steps are (1) reconnaissance, (2) weaponization, (3) delivery, and (4) exploitation.

!!! question "When is Automatable *no*?"

    Reasons why a step may not be reliably automatable could include the following:
    
    1. the vulnerable component is not searchable or enumerable on the network
    2. weaponization may require human direction for each target
    3. delivery may require channels that widely deployed network security configurations block
    4. exploitation is not reliable, due to exploit-prevention techniques (e.g., ASLR) enabled by default
    

!!! question "When is Automatable *yes*?"

    If the vulnerability allows remote code execution or command injection, the expected response should be yes.


Due to vulnerability chaining, there is some nuance as to whether reconnaissance can be automated.

!!! example "Vulnerability Chaining"

    For example, consider a vulnerability A.
    If the systems vulnerable to A are usually not openly connected to incoming traffic (that is, [*Exposure*](#exposure) is [small](#exposure) or [controlled](#exposure)), reconnaissance probably cannot be automated (scans would be blocked, etc.). This would make Automatable equal to [no](#automatable) for vulnerability A.
    However, suppose that another vulnerability B where Automatable is equal to [yes](#automatiability) can be reliably used to chain to vulnerability A.
    This automates the _reconnaissance_ of vulnerable systems.
    In this situation, the analyst should continue to analyze vulnerability A to understand whether the remaining steps in the kill chain can be automated.

!!! tip "Gathering Information About Automatable"

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

## Prior Versions


{% include-markdown "../../_generated/decision_points/virulence_1_0_0.md" %}

!!! warning "Virulence is Superseded by Automatable"

    Virulence is superseded by Automatable, which clarified the concept we 
    we were attempting to capture. 
    