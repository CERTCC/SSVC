## Enumerating Vulnerability Management Actions
SSVC models the decision of “With what priority should the organization take action on a given vulnerability management work unit?” to be agnostic to whether or not a patch is available.
A unit of work means either remediating the vulnerability—such as applying a patch—or deploying a mitigation. Both remediation and mitigations often address multiple identified vulnerabilities.

The unit of work may be different for different stakeholders.
The units of work can also change as the vulnerability response progresses through a stakeholder's process.
We elucidate these ideas with the following examples.

### Supplier Units of Work

On the input side of the Supplier process, Suppliers typically receive reports of vulnerabilities in one or more versions of their product.
Part of the Supplier's task on initial report intake is to resolve the initial report into a set of products and versions that are affected by the reported vulnerability.

Our working assumption is that for SSVC purposes, the supplier's unit of work is the combination of the vulnerability with each affected product.
This implies the need for Suppliers to be able to resolve whatever they receive to that level of granularity in order to make best use of SSVC.

Products will often need to be addressed individually because they may have diverse development processes or usage scenarios.
There are a variety of ways a Supplier might need to resolve the set of affected products. For example, they might

- recognize, on further investigation of the initial report, that additional versions of the product are affected
- discover that other products are affected due to code sharing or programmer error consistent across products
- receive reports of vulnerabilities in third party libraries they utilize in one or more of their products
- receive fix bundles for third party libraries used in one or more of their products (where a fix bundle might resolve multiple vulnerabilities or add new features)

Without belaboring the point, the above methods are similar to how CVE Numbering Authorities discern “independently fixable vulnerabilities” [@mitre2020cna].
We also note that SBOM[@manion2019sbom] seems well-placed to aid in that resolution process for the third-party library scenarios.

In the end, Suppliers provide remediations and/or mitigations for affected products.
A supplier-provided remediation is usually a software update which contains fixes for multiple vulnerabilities and, often, new or improved features.
Supplier output is relevant because it will become input to Deployers.
SSVC focuses only on the remediation in this case; a set of remediations for multiple vulnerabilities is a fix bundle.
Suppliers may also produce mitigations, such as recommended configuration changes, to limit the impact of a vulnerability.


### Deployer Units of Work ###

Deployers are usually in the position of receiving remediations or mitigations from their Suppliers for products they have deployed.
They must then decide whether to deploy the remediation or mitigation to a particular instance (or not).
Whether they have the option of deploying only part of a remediation such as a fix bundle depends on whether the Supplier has engineered their release process to permit that degree of flexibility.
For example, if service packs are fix bundles, the Supplier might choose to release individually deployable fixes as well.

The vulnerability management process for deployers has at its core the collation of data including
- an inventory of deployed instances of product versions
- a mapping of vulnerabilities to remediations or mitigations
- a mapping of remediations and/or mitigations to product versions

The first must be collected by the Deployer, while the latter two most often originate from the product Supplier.
Managing this information is generally called **asset management**.
The relationship between SSVC and asset management is discussed further in [Relationship to asset management](#relationship-to-asset-management).

In turn, Deployers must resolve this information into specific actions in which a remediation or mitigation is slated for deployment to replace or modify a particular instance of the product.
The Deployer tree in SSVC considers the mission and safety risks inherent to the category of systems to which those deployed instances belong.
For this reason, we recommend that the pairing of remediation or mitigation to  a product version instance constitutes the unit of work most appropriate for the SSVC.

### Coordinator Units of Work ###

Coordinator units of work tend to coincide with whatever arrives in a single report, which spans the range from a single vulnerability affecting a specific version of an individual product from one Supplier all the way to fundamental design flaws in system specifications that could affect every Supplier and product that uses or implements the flawed specification.
Coordinators may need to reorganize reports (e.g., merge, split, expand, or contract) according to their workflow demands. SSVC can be applied to either the initial report or to the results of such refinement.

### Aggregation of SSVC across units of work

SSVC users should answer the suggested questions for whatever discrete unit of work they are considering. There is not necessarily a reliable function to aggregate a recommendation about remediation out of its constituent vulnerabilities. For the sake of simplicity of examples, we treat the remediation as a patch of one vulnerability, and comment on any difficulty in generalizing our advice to a more complex patch where appropriate.

To further clarify terms, “Remediation occurs when the vulnerability is eliminated or removed. Mitigation occurs when the impact of the vulnerability is decreased without reducing or eliminating the vulnerability” [@dodi_8531_2020, section 3.5]. Examples of remediation include applying patches, fixes and upgrades; or removing the vulnerable software or system from operation. Mitigating actions may include software configuration changes, adding firewall ACLs, or otherwise limiting the system's exposure to reduce the risk of the impact of the vulnerability; or accepting the risk.

### Supplying Patches

At a basic level, the decision at a software development organization is whether to issue a work order and what resources to expend to remediate a vulnerability in the organization’s software. Prioritization is required because, at least in the current history of software engineering, the effort to patch all known vulnerabilities will exceed available resources. The organization considers several other factors to build the patch; refactoring a large portion of the code base may be necessary for some patches, while others require relatively small changes.
We focus only on the priority of building the patch, and we consider four categories of priority, as outlined in [Table 2](#table-supplier-outcomes).

Table: <a name="table-supplier-outcomes"></a> Proposed Meaning for Supplier Priority Outcomes

| Supplier Priority | Description |
| :---              | :----------  |
| Defer              | Do not work on the patch at present. |
| Scheduled          | Develop a fix within regularly scheduled maintenance using supplier resources as normal. |
| Out-of-Cycle       | Develop mitigation or remediation out-of-cycle, taking resources away from other projects and releasing the fix as a security patch when it is ready. |
| Immediate          | Develop and release a fix as quickly as possible, drawing on all available resources, potentially including drawing on or coordinating resources from other parts of the organization. |

### Deploying Patches

A mitigation that successfully changes the value of a decision point may shift the priority of further action to a reduced state. An effective firewall or IDS rule coupled with an adequate change control process for rules may be enough to reduce the priority where no further action is necessary. In the area of Financial impacts, a better insurance policy may be purchased, providing necessary fraud insurance. Physicial well-being impact may be reduced by testing the physicial barriers designed to restrict a robot's ability to interact with humans. Mission impact could be reduced by correcting the problems identified in a disaster recover test-run of the alternate business flow. If applying a mitigation reduces the priority to *defer*, the deployer may not need to apply a remediation if it later becomes available. [Table 3](#table-deployer-outcomes) displays the action priorities for the deployer, which are similar to the supplier case.

When remediation is available, usually the action is to apply it. When remediation is not yet available, the action space is more diverse, but it should involve mitigating the vulnerability (e.g., shutting down services or applying additional security controls) or accepting the risk of not mitigating the vulnerability. Applying mitigations may change the value of decision points. For example, effective firewall and IDS rules may change [*System Exposure*](#system-exposure) from open to controlled. Financial well-being, a [*Safety Impact*](#safety-impact) category, might be reduced with adequate fraud detection and insurance. Physical well-being, also a [*Safety Impact*](#safety-impact) category, might be reduced by physical barriers that restrict a robot's ability to interact with humans. [*Mission Impact*](#mission-impact) might be reduced by introducing back-up business flows that do not use the vulnerable component. In a later section we combine [Mission and Situated Safety Impact](#table-mission-safety-combined) to reduce the complexity of the tree.

However, these mitigation techniques will not always work. For example, the implementation of a firewall or IDS rule to mitigate [*System Exposure*](#system-exposure) from open to controlled is only valid until someone changes the rule. In the area of Financial impacts, the caps on the insurance may be too low to act as a mitigation.
The Physical impact may be increased by incorrect installation of the physical barriers designed to restrict a robot’s ability to interact with humans.
The [*Mission Impact*](#mission-impact) could be increased when a disaster recovery test-run identifies problems with an alternate business flow. The mitigating action may not be permanent or work as designed.

A mitigation that successfully changes the value of a decision point may shift the priority of further action to a reduced state. If applying a mitigation reduces the priority to *defer*, the deployer may not need to apply a remediation, if later, it becomes available. Table 3 displays the action priorities for the deployer, which are similar to the supplier case.

In a later section, the different types of impacts are defined and then implemented in the decision trees as examples of how the various impacts affect the priority.
For now, assume the decision points are ordered as: [*Exploitation*](#exploitation); [*Exposure*](#exposure); [*Utility*](#utility); and [*Human Impact*](#human-impact).
In this order, an [_active_](#exploitation) state of [*Exploitation*](#exploitation) will never result in a *defer* priority.
A [_none_](#exploitation) state of [*Exploitation*](#exploitation) (no evidence of exploitation) will result in either *defer* or *scheduled* priority—unless the state of [*Human Impact*](#human-impact) is [_very high_](#human-impact), resulting in an *out-of-cycle* priority.

As opposed to mitigation, applying a remediation finishes an SSVC analysis of a deployed system.
While specific vulnerabilities in specific systems can be remediated, the vulnerability cannot be 'disposed of' or eliminated from future consideration within an IT environment.
Since software and systems are dynamic, a single vulnerability can be re-introduced after initial remediation through updates, software rollbacks, or other systemic actions that change the operating conditions within an environment.
It is therefore important to continually monitor remediated environments for vulnerabilities reintroduced by either rollbacks or new deployments of outdated software.


Table: <a name="table-deployer-outcomes"></a> Proposed Meaning for Deployer Priority Outcomes

| Deployer Priority | Description |
| :---              | :----------  |
| Defer            | Do not act at present. |
| Scheduled        | Act during regularly scheduled maintenance time. |
| Out-of-cycle     | Act more quickly than usual to apply the mitigation or remediation out-of-cycle, during the next available opportunity, working overtime if necessary. |
| Immediate        | Act immediately; focus all resources on applying the fix as quickly as possible, including, if necessary, pausing regular organization operations. |

### Coordinating Patches
In coordinated vulnerability disclosure (CVD), there are two available decisions modelled in version 2 of SSVC.
The first is whether or not to coordinate a vulnerability report.
This decision is also known as triage.
Vulnerability Response Decision Assistance (VRDA) provides a starting point for a decision tree for this situation.
VRDA is likely adequate for national-level CSIRTs that do general CVD, but other CSIRT types may have different needs.
The *CERT guide to Coordinated Vulnerability Disclosure* provides something similar for those who are deciding how to report and disclose vulnerabilities they have discovered [@householder2020cvd, section 6.10].
The second decision is whether to publish information about a vulnerability.
We omit a table for this decision because the options are *do not publish* or *publish*.

Table: <a name="table-triage-outcomes"></a> Proposed Coordinator Triage Priority Outcomes

| Triage Priority | Description |
| :---            | :----------  |
| Decline         | Do not act on the report. |
| Track           | Receive information about the vulnerability and monitor for status changes but do not take any overt actions. |
| Coordinate      | Take action on the report. “Action” may include any one or more of: technical analysis, reproduction, notifying vendors, publication, and assist another party. |

