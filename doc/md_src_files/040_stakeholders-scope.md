

# Vulnerability Management Decisions

This section will define who we are trying to give decision advice to, and how we are scoping our advice on vulnerability management decisions. 
Viable decision guidance for vulnerability management should, at a minimum, consider the stakeholder groups, their potential decision outcomes, and the data needed for relevant decision points. 
This section covers the first of these three, and the following sections address the other parts in turn.
The "who" is primarily about categories of stakeholders -- suppliers, deployers, and coordinators -- as well as their individual risk tolerances.
The "what" is about the scope, both in how the affected system is defined and how much of the world an analyst should consider when estimating effects of a vulnerability. 

While we strive to make the examples realistic, we invite the community to engage and conduct empirical assessments to test examples. 
The following construction should be treated as an informed hypothesis rather than a conclusion.

## Enumerating Stakeholders

Stakeholders in vulnerability management can be identified within multiple independent axes. 
For example, they can be identified by their responsibility: whether the group *supplies*, *deploys*, or *coordinates* remediation actions. 
Depending what task a team is performing in a supply chain, the team may be considered a supplier, deployer, or a coordinator.
Therefore, one organization may have teams that take on different roles.
For example, an organization that develops and uses its own software might delegate the supplier role to its development team and the deployer role to its IT operations team.
On the other hand, organizations using a DevOps approach to providing services might have a single group responsible for both the supplier and deployer roles.
Organizations may also be distinguished by type of industry sector. While it might be useful to enumerate all the sectors of the economy, we propose to draft decision points that include those from multiple important sectors. For example, we have safety-related questions in the decision path for all suppliers and deployers, so whether or not the stakeholder is in a safety-critical sector, the decision will be addressed.

The choice not to segregate the decisions by sector is reinforced by the fact that any given software system might be used by different sectors.  It is less likely that one organization has multiple responsibilities within the vulnerability management process. Even if there is overlap within an organization, the two responsibilities are often located in distinct business units with distinct decision-making processes. We can treat the responsibilities as non-overlapping, and, therefore, we can build two decision trees—one for each of the “patch supplier” and “patch deployer” responsibilities in the vulnerability management process. We leave “coordinating patches” as future work. Each of these trees will have different decision points that they take to arrive at a decision about a given unit of work.
<!-- Consider changing the word patch. There are other responses to a vulnerability (mitigation, isolation, etc.) that are backgrounded by using "patch" here. -->

The next two sections describe the decision space and the relevant decision points that we propose for these two responsibilities within the vulnerability management process.

The paper’s target audience is professional staff responsible for making decisions about information systems. This audience includes a broad class of professionals, and includes suppliers, system maintainers, and administrators of many types. It also includes other roles, such as risk managers, technical managers, and incident responders. Although every layperson who owns a computing device makes decisions about managing it, this is not the target audience. The following decision system may help such laypeople, but we do not intend it to be used by that audience.

Relatedly, C-level executives and public policy professionals often make, shape, or incentivize decisions about managing information systems; however, this is not the target audience either. To the extent that decision trees for vulnerability management help higher level policy decisions, we believe the best way to help policy makers is by making the technical decisions more transparent and explainable to policy makers. While policy makers may see indirect benefit, they are not the primary target, and we are not designing an approach for them directly.


## Enumerating Decisions

Stakeholders with different responsibilities in vulnerability management have largely different decisions to make. This section focuses on the differences among organizations based on their vulnerability management responsibilities. Some decision makers may have different responsibilities in relation to different software. For example, an Android app developer is a developer of the app, but is a deployer for any changes to the Android OS API. This situation is true for libraries in general. A web browser developer makes decisions about applying patches to DNS lookup libraries and transport layer security (TLS) libraries. A video game developer makes decisions about applying patches released to the Unreal Engine. A medical device developer makes decisions about applying patches to the Linux kernel. The list goes on.  Alternatively, one might view applying patches as, de facto, including some development and distribution of the updated product. Or one might take the converse view, that development, de facto, includes updating libraries. Either way, in each of these examples (mobile device apps, web browsers, video games, medical devices), we recommend that the professionals making genuine decisions do three things: (1) identify the decisions explicitly, (2) describe how they view their role(s), and (3) identify which software projects their decision relates to. If their decisions are explicit, then the decision makers can use the recommendations from this document that are relevant to them.

## Enumerating Vulnerability Management Actions
SSVC models the decision of “With what priority should the organization take action on a given vulnerability management work unit?” to be agnostic to whether or not a patch is available. 
A unit of work means either remediating the vulnerability---such as applying a patch---or deploying a mitigation. Both remediation and mitigations often address multiple identified vulnerabilities. 

The unit of work may be different for different stakeholders.
The units of work can also change as the vulnerability response progresses through a stakeholder's process.
We elucidate these ideas with the following examples.

### Supplier Units of Work

On the input side of the Supplier process, Suppliers typically receive reports of vulnerabilities in one or more versions of their product. 
Part of the Supplier's task on initial report intake is to resolve the initial report into a set of products and versions that are affected by the reported vulnerability.
 
Our working assumption is that for SSVC purposes, the supplier's unit of work is the combination of the vulnerability with each affected product.
This implies the need for Suppliers to be able to resolve whatever they receive to that level of granularity in order to make best use of SSVC. 

Products will often need to be addressed individually because they may have diverse development processes or usage scenarios.
There are a variety of ways a Supplier might need to resolve the set of affected products. For example they might

* recognize, on further investigation of the initial report, that additional versions of the product are affected
* discover that other products are affected due to code sharing or even consistent programmer error across products
* receive reports of vulnerabilities in third party libraries they include in one or more of their products
* receive fix bundles for third party libraries used in one or more of their products (where a fix bundle might resolve multiple vulnerabilities or add new features)

Without belaboring the point, the above methods are similar to how CVE Numbering Authorities discern "independently fixable vulnerabilities" [@mitre2020cna].
We also note that SBOM[@manion2019sbom] seems well-placed to aid in that resolution process for the third party library scenarios.

In the end, Suppliers provide remediations and/or mitigations for affected products.
A supplier-provided remediation is usually a software update which contains fixes for multiple vulnerabilities and, often, new or improved features.
Supplier output is relevant because it will become Deployers' input.
SSVC focuses just on the remediation in this case; a set of remediations for multiple vulnerabilities is a fix bundle.
Suppliers may also produce mitigations, such as recommended configuration changes, to limit the impact of a vulnerability.


### Deployer Units of Work ###

Deployers are usually in the position of receiving remediations or mitigations from their Suppliers for products they have deployed. 
They are then faced with the decision to deploy the remediation or mitigation to a particular instance or not. 
Whether they have the option of deploying only part of a remediation such as a fix bundle depends on whether the Supplier has engineered their release process to permit that degree of flexibility. 
For example, if service packs are fix bundles, the Supplier might choose to release individually deployable fixes as well.

The vulnerability management process for deployers has at its core the collation of data including
* an inventory of deployed instances of product versions
* a mapping of vulnerabilities to remediations or mitigations
* a mapping of remediations and/or mitigations to product versions

The first of these must be collected by the deployer, while the latter two most often originate from the product Supplier.
Managing this information is generally called asset management.
The relationship between SSVC and asset management is discussed further in (Relationship to asset management)[#relationship-to-asset-management].

In turn, deployers must resolve this information into specific actions in which a remediation or mitigation is slated for deployment to replace or modify a particular instance of the product.
The deployer tree in SSVC takes into account the mission and safety risks inherent to the category of systems to which those deployed instances belong.
For this reason we recommend that the pairing of remediation or mitigation to  a product version instance constitutes the unit of work most appropriate for the SSVC.

### Coordinator Units of Work ###

Coordinator units of work tend to coincide with whatever arrives in a single report, which spans the range from a single vulnerability affecting a specific version of an individual product from one Supplier all the way to fundamental design flaws in system specifications that could affect every Supplier and product that uses or implements the flawed specification. 
Coordinators may need to reorganize reports (e.g., merge, split, expand, or contract) according to their workflow demands. SSVC can be applied to either the initial report or to the results of such refinement.

### Aggregation of SSVC across units of work

SSVC users should answer the suggested questions for whatever discrete unit of work they are considering. There is not necessarily a reliable function to aggregate a recommendation about remediation out of its constituent vulnerabilities. For the sake of simplicity of examples, we treat the remediation as a patch of one vulnerability, and comment on any difficulty in generalizing our advice to a more complex patch where appropriate. 

To further clarify terms, "Remediation occurs when the vulnerability is eliminated or removed. Mitigation occurs when the impact of the vulnerability is decreased without reducing or eliminating the vulnerability." [@dodi_8531_2020, section 3.5] Examples of remediation include: applying patches, fixes and upgrades; or removing the vulnerable software or system from operation. Mitigating actions may include software configuration changes, adding firewall ACLs, or otherwise limiting the system's exposure to reduce the risk of the impact of the vulnerability; or accepting the risk.

### Supplying Patches

At a basic level, the decision at a software development organization is whether to issue a work order and what resources to expend to remediate a vulnerability in the organization’s software. Prioritization is required because, at least in the current history of software engineering, the effort to patch all known vulnerabilities will exceed available resources. The organization considers several other factors to build the patch; refactoring a large portion of the code base may be necessary for some patches, while others require relatively small changes. We focus only on the priority of building the patch, and we consider four categories of priority, as outlined in Table 2.

Table 2: Proposed Meaning for Supplier Priority Outcomes

| Supplier Priority | Description |
| ------------------ | ----------- |
| Defer              | Do not work on the patch at present.   |
| Scheduled          | Develop a fix within regularly scheduled maintenance using supplier resources as normal.  |
| Out-of-Cycle       | Develop mitigation or remediation out-of-cycle, taking resources away from other projects and releasing the fix as a security patch when it is ready. |
| Immediate          | Develop and release a fix as quickly as possible, drawing on all available resources, potentially including drawing on or coordinating resources from other parts of the organization. |

### Deploying Patches
Whether or not to deploy available remediation is a binary decision. However, additional defensive mitigations may be necessary sooner than patches are available and may be advisable after patches are applied. We recognize that vulnerability management actions are different when a patch is available and when it is not available.

When remediation is available, usually the action is to apply it. When remediation is not yet available, the action space is more diverse, but it should involve mitigating the vulnerability (e.g., shutting down services or applying additional security controls) or accepting the risk of not mitigating the vulnerability. Table 3 displays the action priorities for the deployer, which are similar to the supplier case.

<!--**Talk about applying other mitigations here** TODO
-->


Table 3: Proposed Meaning for Deployer Priority Outcomes

| Deployer Priority | Description                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Defer            | Do not act at present.                                                                                                                          |
| Scheduled        | Act during regularly scheduled maintenance time.                                                                                                   |
| Out-of-cycle     | Act more quickly than usual to apply the mitigation or remediation out-of-cycle, during the next available opportunity, working overtime if necessary.                    |
| Immediate        | Act immediately; focus all resources on applying the fix as quickly as possible, including, if necessary, pausing regular organization operations. |

### Coordinating Patches
In coordinated vulnerability disclosure (CVD), the available decision is whether or not to coordinate a vulnerability report. Vulnerability Response Decision Assistance (VRDA) provides a starting point for a decision tree for this situation.<sup>23</sup> VRDA is likely adequate for national-level CSIRTs that do general CVD, but other CSIRT types may have different needs. Future work may elicit those types and make a few different decision options. Specialized coordination organizations exist (e.g., ICS-CERT, which conducts CVD for safety-critical systems). We have not developed a coordination tree in this work, but future work could use our principles and design techniques to refine and evaluate VRDA or some other decision tree for coordinated vulnerability disclosure. The CERT guide to CVD provides something similar for those deciding how to report and disclose vulnerabilities they have discovered [@householder2020cvd, section 6.10].

Within each setting, the decisions are a kind of equivalence class for priority. That is, if an organization must deploy patches for three vulnerabilities, and if these vulnerabilities are all assigned the *scheduled* priority, then the organization can decide which to deploy first. The priority is equivalent. This approach may feel uncomfortable since CVSS gives the appearance of a finer grained priority. CVSS appears to say, “Not just 4.0 to 6.9 is ‘medium’ severity, but 4.6 is more severe than 4.5.” However, as discussed previously (see page 4), CVSS is designed to be accurate only within +/- 0.5, and, in practice, is scored with errors of around +/- 1.5 to 2.5 [@allodi2018effect, see Figure 1]. An error of this magnitude is enough to make all of the “normal” range from 4.0 to 6.9 equivalent, because 5.5 +/- 1.5 is the range 4.0 to 7.0. Our proposal is an improvement over this approach. CVSS errors often cross decision boundaries; in other words, the error range often includes the transition between “high” and “critical” or “medium.” Since our approach keeps the decisions qualitatively defined, this fuzziness does not
affect the results.

Returning to the example of an organization with three vulnerabilities to remediate that were assigned *scheduled* priority, in SSVC, they can be patched in any order. This is an improvement over CVSS, since based on the scoring errors, CVSS was essentially just giving random fine-grained priorities within qualitative categories anyway. With our system, organizations can be more deliberate about conveniently organizing work that is of equivalent priority.

## Risk Tolerance and Response Priority

SSVC enables stakeholders to balance and manage their risks themselves.
We follow [@ISO73] and define risk as "effect of uncertainty on objectives;" see [@ISO73] for notes on the terms in the definition.
For any vulnerability management practice to succeed it must balance at least two risks:

1. Change risk: the potential costs of deploying remediation, which include testing and deployment in addition to any problems that could arise from making changes to production systems.
2. Vulnerability risk: the potential costs of incidents resulting from exploitation of vulnerable systems

To place these risks in context, we follow the SEI's Taxonomy of Operational Cyber Security Risks [@cebula2010taxonomy]. Change risk can be characterized as a combination of Class 2 and/or Class 3 risks. Class 2: Systems and Technology Failures includes hardware, software, and systems risks. Class 3: Failed Internal Processes can arise from process design, process execution, process controls, or supporting processes. Meanwhile, vulnerability risk falls into Subclass 1.2: Actions of People: Deliberate.

In developing the decision trees in this document, we had in mind stakeholders with a moderate tolerance for risk. The resulting trees reflect that assumption. Organizations may of course be more or less conservative in their own vulnerability management practices, and we cannot presume to determine how an organization should balance their risk.

We therefore remind our readers that the labels on the trees (defer, immediate, etc.) can and should be customized to suit the needs of individual stakeholders wherever necessary and appropriate. For example, an organization with a high aversion to change risk might choose to accept more vulnerability risk by lowering the overall response labels for many branches in the trees, resulting in fewer vulnerabilities attaining the most urgent response. On the other hand, an organization with a high aversion to vulnerability risk could elevate the priority of many branches to ensure fixes are deployed quickly.

## Scope

One important variable in the answers to all the below decision points is scope. 
There are at least three aspects to scope.
One is how the boundaries of the affected system are set.
A second is whose security policy is relevant.
Thirdly, how far forward in time or causal steps one reasons about effects and harms.
We put forward recommendations for each of these.

However, users of the decision process may want to define different scopes. 
Users may define a different scope as long as the scope is consistent across decisions, and are credible, explicit, and accessible to all relevant decision makers.

For example, suppliers often decline to support products beyond a declared end-of-life (EOL) date. In those cases, a supplier could reasonably consider vulnerabilities in those products to be out of scope. However, a deployer may still have active instances of EOL products in their infrastructure. It remains appropriate for a deployer to use SSVC to prioritize their response to such situations, since even if there is no remediation forthcoming from the supplier it may be possible for the deployer to mitigate or remediate the vulnerability in other ways, up to and including decommissioning the affected system(s).

### Boundaries of the Affected System

One distinction is whether the system of interest is software per se or a cyber-physical system. One problem is that in every practical case, both are involved. Software is what has vulnerabilities and is what vulnerability management is focused on remediation. Multiple pieces of software run on any given computer system. To consider software vulnerabilities in a useful scope, we follow prior work and propose that a vulnerability affects “the set of software instructions that executes in an environment with a coherent function and set of permissions” [@spring2015global]. This definition is useful because it lets us keep to common usage and intuition and call the Linux kernel—at least a specific version of it—“one piece” of software. But decision points about safety and mission impact are not about the software per se; they are about the cyber-physical system, of which the software is a part.  The term "physical" in "cyber-physical system" should be interpreted broadly; selling stocks or manipulating press outlet content are both best understood as affecting human social institutions. These social institutions do not have much of a corporeal instantiation, but they are physical in the sense that they are not merely software, and so are parts of cyber-physical systems.

The hard part of delineating the boundaries of the affected system is specifying what it means for one system to be a part of another. Just because a computer is bolted to a wall does not mean the computer is part of the wall’s purpose, which is separating physical space. At the same time, an off-premises DNS server may be part of the site security assurance system if the on-premises security cameras rely on the DNS server to connect to the displays at the guard’s desk. We define computer software as part of a cyber-physical system if the two systems are mutually manipulable; that is, changes in the part (the software) will (at least, often) make detectable and relevant changes to the whole (the cyber-physical system), and changes in the whole will (often) make relevant and detectable changes in the part [@spring2018generalization].

When reasoning about a vulnerability, we assign the vulnerability to the nearest, relevant—yet more abstract—discrete component. This assignment is particularly important when assessing technical impact on a component. This description bears some clarification, via each of the adjectives:

  - **Nearest** is relative to the abstraction at which the vulnerability exists.

  - **Relevant** implies that the impacted component must be in the chain of abstraction moving upward from the location of the flaw.

  - **More abstract** means it’s at least one level of abstraction above the specific location of the vulnerability. For example, if the vulnerability is localized to a single line of code in a function, then the function, the module, the library, the application, the product, and the system it belongs to are all "more abstract."

  - **Discrete** means there is an identifiable thing that can be remediated (e.g., the unit of patching).

Products, libraries, and applications tend to be appropriate objects of focus when seeking the right level to analyze the impact of a vulnerability. Hence, when reasoning about the technical impact of a vulnerability localized to a function in a module in an open source library, the nearest relevant discrete abstraction is the library because the patches are made available at the library level. Similarly, analysis of a vulnerability in closed source database software that supports an enterprise resource management (ERM) system would consider the technical impact to the database, not to the ERM system.

### Relevant Security Policy

Our definition of a vulnerability includes a security policy violation, but it does not clarify whose security policies are relevant [@householder2020cvd].
For an organizational PSIRT or CSIRT, the organization's security policy is most relevant.
The answer is less clear for coordinators or ISACs.
An example scenario that brings the question into focus is phone OS jailbreak methods.
The owner of the phone may elect to jailbreak it; there is at least an implicit security policy from the owner that allows this method.
However, from the perspective of the explicit phone OS security policy embedded in the access controls and separation of privileges, the jailbreak is exploiting a vulnerability.
If a security policy is embedded in technical controls, such as OS access controls on a phone, then anything that violates that security policy is a vulnerability. 

## Reasoning Steps Forward

This aspect of scope is about immediacy, prevalence, and causal importance. Immediacy is about how soon after the decision point adverse effects should occur to be considered relevant. Prevalence is about how common adverse effects should be to be considered relevant. Causal importance is about how much an exploitation of the software in the cyber-physical system contributes to adverse effects to be considered relevant. Our recommendation is to walk a pragmatic middle path on all three aspects. Effects are not relevant if they are merely possible, too infrequent, far distant, or unchanged by the vulnerability. But effects are relevant long before they are absolutely certain, ubiquitous, or occurring presently. Overall, we summarize this aspect of scope as *consider credible effects based on known use cases of the software system as a part of cyber-physical systems*.
