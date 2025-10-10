# Automatable (SSVC)

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.automatable import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

!!! tip "Gathering Information about Automatable"

      See this [HowTo](../../howto/gathering_info/automatable.md) for advice on gathering information about the Automatable decision point.

{% include-markdown "../../_includes/default_automatable_values.md" %}

!!! tip "See also"

    Automatable combines with [Value Density](./value_density.md) to inform 
    [Utility](./utility.md)

{% include-markdown "../../_includes/automatable_cvss_ssvc.md" %}

*Automatable* captures the answer to the question “Can an attacker reliably automate creating exploitation events for this vulnerability?”

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
    If the systems vulnerable to A are usually not openly connected to incoming traffic (that is, [Exposure](system_exposure.md) is [small](system_exposure.md) or [controlled](system_exposure.md)), reconnaissance probably cannot be automated (scans would be blocked, etc.). This would make Automatable equal to [no](automatable.md) for vulnerability A.
    However, suppose that another vulnerability B where Automatable is equal to _yes_ can be reliably used to chain to vulnerability A.
    This automates the _reconnaissance_ of vulnerable systems.
    In this situation, the analyst should continue to analyze vulnerability A to understand whether the remaining steps in the kill chain can be automated.

## Prior Versions

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.automatable import VERSIONS
from ssvc.doc_helpers import prior_version, example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\n---\n")
```

!!! warning "*Virulence* is Superseded by *Automatable*"

    *Virulence* is superseded by *Automatable*, which clarified the concept we 
    we were attempting to capture. 
