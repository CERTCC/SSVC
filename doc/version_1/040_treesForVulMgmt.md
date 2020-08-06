


# Decision Trees for Vulnerability Management

Viable decision guidance for vulnerability management should, at a minimum, consider the stakeholder groups, their potential decision outcomes, and the data needed for relevant decision points. The following sections address each of these parts, in turn, and should be taken as instructive examples. While we strive to make the examples realistic, we invite the community to engage and conduct empirical assessments to test examples. The following construction should be treated as an informed hypothesis rather than a conclusion.

## Enumerating Stakeholders

Stakeholders in vulnerability management can be identified within multiple independent axes. For example, they can be identified by their responsibility: whether the organization *develops*, *applies*, or *coordinates* patches. Organizations may also be distinguished by type of industry sector. While it might be useful to enumerate all the sectors of the economy, we propose to draft decision points that include those from multiple important sectors. For example, we have safety-related questions in the decision path for all developers and appliers, so whether or not the stakeholder is in a safety-critical sector, the decision will be addressed.

The choice not to segregate the decisions by sector is reinforced by the fact that any given software system might be used by different sectors.  It is less likely that one organization has multiple responsibilities within the vulnerability management process. Even if there is overlap within an organization, the two responsibilities are often located in distinct business units with distinct decision-making processes. We can treat the responsibilities as non-overlapping, and, therefore, we can build two decision trees—one for each of the “patch development” and “patch deployment” responsibilities in the vulnerability management process. We leave “coordinating patches” as future work. Each of these trees will have different decision points that they take to arrive at a decision about a given unit of work.

The next two sections describe the decision space and the relevant decision points that we propose for these two responsibilities within the vulnerability management process.

The paper’s target audience is professional staff responsible for making decisions about information systems. This audience includes a broad class of professionals, and includes developers, system maintainers, and administrators of many types. It also includes other roles, such as risk managers, technical managers, and incident responders. Although every layperson who owns a computing device makes decisions about managing it, this is not the target audience. The following decision system may help such laypeople, but we do not intend it to be used by that audience.

Relatedly, C-level executives and public policy professionals often make, shape, or incentivize decisions about managing information systems; however, this is not the target audience either. To the extent that decision trees for vulnerability management help higher level policy decisions, we believe the best way to help policy makers is by making the technical decisions more transparent and explainable to policy makers. While policy makers may see indirect benefit, they are not the primary target, and we are not designing an approach for them directly.


## Enumerating Decisions

Stakeholders with different responsibilities in vulnerability management have largely different decisions to make. This section focuses on the differences among organizations based on their vulnerability management responsibilities. Some decision makers may have different responsibilities in relation to different software. For example, an Android app developer is a developer of the app, but is a patch applier for any changes to the Android OS API. This situation is true for libraries in general. A web browser developer makes decisions about applying patches to DNS lookup libraries and transport layer security (TLS) libraries. A video game developer makes decisions about applying patches released to the Unreal Engine. A medical device developer makes decisions about applying patches to the Linux kernel. The list goes on.  Alternatively, one might view applying patches as, de facto, including some development and distribution of the updated product. Or one might take the converse view, that development, de facto, includes updating libraries. Either way, in each of these examples (mobile device apps, web browsers, video games, medical devices), we recommend that the professionals making genuine decisions do three things: (1) identify the decisions explicitly, (2) describe how they view their role(s), and (3) identify which software projects their decision relates to. If their decisions are explicit, then the decision makers can use the recommendations from this document that are relevant to them.

###Developing Patches


At a basic level, the decision at a software development organization is whether to issue a work order and what resources to expend to fix a vulnerability in the organization’s software. Prioritization is required because, at least in the current history of software engineering, the effort to patch all known vulnerabilities will exceed available resources. The organization considers several other factors to build the patch; refactoring a large portion of the code base may be necessary for some patches, while others require relatively small changes. We focus only on the priority of building the patch, and we consider four categories of priority, as outlined in Table 2.

Table 2: Proposed Meaning for Developer Priority Outcomes

| Developer Priority | Description                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Defer              | Do not work on the patch at present.                                                                                                                                                  |
| Scheduled          | Develop a fix within regularly scheduled maintenance using developer resources as normal.                                                                                             |
| Out-of-Band        | Develop a fix out-of-band, taking resources away from other projects and releasing the fix as a security patch when it is ready.                                                       |
| Immediate          | Develop and release a fix as quickly as possible, drawing on all available resources, potentially including drawing on or coordinating resources from other parts of the organization. |

###Applying Patches
 Whether or not to apply an available patch is a binary decision. However, additional defensive mitigations may be necessary sooner than patches are available and may be advisable after patches are applied. We recognize that vulnerability management actions are different when a patch is available and when it is not available.

When a patch is available, usually the action is to apply it. When a patch it not yet available, the action space is more diverse, but it should involve mitigating the vulnerability (e.g., shutting down services or applying additional security controls) or accepting the risk of not mitigating the vulnerability.

In this paper, we model the decision of “With what priority should the organization take action on a given vulnerability management work unit?” to be agnostic to whether or not a patch is available. A unit of work means either applying a patch or deploying a mitigation. Both patches and mitigations often remediate multiple identified vulnerabilities. The patch applier should answer the suggested questions for whatever unit of work they are considering as a whole, single unit. There is not necessarily a reliable function to aggregate a recommendation about a patch out of its constituent vulnerabilities. For the sake of simplicity of examples, we treat a patch as a patch of one vulnerability, and comment on any difficulty in generalizing our advice to a more complex patch where appropriate. Table 3 displays the action priorities for the patch applier, which are similar to the patch developer case.

<!--**Talk about applying other mitigations here** TODO
-->

Table 3: Proposed Meaning for Applier Priority Outcomes

| Applier Priority | Description                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Defer            | Do not act at present.                                                                                                                             |
| Scheduled        | Act during regularly scheduled maintenance time.                                                                                                   |
| Out-of-Band      | Act more quickly than usual to apply the fix out-of-band, during the next available opportunity, working overtime if necessary.                    |
| Immediate        | Act immediately; focus all resources on applying the fix as quickly as possible, including, if necessary, pausing regular organization operations. |

###Coordinating Patches
In coordinated vulnerability disclosure (CVD), the available decision is whether or not to coordinate a vulnerability report. VRDA provides a starting point for a decision tree for this situation.<sup>23</sup> VRDA is likely adequate for national-level CSIRTs that do general CVD, but other CSIRT types may have different needs. Future work may elicit those types and make a few different decision options. Specialized coordination organizations exist (e.g., ICS-CERT, which conducts CVD for safety-critical systems). We have not developed a coordination tree in this work, but future work could use our principles and design techniques to refine and evaluate VRDA or some other decision tree for coordinated vulnerability disclosure. The CERT guide to CVD provides something similar for those deciding how to report and disclose vulnerabilities they have discovered.\[24\]

Within each setting, the decisions are a kind of equivalence class for priority. That is, if an organization must deploy patches for three vulnerabilities, and if these vulnerabilities are all assigned the “scheduled” priority, then the organization can decide which to deploy first. The priority is equivalent. This approach may feel uncomfortable since CVSS gives the appearance of a finer grained priority. CVSS appears to say, “Not just 4.0 to 6.9 is ‘medium’ severity, but 4.6 is more severe than 4.5.” However, as discussed previously (see page 4), CVSS is designed to be accurate only within +/- 0.5, and, in practice, is scored with errors of around +/- 1.5 to 2.5.\[25\] An error of this magnitude is enough to make all of the “normal” range from 4.0 to 6.9 equivalent, because 5.5 +/- 1.5 is the range 4.0 to 7.0. Our proposal is an improvement over this approach. CVSS errors often cross decision boundaries; in other words, the error range often includes the transition between “high” and “critical” or “medium.” Since our approach keeps the decisions qualitatively defined, this fuzziness does not
affect the results.

Returning to the example of an organization with three vulnerabilities to patch that were assigned “scheduled” priority, in SSVC, they can be patched in any order. This is an improvement over CVSS, since based on the scoring errors, CVSS was essentially just giving random fine-grained priorities within qualitative categories anyway. With our system, organizations can be more deliberate about conveniently organizing work that is of equivalent priority.

## Scope

One important variable in the answers to all the below decision points is scope. There are at least two aspects to scope. One is how the boundaries of the affected system are set. A second is how far forward in time or causal steps one reasons about effects and harms. We put forward recommendations for both of these. However, users of the decision process may want to define different scopes. Users may define a different scope as long as the scope is consistent across decisions, and are plausible, explicit, and accessible to all relevant decision makers.

### Boundaries of the Affected System

One distinction is whether the system of interest is software per se or a cyber-physical system. One problem is that in every practical case, both are involved. Software is what has vulnerabilities and is what vulnerability management is focused on patching. Multiple pieces of software run on any given computer system. To consider software vulnerabilities in a useful scope, we follow prior work and propose that a vulnerability affects “the set of software instructions that executes in an environment with a coherent function and set of permissions.”\[26\] This definition is useful because it lets us keep to common usage and intuition and call the Linux kernel—at least a specific version of it—“one piece” of software. But decision points about safety and mission impact are not about the software per se; they are about the cyber-physical system, of which the software is a part.  The term *physical* in *cyber-physical system* should be interpreted broadly; selling stocks or manipulating press outlet content are both best understood as affecting human social institutions. These social institutions do not have much of a corporeal instantiation, but they are physical in the sense that they are not merely software, and so are parts of cyber-physical systems.

The hard part of delineating the boundaries of the affected system is specifying what it means for one system to be a part of another. Just because a computer is bolted to a wall does not mean the computer is part of the wall’s purpose, which is separating physical space. At the same time, an off-premises DNS server may be part of the site security assurance system if the on-premises security cameras rely on the DNS server to connect to the displays at the guard’s desk. We define computer software as part of a cyber-physical system if the two systems are mutually manipulable; that is, changes in the part (the software) will (at least, often) make detectable and relevant changes to the whole (the cyber-physical system), and changes in the whole will (often) make relevant and detectable changes in the part.\[27\]

When reasoning about a vulnerability, we assign the vulnerability to the nearest, relevant—yet more abstract—discrete component. This assignment is particularly important when assessing technical impact on a component. This description bears some clarification, via each of the adjectives:

  - *Nearest* is relative to the abstraction at which the vulnerability
    exists.

  - *Relevant* implies that the impacted component must be in the chain
    of abstraction moving upward from the location of the flaw.

  - *More abstract* means it’s at least one level of abstraction above
    the specific location of the vulnerability. For example, if the
    vulnerability is localized to a single line of code in a function,
    then the function, the module, the library, the application, the
    product, and the system it belongs to are all *more abstract*.

  - *Discrete* means there is an identifiable thing that can be fixed
    (e.g., the unit of patching).

Products, libraries, and applications tend to be appropriate objects of focus when seeking the right level to analyze the impact of a vulnerability. Hence, when reasoning about the technical impact of a vulnerability localized to a function in a module in an open source library, the nearest relevant discrete abstraction is the library because the patches are made available at the library level. Similarly, analysis of a vulnerability in closed source database software that supports an enterprise resource management (ERM) system would consider the technical impact to the database, not to the ERM system.

### Reasoning Steps Forward

This aspect of scope is about immediacy, prevalence, and causal importance. Immediacy is about how soon after the decision point adverse effects should occur to be considered relevant. Prevalence is about how common adverse effects should be to be considered relevant. Causal importance is about how much an exploitation of the software in the cyber-physical system contributes to adverse effects to be considered relevant. Our recommendation is to walk a pragmatic middle path on all three aspects. Effects are not relevant if they are merely possible, too infrequent, far distant, or unchanged by the vulnerability. But effects are relevant long before they are absolutely certain, ubiquitous, or occurring presently. Overall, we summarize this aspect of scope as *consider plausible effects based on known use cases of the software system as a part of cyber-physical systems*.

## Likely Decision Points and Relevant Data

We propose the following decision points and associated values should be a factor when making decisions about vulnerability prioritization. Each decision point is tagged with the stakeholder it is relevant to: patch appliers, patch developers, or both. We emphasize that these descriptions are hypotheses to be further tested and validated. We made every effort to put forward informed and useful decision frameworks with wide applicability, but the goal of this paper is more to solicit feedback than make a declaration. We welcome questions, constructive criticism, refuting evidence, or supporting evidence about any aspect of this proposal.

One important omission from the values for each category is an “unknown” option. Instead, we recommend explicitly identifying an option that is a reasonable assumption based on prior events. Such an option requires reliable historical evidence for what tends to be the case; of course, future events may require changes to these assumptions over time.  Therefore, our assumptions require evidence and are open to debate in light of new evidence. Different risk tolerance or risk discounting postures are not addressed in the current work; accommodating such tolerance or discounting explicitly is an area for future work. This flexibility fits into our overall goal of supplying a decision-making framework that is both transparent and fits the needs of different communities. Resisting an “unknown” option discourages the modeler from silently embedding these assumptions in their choices for how the decision tree flows below the selection of any “unknown” option.

We propose satisfactory decision points for vulnerability management in the next sections, in no particular order.

### Exploitation (Developer, Applier)
> Evidence of Active Exploitation of a Vulnerability

The intent of this measure is the present state of exploitation of the vulnerability. The intent is not to predict future exploitation but only to acknowledge the current state of affairs. Predictive systems, such as EPSS, could be used to augment this decision or to notify stakeholders of likely changes.\[28\]

Table 4: Exploitation Decision Values

<table>
<tbody>
<tr class="odd">
<td>None</td>
<td>There is no evidence of active exploitation and no public proof of concept (PoC) of how to exploit the vulnerability.</td>
</tr>
<tr class="even">
<td>PoC<br />
(Proof of Concept)</td>
<td>One of the following cases is true: (1) exploit code sold or traded on underground or restricted fora; (2) typical public PoC in places such as Metasploit or ExploitDB; or (3) the vulnerability has a well-known method of exploitation. Some examples of condition (3) are open-source web proxies serve as the PoC code for how to exploit any vulnerability in the vein of improper validation of TLS certificates. As another example, Wireshark serves as a PoC for packet replay attacks on ethernet or WiFi networks.</td>
</tr>
<tr class="odd">
<td>Active</td>
<td>Shared, observable, reliable evidence that the exploit is being used in the wild by real attackers; there is credible public reporting.</td>
</tr>
</tbody>
</table>

### Technical Impact (Developer)
> Technical Impact of Exploiting the Vulnerability

When evaluating *technical impact*, recall the scope definition above. Total control is relative to the affected component where the vulnerability resides. If a vulnerability discloses authentication or authorization credentials to the system, this information disclosure should also be scored as “total” if those credentials give an adversary total control of the component.

Table 5: Technical Impact Decision Values

|  |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Partial | The exploit gives the adversary *limited* control over, or information exposure about, the behavior of the software that contains the vulnerability. Or the exploit gives the adversary an importantly low stochastic opportunity for total control. In this context, “low” means that the attacker cannot reasonably make enough attempts to overcome the low chance of each attempt not working. Denial of service is a form of limited control over the behavior of the vulnerable component. |
| Total   | The exploit gives the adversary *total* control over the behavior of the software, or it gives total disclosure of all information on the system that contains the vulnerability                                                                                                                                                                                                                                                                                                                 |

### Utility (Developer, Applier\[29\])
> The Usefulness of the Exploit to the Adversary

Heuristically, we base *utility* on a combination of value density of vulnerable components and virulence of potential exploitation. This framing makes it easier to analytically derive these categories from a description of the vulnerability and the affected component. Virulence (slow or rapid) and value density (diffuse or concentrated) are defined in Sections 4.4.3.1 and 4.4.3.2.

Roughly, *utility* is a combination of two things: (1) the value of each exploitation event and (2) the ease and speed with which the adversary can cause exploitation events. We define *utility* as laborious, efficient, or super effective, as described in Table 6.

Table 6: Utility Decision Values

|  |
| --------------- | ------------------------------------------------------------------------------ |
| Laborious       | Slow virulence and diffuse value                                               |
| Efficient       | {Rapid virulence and diffuse value} OR {Slow virulence and concentrated value} |
| Super Effective | Rapid virulence and concentrated value                                         |

#### Virulence

*Virulence* is described as slow or rapid:

  - **Slow**. Steps 1-4 of the kill chain\[30\] cannot be reliably
    automated for this vulnerability for some reason. These steps are
    reconnaissance, weaponization, delivery, and exploitation. Example
    reasons for why a step may not be reliably automatable include (1)
    the vulnerable component is not searchable or enumerable on the
    network, (2) weaponization may require human direction for each
    target, (3) delivery may require channels that widely deployed
    network security configurations block, and (3) exploitation may be
    frustrated by adequate exploit-prevention techniques enabled by
    default; ASLR is an example of an exploit-prevention tool.

  - **Rapid**. Steps 1-4 of the of the kill chain can be reliably
    automated. If the vulnerability allows remote code execution or
    command injection, the default response should be rapid.

#### Value Density

*Value density* is described as diffuse or concentrated:

  - **Diffuse**. The system that contains the vulnerable component has
    limited resources. That is, the resources that the adversary will
    gain control over with a single exploitation event are relatively
    small. Examples of systems with diffuse value are email accounts,
    most consumer online banking accounts, common cell phones, and most
    personal computing resources owned and maintained by users. (A
    “user” is anyone whose professional task is something other than
    the maintenance of the system or component. As with *safety impact*,
    a “system operator” is anyone who is professionally responsible for
    the proper operation or maintenance of a system.)

  - **Concentrated**. The system that contains the vulnerable component
    is rich in resources. Heuristically, such systems are often the
    direct responsibility of “system operators” rather than users.
    Examples of concentrated value are database systems, Kerberos
    servers, web servers hosting login pages, and cloud service
    providers. However, usefulness and uniqueness of the resources on
    the vulnerable system also inform value density. For example,
    encrypted mobile messaging platforms may have concentrated value,
    not because each phone’s messaging history has a particularly large
    amount of data, but because it is uniquely valuable to law
    enforcement.

The output for the *utility* decision point is visualized in Table 7.

Table 7: Utility to the Adversary, as a Combination of Virulence and
Value Density

| **Virulence** | Rapid | Efficient         | Super Effective |
| ------------- | ----- | ----------------- | --------------- |
|               | Slow  | Laborious         | Efficient       |
|               |       | Diffuse           | Concentrated    |
|               |       | **Value Density** |                 |

Alternative heuristics for proxying adversary utility are plausible. One such example is the value the vulnerability would have were it sold on the open market. Some firms, such as Zerodium,\[31\] make such pricing structures public. The valuable exploits track the virulence and value density heuristics for the most part. Within a single system—whether it is Apache, Windows, iOS or WhatsApp—more automated kill chain steps successfully leads to higher exploit value. Remote code execution with sandbox escape and without user interaction are the most valuable exploits, and those features describe automation of the relevant kill chain steps. How equivalently virulent exploits for different systems are priced relative to each other is more idiosyncratic. Price does not only track value density of the system, but presumably also the existing supply of exploits and the installation distribution among the targets of Zerodium’s customers. Currently, we simplify the analysis and ignore these factors. However, future work should look for and prevent large mismatches between the outputs of the *utility* decision point and the exploit markets.

### Safety Impact (Developer, Applier)
> Safety Impacts of Affected System Compromise

We take an expansive view of safety, in which a safety violation is a violation of what the Centers for Disease Control (CDC) calls `well-being`.\[32\] Physical well-being violations are common safety violations, but we also include economic, social, emotional, and psychological well-being as important. Weighing fine differences among these categories is probably not possible, so we will not try. Each decision option lists examples of the effects that qualify for that value/answer in the various types of violations of well-being. These examples should not be considered comprehensive or exhaustive, but rather as suggestive.

The stakeholder should consider the safety impact on the operators\[33\] and users of the software they provide. If software is repackaged and resold by a stakeholder to further downstream entities who will then sell a product, the initial stakeholder can only reasonably consider so many links in that supply chain. But a stakeholder should know its immediate consumers one step away in the supply chain. Those consumers may repackage or build on the software and then provide that product further on.

We expect that a stakeholder should be aware of common usage of their software about two steps in the supply chain away. This expectation holds in both open source and proprietary contexts. Further steps along the supply chain are probably not reasonable for the stakeholder to consider consistently; however, this is not license to willfully ignore common downstream uses of the stakeholder’s software. If the stakeholder is contractually or legally responsible for safe operation of the software or cyber-physical system of which it is part, that also supersedes our rough supply-chain depth considerations. For software used in a wide variety of sectors and deployments, the stakeholder may need to estimate an aggregate safety impact. Aggregation suggests that the stakeholder’s response to this decision point cannot be less than the most severe plausible safety impact, but we leave the specific aggregation method or function as a domain-specific extension for future work.

#### Advice for Gathering Information to Answer the Safety Impact Question

The factors that influence the safety impact level are diverse. This paper does not exhaustively discuss how a stakeholder should answer a question; that is a topic for future work. At a minimum, understanding safety impact should include gathering information about survivability of the vulnerable component, determining available operator actions to compensate for the vulnerable component, understanding relevant insurance, and determining the viability of existing backup measures. Each of these information items depends heavily on domain-specific knowledge, and so it is out of the scope of this paper to give a general-purpose strategy for how they should be included. For example, viable manual backup mechanisms are likely important in assessing the safety impact of an industrial control system in a sewage plant, but in banking the insurance structures that prevent bankruptcies are more important.

Table 8: Safety Impact Decision Values

<table>
<thead>
<tr class="header">
<th><strong>Safety Impact</strong>[34]</th>
<th><strong>Type of Harm</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>None</td>
<td>All</td>
<td>Does not mean <em>no impact</em> literally; it just means that the effect is below the threshold for all aspects described in Minor</td>
</tr>
<tr class="even">
<td>Minor<br />
(Any one or more of these conditions hold.)</td>
<td>Physical harm</td>
<td>Physical discomfort for users (not operators) of the system</td>
</tr>
<tr class="odd">
<td></td>
<td>Operator<br />
resiliency</td>
<td>Requires action by system operator to maintain safe system state as a result of exploitation of the vulnerability where operator actions would be well within expected operator abilities; OR causes a minor occupational safety hazard</td>
</tr>
<tr class="even">
<td></td>
<td>System<br />
resiliency</td>
<td>Small reduction in built-in system safety margins; OR small reduction in system functional capabilities that support safe operation</td>
</tr>
<tr class="odd">
<td></td>
<td>Environment</td>
<td>Minor externalities (property damage, environmental damage, etc.) imposed on other parties</td>
</tr>
<tr class="even">
<td></td>
<td>Financial</td>
<td>Financial losses, which are not readily absorbable, to multiple persons</td>
</tr>
<tr class="odd">
<td></td>
<td>Psychological</td>
<td>Emotional or psychological harm, sufficient to be cause for counselling or therapy, to multiple persons</td>
</tr>
<tr class="even">
<td>Major<br />
(Any one or more of these conditions hold.)</td>
<td>Physical harm</td>
<td>Physical distress and injuries for users (not operators) of the system</td>
</tr>
<tr class="odd">
<td></td>
<td>Operator<br />
resiliency</td>
<td>Requires action by system operator to maintain safe system state as a result of exploitation of the vulnerability where operator actions would be within their capabilities but the actions require their full attention and effort; OR significant distraction or discomfort to operators; OR causes significant occupational safety hazard</td>
</tr>
<tr class="even">
<td></td>
<td>System<br />
resiliency</td>
<td>System safety margin effectively eliminated but no actual harm; OR failure of system functional capabilities that support safe operation</td>
</tr>
<tr class="odd">
<td></td>
<td>Environment</td>
<td>Major externalities (property damage, environmental damage, etc.) imposed on other parties</td>
</tr>
<tr class="even">
<td></td>
<td>Financial</td>
<td>Financial losses that likely lead to bankruptcy of multiple persons</td>
</tr>
<tr class="odd">
<td></td>
<td>Psychological</td>
<td>Widespread emotional or psychological harm, sufficient to be cause for counselling or therapy, to populations of people</td>
</tr>
<tr class="even">
<td>Hazardous<br />
(Any one or more of these conditions hold.)</td>
<td>Physical harm</td>
<td>Serious or fatal injuries, where fatalities are plausibly preventable via emergency services or other measures</td>
</tr>
<tr class="odd">
<td></td>
<td>Operator<br />
resiliency</td>
<td>Actions that would keep the system in a safe state are beyond system operator capabilities, resulting in adverse conditions; OR great physical distress to system operators such that they cannot be expected to operate the system properly</td>
</tr>
<tr class="even">
<td></td>
<td>System<br />
resiliency</td>
<td>Parts of the cyber-physical system break; system’s ability to recover lost functionality remains intact</td>
</tr>
<tr class="odd">
<td></td>
<td>Environment</td>
<td>Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties</td>
</tr>
<tr class="even">
<td></td>
<td>Financial</td>
<td>Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state</td>
</tr>
<tr class="odd">
<td></td>
<td>Psychological</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Catastrophic (Any one or more of these conditions hold.)</td>
<td>Physical harm</td>
<td>Multiple immediate fatalities (Emergency response probably cannot save the victims.)</td>
</tr>
<tr class="odd">
<td></td>
<td>Operator<br />
resiliency</td>
<td>Operator incapacitated (includes fatality or otherwise incapacitated)</td>
</tr>
<tr class="even">
<td></td>
<td>System resiliency</td>
<td>Total loss of whole cyber-physical system, of which the software is a part</td>
</tr>
<tr class="odd">
<td></td>
<td>Environment</td>
<td>Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties</td>
</tr>
<tr class="even">
<td></td>
<td>Financial</td>
<td>Social systems (elections, financial grid, etc.) supported by the software collapse</td>
</tr>
<tr class="odd">
<td></td>
<td>Psychological</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### System Exposure (Applier)
> The Accessible Attack Surface of the Affected System or Service

Measuring attack surface precisely is difficult, and we do not propose to perfectly delineate between small and controlled access. If a vulnerability cannot be patched, other mitigations may be used. Usually, the effect of these mitigations is to reduce exposure of the vulnerable component. Therefore, an applier’s response to Exposure may change if such mitigations are put in place. If a mitigation changes exposure and thereby reduces the priority of a vulnerability, that mitigation can be considered a success. Whether that mitigation allows the applier to defer further action varies according to each case.

Table 9: Exposure Decision Values

|  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Small       | Local service or program; highly controlled network                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Controlled  | Networked service with some access restrictions or mitigations already in place (whether locally or on the network). A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable both reliably and quickly enough to respond. *Controlled* covers the situation in which a vulnerability can be exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably execute it, then *exposure* should be *small*. |
| Unavoidable | Internet or another widely accessible network where access cannot plausibly be restricted or controlled (e.g., DNS servers, web servers, VOIP servers, email servers)                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Mission Impact (Applier)
> Impact on Mission Essential Functions\[35\] of the Organization

A `mission essential function (MEF)` is a function “directly related to accomplishing the organization’s mission as set forth in its statutory or executive charter” (footnote 35, page A-1). Identifying MEFs is part of business continuity planning or crisis planning. The rough difference between MEFs and non-essential functions is that an organization “must perform a\[n MEF\] during a disruption to normal operations” (footnote 35, page B-2). The mission is the reason an organization exists, and MEFs are how that mission is affected. Non-essential functions do not directly support the mission per se; however, they support the smooth delivery or success of MEFs. Financial losses—especially to publicly traded for-profit corporations—are covered here as a (legally mandated) mission of such corporations is financial performance.

Table 10: Mission Impact Decision Values

|  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| None                   | Little to no impact                                                                                                                                                       |
| Non-Essential Degraded | Degradation of non-essential functions; chronic degradation would eventually harm essential functions                                                                     |
| MEF Support Crippled   | Activities that directly support essential functions are crippled; essential functions continue for a time                                                                |
| MEF Failure            | Any one mission essential function fails for period of time longer than acceptable; overall mission of the organization degraded but can still be accomplished for a time |
| Mission Failure        | Multiple or all mission essential functions fail; ability to recover those functions degraded; organization’s ability to deliver its overall mission fails                |

#### Advice for Gathering Information to Answer the Mission Impact Question

The factors that influence the mission impact level are diverse. This paper does not exhaustively discuss how a stakeholder should answer a question; that is a topic for future work. At a minimum, understanding mission impact should include gathering information about the critical paths that involve vulnerable components, viability of contingency measures, and resiliency of the systems that support the mission. There are various sources of guidance on how to gather this information; see for example the FEMA guidance in Continuity Directive 2<sup>35</sup> or OCTAVE FORTE.\[36\] This is part of risk management more broadly. It should require the vulnerability management team to interact with more senior management to understand mission priorities and other aspects of risk mitigation.

As a heuristic, we suggest using the question described in Section 4.4.3, *Utility*, to constrain *Mission Impact*. If *Utility* is **super effective**, then *Mission Impact* is at least **MEF support crippled**. If *Utility* is **efficient**, then *Mission Impact* is at least **non-essential degraded**.

## Relationship to asset management

Our method is for prioritizing vulnerabilities based on the risk stemming from exploitation. There are other reasonable asset management considerations that may influence remediation timelines. There are at least three aspects of asset management that may be important but are out of scope for SSVC. First and most obvious is the transaction cost of conducting the mitigation or fix. System administrators are paid to develop or apply any fixes or mitigations, and there may be other transactional costs such as downtime for updates. Second is the risk of the fix or mitigation introducing a new error or vulnerability. Regression testing is part of managing this type of risk. Finally, there may be an operational cost of applying a fix or mitigation, representing an ongoing change of functionality or increased overhead. A decision maker could order work within one SSVC priority class (scheduled, out-of-band, etc.) based on these asset management considerations, for example. Once the organization fixes all the high-priority vulnerabilities, they can then fix the medium-level vulnerabilities with the same effort spent on the high-priority ones.

Asset management and risk management also drive some of the up-front work an organization would need to do to gather some of the necessary information. This situation is not new; an asset owner cannot prioritize which fixes to deploy to its assets if it does not know what assets it owns and their locations. The organization can pick its choice of tools for these things; there are about 200 asset management tools on the market.\[37\] Standards like the Software Bill of Materials (SBOM)\[38\] would likely reduce the burden on asset management, but these are still maturing. If an organization does not have an asset management or risk management (see Section 4.4.6.1) plan and process in place, then it will have a non-trivial amount of work to do to establish these processes before it can take full advantage of SSVC.

## Patch Developer Tree

Figure 1 shows the proposed prioritization decision tree for the patch developer. Both developer and applier trees use the above decision point definitions. Each tree is a compact way of expressing assertions or hypotheses about the relative priority of different situations. Each tree organizes how we propose a stakeholder should treat these situations. Rectangles are decision points, and triangles represent outcomes. The values for each decision point are different, as described above. Outcomes are priority decisions (defer, scheduled, out-of-band, immediate); outcome triangles are color coded:

  - Defer = gray with green outline
  - Scheduled = yellow
  - Out-of-Band = orange
  - Immediate = red with black outline

<img src="version_1/gfx/vul-management_v1-6-page2.png" alt="Figure 1: Suggested developer tree" style="width: 90%;" />

Figure 1: Proposed Vulnerability Prioritization Decision Tree for Patch
Developer

## Patch Applier Tree

The proposed patch applier tree is depicted in Figure 3, Figure 4, and Figure 5. The state of *Exploitation* is the first decision point, but in an effort to make the tree legible, we split the tree into three sub-trees over three pages. We suggest making the decision about *Exploitation* as usual, and then going to the correct subtree.

<img src="version_1/gfx/vul-management_v1-6-page3.png" alt="Figure 2" style="width: 90%;" />

Figure 2: Proposed Vulnerability Prioritization Decision Tree for Patch
Appliers (Continued in Figure 3 and Figure 4)

<img src="version_1/gfx/vul-management_v1-6-page4.png" alt="Figure 3" style="width: 90%;" />

Figure 3: Proposed Vulnerability Prioritization Decision Tree for Patch
Appliers (Continued from Figure 2 and in Figure 4).

<img src="version_1/gfx/vul-management_v1-6-page5.png" alt="Figure 4" style="width: 90%;" />

Figure 4: Proposed Vulnerability Prioritization Decision Tree for Patch
Appliers (Continued from Figure 2 and Figure 3)

## Evidence Gathering Guidance

To answer each of these decision points, a patch developer or patch applier should, as much as possible, have a repeatable evidence collection and evaluation process. However, we are proposing decisions for humans to make, so evidence collection and evaluation is not totally automatable. That caveat notwithstanding, some automation is possible.

For example, whether exploitation modules are available in ExploitDB, Metasploit, or other sources is straightforward. We hypothesize that searching Github and Pastebin for exploit code should be automatable. A developer or applier could then define *Exploitation* **PoC available** to be positive search results for a set of inputs derived from the CVE entry in at least one of these venues. At least, for those vulnerabilities that are not “automatically” PoC-ready, such as on-path attackers for TLS or network replays.

Some of the decision points require some substantial upfront analysis effort to gather risk assessment or organizational data. However, once gathered, this information can be efficiently reused across many vulnerabilities and only refreshed occasionally. An obvious example of this is the mission impact decision point. To answer this, a patch applier must analyze their essential functions, how they interrelate, and how they are supported. Exposure is similar; answering that decision point requires an asset inventory, adequate understanding of the network topology, and a view of the enforced security controls. Independently operated scans, such as Shodan or Shadowserver, may play a role in evaluating exposure, but the entire exposure question cannot be reduced to a binary question of whether an organization’s assets appear in such databases. Once the applier has the situational awareness to understand MEFs or exposure, selecting the answer for each individual vulnerability is usually straightforward.

Stakeholders who use the prioritization method should consider releasing the priority with which they handled the vulnerability. This disclosure has various benefits. For example, if the developer publishes a priority ranking, then appliers could consider that in their decision-making process. One reasonable way to include it is to break ties for the applier. If an applier has three “scheduled” vulnerabilities to patch, they may address them in any order. If two vulnerabilities were produced by the developer as “scheduled” patches, and one was “out-of-band,” then the applier may want to use that information to favor the latter.

In the case where no information is available or the organization has not yet matured its initial situational analysis, we can suggest something like defaults for some decision points. If the applier does not know their exposure,<!--lowercase exposure on purpose, this is the general concept--> that means they do not know where the devices are or how they are controlled, so they should assume *Exposure* is **unavoidable**. If the decision maker knows nothing about the environment in which the device is used, we suggest assuming a **major** *Safety Impact*. This position is conservative, but software is thoroughly embedded in daily life now, so we suggest that the decision maker provide evidence that no one’s well-being will suffer. The reach of software exploits is no longer limited to a research network. Similarly, with *Mission Impact*, the applier should assume that the software is in use at the organization for a reason, and that it supports essential functions unless they have evidence otherwise. With a total lack of information, assume **MEF support crippled** as a default. *Exploitation* needs no special default; if adequate searches are made for exploit code and none is found, the answer is **none**. The decision set {**none**, **unavoidable**, **MEF crippled**, **major**} results in a scheduled patch application.

## Development Methodology

Our initial starting point for the decision trees was different than what we present here. For example, we initially hypothesized different trees for different sectors (e.g., safety-critical, highly regulated, and everyone else). The initial trees also included additional decision points, such as developer’s patch distribution channels and financial loss to the applier of the vulnerability being exploited. We conducted informal evaluations of these trees by selecting a past CVE and discussing how each author would evaluate the priority of that vulnerability. This method quickly revealed some problems; we iterated this tabletop exercise until broad-scope problems stopped blocking our informal evaluations. We quickly reorganized the trees for different sectors into just one tree per role, for example, but with the new trees always asking the safety impact question. We also elaborated assumptions about scope and what safety and mission impact mean during this process. During this process, we also focused on decision trees for the patch developer and patch applier; we left the coordination decision for future work.

For this tabletop refinement, we could not select a mathematically representative set of CVEs. The goal was to select a handful of CVEs that would cover diverse types of vulnerabilities. The CVEs that we used for our tabletop exercises are CVE-2017-8083, CVE-2019-2712, CVE-2014-5570, and CVE-2017-5753. We discussed each one from the perspective of patch developer and patch applier. We evaluated CVE-2017-8083 twice because our understanding and descriptions had changed materially after the first three CVEs (six evaluation exercises). After we were satisfied that the decision trees were clearly defined and captured our intentions, we began the formal evaluation of the draft trees, which we describe in the next section.
