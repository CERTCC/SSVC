# Deploying Patches

A mitigation that successfully changes the value of a decision point may shift the priority of further action to a reduced state. An effective firewall or IDS rule coupled with an adequate change control process for rules may be enough to reduce the priority where no further action is necessary. In the area of Financial impacts, a better insurance policy may be purchased, providing necessary fraud insurance. Physicial well-being impact may be reduced by testing the physicial barriers designed to restrict a robot's ability to interact with humans. Mission impact could be reduced by correcting the problems identified in a disaster recover test-run of the alternate business flow. If applying a mitigation reduces the priority to *defer*, the deployer may not need to apply a remediation if it later becomes available. The table below displays the action priorities for the deployer, which are similar to the supplier case.

When remediation is available, usually the action is to apply it. When remediation is not yet available, the action space is more diverse, but it should involve mitigating the vulnerability (e.g., shutting down services or applying additional security controls) or accepting the risk of not mitigating the vulnerability. Applying mitigations may change the value of decision points. For example, effective firewall and IDS rules may change [*System Exposure*](../reference/decision_points/system_exposure.md) from open to controlled. Financial well-being, a [*Safety Impact*](../reference/decision_points/safety_impact.md) category, might be reduced with adequate fraud detection and insurance. Physical well-being, also a [*Safety Impact*](../reference/decision_points/safety_impact.md) category, might be reduced by physical barriers that restrict a robot's ability to interact with humans. [*Mission Impact*](../reference/decision_points/mission_impact.md) might be reduced by introducing back-up business flows that do not use the vulnerable component. In a later section we combine [Mission and Situated Safety Impact](../reference/decision_points/human_impact.md) to reduce the complexity of the tree.

However, these mitigation techniques will not always work.

!!! example "Examples of Inadequate Mitigation"

    - The implementation of a firewall or IDS rule to mitigate [*System Exposure*](../reference/decision_points/system_exposure.md) from 
    open to controlled is only valid until someone changes the rule. 
    - In the area of Financial impacts, the caps on the insurance may be too low to act as a mitigation.
    - The Physical impact may be increased by incorrect installation of the physical barriers designed to restrict a
    robot’s ability to interact with humans.
    - The [*Mission Impact*](../reference/decision_points/mission_impact.md) could be increased when a disaster recovery test-run identifies problems
    with an alternate business flow.
    - The mitigating action may not be permanent or work as designed.

A mitigation that successfully changes the value of a decision point may shift the priority of further action to a reduced state.
If applying a mitigation reduces the priority to *defer*, the deployer may not need to apply a remediation, if later, it becomes available.
{== Table 3 ==} displays the action priorities for the deployer, which are similar to the supplier case.

In a later section, the different types of impacts are defined and then implemented in the decision trees as examples of how the various impacts affect the priority.
For now, assume the decision points are ordered as: [*Exploitation*](../reference/decision_points/exploitation.md); [Exposure](../reference/decision_points/system_exposure.md); [Utility](../reference/decision_points/utility.md); and [*Human Impact*](../reference/decision_points/human_impact.md).
In this order, an [_active_](../reference/decision_points/exploitation.md) state of [*Exploitation*](../reference/decision_points/exploitation.md) will never result in a *defer* priority.
A [_none_](../reference/decision_points/exploitation.md) state of [*Exploitation*](../reference/decision_points/exploitation.md) (no evidence of exploitation) will result in either *defer* or *scheduled* priority—unless the state of [*Human Impact*](../reference/decision_points/human_impact.md) is [_very high_](../reference/decision_points/human_impact.md), resulting in an *out-of-cycle* priority.

As opposed to mitigation, applying a remediation finishes an SSVC analysis of a deployed system.

!!! warning "Remediation is not a final state"

    While specific vulnerabilities in specific systems can be remediated, the vulnerability cannot be 'disposed of' or eliminated from future consideration within an IT environment.
    Since software and systems are dynamic, a single vulnerability can be re-introduced after initial remediation through updates, software rollbacks, or other systemic actions that change the operating conditions within an environment.
    It is therefore important to continually monitor remediated environments for vulnerabilities reintroduced by either rollbacks or new deployments of outdated software.

!!! note "Patch Deployer Priority"

    | Deployer Priority | Description |
    | :---              | :----------  |
    | Defer            | Do not act at present. |
    | Scheduled        | Act during regularly scheduled maintenance time. |
    | Out-of-cycle     | Act more quickly than usual to apply the mitigation or remediation out-of-cycle, during the next available opportunity, working overtime if necessary. |
    | Immediate        | Act immediately; focus all resources on applying the fix as quickly as possible, including, if necessary, pausing regular organization operations. |


## Deployer Tree

The example deployer tree [PDF](../pdf/ssvc_2_deployer_SeEUMss.pdf) is depicted below.


<embed src="../../pdf/ssvc_2_deployer_SeEUMss.pdf" alt="Suggested deployer tree"
 type="application/pdf"
 style="width: 100%;"
 height = "1000"/>

## Table of Values

<!-- relative to /data/csvs/ -->
{{ read_csv('deployer-options.csv') }}