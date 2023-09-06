# Enumerating Action Priority

SSVC models the decision of
“With what priority should the organization take action on a given vulnerability management work unit?”
to be agnostic to whether or not a patch is available.
We explain what we mean by a “work unit” in the previous section.
Here we explain what we mean by “priority”.

## Supplying Patches

At a basic level, the decision at a software development organization is whether to issue a work order and what resources to expend to remediate a vulnerability in the organization’s software. Prioritization is required because, at least in the current history of software engineering, the effort to patch all known vulnerabilities will exceed available resources. The organization considers several other factors to build the patch; refactoring a large portion of the code base may be necessary for some patches, while others require relatively small changes.
We focus only on the priority of building the patch, and we consider four categories of priority, as outlined in [Table 2](#table-supplier-outcomes).

!!! note "Patch Supplier Priority"
   
    | Supplier Priority | Description |
    | :---              | :----------  |
    | Defer              | Do not work on the patch at present. |
    | Scheduled          | Develop a fix within regularly scheduled maintenance using supplier resources as normal. |
    | Out-of-Cycle       | Develop mitigation or remediation out-of-cycle, taking resources away from other projects and releasing the fix as a security patch when it is ready. |
    | Immediate          | Develop and release a fix as quickly as possible, drawing on all available resources, potentially including drawing on or coordinating resources from other parts of the organization. |

## Deploying Patches

A mitigation that successfully changes the value of a decision point may shift the priority of further action to a reduced state. An effective firewall or IDS rule coupled with an adequate change control process for rules may be enough to reduce the priority where no further action is necessary. In the area of Financial impacts, a better insurance policy may be purchased, providing necessary fraud insurance. Physicial well-being impact may be reduced by testing the physicial barriers designed to restrict a robot's ability to interact with humans. Mission impact could be reduced by correcting the problems identified in a disaster recover test-run of the alternate business flow. If applying a mitigation reduces the priority to *defer*, the deployer may not need to apply a remediation if it later becomes available. [Table 3](#table-deployer-outcomes) displays the action priorities for the deployer, which are similar to the supplier case.

When remediation is available, usually the action is to apply it. When remediation is not yet available, the action space is more diverse, but it should involve mitigating the vulnerability (e.g., shutting down services or applying additional security controls) or accepting the risk of not mitigating the vulnerability. Applying mitigations may change the value of decision points. For example, effective firewall and IDS rules may change [*System Exposure*](#system-exposure) from open to controlled. Financial well-being, a [*Safety Impact*](#safety-impact) category, might be reduced with adequate fraud detection and insurance. Physical well-being, also a [*Safety Impact*](#safety-impact) category, might be reduced by physical barriers that restrict a robot's ability to interact with humans. [*Mission Impact*](#mission-impact) might be reduced by introducing back-up business flows that do not use the vulnerable component. In a later section we combine [Mission and Situated Safety Impact](#table-mission-safety-combined) to reduce the complexity of the tree.

However, these mitigation techniques will not always work.

!!! example "Examples of Inadequate Mitigation"

    - The implementation of a firewall or IDS rule to mitigate [*System Exposure*](#system-exposure) from 
    open to controlled is only valid until someone changes the rule. 
    - In the area of Financial impacts, the caps on the insurance may be too low to act as a mitigation.
    - The Physical impact may be increased by incorrect installation of the physical barriers designed to restrict a
    robot’s ability to interact with humans.
    - The [*Mission Impact*](#mission-impact) could be increased when a disaster recovery test-run identifies problems
    with an alternate business flow.
    - The mitigating action may not be permanent or work as designed.

A mitigation that successfully changes the value of a decision point may shift the priority of further action to a reduced state.
If applying a mitigation reduces the priority to *defer*, the deployer may not need to apply a remediation, if later, it becomes available.
{== Table 3 ==} displays the action priorities for the deployer, which are similar to the supplier case.

In a later section, the different types of impacts are defined and then implemented in the decision trees as examples of how the various impacts affect the priority.
For now, assume the decision points are ordered as: [*Exploitation*](#exploitation); [*Exposure*](#exposure); [*Utility*](#utility); and [*Human Impact*](#human-impact).
In this order, an [_active_](#exploitation) state of [*Exploitation*](#exploitation) will never result in a *defer* priority.
A [_none_](#exploitation) state of [*Exploitation*](#exploitation) (no evidence of exploitation) will result in either *defer* or *scheduled* priority—unless the state of [*Human Impact*](#human-impact) is [_very high_](#human-impact), resulting in an *out-of-cycle* priority.

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

## Coordinating Patches
In coordinated vulnerability disclosure (CVD), there are two available decisions modelled in version 2 of SSVC.
The first is whether or not to coordinate a vulnerability report.
This decision is also known as triage.
Vulnerability Response Decision Assistance (VRDA) provides a starting point for a decision tree for this situation.
VRDA is likely adequate for national-level CSIRTs that do general CVD, but other CSIRT types may have different needs.
The *CERT guide to Coordinated Vulnerability Disclosure* provides something similar for those who are deciding how to report and disclose vulnerabilities they have discovered [@householder2020cvd, section 6.10].

!!! note "Coordinator Triage Priority"

    | Triage Priority | Description |
    | :---            | :----------  |
    | Decline         | Do not act on the report. |
    | Track           | Receive information about the vulnerability and monitor for status changes but do not take any overt actions. |
    | Coordinate      | Take action on the report. “Action” may include any one or more of: technical analysis, reproduction, notifying vendors, publication, and assist another party. |

The second decision is whether to publish information about a vulnerability.

!!! note "Coordinator Publish Priority"

    | Publish Priority | Description |
    | :---             | :----------  |
    | Do not publish   | Do not publish information about the vulnerability. |
    | Publish          | Publish information about the vulnerability. |
