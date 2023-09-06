# SSVC using Current Information Sources

Some SSVC decision points can be informed or answered by currently available information feeds or sources.
These include

- [*Exploitation*](#exploitation)
- [*System Exposure*](#system-exposure)
- [*Technical Impact*](#technical-impact)
- [*Public Safety Impact*](#public-safety-impact).

This section provides an overview of some options; we cannot claim it is exhaustive.
Each decision point has a subsection for `Gathering Information About` it.
These sections provide suggestions that would also contribute to creating or honing information feeds.
However, if there is a category of information source we have not captured, please create an [issue on the SSVC GitHub page](https://github.com/CERTCC/SSVC/issues) explaining it and what decision point it informs.

## Exploitation

Various vendors provide paid feeds of vulnerabilities that are currently exploited by attacker groups.
Any of these could be used to indicate that [*active*](#exploitation) is true for a vulnerability.
Although the lists are all different, we expect they are all valid information sources; the difficulty is matching a list's scope and vantage with a compatible scope and vantage of the consumer.
We are not aware of a comparative study of the different lists of active exploits; however, we expect they have similar properties to block lists of network touchpoints [@metcalf2015blocklist] and malware [@kuhrer2014paint].
Namely, each list has a different view and vantage on the problem, which makes them appear to be different, but each list accurately represents its particular vantage at a point in time.


## System Exposure

[*System Exposure*](#system-exposure) could be informed by the various scanning platforms such as Shodan and Shadowserver.
A service on a device should be scored as [*open*](#system-exposure) if such a general purpose Internet scan finds that the service responds.
Such scans do not find all [*open*](#system-exposure) systems, but any system they find should be considered [*open*](#system-exposure).
Scanning software, such as the open-source tool Nessus, could be used to scan for connectivity inside an organization to catalogue what devices should be scored [*controlled*](#system-exposure) if, say, the scan finds them on an internal network where devices regularly connect to the Internet.

---
## Adapting other Information Sources

Some information sources that were not designed with SSVC in mind can be adapted to work with it.
Three prominent examples are CVSS impact base metrics, CWE, and CPE.

### CVSS and Technical Impact

[*Technical Impact*](#technical-impact) is directly related to the CVSS impact metric group.
However, this metric group cannot be directly mapped to [*Technical Impact*](#technical-impact) in CVSS version 3  because of the Scope metric.
[*Technical Impact*](#technical-impact) is only about adversary control of the vulnerable component.
If the CVSS version 3 value of “Scope” is “Changed,” then the impact metrics are the maximum of the impact on the vulnerable component and other components in the environment.
If confidentiality, integrity, and availability metrics are all “high” then [*Technical Impact*](#technical-impact) is [*total*](#technical-impact), as long as the impact metrics in CVSS are clearly about just the vulnerable component.
However, the other values of the CVSS version 3 impact metrics cannot be mapped directly to [*partial*](#technical-impact) because of CVSS version 3.1 scoring guidance.
Namely, “only the increase in access, privileges gained, or other negative outcome as a result of successful exploitation should be considered” [@cvss_v3-1].
The example given is that if an attacker already has read access, but gains all other access through the exploit, then read access didn't change and the confidentiality metric score should be “None” .
However, in this case, SSVC would expect the decision point to be evaluated as [*total*](#technical-impact) because as a result of the exploit the attacker gains total control of the device, even though they started with partial control.

### CWE and Exploitation

As mentioned in the discussion of [*Exploitation*](#exploitation), [CWE](https://cwe.mitre.org/) could be used to inform one of the conditions that satisfy [*proof of concept*](#exploitation).
For some classes of vulnerabilities, the proof of concept is well known because the method of exploitation is already part of open-source tools.
For example, on-path attacker scenarios for intercepting TLS certificates.
These scenarios are a cluster of related vulnerabilities.
Since CWE classifies clusters of related vulnerabilities, the community could likely curate a list of CWE-IDs for which this condition of well known exploit technique is satisfied.
Once that list were curated, it could be used to automatically populate a CVE-ID as [*proof of concept*](#exploitation) if the CWE-ID of which it is an instance is on the list.
Such a check could not be exhaustive, since there are other conditions that satisfy [*proof of concept*](#exploitation).
If paired with automatic searches for exploit code in public repositories, these checks would cover many scenarios.
If paired with active exploitation feeds discussed above, then the value of  [*Exploitation*](#exploitation) could be determined almost entirely from available information without direct analyst involvement at each organization.

### CPE and Safety Impact

[CPE](https://cpe.mitre.org/specification/) could possibly be curated into a list of representative [*Public Safety Impact*](#public-safety-impact) values for each platform or product.
The [*Situated Safety Impact*](#situated-safety-impact) would be too specific for a classification as broad as CPE.
But it might work for [*Public Safety Impact*](#public-safety-impact), since it is concerned with a more general assessment of usual use of a component.
Creating a mapping between CPE and [*Public Safety Impact*](#public-safety-impact) could be a community effort to associate a value with each CPE entry, or an organization might label a fragment of the CPE data with [*Public Safety Impact*](#public-safety-impact) based on the platforms that the supplier needs information about most often.

## Potential Future Information Feeds

So far, we have identified information sources that can support scalable decision making for most decision points.
Some sources, such as CWE or existing asset management solutions, would require a little bit of connective glue to support SSVC, but not too much.

### Automatable and Value Density

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
