# What is SSVC?

## Intro

Risk exists on a continuum, and different stakeholders have different threat models and risk appetites. Cybersecurity risk is no exception.

Imagine you're a software developer, and you just found out about a vulnerability in a library upon which your product depends. You are now concerned that your software is also vulnerable. Upon investigation, you learn that your software does not use the vulnerable part of the imported library. Is your software, in its current state, at risk of this vulnerability? You likely answered, "probably not."

In this example, you are a Supplier of software that has an upstream Supplier vulnerability, but this vulnerability is not very risky to your business, so you are not very concerned. Conversely, the upstream Supplier probably wants the vulnerability patched as quickly as possible.

Unlike other vulnerability categorization systems that rate on technical severity (how bad it could be if the vulnerability were exploited) or exploitability (how likely it is that there will be an exploit), SSVC rates vulnerabilities on *risk* to the concerned stakeholder. It is not an attempted one-size-fits-all solution. SSVC follows a stakeholder-defined decision model to make these determinations of risk.

!!! note "Caveats"

    All information in this document is suggested following research, but we must reiterate: it is *not a one-size-fits-all* system. We encourage stakeholders to define to define their own decision points, timeframes of actionability, and possibly, even their own roles.

## Defining stakeholders

The above example includes a *Supplier* and a *Deployer*, and the third role is *Coordinator*. A stakeholder can be an individual or a group. It is possible for all three roles to exist within the same organization. Stakeholders are determined by their role in remidiation actions. For convenience, let's define these three:

- *Suppliers* distribute software, and maintenance of their product can include providing remediations (patches) or suggesting mitigations for the affected product.
- *Deployers* receive, evaluate, and apply the remediations or mitigations that the Suppliers provide.
- *Coordinators* receive vulnerability reports and decide how, and whether, additional coordination is needed to improve response to the vulnerability.

All three stakeholders, even if within the same organization, will have different perspectives on risk, and therefore have different decisions to make.

!!! note
    The three aforementioned roles are not exhaustive and are only the ones for which we have created decision models *so far*.

## How vulnerabilities are categorized in SSVC

SSVC categorizes vulnerabilities by priority based on risk that varies among stakeholders. These categories reflect the timeliness of action to be taken. Suppliers and Deployers have different end-categories than Coordinators because they are making different decisions at different points in their responses. [Decision Trees](../topics/decision_trees/) are used when asking the series of questions to categorize a vulnerability's priority. There will be more information on decision points (tree nodes) in the next section.

### Prioritization categories for Suppliers and Deployers

The following categories, listed in increasing order of priority, are suggested end-categories for how a Supplier or Deployer should respond to a vulnerability. The actual actions will differ between Supplier and Deployer, but their immediacy is similar. We provide these categories as examples and encourage Suppliers and Deployers to define prioritization categories that match their needs. We've found many places have a 4-level Service Level Expectation that maps onto our categories; however, if an organization uses fewer or more priority levels, they can adapt.

- *Defer*: do not act at present.
- *Scheduled*: work during regularly scheduled time with normal resource constraints.
- *Out-of-cycle*: act more quickly and potentially with extra resources than usual to resolve the vulnerability at the next available opportunity.
- *Immediate*: use all possible resources to mitigate the the vulnerability as quickly as possible, potentially including pausing normal operations.

Many Suppliers and Deployers will want to resolve *Defer* vulnerabilities in due time, perhaps within 90 days. *Defer* simply means 'do not act at present,' not 'do not act at all.'

### Prioritization categories for Coordinators

Our advice for Coordinators is based on the [CERT/CC Coordinated Vulnerability Disclosure (CVD) project](../howto/coordination_triage_decision/#coordinator-triage-units-of-work). Because we make separate decisions for triage and publication, we provide separate example decision tables, each of which has different prioritizations at the end. These decision tables represent how we apply SSVC to our needs, and other coordinators might make *different* decisions based on different inputs and output scales. The following categories are listed in increasing order of involvement.

A triage decision table might have:

- *Decline* to act on the report.
- *Track* information about the reported vulnerability, but do not take overt actions.
- *Coordinate* a response to the vulnerabilty report, potentially including technical analysis, reproduction, notifying vendors, publication, and assisting another party.

Whereas a publication decision table might have:

- *Don't publish* information about the vulnerability.
- *Publish* information about the vulnerability.

## How decision models are designed

All decision points and decision outcomes (priority categories) must be explainable to the non-expert. A decision point itself is not representative of risk, but the series of decisions point values help a stakeholder determine how risky a vulnerability is to their operation. We suggest the use of Decision Trees as a visual model to aid explanation to non-experts and experts alike.
While we encourage stakeholders to customize SSVC to their needs, in the interest of preserving a common vocabulary, we discourage stakeholders from modifying existing decision points; however, stakeholders are encouraged to set their responses based on their risk appetites.

### Supplier decision points

<embed src="../pdf/ssvc_2_supplier.pdf" alt="Suggested supplier tree" type="application/pdf"
style="width: 100%;"
height = "700" />

#### Exploitation

*Exploitation* refers to how much evidence currently exists that the vulnerability is being exploited. This value is mutable because new evidence of exploit can arise at any time.

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.exploitation import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

#### Utility

*Utility* is about how much an adversary might benefit (relative to effort) from an attack campaign via use of the vulnerability. In other words, Utility is a combination of the value of each exploit event (Value Density) and the ease and speed (Automatable) at which an adversary can cause exploit events.

*Value Density* is described as "diffuse" (the system has limited resources) or "concentrated" (the system is resource-rich).

*Automatable* is a simple yes or no, can the attacker reliably automate all four steps (reconnaissance, weaponization, delivery, exploitation) of the kill chain? If the vulnerability allows remote code execution or command injection, the expected response should be 'yes.'

We define the following combinations to determine *Utility* values:

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.utility import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

#### Technical Impact

*Technical Impact* refers to how much control of a system an attacker can gain. If 'yes' to any of the following questions, then the attacker has *Total* control of the system:

- can the attacker install and run arbitrary software?
- can the attacker trigger all the actions that the vulnerable component can perform?
- does the attacker get an account with full privileges to the vulnerable component (administrator or root user accounts, for example)?

If the answer is 'no' to all of the above questions, then the attack is presumed to gain *Partial* control of the system. Examples of *Partial* control include denial of service and memory address information leaks.

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.technical_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

#### Public Safety Impact

*Public Safety Impact* is a reduction of the more expansive *Safety Impact* decision point to *Signficant* or *Minimal*. If the highest category of *Safety Impact* is Marginal, Critical, or Catastrophic, then the *Public Safety Impact* is *Significant*. If no types of harm are more severe than Neglible, then the *Public Safety Impact* is *Minimal*.

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.public_safety_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

*Safety Impact* is expansive to include impacts of physical harm, operator resiliency, system resiliency, environment, financial, and psychological harm. We used IEC 61508 to guide determinations of Negligible, Marginal, Critical, and Catastrophic impact on the aforementioned types of harm. Only one type of harm needs to qualify per category. Use the highest qualifying category to determine safety impact.

*Safety Impact*

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.safety_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

### Deployer decision points

<embed src="../pdf/ssvc_2_deployer_SeEUMss.pdf" alt="Suggested deployer tree"
 type="application/pdf"
 style="width: 100%;"
 height = "1000"/>

#### Exploitation

*Exploitation* is the same as for Exploitation in the *Supplier* model.

#### Exposure

*Exposure* refers to how difficult it would be for an attacker to access a system from the open Internet. This will vary with configurations and is therefore determined on a per-system basis.

If a system is not 'Open', we suggest the following questions to guide your decision:

- If the system's networking and communication interfaces have been physically removed or disabled, choose *small*.
- If *Automatable* is *yes*, then choose *controlled*. The reasoning behind this heuristic is that if reconnaissance through exploitation is automatable, then the usual deployment scenario exposes the system sufficiently that access can be automated, which contradicts the expectations of *small*.
- If the vulnerable component is on a network where other hosts can browse the web or receive email, choose *controlled*.
- If the vulnerable component is in a third party library that is unreachable because the feature is unused in the surrounding product, choose *small*.

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.system_exposure import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

#### Automatable

*Automatable* is the same question as contained in the Supplier's Utility decision point.
For easy reference, *Automatable* is a simple yes or no, can the attacker reliably automate all four steps (reconnaissance, weaponization, delivery, exploitation) of the kill chain? If the vulnerability allows remote code execution or command injection, the expected response should be 'yes.'

#### Human Impact

*Human Impact* is similar to the Supplier's decision point *Public Safety Impact* in that it factors *Safety Impact*, but it differs in that it is a compound decision point to also consider *Mission Impact*.

For easy reference, the information on *Safety Impact* is again provided here:

*Safety Impact* is expansive to include impacts of physical harm, operator resiliency, system resiliency, environment, financial, and psychological harm. We used IEC 61508 to guide determinations of Negligible, Marginal, Critical, and Catastrophic impact on the aforementioned types of harm. Only one type of harm needs to qualify per category. Use the highest qualifying category to determine safety impact.

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.safety_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

*Mission Impact* is the impact on the Mission Essential Functions of the organization. A **mission essential function (MEF)** is a function “directly related to accomplishing the organization’s mission as set forth in its statutory or executive charter” [@FCD2_2017, page A-1].

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.mission_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

We define the following combinations of *Safety Impact* and *Mission Impact* values to determine *Human Impact* values:

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.human_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST, include_json=False))
```

### Coordinator decision points for Triage

<embed src="../pdf/ssvc_2_coord-triage.pdf" alt="Coordination Triage Tree" type="application/pdf"
style="width: 100%;"
height = "700" />

The below decision points are  modeled on [CERT/CC Coordinated Vulnerability Disclosure (CVD) practice](../howto/coordination_triage_decision/#coordinator-triage-decision-outcomes), but we encourage Coordinators to define their own criteria for Triage.

The first two questions help the CERT/CC determine if our help is required.

- [Report Public](reference/decision_points/report_public.md): If a report is already public, then CERT/CC will decline the case unless there are multiple suppliers, [*super effective*](reference/decision_points/system_exposure.md) [Utility](reference/decision_points/utility.md), and [*significant*](reference/decision_points/public_safety_impact.md) [Public Safety Impact](reference/decision_points/public_safety_impact.md).
- [Supplier Contacted](reference/decision_points/supplier_contacted.md): If no suppliers have been contacted, then CERT/CC will decline the case unless there are multiple suppliers, [*super effective*](reference/decision_points/system_exposure.md) [Utility](reference/decision_points/utility.md), and [*significant*](reference/decision_points/public_safety_impact.md) [Public Safety Impact](reference/decision_points/public_safety_impact.md).
  In this case, CERT/CC may encourage the reporter to contact the supplier and submit a new case request if the supplier is unresponsive.
- [Report Credibility](reference/decision_points/report_credibility.md): If the report is not credible, then CERT/CC will decline the case.
Please see the [CERT® Guide to Coordinated Vulnerability Disclosure](https://certcc.github.io/CERT-Guide-to-CVD/howto/coordination/_report_credibility) for more information about assessing credibility.
- [Supplier Cardinality](reference/decision_points/supplier_cardinality.md): Cases involving multiple suppliers can get complicated very quickly, so we are more likely to get involved in those cases.
- [Supplier Engagement](reference/decision_points/supplier_engagement.md): If the suppliers are already engaged in a case, there is usually less for a coordinator to do, making it less likely that we will coordinate a case.
- [Utility](reference/decision_points/utility.md): If the vulnerability has high utility, then CERT/CC is more likely to coordinate the case.
- [Public Safety Impact](reference/decision_points/public_safety_impact.md): If the vulnerability has significant
   public safety impact, then CERT/CC is more likely to coordinate the case.

The last two questions, *Utility* and *Public Safety Impact*, are the same as asked in the Supplier decision model.

### Coordinator decision points for Publication

<embed src="../pdf/ssvc_2_coord-publish.pdf" alt="Suggested tree for a coordinator's publication decision" type="application/pdf"
style="width: 100%;"
height = "600" />

At the CERT/CC, a decision to publish is determined after criteria for Publication are met. SSVC adds value by codifying publication criteria so that the decision is explainable. Publishing a vulnerability should add public value, and a Coordinator must decide why they should publish instead of or in addition to the Supplier. Again, the below decision points are modeled on the [CERT/CC Coordinated Vulnerability Disclosure (CVD) project](../howto/coordination_triage_decision/#coordinator-triage-units-of-work), but we encourage Coordinators to define their own rationales for publication based on their missions.

The publication decision reuses the [*Exploitation*](reference/decision_points/exploitation.md) decision point and adds two new ones ([*Supplier Involvement*](reference/decision_points/supplier_involvement.md) and [*Public Value Added*](reference/decision_points/public_value_added.md)).

!!! tip inline end

    *Exploitation* was first described in this document under the *Supplier* model, and the definition is the same regardless of the stakeholder.

- [Supplier Involvement](reference/decision_points/supplier_involvement.md) - If the supplier is involved and likely to publish already, there is less need for the CERT/CC to publish.
- [Exploitation](reference/decision_points/exploitation.md) - If the vulnerability is being actively exploited, the CERT/CC is more likely to publish.

- [Public Value Added](reference/decision_points/public_value_added.md) - If there is already significant public discussion of the vulnerability, there might not be much for the CERT/CC to add, making us less likely to publish.

!!! note "What is the difference between *Supplier Engagement* and *Supplier Involvement*?"

    *Supplier Engagement*, asks whether a Supplier has acknowledged the vulnerability and is participating in the coordination effort.
    *Supplier Involvement*, asks what, if anything, the Supplier is doing about the vulnerability.

## Final notes

SSVC enables different stakeholders to make determinations about how a vulnerability will impact them, how to respond to a vulnerability, and how to communicate and explain their decisions. Unlike other vulnerability scoring systems, SSVC evaluates risk to a particular stakeholder without imposing a one-size-fits-all approach. The below subsections describe some other details about SSVC's features and provide links to further reading about SSVC and CVD.

### Multiple vulnerabilities of the same priority

Naturally, a stakeholder will have multiple vulnerabilities at any given time, and it is likely that there will be multiple vulnerabilities of the same priority. The stakeholder can choose how to order vulnerabilities within the same priority- vulnerabilities of the same priority can be addressed in *any* order.

### Communicating results

Coordinators will be especially concerned with communicating information about vulnerabilities, but Suppliers will be just as concerned about communicating to Deployers. Because information changes over time, SSVC decisions should always be timestamped and marked with the version of SSVC that was used. We provide a self-contained, machine-readable [JSON schema](../howto/bootstrap/use/).

### Further reading

[Reference material](../reference/)

[Guidance for customizing a Decision Tree](../howto/tree_customization)
