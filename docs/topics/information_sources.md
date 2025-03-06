# SSVC using Current Information Sources

Some SSVC decision points can be informed or answered by currently available information feeds or sources.
These include

- [*Exploitation*](../reference/decision_points/exploitation.md)
- [*System Exposure*](../reference/decision_points/system_exposure.md)
- [*Technical Impact*](../reference/decision_points/technical_impact.md)
- [*Public Safety Impact*](../reference/decision_points/public_safety_impact.md).

This section provides an overview of some options; we cannot claim it is exhaustive.
Each decision point has a subsection for `Gathering Information About` it.
These sections provide suggestions that would also contribute to creating or honing information feeds.
However, if there is a category of information source we have not captured, please create an [issue on the SSVC GitHub page](https://github.com/CERTCC/SSVC/issues) explaining it and what decision point it informs.

## Exploitation

Various vendors provide paid feeds of vulnerabilities that are currently exploited by attacker groups.
Any of these could be used to indicate that [*active*](../reference/decision_points/exploitation.md/#cwe-ids-for-poc) is true for a vulnerability.
Although the lists are all different, we expect they are all valid information sources; the difficulty is matching a list's scope and vantage with a compatible scope and vantage of the consumer.
We are not aware of a comparative study of the different lists of active exploits; however, we expect they have similar properties to block lists of network touchpoints [@metcalf2015blocklist] and malware [@kuhrer2014paint].
Namely, each list has a different view and vantage on the problem, which makes them appear to be different, but each list accurately represents its particular vantage at a point in time.

## System Exposure

[*System Exposure*](../reference/decision_points/system_exposure.md) could be informed by the various scanning platforms such as Shodan and Shadowserver.
A service on a device should be scored as [*open*](../reference/decision_points/system_exposure.md) if such a general purpose Internet scan finds that the service responds.
Such scans do not find all [*open*](../reference/decision_points/system_exposure.md) systems, but any system they find should be considered [*open*](../reference/decision_points/system_exposure.md).
Scanning software, such as the open-source tool Nessus, could be used to scan for connectivity inside an organization to catalogue what devices should be scored [*controlled*](../reference/decision_points/system_exposure.md) if, say, the scan finds them on an internal network where devices regularly connect to the Internet.

---

## Adapting other Information Sources

Some information sources that were not designed with SSVC in mind can be adapted to work with it.
Three prominent examples are CVSS impact base metrics, CWE, and CPE.

### CVSS and Technical Impact

[*Technical Impact*](../reference/decision_points/technical_impact.md) is directly related to the CVSS impact metric group.
The interpretation is different for CVSS version 3 than version 4.

!!! tip "Mapping CVSS v4 to Technical Impact"

    For CVSS v4, the [impact metric group](https://www.first.org/cvss/v4.0/specification-document#Impact-Metrics) can be
    directly mapped to [*Technical Impact*](../reference/decision_points/technical_impact.md). 
    Stakeholders can define their own mapping, but the recommended mapping between CVSS v4 metric values and [*Technical Impact*](../reference/decision_points/technical_impact.md) is

    | Confidentiality<br/>(VC) | Integrity<br/>(VI)      | Availability<br/>(VA)  | [*Technical Impact*](../reference/decision_points/technical_impact.md) |
    |:--------------------:|---------------------|--------------------|------------------------------------------------------------------------|
    |   High (H)           | High (H)            | *any*              | Total                                                                  |
    |       High (H)       | Low (L) or None (N) | *any*              | Partial                                                                |
    | Low (L) or None (N)  | High (H)            | *any*              | Partial                                                                |

    That is, if the vulnerability leads to a high impact on the confidentiality and integrity of the vulnerable system, then that is equivalent to total technical impact on the system.

The following considerations are accounted for in this recommendation.

1. A denial of service condition is modeled as a *partial* [*Technical Impact*](../reference/decision_points/technical_impact.md).
Therefore, a high availability impact to the vulnerable system should not be mapped to *total* [*Technical Impact*](../reference/decision_points/technical_impact.md) on its own.
2. There may be situations in which a high confidentiality impact is sufficient for total technical impact; for example, disclosure of the root or administrative password for the system leads to total technical control of the system.
So this suggested mapping is a useful heuristic, but there may be exceptions, depending on exactly what the CVSS v4 metric value assignment norms are and become for these situations.
3. While the Subsequent System impact metric group in CVSS v4 is useful, those concepts are not captured by [*Technical Impact*](../reference/decision_points/technical_impact.md).
Subsequent System impacts are captured, albeit in different framings, by decision points such as [*Situated Safety Impact*](../reference/decision_points/safety_impact.md), [*Mission Impact*](../reference/decision_points/mission_impact.md), and [*Value Density*](../reference/decision_points/value_density.md).
There is not a direct mapping between the subsequent system impact metric group and these decision points, except in the case of [*Public Safety Impact*](../reference/decision_points/public_safety_impact.md) and the CVSS v4 environmental metrics for Safety Impact in the subsequent system metric group.
In that case, both definitions map back to the same safety impact standard for definitions (IEC 61508) and so are easily mapped to each other.

#### CVSS v3 and Technical Impact

For CVSS v3, the impact metric group cannot be directly mapped to [*Technical Impact*](../reference/decision_points/technical_impact.md) because of the [Scope metric](https://www.first.org/cvss/v3.1/specification-document#2-2-Scope-S).
[*Technical Impact*](../reference/decision_points/technical_impact.md) is only about adversary control of the vulnerable component.
If the CVSS version 3 value of “Scope” is “Unchanged,” then the recommendation is the same as that for CVSS v4, above, as the impact metric group is information exclusively about the vulnerable system.
If the CVSS version 3 value of “Scope” is “Changed,” then the impact metrics may be about either the vulnerable system or the subsequent systems, based on whichever makes the final score higher.
Since [*Technical Impact*](../reference/decision_points/technical_impact.md) is based only on the vulnerable system impacts, if "Scope" is "Changed" then the ambiguity between vulnerable and subsequent system impacts is not documented in the vector string.
This ambiguity makes it impossible to cleanly map the [*Technical Impact*](../reference/decision_points/technical_impact.md) value in this case.

!!! tip "Mapping CVSS v3 to Technical Impact"

    Summarizing the discussion above, the mapping between CVSS v3 and [*Technical Impact*](../reference/decision_points/technical_impact.md) is

    | CVSS Scope | Confidentiality<br/>(C) | Integrity<br/>(I) | Availability<br/>(A) | [*Technical Impact*](../reference/decision_points/technical_impact.md) |
    |:----------:|:-----------------------:|:------------------:|:---------------------:|------------------------------------------------------------------------|
    | Unchanged  | High (H)               | High (H)           | *any*                 | Total                                                                  |
    | Unchanged  | High (H)               | Low (L) or None (N)| *any*                 | Partial                                                                |
    | Unchanged  | Low (L) or None (N)    | High (H)           | *any*                 | Partial                                                                |
    | Changed    | *any*                  | *any*              | *any*                 | (ambiguous)                                                            |

### CWE and Exploitation

As mentioned in the discussion of [*Exploitation*](../reference/decision_points/exploitation.md), [CWE](https://cwe.mitre.org/) could be used to inform one of the conditions that satisfy [*proof of concept*](../reference/decision_points/exploitation.md).
For some classes of vulnerabilities, the proof of concept is well known because the method of exploitation is already part of open-source tools.
An example of this is on-path attacker scenarios for intercepting TLS certificates.
These scenarios are a cluster of related vulnerabilities.
We provide a non-exhaustive [list of CWE-IDs with known proofs of concept](../reference/decision_points/exploitation.md/#cwe-ids-for-poc). This is list is non-exhaustive becuase there are other conditions that satisfy [*proof of concept*](../reference/decision_points/exploitation.md).
If paired with automatic searches for exploit code in public repositories, these checks would cover many scenarios.
If paired with active exploitation feeds discussed above, then the value of  [*Exploitation*](../reference/decision_points/exploitation.md) could be determined almost entirely from available information without direct analyst involvement at each organization.

### CPE and Safety Impact

[CPE](https://cpe.mitre.org/specification/) could possibly be curated into a list of representative [*Public Safety Impact*](../reference/decision_points/public_safety_impact.md) values for each platform or product.
The [*Situated Safety Impact*](../reference/decision_points/safety_impact.md) would be too specific for a classification as broad as CPE.
But it might work for [*Public Safety Impact*](../reference/decision_points/public_safety_impact.md), since it is concerned with a more general assessment of usual use of a component.
Creating a mapping between CPE and [*Public Safety Impact*](../reference/decision_points/public_safety_impact.md) could be a community effort to associate a value with each CPE entry, or an organization might label a fragment of the CPE data with [*Public Safety Impact*](../reference/decision_points/public_safety_impact.md) based on the platforms that the supplier needs information about most often.

## Potential Future Information Feeds

So far, we have identified information sources that can support scalable decision making for most decision points.
Some sources, such as CWE or existing asset management solutions, would require a little bit of connective glue to support SSVC, but not too much.

### Automatable and Value Density

The SSVC decision point that we have not identified an information source for is [Utility](../reference/decision_points/utility.md).
[Utility](../reference/decision_points/utility.md) is composed of [*Automatable*](../reference/decision_points/automatable.md) and [*Value Density*](../reference/decision_points/value_density.md), so the question is what sort of feed could support each of those decision points.

A feed is plausible for both of these decision points.
The values for [*Automatable*](../reference/decision_points/automatable.md) and [*Value Density*](../reference/decision_points/value_density.md) are both about the relationship between a vulnerability, the attacker community, and the aggregate state of systems connected to the Internet.
While that is a broad analysis frame, it means that any community that shares a similar set of adversaries and a similar region of the Internet can share the same response to both decision points.
An organization in the People's Republic of China may have a different view than an organization in the United States, but most organizations within each region should should have close enough to the same view to share values for [*Automatable*](../reference/decision_points/automatable.md) and [*Value Density*](../reference/decision_points/value_density.md).
These factors suggest a market for an information feed about these decision points is a viable possibility.

!!! note inline end "CVSS v4, Automatable, and Value Density"

    It is not coincidental that the CVSS v4 supplemental metrics include [Automatable](https://www.first.org/cvss/v4.0/specification-document#Automatable-AU)
    (AU) and [Value Density](https://www.first.org/cvss/v4.0/specification-document#Value-Density-V) (V).
    The SSVC team collaborated in the development of these metrics with the [FIRST CVSS Special Interest Group](https://www.first.org/cvss).

At this point, it is not clear that an algorithm or search process could be designed to automate scoring [*Automatable*](../reference/decision_points/automatable.md) and [*Value Density*](../reference/decision_points/value_density.md).
It would be a complex natural language processing task.
Perhaps a machine learning system could be designed to suggest values.
But more likely, if there is a market for this information, a few analysts could be paid to score vulnerabilities on these values for the community.
Supporting such analysts with further automation could proceed by small incremental improvements.
For example, perhaps information about whether the Reconnaissance step in the kill chain is [*Automatable*](../reference/decision_points/automatable.md) or not could be automatically gathered from Internet scanning firms such as Shodan or Shadowserver.
This wouldn't make a determination for an analyst, but would be a step towards automatic assessment of the decision point.
