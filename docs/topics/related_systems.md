
# Related Vulnerability Management Systems

There are several other bodies of work that are used in practice to assist vulnerability managers in making decisions.
Three relevant systems are CVSS [@cvss_v3-1], EPSS [@jacobs2021epss], and Tenable's Vulnerability Priority Rating ([VPR](https://www.tenable.com/blog/what-is-vpr-and-how-is-it-different-from-cvss)).
There are other systems derived from CVSS, such as RVSS for robots [@vilches2018towards] and MITRE's effort to adapt CVSS to medical devices [@mitre2019medical].
There are also other nascent efforts to automate aspects of the decision making process, such as [vPrioritizer](https://github.com/varchashva/vPrioritizer).
This section discusses the relationship between these various systems and SSVC.

## CVSS

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
Product vendors have varying degrees of adaptation of CVSS for development prioritization, including but not limited to [Red Hat](https://access.redhat.com/security/updates/classification), [Microsoft](https://www.microsoft.com/en-us/msrc/security-update-severity-rating-system), and [Cisco](https://tools.cisco.com/security/center/resources/security_vulnerability_policy.html#asr).
The vendors codify CVSS’s recommended qualitative severity rankings in different ways, and Red Hat and Microsoft make the user interaction base metric more important.

> Exploitability metrics (Base metric group)

The four metrics in this group are Attack Vector, Attack Complexity, Privileges Required, and User Interaction.
This considerations may likely be involved in the [*Automatability*](#automatability) decision point.
If Attack Vector = Network and Privileges Required = None, then the delivery phase of the kill chain is likely to be automatable.
Attack Vector may also be correlated with the [*Exposure*](#exposure) decision point.
Attack Complexity may influence how long it may take an adversary to craft an automated exploit, but [*Automatability*](#automatability) only asks whether exploitation can be automated, not how difficult it was.
However, Attack Complexity may influence the weaponization phase of the kill chain.
User Interaction does not cleanly map to a decision point.
In general, SSVC does not care whether a human is involved in exploitation of the vulnerability or not.
Some human interaction is for all intents and purposes automatable by attackers: most people click on links in emails as part of their normal processes.
In most such situations, user interaction does not present a firm barrier to automatability; it presents a stochastic barrier.
[*Automatability*](#automatability) is written to just consider firm barriers to automation.

[*Automatability*](#automatability) includes considerations that are not included in the exploitability metrics.
Most notably the concept of vulnerability chaining is addressed in [*Automatability*](#automatability) but not addressed anywhere in CVSS.
[*Automatability*](#automatability) is also outcomes focused.
A vulnerability is evaluated based on an observable outcome of whether the first four steps of the kill chain can be automated for it.
A proof of automation in a relevant environment is an objective evaluation of the score in a way that cannot be provided for some CVSS elements, such as Attack Complexity.

> Impact metrics (Base metric group)

The metrics in this group are Confidentiality, Integrity, and Availability.
There is also a loosely associated Scope metric.
The CIA impact metrics are directly handled by [*Technical Impact*](#technical-impact).

Scope is a difficult CVSS metric to categorize.
The specification describes it as “whether a vulnerability in one vulnerable component impacts resources in components beyond its security scope” [@cvss_v3-1].
This is a fuzzy concept.
SSVC better describes this concept by breaking it down into component parts.
The impact of exploitation of the vulnerable component on other components is covered under [*Mission Impact*](#mission-impact), public and situated [*Well-being Impact*](#well-being-impact), and the stakeholder-specific nature where SSVC is tailored to stakeholder concerns.
CVSS addresses some definitions of the scope of CVSS as a whole under the Scope metric definition.
In SSVC, these definitions are in the [Scope](#scope) section.

> Temporal metric groups

The temporal metric group primarily contains the Exploit Code Maturity metric.
This metric expresses a concept similar to [*Exploitation*](#exploitation).
The main difference is that [*Exploitation*](#exploitation) is not optional in SSVC and that SSVC accounts for the observation that most vulnerabilities with CVE-IDs do not have public exploit code [@householder2020historical] and are not actively exploited [@guido2011exploit,@jacobs2021epss].

> Environmental metric group

The environmental metric group allows a consumer of a CVSS base score to change it based on their environment.
CVSS needs this functionality because the organizations that produce CVSS scores tend to be what SSVC calls **suppliers** and consumers of CVSS scores are what SSVC calls **deployers**.
These two stakeholder groups have a variety of natural differences, which is why SSVC treats them separately.
SSVC does not have such customization as a bolt-on optional metric group because SSVC is stakeholder-specific by design.

## EPSS

The [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/) is “a data-driven effort for estimating the likelihood (probability) that a software vulnerability will be exploited in the wild.”
EPSS is currently based on a machine-learning classifier and proprietary data from Fortiguard, Alienvault OTX, the Shadowserver Foundation and GreyNoise.
While the group has made an effort to make the ML classifier transparent, ML classifiers are not able to provide an intelligible, human-accessible explanation for their behavior [@spring2019ml].
The use of proprietary training data makes the system less transparent.

EPSS could be used to inform the [*Exploitation*](#exploitation) decision point.
Currently, [*Exploitation*](#exploitation) focuses on the observable state of the world at the time of the SSVC decision.
EPSS is about predicting if a transition will occur from the SSVC state of [*none*](#exploitation) to [*active*](#exploitation).
A sufficiently high EPSS score could therefore be used as an additional criterion for scoring a vulnerability as [*active*](#exploitation) even when there is no observed active exploitation.

## VPR

VPR is a prioritization product sold by Tenable.
VPR determines the severity level of a vulnerability based on “[technical impact and threat](https://www.tenable.com/blog/what-is-vpr-and-how-is-it-different-from-cvss).”
Just as [*Technical Impact*](#technical-impact) in SSVC, technical impact in VPR tracks the CVSS version 3 impact metrics in the base metric group.
The VPR threat component is about recent and future threat activity; it is comparable to [*Exploitation*](#exploitation) if EPSS were added to [*Exploitation*](#exploitation).

VPR is therefore essentially a subset of SSVC.
VPR is stylistically methodologically quite different from SSVC.
VPR is based on machine learning models and proprietary data, so the results are totally opaque.
There is no ability to coherently and transparently customize the VPR system.
Such customization is a central feature of SSVC, as described in [Tree Construction and Customization Guidance](#tree-construction-and-customization-guidance).

## CVSS spin offs

Attempts to tailor CVSS to specific stakeholder groups, such as robotics or medical devices, are are perhaps the biggest single reason we created SSVC.
CVSS is one-size-fits-all by design.
These customization efforts struggle with adapting CVSS because it was not designed to be adaptable to different stakeholder considerations.
The SSVC section [Tree Construction and Customization Guidance](#tree-construction-and-customization-guidance) explains how stakeholders or stakeholder communities can adapt SSVC in a reliable way that still promotes repeatability and communication.


## vPrioritizer

vPrioritizer is an open-source project that attempts to integrate asset management and vulnerablity prioritization.
The software is mostly the asset management aspects.
It currently includes CVSS base scores as the de facto vulnerability prioritization method; however, fundamentally the system is agnostic to prioritization method.
vPrioritizer is an example of a product that is closely associated with vulnerability prioritization, but is not directly about the prioritization method.
In that sense, it is compatible with any of methods mentioned above or SSVC.
However, SSVC would be better suited to address vPrioritizer's broad spectrum asset management data.
For example, vPrioritizer aims to collect data points on topics such as asset significance.
Asset significance could be expressed through the SSVC decision points of  [*Mission Impact*](#mission-impact) and situated [*Well-being Impact*](#well-being-impact), but it does not have a ready expression in CVSS, EPSS, or VPR.


## SSVC using Current Information Sources

Some SSVC decision points can be informed or answered by currently available information feeds or sources.
These include [*Exploitation*](#exploitation), [*System Exposure*](#system-exposure), [*Technical Impact*](#technical-impact), and [*Public Safety Impact*](#public-safety-impact).
This section provides an overview of some options; we cannot claim it is exhaustive.
Each decision point has a subsection for `Gathering Information About` it.
These sections provide suggestions that would also contribute to creating or honing information feeds.
However, if there is a category of information source we have not captured, please create an [issue on the SSVC GitHub page](https://github.com/CERTCC/SSVC/issues) explaining it and what decision point it informs.

Various vendors provide paid feeds of vulnerabilities that are currently exploited by attacker groups.
Any of these could be used to indicate that [*active*](#exploitation) is true for a vulnerability.
Although the lists are all different, we expect they are all valid information sources; the difficulty is matching a list's scope and vantage with a compatible scope and vantage of the consumer.
We are not aware of a comparative study of the different lists of active exploits; however, we expect they have similar properties to block lists of network touchpoints [@metcalf2015blocklist] and malware [@kuhrer2014paint].
Namely, each list has a different view and vantage on the problem, which makes them appear to be different, but each list accurately represents its particular vantage at a point in time.


[*System Exposure*](#system-exposure) could be informed by the various scanning platforms such as Shodan and Shadowserver.
A service on a device should be scored as [*open*](#system-exposure) if such a general purpose Internet scan finds that the service responds.
Such scans do not find all [*open*](#system-exposure) systems, but any system they find should be considered [*open*](#system-exposure).
Scanning software, such as the open-source tool Nessus, could be used to scan for connectivity inside an organization to catalogue what devices should be scored [*controlled*](#system-exposure) if, say, the scan finds them on an internal network where devices regularly connect to the Internet.


Some information sources that were not designed with SSVC in mind can be adapted to work with it.
Three prominent examples are CVSS impact base metrics, CWE, and CPE.

[*Technical Impact*](#technical-impact) is directly related to the CVSS impact metric group.
However, this metric group cannot be directly mapped to [*Technical Impact*](#technical-impact) in CVSS version 3  because of the Scope metric.
[*Technical Impact*](#technical-impact) is only about adversary control of the vulnerable component.
If the CVSS version 3 value of “Scope” is “Changed,” then the impact metrics are the maximum of the impact on the vulnerable component and other components in the environment.
If confidentiality, integrity, and availability metrics are all “high” then [*Technical Impact*](#technical-impact) is [*total*](#technical-impact), as long as the impact metrics in CVSS are clearly about just the vulnerable component.
However, the other values of the CVSS version 3 impact metrics cannot be mapped directly to [*partial*](#technical-impact) because of CVSS version 3.1 scoring guidance.
Namely, “only the increase in access, privileges gained, or other negative outcome as a result of successful exploitation should be considered” [@cvss_v3-1].
The example given is that if an attacker already has read access, but gains all other access through the exploit, then read access didn't change and the confidentiality metric score should be “None” .
However, in this case, SSVC would expect the decision point to be evaluated as [*total*](#technical-impact) because as a result of the exploit the attacker gains total control of the device, even though they started with partial control.

As mentioned in the discussion of [*Exploitation*](#exploitation), [CWE](https://cwe.mitre.org/) could be used to inform one of the conditions that satisfy [*proof of concept*](#exploitation).
For some classes of vulnerabilities, the proof of concept is well known because the method of exploitation is already part of open-source tools.
For example, on-path attacker scenarios for intercepting TLS certificates.
These scenarios are a cluster of related vulnerabilities.
Since CWE classifies clusters of related vulnerabilities, the community could likely curate a list of CWE-IDs for which this condition of well known exploit technique is satisfied.
Once that list were curated, it could be used to automatically populate a CVE-ID as [*proof of concept*](#exploitation) if the CWE-ID of which it is an instance is on the list.
Such a check could not be exhaustive, since there are other conditions that satisfy [*proof of concept*](#exploitation).
If paired with automatic searches for exploit code in public repositories, these checks would cover many scenarios.
If paired with active exploitation feeds discussed above, then the value of  [*Exploitation*](#exploitation) could be determined almost entirely from available information without direct analyst involvement at each organization.

[CPE](https://cpe.mitre.org/specification/) could possibly be curated into a list of representative [*Public Safety Impact*](#public-safety-impact) values for each platform or product.
The [*Situated Safety Impact*](#situated-safety-impact) would be too specific for a classification as broad as CPE.
But it might work for [*Public Safety Impact*](#public-safety-impact), since it is concerned with a more general assessment of usual use of a component.
Creating a mapping between CPE and [*Public Safety Impact*](#public-safety-impact) could be a community effort to associate a value with each CPE entry, or an organization might label a fragment of the CPE data with [*Public Safety Impact*](#public-safety-impact) based on the platforms that the supplier needs information about most often.

## Potential Future Information Feeds

So far, we have identified information sources that can support scalable decision making for most decision points.
Some sources, such as CWE or existing asset management solutions, would require a little bit of connective glue to support SSVC, but not too much.
The SSVC decision point that we have not identified an information source for is [*Utility*](#utility).
[*Utility*](#utility) is composed of [*Automatable*](#automatable) and [*Value Density*](#value-density), so the question is what a sort of feed could support each of those decision points.

A feed is plausible for both of these decision points.
The values for [*Automatable*](#automatable) and [*Value Density*](#value-density) are both about the relationship between a vulnerability, the attacker community, and the aggregate state of systems connected to the Internet.
While that is a broad analysis frame, it means that any community that shares a similar set of adversaries and a similar region of the Internet can share the same response to both decision points.
An organization in the People's Republic of China may have a different view than an organization in the United States, but most organizations within each region should should have close enough to the same view to share values for [*Automatable*](#automatable) and [*Value Density*](#value-density).
These factors suggest a market for an information feed about these decision points is a viable possibility.

At this point, it is not clear that an algorithm or search process could be designed to automate scoring [*Automatable*](#automatable) and [*Value Density*](#value-density).
It would be a complex natural language processing task.
Perhaps a machine learning system could be designed to suggest values.
But more likely, if there is a market for this information, a few analysts could be paid to score vulnerabilities on these values for the community.
Supporting such analysts with further automation could proceed by small incremental improvements.
For example, perhaps information about whether the Reconnaissance step in the kill chain is [*Automatable*](#automatable) or not could be automatically gathered from Internet scanning firms such as Shodan or Shadowserver.
This wouldn't make a determination for an analyst, but would be a step towards automatic assessment of the decision point.
