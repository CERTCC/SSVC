

# Current state of practice

**Vulnerability management** covers “the discovery, analysis, and handling of new or reported security vulnerabilities in information systems \[and\] the detection of and response to known vulnerabilities in order to prevent them from being exploited” [@csirtservices_v2].
Prioritization of organizational and analyst resources is an important precursor to vulnerability analysis, handling, and response.
The general problem is: given limited resources, which vulnerabilities should be processed and which can be ignored for now. We approach this problem from a pragmatic, practitioner-centered perspective.

The de facto standard prioritization language is CVSS [@spring2018litrev].
CVSS avoids discussing decisions and, instead, takes **technical severity** as its fundamental operating principle.
However, the standard does not provide clear advice about how CVSS scores might inform decisions [@cvss_sig].
SSVC instead considers technical severity as one decision point in vulnerability management.
Severity should only be a part of vulnerability response prioritization [See, e.g., @farris2018vulcon].

Any re-adaptation of the basic CVSS mindset inherits its deeper issues.
As one example, the CVSS scoring algorithm has not been argued for transparently, and the standardization group has not justified the use of the formula either formally or empirically [@spring2018cvss].
One complaint is that a high CVSS score is not predictive of which vulnerabilities will be commonly exploited or have exploits publicly released [@allodi2012preliminary].
Studies of CVSS scoring consistency indicate that analysts do not consistently interpret the elements of a CVSSv3.0 score [@allodi2018effect], and as many adaptations of CVSS simply add additional metrics we expect they inherit such inconsistency.
Analyst usability has so far been an afterthought, but we know from other areas of information security that usability is not well-served as an afterthought [@garfinkel2014usable].
SSVC aims to learn from and improve upon these issues.

Surveys of security metrics [@pendleton2016survey] and information sharing in cybersecurity [@laube2017survey] do not indicate any major efforts to conduct a wholesale rethinking of vulnerability prioritization.
The surveys indicate some options a prioritization method might consider, such as exploit availability or system attack surface.  
[Representing Information for Decisions About Vulnerabilities](#representing-information-for-decisions-about-vulnerabilities) describes our design goals for a pragmatic prioritization methodology that can improve and build on the state of current practice.  

The target audience for SSVC is vulnerability managers of any kind.
SSVC assumes that the vulnerability manager has identified that there is a vulnerability.  
We take our definition of **vulnerability** from [@householder2020cvd]: "a set of conditions or behaviors that allows the violation of an explicit or implicit security policy."
There are a variety of problems or issues with computer systems that are important that are not vulnerabilities.
SSVC presents a risk prioritization method that might be useful or at least allied to other risk management methods for these other kinds of issues.
However, for this work we focus on decisions in the situation where there is a vulnerability and the vulnerability management team wants to decide what to do about it.
