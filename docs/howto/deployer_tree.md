# Prioritizing Patch Deployment

Here we describe an example decision model for a Deployer deciding the priority of deploying a patch for a vulnerability
in their infrastructure.

!!! info "Deployer Patch Deployment Priority"

    As noted in [Enumerating Decisions](../topics/enumerating_decisions.md), the root of a decision model's identity is
    the combination of the stakeholder and the decision being modeled. In this case, the stakeholder is the **Deployer** and the
    decision is the **priority of deploying a patch**.

## Deployer Units of Work

!!! info inline end "Deployer Unit of Work"

    The unit of work for a Deployer is usually a single deployable patch or patch bundle such as a service pack.

Deployers are usually in the position of receiving remediations or mitigations from their [Suppliers](supplier_tree.md)
for products they have deployed.
They must then decide whether to deploy the remediation or mitigation to a particular instance (or not).
Whether they have the option of deploying only part of a remediation such as a fix bundle depends on whether the
Supplier has engineered their release process to permit that degree of flexibility.
For example, if service packs are fix bundles, the Supplier might choose to release individually deployable fixes as well.

The vulnerability management process for deployers has at its core the collation of data including

!!! tip inline end "Relationship to asset management"

    The relationship between SSVC and asset management is discussed further in [SSVC and Asset Management](../topics/asset_management.md).

- an inventory of deployed instances of product versions
- a mapping of vulnerabilities to remediations or mitigations
- a mapping of remediations and/or mitigations to product versions

The first must be collected by the Deployer, while the latter two most often originate from the product Supplier.
Managing this information is generally called **asset management**.

In turn, Deployers must resolve this information into specific actions in which a remediation or mitigation is slated
for deployment to replace or modify a particular instance of the product.
The Deployer model described below considers the mission and safety risks inherent to the category of systems to which those
deployed instances belong.
For this reason, we recommend that the pairing of remediation or mitigation to a product version instance constitutes
the unit of work most appropriate for the Deployer.

## Deployer Decision Outcomes

A deployer's decision centers on with what priority to deploy a given remediation or mitigation to their infrastructure.
Similar to the [Supplier](supplier_tree.md) case, we consider four categories of priority, as outlined in the table below.
While we've used the same priority names, the meaning of the priority may have different implications for the deployer than for the supplier.

```python exec="true" idprefix=""
from ssvc.decision_tables.ssvc.deployer_dt import LATEST as DT
from ssvc.doc_helpers import example_block

dp = DT.decision_points[DT.outcome]
print(example_block(dp))
```

A more specific interpretation for the priority levels for deployers is as follows:

| Deployer Priority | Description |
| :---              | :----------  |
| Defer            | Do not act at present. |
| Scheduled        | Act during regularly scheduled maintenance time. |
| Out-of-cycle     | Act more quickly than usual to apply the mitigation or remediation out-of-cycle, during the next available opportunity, working overtime if necessary. |
| Immediate        | Act immediately; focus all resources on applying the fix as quickly as possible, including, if necessary, pausing regular organization operations. |

When remediation is available, usually the action is to apply it.
When remediation is not yet available, the action space is more diverse, but it should involve mitigating the vulnerability
(e.g., shutting down services or applying additional security controls) or accepting the risk of not mitigating the vulnerability.

Applying mitigations may change the value of decision points.
A mitigation that successfully changes the value of a decision point may shift the priority of further action to a
reduced state.
If applying a mitigation reduces the priority to *defer*, the deployer may not need to apply a remediation if it later
becomes available.

!!! example "Mitigation Examples"

     - An effective firewall or IDS rule coupled with an adequate change control process for rules may change
     [*System Exposure*](../reference/decision_points/system_exposure.md) from open to controlled. This could be enough
     to reduce the priority where no further action is necessary.
     - In the area of Financial [*Safety Impact*](../reference/decision_points/safety_impact.md), a better insurance policy may be purchased, providing necessary fraud insurance.
     - Physical [*Safety Impact*](../reference/decision_points/safety_impact.md) may be reduced by testing the
     physical barriers designed to restrict a robot's ability to interact with humans.
     - [*Mission Impact*](../reference/decision_points/mission_impact.md) could be reduced by correcting the problems identified in a disaster recover test-run of the alternate business flow.

However, mitigation techniques will not always be adequate to address the risk posed by the vulnerability.

!!! example "Examples of Inadequate Mitigation"

    - The implementation of a firewall or IDS rule to mitigate [*System Exposure*](../reference/decision_points/system_exposure.md) from 
    open to controlled is only valid until someone changes the rule. 
    - In the area of Financial impacts, the caps on the insurance may be too low to act as a mitigation.
    - The Physical impact may be increased by incorrect installation of the physical barriers designed to restrict a
    robot’s ability to interact with humans.
    - The [*Mission Impact*](../reference/decision_points/mission_impact.md) could be increased when a disaster recovery test-run identifies problems
    with an alternate business flow.
    - The mitigating action may not be permanent or work as designed.

As opposed to mitigation, applying a remediation finishes an SSVC analysis of a deployed system.

!!! warning "Remediation is not a final state"

    While specific vulnerabilities in specific systems can be remediated, the vulnerability cannot be 'disposed of' or 
    eliminated from future consideration within an IT environment.
    Since software and systems are dynamic, a single vulnerability can be re-introduced after initial remediation 
    through updates, software rollbacks, or other systemic actions that change the operating conditions within an environment.
    It is therefore important to continually monitor remediated environments for vulnerabilities reintroduced by 
    either rollbacks or new deployments of outdated software.

## Deployer Decision Points

The Deployer Patch Deployment Priority decision model uses the following decision points:

- [*Exploitation*](../reference/decision_points/exploitation.md) - A vulnerability with known exploitation is more likely to be given a higher priority.
- [*System Exposure*](../reference/decision_points/system_exposure.md) - The more exposed a system is, the more likely it is to be given a higher priority.
- [*Utility*](../reference/decision_points/utility.md) - The more useful a vulnerability is to an attacker, the more likely it is to be given a higher priority.
- [*Human Impact*](../reference/decision_points/human_impact.md) - The more severe the human (safety, mission) impact of a vulnerability, the more likely it is to be given a higher priority.

More detail about each of these decision points is provided at the links above, here we provide a brief summary of each.

```python exec="true" idprefix=""
from ssvc.decision_tables.ssvc.deployer_dt import LATEST as DT
from ssvc.doc_helpers import example_block

for dp in [v for k,v in DT.decision_points.items() if k != DT.outcome]:
    print(example_block(dp))
```

In the *Human Impact* table above, *MEF* stands for Mission Essential Function.

## Deployer Decision Model

Below we provide an example deployer prioritization policy that maps the decision points just listed to the outcomes described above.

!!! tip "Notes on the Deployer Decision Model Example Policy"

    In the example policy shown below:

    - An [_active_](../reference/decision_points/exploitation.md) state of [*Exploitation*](../reference/decision_points/exploitation.md) will never result in a *defer* priority.
    - A [_none_](../reference/decision_points/exploitation.md) state of [*Exploitation*](../reference/decision_points/exploitation.md) (no evidence of exploitation) will result in either *defer* or *scheduled* priority—unless the state of [*Human Impact*](../reference/decision_points/human_impact.md) is [_very high_](../reference/decision_points/human_impact.md), resulting in an *out-of-cycle* priority.

### Decision Model Visualization

The following diagram shows the decision model for the deployer decision.

```python exec="true" idprefix=""
from ssvc.decision_tables.ssvc.deployer_dt import LATEST as DT
from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt

rows = DT.mapping
title = mermaid_title_from_dt(DT)
print(mapping2mermaid(rows, title=title))
```

### Table of Values

The table below shows the values for the decision model.
Each row of the table corresponds to a path through the decision model diagram above.

```python exec="true" idprefix=""

from ssvc.decision_tables.ssvc.deployer_dt import LATEST as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```
