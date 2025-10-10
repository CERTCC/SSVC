# Gathering Information about Automatable

``` python exec="true" idprefix=""
from ssvc.decision_points.ssvc.automatable import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

An analyst should be able to sketch the automation scenario and how it either does or does not satisfy each of the four kill chain steps.
Once one step is not satisfied, the analyst can stop and select [*no*](automatable.md).
Code that demonstrably automates all four kill chain steps certainly satisfies as a sketch.
We say sketch to indicate that plausible arguments, such as convincing psuedocode of an automation pathway for each step, are also adequate evidence in favor of a [*yes*](automatable.md) to *Automatable*.

Like all SSVC decision points, *Automatable* should capture the analyst's best understanding of plausible scenarios at the time of the analysis.
An answer of *no* does not mean that it is absolutely inconceivable to automate exploitation in any scenario.
It means the analyst is not able to sketch a plausible path through all four kill chain steps.
“Plausible” sketches should account for widely deployed network and host-based defenses.
Liveness of Internet-connected services means quite a few overlapping things [@bano2018scanning].
For most vulnerabilities, an open port does not automatically mean that reconnaissance, weaponization, and delivery are automatable.
Furthermore, discovery of a vulnerable service is not automatable in a situation where only two hosts are misconfigured to expose the service out of 2 million hosts that are properly configured.
As discussed in in [Reasoning Steps Forward](../../topics/scope.md), the analyst should consider *credible* effects based on *known* use cases of the software system to be pragmatic about scope and providing values to decision points.

{% include-markdown "../../_includes/default_automatable_values.md" %}
