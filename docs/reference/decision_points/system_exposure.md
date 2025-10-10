# System Exposure

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.system_exposure import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

!!! tip "Gathering Information about System Exposure"

      See this [HowTo](../../howto/gathering_info/system_exposure.md) for advice on gathering information about the System Exposure decision point.

{% include-markdown "../../_includes/default_system_exposure_values.md" %}

Measuring the attack surface precisely is difficult, and we do not propose to perfectly delineate between small and controlled access.
Exposure should be judged against the system in its deployed context, which may differ from how it is commonly expected to be deployed.
For example, the exposure of a device on a vehicle's CAN bus will vary depending on the presence of a cellular telemetry device on the same bus.

If a vulnerability cannot be remediated, other mitigations may be used.
Usually, the effect of these mitigations is to reduce exposure of the vulnerable component.
Therefore, a deployer’s response to Exposure may change if such mitigations are put in place.
If a mitigation changes exposure and thereby reduces the priority of a vulnerability, that mitigation can be considered a success.
Whether that mitigation allows the deployer to defer further action varies according to each case.

## Prior Versions

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.system_exposure import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\n---\n")
```
