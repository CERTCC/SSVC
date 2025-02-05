# What is SSVC

## Intro

Risk exists on a continuum, and different stakeholders have different threat models and risk appetites.

Take, for example, an exported software library that contains many functions, one of which is vulnerable to SQL injection. Your software imports this library but does not use this vulnerable function. Is your software, in its current state, at risk of this vulnerability? You likely answered, "probably not."
In this example, you are the _Deployer_ of software that contains a vulnerability, but this vulnerability is not very risky to your business, so you are not very concerned. Conversely, the exported software library's owner is the _Supplier_, and they probably want the vulnerability patched as quickly as possible.

Unlike other vulnerability categorization systems that rate on technical severity (how bad it could be if the vulnerability were exploited) or exploitability (how likely it is that there will be an exploit), SSVC rates vulnerabilities on _risk_ to the concerned stakeholder. It is not an attempted one-size-fits-all solution. SSVC follows a stakeholder-defined algorithm to make these determinations of risk.

### Caveats

All information in this document is suggested following research, but we must reiterate: it is _not a one-size-fits-all_ system. We encourage stakeholders to define to define their own decision points, timeframes of actionability, and possibly, even their own roles.

## Defining stakeholders

The above example includes a _Supplier_ and a _Deployer_, and the third category is _Coordinator_. A stakeholder can be an individual or a group. It is possible for all three categories to exist within the same organization. Stakeholder roles are determined by their role in remidiation actions. For convenience, let's define all three:

* _Suppliers_ provide remediations (patches) or suggest mitigations for their affected products.
* _Deployers_ apply the remediations or mitigations that the Suppliers provide.
* _Coordinators_ receive vulnerability reports and decide how to respond.

All three stakeholders, even if within the same organization, will have different opinions on risk, and therefore have different decisions to make. 

## How vulnerabilities are categorized

Following a series of decisions based on a stakeholder's threat model and risk appetite, a vulnerability is categorized based on how risky it is, in other words, priority. These categories reflect the timeliness of action to be taken. Suppliers and Deployers have different end-categories than Coordinators. [Decision Trees](https://certcc.github.io/SSVC/topics/decision_trees/) are used when asking the series of questions to categorize a vulnerability's priority. There will be more information on decision points (tree nodes) in the next section.

### Priority categorizations for Suppliers and Deployers

The following categories, listed in increasing order of priority, are the suggested end-categories for how a Supplier or Deployer should respond to a vulnerability. The actual actions will differ between Supplier and Deployer, but their immediacy is similar.

* _Defer_: do not act at present.
* _Scheduled_: work during regularly scheduled time with normal resource constraints.
* _Out-of-cycle_: act more quickly and potentially with extra resources than usual to resolve the vulnerability at the next available opportunity.
* _Immediate_: use all possible resources to mitigate the the vulnerability as quickly as possible, potentially including pausing normal operations.

Many Suppliers and Deployers will want to resolve _Defer_ vulnerabilities in due time, perhaps within 90 days. _Defer_ simply means 'do not act at present,' not 'do not act at all.'

### Priority categorizations for Coordinators

Because Coordinators make separate decisions for triage and publication, we recommend separate trees, each of which has different prioritizations at the end. Our advice for Coordinators is based on the [CERT/CC Coordinated Vulnerability Disclosure (CVD) project](https://certcc.github.io/SSVC/howto/coordination_triage_decision/#coordinator-triage-units-of-work). The following categories are listed in increasing order of involvement.

A triage tree might have:

* _Decline_ to act on the report.
* _Track_ information about the reported vulnerability, but do not take overt actions.
* _Coordinate_ a response to the vulnerabilty report, potentially including technical analysis, reproduction, notifying vendors, publication, and assisting another party.

Whereas a publication tree might have:

* _Don't publish_ information about the vulnerability.
* _Publish_ information about the vulnerability.

## How decision trees are designed

All decision points and end decisions (priority categories) must be explainable to the non-expert. A decision point itself is not representative of risk, but the series of decisions help a stakeholder determine how risky a vulnerability is to their operation. We suggest use of Decision Trees as a visual model to aid explanation to non-experts and experts alike. While we encourage stakeholders to customize SSVC to their needs, we do not advise changing any of the following decision points, their definitions, nor their values in order to enforce a common vocabulary; however, stakeholders are encouraged to set their responses based on their risk appetites.

### Supplier decision points

[image of supplier decision tree]

#### Exploitability

_Exploitability_ is about how easy it would be to start an attack campaign or if one is already underway. The value refers to how much evidence currently exists that the vulnerability is being exploited. This value is mutable.

| Value | Definition |
|:-----|:-----------|
| None | There is no evidence of active exploitation and no public proof of concept (PoC) of how to exploit the vulnerability. |
| Public PoC | One of the following is true: (1) Typical public PoC exists in sources such as Metasploit or websites like ExploitDB; or (2) the vulnerability has a well-known method of exploitation. |
| Active | Shared, observable, reliable evidence that the exploit is being used in the wild by real attackers; there is credible public reporting. |

#### Utility

_Utility_ is about how much an adversary might benefit (relative to effort) from an attack campaign via use of the vulnerability. In other words, Utility is a combination of the value of each exploit event (Value Density) and the ease and speed (Automability) at which an adversary can cause exploit events.

_Value Density_ is described as "diffuse" (the system has limited resources) or "concentrated" (the system is resource-rich).

_Automability_ is a simple yes or no, can the attacker reliably automate all four steps (reconnaissance, weaponization, delivery, exploitation) of the kill chain? If the vulnerability allows remote code execution or command injection, the expected response should be 'yes.'

We propose the following combinatorics to determine _Utility_ values:

| Value | Definition |
|:-----|:-----------|
| Laborious | Automatable:No AND Value Density:Diffuse |
| Efficient | (Automatable:Yes AND Value Density:Diffuse) OR (Automatable:No AND Value Density:Concentrated) |
| Super Effective | Automatable:Yes AND Value Density:Concentrated |

#### Technical Impact

_Technical Impact_ refers to how much control of a system an attacker can gain. If 'yes' to any of the following questions, then the attacker has _Total_ control of the system:

- can the attacker install and run arbitrary software?
- can the attacker trigger all the actions that the vulnerable component can perform?
- does the attacker get an account with full privileges to the vulnerable component (administrator or root user accounts, for example)?

If the answer is 'no' to all of the above questions, then the attack is presumed to gain _Partial_ control of the system. Examples of _Partial_ control include denial of service and memory address information leaks.

| Value | Definition |
|:-----|:-----------|
| Partial | The exploit gives the adversary limited control over, or information exposure about, the behavior of the software that contains the vulnerability. Or the exploit gives the adversary an importantly low stochastic opportunity for total control. |
| Total | The exploit gives the adversary total control over the behavior of the software, or it gives total disclosure of all information on the system that contains the vulnerability. |

#### Public Safety Impact

_Public Safety Impact_ is a reduction of _Safety Impact_ to _Signficant_ or _Minimal_. If the highest category of _Safety Impact_ is Marginal, Critical, or Catastrophic, then the _Public Safety Impact_ is _Significant_. If no types of harm are more severe than Neglible, then the _Public Safety Impact_ is _Minimal_.

_Safety Impact_ is expansive to include impacts of physical harm, operator resiliency, system resiliency, environment, financial, and psychological harm. We used IEC 61508 to guide determinations of Negligible, Marginal, Critical, and Catastrophic impact on the aforementioned types of harm. Only one type of harm needs to qualify per category. Use the highest qualifying category to determine safety impact. 
 
_Safety Impact_ 

| Value | Definition |
|:-----|:-----------|
| Negligible | Any one or more of these conditions hold.<br/><br/>- *Physical harm*: Minor injuries at worst (IEC 61508 Negligible).<br/>- *Operator resiliency*: Requires action by system operator to maintain safe system state as a result of exploitation of the vulnerability where operator actions would be well within expected operator abilities; OR causes a minor occupational safety hazard.<br/>- *System resiliency*: Small reduction in built-in system safety margins; OR small reduction in system functional capabilities that support safe operation.<br/>- *Environment*: Minor externalities (property damage, environmental damage, etc.) imposed on other parties.<br/>- *Financial*: Financial losses, which are not readily absorbable, to multiple persons.<br/>- *Psychological*: Emotional or psychological harm, sufficient to be cause for counselling or therapy, to multiple persons. |
| Marginal | Any one or more of these conditions hold.<br/><br/>- *Physical harm*: Major injuries to one or more persons (IEC 61508 Marginal).<br/>- *Operator resiliency*: Requires action by system operator to maintain safe system state as a result of exploitation of the vulnerability where operator actions would be within their capabilities but the actions require their full attention and effort; OR significant distraction or discomfort to operators; OR causes significant occupational safety hazard.<br/>- *System resiliency*: System safety margin effectively eliminated but no actual harm; OR failure of system functional capabilities that support safe operation.<br/>- *Environment*: Major externalities (property damage, environmental damage, etc.) imposed on other parties.<br/>- *Financial*: Financial losses that likely lead to bankruptcy of multiple persons.<br/>- *Psychological*: Widespread emotional or psychological harm, sufficient to be cause for counselling or therapy, to populations of people. |
| Critical | Any one or more of these conditions hold.<br/><br/>- *Physical harm*: Loss of life (IEC 61508 Critical).<br/>- *Operator resiliency*: Actions that would keep the system in a safe state are beyond system operator capabilities, resulting in adverse conditions; OR great physical distress to system operators such that they cannot be expected to operate the system properly.<br/>- *System resiliency*: Parts of the cyber-physical system break; system’s ability to recover lost functionality remains intact.<br/>- *Environment*: Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties.<br/>- *Financial*: Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state.<br/>- *Psychological*: N/A. |
| Catastrophic | Any one or more of these conditions hold.<br/><br/>- *Physical harm*: Multiple loss of life (IEC 61508 Catastrophic).<br/>- *Operator resiliency*: Operator incapacitated (includes fatality or otherwise incapacitated).<br/>- *System resiliency*: Total loss of whole cyber-physical system, of which the software is a part.<br/>- *Environment*: Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties.<br/>- *Financial*: Social systems (elections, financial grid, etc.) supported by the software collapse.<br/>- *Psychological*: N/A. |

_Public Safety Impact_

| Value | Definition |
|:-----|:-----------|
| Minimal | Safety Impact:Negligible |
| Significant | Safety Impact:(Marginal OR Critical OR Catastrophic) |

### Deployer decision points

[image of deployer decision tree]

#### Exploitability

_Exploitability_ is the same as for Supplier Exploitability.

#### Exposure

_Exposure_ refers to how much of a particular system is open to network access; in other words, the system provides service to the Internet. This will vary with configurations and is therefore determined on a per-system basis.

If a system is not 'Open', we suggest the following questions to guide your decision:

 - If the system's networking and communication interfaces have been physically removed or disabled, choose *small*.
 - If [*Automatable*](automatable.md) is *yes*, then choose *controlled*. The reasoning behind this heuristic is that if reconnaissance through exploitation is automatable, then the usual deployment scenario exposes the system sufficiently that access can be automated, which contradicts the expectations of *small*.
 - If the vulnerable component is on a network where other hosts can browse the web or receive email, choose *controlled*.
 - If the vulnerable component is in a third party library that is unreachable because the feature is unused in the surrounding product, choose *small*.

The Accessible Attack Surface of the Affected System or Service

| Value | Definition |
|:-----|:-----------|
| Small | Local service or program; highly controlled network |
| Controlled | Networked service with some access restrictions or mitigations already in place (whether locally or on the network). A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable both reliably and quickly enough to respond. Controlled covers the situation in which a vulnerability can be exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably execute it, then exposure should be small. |
| Open | Internet or another widely accessible network where access cannot plausibly be restricted or controlled (e.g., DNS servers, web servers, VOIP servers, email servers) |

#### Automability

_Automability_ is the same question as contained in the Supplier's Utility decision point.
For easy reference, _Automability_ is a simple yes or no, can the attacker reliably automate all four steps (reconnaissance, weaponization, delivery, exploitation) of the kill chain? If the vulnerability allows remote code execution or command injection, the expected response should be 'yes.'

#### Human Impact

_Human impact_ is similar to the Supplier's decision point _Public Safety Impact_ in that it factors _Safety Impact_, but it differs in that it is a compound decision point to also consider _Mission Impact_.

For easy reference, the information on _Safety Impact_ is again provided here:

_Safety Impact_ is expansive to include impacts of physical harm, operator resiliency, system resiliency, environment, financial, and psychological harm. We used IEC 61508 to guide determinations of Negligible, Marginal, Critical, and Catastrophic impact on the aforementioned types of harm. Only one type of harm needs to qualify per category. Use the highest qualifying category to determine safety impact. 
 
_Safety Impact_ 

| Value | Definition |
|:-----|:-----------|
| Negligible | Any one or more of these conditions hold.<br/><br/>- *Physical harm*: Minor injuries at worst (IEC 61508 Negligible).<br/>- *Operator resiliency*: Requires action by system operator to maintain safe system state as a result of exploitation of the vulnerability where operator actions would be well within expected operator abilities; OR causes a minor occupational safety hazard.<br/>- *System resiliency*: Small reduction in built-in system safety margins; OR small reduction in system functional capabilities that support safe operation.<br/>- *Environment*: Minor externalities (property damage, environmental damage, etc.) imposed on other parties.<br/>- *Financial*: Financial losses, which are not readily absorbable, to multiple persons.<br/>- *Psychological*: Emotional or psychological harm, sufficient to be cause for counselling or therapy, to multiple persons. |
| Marginal | Any one or more of these conditions hold.<br/><br/>- *Physical harm*: Major injuries to one or more persons (IEC 61508 Marginal).<br/>- *Operator resiliency*: Requires action by system operator to maintain safe system state as a result of exploitation of the vulnerability where operator actions would be within their capabilities but the actions require their full attention and effort; OR significant distraction or discomfort to operators; OR causes significant occupational safety hazard.<br/>- *System resiliency*: System safety margin effectively eliminated but no actual harm; OR failure of system functional capabilities that support safe operation.<br/>- *Environment*: Major externalities (property damage, environmental damage, etc.) imposed on other parties.<br/>- *Financial*: Financial losses that likely lead to bankruptcy of multiple persons.<br/>- *Psychological*: Widespread emotional or psychological harm, sufficient to be cause for counselling or therapy, to populations of people. |
| Critical | Any one or more of these conditions hold.<br/><br/>- *Physical harm*: Loss of life (IEC 61508 Critical).<br/>- *Operator resiliency*: Actions that would keep the system in a safe state are beyond system operator capabilities, resulting in adverse conditions; OR great physical distress to system operators such that they cannot be expected to operate the system properly.<br/>- *System resiliency*: Parts of the cyber-physical system break; system’s ability to recover lost functionality remains intact.<br/>- *Environment*: Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties.<br/>- *Financial*: Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state.<br/>- *Psychological*: N/A. |
| Catastrophic | Any one or more of these conditions hold.<br/><br/>- *Physical harm*: Multiple loss of life (IEC 61508 Catastrophic).<br/>- *Operator resiliency*: Operator incapacitated (includes fatality or otherwise incapacitated).<br/>- *System resiliency*: Total loss of whole cyber-physical system, of which the software is a part.<br/>- *Environment*: Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties.<br/>- *Financial*: Social systems (elections, financial grid, etc.) supported by the software collapse.<br/>- *Psychological*: N/A. |

_Mission Impact_ is the impact on the Mission Essential Functions of the organization. A **mission essential function (MEF)** is a function “directly related to accomplishing the organization’s mission as set forth in its statutory or executive charter” [@FCD2_2017, page A-1]. 

Impact on Mission Essential Functions of the Organization

| Value | Definition |
|:-----|:-----------|
| Degraded | Little to no impact up to degradation of non-essential functions; chronic degradation would eventually harm essential functions |
| MEF Support Crippled | Activities that directly support essential functions are crippled; essential functions continue for a time |
| MEF Failure | Any one mission essential function fails for period of time longer than acceptable; overall mission of the organization degraded but can still be accomplished for a time |
| Mission Failure | Multiple or all mission essential functions fail; ability to recover those functions degraded; organization’s ability to deliver its overall mission fails |

We propose the following combinatorics of _Safety Impact_ and _Mission Impact_ values to determine _Human Impact_ values:

| Value | Definition |
|:-----|:-----------|
| Low | Safety Impact:(Negligible) AND Mission Impact:(None OR Degraded OR Crippled) |
| Medium | (Safety Impact:Negligible AND Mission Impact:MEF Failure) OR (Safety Impact:Marginal AND Mission Impact:(None OR Degraded OR Crippled)) |
| High | (Safety Impact:Critical AND Mission Impact:(None OR Degraded OR Crippled)) OR (Safety Impact:Marginal AND Mission Impact:MEF Failure) |
| Very High | Safety Impact:Catastrophic OR Mission Impact:Mission Failure |

### Coordinator decision points for Triage

[image of triage decision tree]

The below decision points are  modeled on [CERT/CC Coordinated Vulnerability Disclosure (CVD) project](https://certcc.github.io/SSVC/howto/coordination_triage_decision/#coordinator-triage-units-of-work), but we encourage Coordinators to define their own reasons to engage in Triage.

Generally speaking, we believe in Supplier agency, and is why the first two questions are about damage control.

- [Report Public](../reference/decision_points/report_public.md): If a report is already public, then CERT/CC will decline the case unless there are multiple suppliers, [*super effective*](../reference/decision_points/system_exposure.md) [Utility](../reference/decision_points/utility.md), and [*significant*](../reference/decision_points/public_safety_impact.md) [Public Safety Impact](../reference/decision_points/public_safety_impact.md).
- [Supplier Contacted](../reference/decision_points/supplier_contacted.md): If no suppliers have been contacted, then CERT/CC will decline the case unless there are multiple suppliers, [*super effective*](../reference/decision_points/system_exposure.md) [Utility](../reference/decision_points/utility.md), and [*significant*](../reference/decision_points/public_safety_impact.md) [Public Safety Impact](../reference/decision_points/public_safety_impact.md). 
  In this case, CERT/CC may encourage the reporter to contact the supplier and submit a new case request if the supplier is unresponsive.
- [Report Credibility](../reference/decision_points/report_credibility.md): If the report is not credible, then CERT/CC will decline the case.
Please see the [CERT® Guide to Coordinated Vulnerability Disclosure](https://certcc.github.io/CERT-Guide-to-CVD/howto/coordination/_report_credibility/?h=credibilit) for more information about assessing credibility.
- [Supplier Cardinality](../reference/decision_points/supplier_cardinality.md): Cases involving multiple suppliers can get complicated very quickly, so we are more likely to get involved in those cases. 
- [Supplier Engagement](../reference/decision_points/supplier_engagement.md): If the suppliers are already engaged in a case, there is usually less for a coordinator to do, making it less likely that we will coordinate a case.
- [Utility](../reference/decision_points/utility.md): If the vulnerability has high utility, then CERT/CC is more likely to coordinate the case.
- [Public Safety Impact](../reference/decision_points/public_safety_impact.md): If the vulnerability has significant 
   public safety impact, then CERT/CC is more likely to coordinate the case.

The last two questions, _Utility_ and _Public Safety Impact_, are the same as asked in the Supplier tree.

### Coordinator decision points for Publication

[image of publication decision tree]

A decision to publish is determined after criteria for Publication are met. SSVC adds value by codifying publication criteria so that the decision is explainable. Publishing a vulnerability should add public value, and a Coordinator must decide why they should publish instead of or in addition to the Supplier. Again, the below decision points are modeled on the [CERT/CC Coordinated Vulnerability Disclosure (CVD) project](https://certcc.github.io/SSVC/howto/coordination_triage_decision/#coordinator-triage-units-of-work), but we encourage Coordinators to define their own rationales for publication.


The publication decision reuses the [*Exploitation*](../reference/decision_points/exploitation.md) decision point and adds two new ones ([*Supplier Involvement*](../reference/decision_points/supplier_involvement.md) and [*Public Value Added*](../reference/decision_points/public_value_added.md)).

- [*Supplier Involvement*](../reference/decision_points/supplier_involvement.md) - If the supplier is involved and likely to publish already, there is less need for the CERT/CC to publish.
- [*Exploitation*](../reference/decision_points/exploitation.md) - If the vulnerability is being actively exploited, the CERT/CC is more likely to publish. Exploitation has the same values as Supplier Exploitability.
- [*Public Value Added*](../reference/decision_points/public_value_added.md) - If there is already significant public discussion of the vulnerability, there might not be much for the CERT/CC to add, making us less likely to publish. 


## Final notes

SSVC enables different stakeholders to make determinations about how a vulnerability will impact them, how to respond to a vulnerability, and how to communicate and explain their decisions. Unlike existing vulnerability scoring systems, SSVC evaluates risk to a particular stakeholder without imposing a one-size-fits-all approach. The below subsections describe some other details about SSVC's features and provide links to further reading about SSVC and CVD.

### Multiple vulnerabilities of the same priority

Naturally, a stakeholder will have multiple vulnerabilities at any given time, and it is likely that there will be multiple vulnerabilities of the same priority. The stakeholder can choose how to order vulnerabilities within the same priority- vulnerabilities of the same priority can be addressed in _any_ order.


### Communicating results

Coordinators will be especially concerned with communicating information about vulnerabilities, but Suppliers will be just as concerned about communicating to Deployers. Because information changes over time, SSVC decisions should always be timestamped and marked with the version of SSVC that was used. We provide a self-contained, machine-readable [JSON schema]() and an abbreviated ["vector string" notation](). Please note that while the JSON schema can be compressed to an abbreviated vector string, we do not currently support converting from an abbreviated vector string to the full JSON schema.

### Further reading

[Links to Tutorial, How-to, Reference...]

[Guidance for customizing a Decision Tree](https://certcc.github.io/SSVC/howto/tree_customization)
