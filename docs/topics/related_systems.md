
# Related Vulnerability Management Systems

There are several other bodies of work that are used in practice to assist vulnerability managers in making decisions.
Three relevant systems are CVSS [@cvss_v3-1], EPSS [@jacobs2021epss], and Tenable's Vulnerability Priority Rating ([VPR](https://www.tenable.com/blog/what-is-vpr-and-how-is-it-different-from-cvss)).
There are other systems derived from CVSS, such as RVSS for robots [@vilches2018towards] and MITRE's effort to adapt CVSS to medical devices [@mitre2019medical].
There are also other nascent efforts to automate aspects of the decision making process, such as [vPrioritizer](https://github.com/varchashva/vPrioritizer).
This section discusses the relationship between these various systems and SSVC.

## CVSS

{% include-markdown "../_includes/_cvss4_question.md" heading-offset=1 %}

CVSS version 3.1 has three metric groups: base, environmental, and temporal.
The metrics in the base group are all required, and are the only required metrics.
In connection with this design, CVSS base scores and base metrics are far and away the most commonly used and communicated.
A CVSS base score has two parts: the exploitability metrics and the impact metrics.
Each of these are echoed or reflected in aspects of SSVC, though the breadth of topics considered by SSVC is wider than CVSS version 3.1.

How CVSS is used matters.
Using just the base scores, which are “the intrinsic characteristics of a vulnerability that are constant over time and across user environments,” as a stand-alone prioritization method is not recommended [@cvss_v3-1].
Two examples of this include the U.S. government [see @nist800-115, p. 7-4; @nist800-40r3, p. 4; and @bod15-01] and the global payment card industry [@pcidss_v3] where both have defined such misuse as expected practice in their vulnerability management requirements.
CVSS scores have a complex relationship with patch deployment in situations where it is not mandated, at least in an ICS context [@wang2017characterizing].

CVSS has struggled to adapt to other stakeholder contexts.
Various stakeholder groups have expressed dissatisfaction by making new versions of CVSS, such as medical devices [@mitre2019medical], robotics [@vilches2018towards], and industrial systems [@figueroa2020survey].
In these three examples, the modifications tend to add complexity to CVSS by adding metrics.
Product vendors have varying degrees of adaptation of CVSS for development prioritization, including but not limited to [Red Hat](https://access.redhat.com/security/updates/classification), [Microsoft](https://www.microsoft.com/en-us/msrc/security-update-severity-rating-system), and [Cisco](https://tools.cisco.com/security/center/resources/security_vulnerability_policy.html).
The vendors codify CVSS’s recommended qualitative severity rankings in different ways, and Red Hat and Microsoft make the user interaction base metric more important.

### Exploitability metrics (Base metric group)

The four metrics in this group are Attack Vector, Attack Complexity, Privileges Required, and User Interaction.
This considerations may likely be involved in the [Automatability](../reference/decision_points/automatable.md) decision point.
If Attack Vector = Network and Privileges Required = None, then the delivery phase of the kill chain is likely to be automatable.
Attack Vector may also be correlated with the [Exposure](../reference/decision_points/system_exposure.md) decision point.
Attack Complexity may influence how long it may take an adversary to craft an automated exploit, but [Automatability](../reference/decision_points/automatable.md) only asks whether exploitation can be automated, not how difficult it was.
However, Attack Complexity may influence the weaponization phase of the kill chain.
User Interaction does not cleanly map to a decision point.
In general, SSVC does not care whether a human is involved in exploitation of the vulnerability or not.
Some human interaction is for all intents and purposes automatable by attackers: most people click on links in emails as part of their normal processes.
In most such situations, user interaction does not present a firm barrier to automatability; it presents a stochastic barrier.
[Automatability](../reference/decision_points/automatable.md) is written to just consider firm barriers to automation.

[Automatability](../reference/decision_points/automatable.md) includes considerations that are not included in the exploitability metrics.
Most notably the concept of vulnerability chaining is addressed in [Automatability](../reference/decision_points/automatable.md) but not addressed anywhere in CVSS.
[Automatability](../reference/decision_points/automatable.md) is also outcomes focused.
A vulnerability is evaluated based on an observable outcome of whether the first four steps of the kill chain can be automated for it.
A proof of automation in a relevant environment is an objective evaluation of the score in a way that cannot be provided for some CVSS elements, such as Attack Complexity.

### Impact metrics (Base metric group)

The metrics in this group are Confidentiality, Integrity, and Availability.
There is also a loosely associated Scope metric.
The CIA impact metrics are directly handled by [*Technical Impact*](../reference/decision_points/technical_impact.md).

Scope is a difficult CVSS metric to categorize.
The specification describes it as “whether a vulnerability in one vulnerable component impacts resources in components beyond its security scope” [@cvss_v3-1].
This is a fuzzy concept.
SSVC better describes this concept by breaking it down into component parts.
The impact of exploitation of the vulnerable component on other components is covered under [*Mission Impact*](../reference/decision_points/mission_impact.md), public and situated [*Well-being Impact*](../reference/decision_points/human_impact.md), and the stakeholder-specific nature where SSVC is tailored to stakeholder concerns.
CVSS addresses some definitions of the scope of CVSS as a whole under the Scope metric definition.
In SSVC, these definitions are in the [Scope](scope.md) section.

### Temporal metric groups

The temporal metric group primarily contains the Exploit Code Maturity metric.
This metric expresses a concept similar to [*Exploitation*](../reference/decision_points/exploitation.md).
The main difference is that [*Exploitation*](../reference/decision_points/exploitation.md) is not optional in SSVC and that SSVC accounts for the observation that most vulnerabilities with CVE-IDs do not have public exploit code [@householder2020historical] and are not actively exploited [@guido2011exploit,@jacobs2021epss].

### Environmental metric group

The environmental metric group allows a consumer of a CVSS base score to change it based on their environment.
CVSS needs this functionality because the organizations that produce CVSS scores tend to be what SSVC calls **suppliers** and consumers of CVSS scores are what SSVC calls **deployers**.
These two stakeholder groups have a variety of natural differences, which is why SSVC treats them separately.
SSVC does not have such customization as a bolt-on optional metric group because SSVC is stakeholder-specific by design.

## EPSS

The [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/) is “a data-driven effort for estimating the likelihood (probability) that a software vulnerability will be exploited in the wild.”
EPSS is currently based on a machine-learning classifier and proprietary data from Fortiguard, Alienvault OTX, the Shadowserver Foundation and GreyNoise.
While the group has made an effort to make the ML classifier transparent, ML classifiers are not able to provide an intelligible, human-accessible explanation for their behavior [@spring2019ml].
The use of proprietary training data makes the system less transparent.

EPSS could be used to inform the [*Exploitation*](../reference/decision_points/exploitation.md) decision point.
Currently, [*Exploitation*](../reference/decision_points/exploitation.md) focuses on the observable state of the world at the time of the SSVC decision.
EPSS is about predicting if a transition will occur from the SSVC state of [*none*](../reference/decision_points/exploitation.md) to [*active*](../reference/decision_points/exploitation.md).
A sufficiently high EPSS score could therefore be used as an additional criterion for scoring a vulnerability as [*active*](../reference/decision_points/exploitation.md) even when there is no observed active exploitation.

## VPR

VPR is a prioritization product sold by Tenable.
VPR determines the severity level of a vulnerability based on “[technical impact and threat](https://www.tenable.com/blog/what-is-vpr-and-how-is-it-different-from-cvss).”
Just as [*Technical Impact*](../reference/decision_points/technical_impact.md) in SSVC, technical impact in VPR tracks the CVSS version 3 impact metrics in the base metric group.
The VPR threat component is about recent and future threat activity; it is comparable to [*Exploitation*](../reference/decision_points/exploitation.md) if EPSS were added to [*Exploitation*](../reference/decision_points/exploitation.md).

VPR is therefore essentially a subset of SSVC.
VPR is stylistically methodologically quite different from SSVC.
VPR is based on machine learning models and proprietary data, so the results are totally opaque.
There is no ability to coherently and transparently customize the VPR system.
Such customization is a central feature of SSVC, as described in [Tree Construction and Customization Guidance](../howto/tree_customization.md).

## CVSS spin offs

Attempts to tailor CVSS to specific stakeholder groups, such as robotics or medical devices, are are perhaps the biggest single reason we created SSVC.
CVSS is one-size-fits-all by design.
These customization efforts struggle with adapting CVSS because it was not designed to be adaptable to different stakeholder considerations.
The SSVC section [Tree Construction and Customization Guidance](../howto/tree_customization.md) explains how stakeholders or stakeholder communities can adapt SSVC in a reliable way that still promotes repeatability and communication.


## vPrioritizer

vPrioritizer is an open-source project that attempts to integrate asset management and vulnerablity prioritization.
The software is mostly the asset management aspects.
It currently includes CVSS base scores as the de facto vulnerability prioritization method; however, fundamentally the system is agnostic to prioritization method.
vPrioritizer is an example of a product that is closely associated with vulnerability prioritization, but is not directly about the prioritization method.
In that sense, it is compatible with any of methods mentioned above or SSVC.
However, SSVC would be better suited to address vPrioritizer's broad spectrum asset management data.
For example, vPrioritizer aims to collect data points on topics such as asset significance.
Asset significance could be expressed through the SSVC decision points of  [*Mission Impact*](../reference/decision_points/mission_impact.md) and situated [*Well-being Impact*](../reference/decision_points/human_impact.md), but it does not have a ready expression in CVSS, EPSS, or VPR.


