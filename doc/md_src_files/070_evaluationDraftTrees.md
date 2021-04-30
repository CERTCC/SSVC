

# Evaluation of the Draft Trees

We conducted a pilot test on the adequacy of the hypothesized decision trees.
This section reports results for SSVC version 1.
 The method of the pilot test is described in [Pilot Methodogy](#pilot-methodology). The study resulted in several changes to the hypothesized trees; we capture those changes and the reason for each of them in [Pilot Results](#pilot-results). The version 1 supplier and deployer trees included the improvements reported in [Improvement Instigated by the Pilot](#improvements-instigated-by-the-pilot).

## Pilot Methodology

The pilot study tested inter-rater agreement of decisions reached. Each author played the role of an analyst in both stakeholder groups (supplying and deploying) for nine vulnerabilities. We selected these nine vulnerabilities based on expert analysis, with the goal that the nine cases cover a useful series of vulnerabilities of interest. Specifically, we selected three vulnerabilities to represent safety-critical cases, three to represent regulated-systems cases, and three to represent general computing cases.

During the pilot, we did not form guidance on how to assess the values of the decision points.
However, we did standardize the set of evidence that was taken to be true for the point in time representing the evaluation.
Given this static information sheet, we did not synchronize an evaluation process for how to decide whether [*Exploitation*](#exploitation), for example, should take the value of [*none*](#exploitation), [*PoC*](#exploitation), or [*active*](#exploitation).
We agreed on the descriptions of the decision points and the descriptions of their values. The goal of the pilot was to test the adequacy of those descriptions by evaluating whether the analysts agreed. We improved the decision point descriptions based on the results of the pilot; our changes are documented in [Improvement Instigated by the Pilot](#improvements-instigated-by-the-pilot).

In the design of the pilot, we held constant the information available about the vulnerability. This strategy restricted the analyst to decisions based on the framework given that information. That is, it controlled for differences in information search procedure among the analysts. The information search procedure should be controlled because this pilot was about the framework content, not how people answer questions based on that content. After the framework is more stable, a separate study should be devised that shows how analysts should answer the questions in the framework. The basis for the assessment that information search will be an important aspect in using the evaluation framework is based on our experience while developing the framework. During informal testing, often disagreements about a result involved a disagreement about what the scenario actually was; different information search methods and prior experiences led to different understandings of the scenario. This pilot methodology holds the information and scenario constant to test agreement about the descriptions themselves. This strategy makes constructing a prioritization system more tractable by separating problems in how people search for information from problems in how people make decisions. This paper focuses only on the structure of decision making. Advice about how to search for information about a vulnerability is a separate project that will be part of future work. In some domains, namely exploit availability, we have started that work in parallel.

The structure of the pilot test is as follows. Table 11 provides an example of the information provided to each analyst. The supplier portfolio details use ~~strikeout font~~ because this decision item was removed after the pilot. The decision procedure for each case is as follows: for each analyst, for each vulnerability, for each stakeholder group, do the following.

1.  Start at the root node of the relevant decision tree (deployer or supplier).

2.  Document the decision branch that matches the vulnerability for this stakeholder context.

3.  Document the evidence that supports that decision.

4.  Repeat this decision-and-evidence process until the analyst reaches a leaf node in the tree.

Table: Example of Scenario Information Provided to Analysts (Using
CVE-2019-9042 as the Example)

| Information Item                      | Description Provided to Analysts  |
| :--- | :----------- |
| Use of Cyber-Physical System          | Sitemagic’s content management system (CMS) seems to be fairly popular among smaller businesses because it starts out with a free plan to use it. Then it gradually has small increments in payment for additional features. Its ease-of-use, good designs, and one-stop-shopping for businesses attracts a fair number of clients. Like any CMS, it “manages the creation and modification of digital content. These systems typically support multiple users in a collaborative environment, allowing document management with different styles of governance and workflows. Usually the content is a website” \([Wikipedia](https://en.wikipedia.org/w/index.php?title=Content_management_system&oldid=913022120), 2019\) |
| State of Exploitation                 | Appears to be active exploitation of this vulnerability according to NVD. They have linked to the exploit: <u>http://www.iwantacve.cn/index.php/archives/116/</u>.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ~~Developer Portfolio Details~~       | ~~Sitemagic is an open-source project. The only thing the brand name applies to is the CMS, and it does not appear to be part of another open-source umbrella. The project is under active maintenance (i.e., it is not a dead project).~~                                                                                                                                                                                                                                                                                                                                                                                |
| Technical Impact of Exploit           | An authenticated user can upload a .php file to execute arbitrary code with system privileges.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Scenario Blurb                        | We are a small business that uses Sitemagic to help run our business. Sitemagic handles everything from digital marketing and site design to facilitating the e-commerce transactions of the website. We rely on this website heavily, even though we do have a brick-and-mortar store. Many times, products are not available in-store, but are available online, so we point many customers to our online store.                                                                                                                                                                                                           |
| Deployer Mission                       | We are a private company that must turn a profit to remain competitive. We want to provide customers with a valuable product at a reasonable price, while still turning a profit to run the business. As we are privately held (and not public), we are free to choose the best growth strategy (that is, we are not legally bound to demonstrate quarterly earnings for shareholders and can take a longer-term view if it makes us competitive).                                                                                                                                                                        |
| Deployment of Affected System | We have deployed this system such that only the web designer Cheryl and the IT admin Sally are allowed to access the CMS as users. They login through a password-protected portal that can be accessed anywhere in the world for remote administration. The CMS publishes content to the web, and that web server and site are publicly available.                                                                                                                                                                                                                                                                    |

This test structure produced a series of lists similar in form to the
contents of Table 12. Analysts also noted how much time they spent on
each vulnerability in each stakeholder group.

Table: Example Documentation of a Single Decision Point

| Decision Point | Branch Selected | Supporting Evidence |
| :---           | :---            | :-------            |
| Exploitation=active | Controlled | The CMS has a limited number of authorized users, and the vulnerability is exploitable only by an authenticated user |

We evaluated inter-rater agreement in two stages. In the first stage, each analyst independently documented their decisions. This stage produced 18 sets of decisions (nine vulnerabilities across each of two stakeholder groups) per analyst. In the second stage, we met to discuss decision points where at least one analyst differed from the others. If any analyst changed their decision, they appended the information and evidence they gained during this meeting in the “supporting evidence” value in their documentation. No changes to decisions were forced, and prior decisions were not erased, just amended. After the second stage, we calculated some statistical measures of inter-rater agreement to help guide the analysis of problem areas.

To assess agreement, we calculate Fleiss’ kappa, both for the value in the leaf node reached for each case and every decision in a case [@fleiss1973equivalence]. Evaluating individual decisions is complicated slightly because the different paths through the tree mean that a different number of analysts may have evaluated certain items, and Fleiss’ kappa requires a static number of raters.
“Leaf node reached” is described to pick out the specific path through the tree the analyst selected and to treat that as a label holistically.
Measuring agreement based on the path has the drawback that ostensibly similar paths (for example, paths that agree on 3 of 4 decisions) are treated as no more similar than paths that agree on 0 of 4 decisions.
The two measures of agreement (per decision and per path) are complementary, so we report both.

### Pilot participant details

The pilot participants are the five authors plus one analyst who had not seen the draft system before participating. Five of the six participants had spent at least one year as professional vulnerability analysts prior to the pilot (Spring was the exception). Three of the participants had at least ten years of experience each. The participants experience is primarily as coordinators at the CERT® Coordination Center. On the one hand, this is a different perspective than either suppliers or deployers; on the other, the coordinator role is an information broker that often interacts with these perspectives [@householder2020cvd, section 3].

These participant demographics limit the generalizability of the results of the pilot. Even though the results cannot be systematically generalized to other analysts, there are at least three benefits to conducting the pilot among this limited demographic.
First, it should surface any material tacit disagreements about term usage among the authors. Tacit agreements that are not explained in the text likely survive the pilot study without being acknowledged, but places where the authors tacitly disagreed should be surfaced. We found this to be the case; [Improvement Instigated by the Pilot](#improvements-instigated-by-the-pilot) documents these results.
Second, the pilot provides a case study that demonstrate SSVC is at least possible for some small group of analysts to use.
This achievement is not large, but it is a first step.
Third, the pilot provides a proof of concept method and metric that any vulnerability prioritization method could use to examine usability for analysts more generally. While the effect of education on vulnerability assessment with CVSS has been tested [@allodi2018effect], we are not aware of any current vulnerability prioritization method that tests usability or agreement among analysts as part of the development process. Future work on SSVC as well as further development of other prioritization methods can benefit from using the method described in the pilot. Future instances should use more representative participant demographics.

### Vulnerabilities used as examples

The vulnerabilities used as case studies are as follows. All quotes are from the [National Vulnerability Database (NVD)](https://nvd.nist.gov/) and are illustrative of the vulnerability; however, during the study each vulnerability was evaluated according to information analogous to that in Table 11.

### Safety-Critical Cases

  - CVE-2015-5374: “Vulnerability … in \[Siemens\] Firmware variant PROFINET IO for EN100 Ethernet module… Specially crafted packets sent to port 50000/UDP could cause a denial-of-service of the affected device…”

  - CVE-2014-0751: “Directory traversal vulnerability in … GE Intelligent Platforms Proficy HMI/SCADA - CIMPLICITY before 8.2 SIM 24, and Proficy Process Systems with CIMPLICITY, allows remote attackers to execute arbitrary code via a crafted message to TCP port 10212, aka ZDI-CAN-1623.”

  - CVE-2015-1014: “A successful exploit of these vulnerabilities requires the local user to load a crafted DLL file in the system directory on servers running Schneider Electric OFS v3.5 with version v7.40 of SCADA Expert Vijeo Citect/CitectSCADA, OFS v3.5 with version v7.30 of Vijeo Citect/CitectSCADA, and OFS v3.5 with version v7.20 of Vijeo Citect/CitectSCADA. If the application attempts to open that file, the application could crash or allow the attacker to execute arbitrary code.”

### Regulated Systems Cases

  - CVE-2018-14781: “Medtronic insulin pump \[specific versions\] when paired with a remote controller and having the “easy bolus” and “remote bolus” options enabled (non-default), are vulnerable to a capture-replay attack. An attacker can … cause an insulin (bolus) delivery.”

  - CVE-2017-9590: “The State Bank of Waterloo Mobile … app 3.0.2 … for iOS does not verify X.509 certificates from SSL servers, which allows man-in-the-middle attackers to spoof servers and obtain sensitive information via a crafted certificate.”

  - CVE-2017-3183: “Sage XRT Treasury, version 3, fails to properly restrict database access to authorized users, which may enable any authenticated user to gain full access to privileged database functions. Sage XRT Treasury is a business finance management application. …”

### General Computing Cases

  - CVE-2019-2691: “Vulnerability in the MySQL Server component of Oracle MySQL (subcomponent: Server: Security: Roles). Supported versions that are affected are 8.0.15 and prior. Easily exploitable vulnerability allows high privileged attacker with network access via multiple protocols to … complete DoS of MySQL Server.”

  - CVE-2019-9042: “\[I\]n Sitemagic CMS v4.4… the user can upload a .php file to execute arbitrary code, as demonstrated by 404.php. This can only occur if the administrator neglects to set FileExtensionFilter and there are untrusted user accounts. …”

  - CVE-2017-5638: “The Jakarta Multipart parser in Apache Struts 2 2.3.x before 2.3.32 and 2.5.x before 2.5.10.1 has incorrect exception handling and error-message generation during file-upload attempts, which allows remote attackers to execute arbitrary commands via crafted \[specific headers\], as exploited in the wild in March 2017…”

## Pilot Results

For each of the nine CVEs, six analysts rated the priority of the vulnerability as both a supplier and deployer. Table 13 summarizes the results by reporting the inter-rater agreement for each decision point. For all measures, agreement (κ) is above zero, which is generally interpreted as some agreement among analysts. Below zero is interpreted as noise or discord. Closer to 1 indicates more or stronger agreement.

How close κ should be to 1 before agreement can be considered strong enough or reliable enough is a matter of some debate. The value certainly depends on the number of options among which analysts select. For those decision points with five options (mission and safety impact), agreement is lowest. Although portfolio value has a higher κ than mission or safety impact, it may not actually have higher agreement because portfolio value only has two options. The results for portfolio value are nearly indistinguishable as far as level of statistical agreement from mission impact and safety impact. The statistical community does not have hard and fast rules for cut lines on adequate agreement. We treat κ as a descriptive statistic rather than a test statistic.

Table 13 is encouraging, though not conclusive. κ\<0 is a strong sign of discordance. Although it is unclear how close to 1 is success, κ\<0 would be clear sign of failure. In some ways, these results may be undercounting the agreement for SSVC as presented. These results are for SSVC prior to the improvements documented in [Improvement Instigated by the Pilot](#improvements-instigated-by-the-pilot), which are implemented in SSVC version 1. On the other hand, the participant demographics may inflate the inter-rater agreement based on shared tacit understanding through the process of authorship. The one participant who was not an author surfaced two places where this was the case, but we expect the organizational homogeneity of the participants has inflated the agreement somewhat. The anecdotal feedback from vulnerability managers at several organizations (including VMware [@akbar2020ssvc] and McAfee) is about refinement and tweaks, not gross disagreement. Therefore, while further refinement is necessary, this evidence suggests the results have some transferability to other organizations and are not a total artifact of the participant organization demographics.

Table: Inter-Rater Agreement for Decision Points

| | Safety Impact | Exploitation | Technical Impact | Portfolio Value | Mission Impact| Exposure | Dev Result | Deployer Result |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
Fleiss’ κ | 0.122 | 0.807        | 0.679            | 0.257           | 0.146         | 0.480    | 0.226      | 0.295           |
|Disagreement range  | 2,4 | 1,2 | 1,1 | 1,1 | 2,4 | 1,2 | 1,3 | 2,3 |

For all decision points, the presumed goal is for κ to be close or equal to 1. The statistics literature has identified some limited cases in which Fleiss’ k behaves strangely—for example it is lower than expected when raters are split between 2 of q ratings when q\>2 [@falotico2015fleiss]. This paradox may apply to the safety and mission impact values, in particular. The paradox would bite hardest if the rating for each vulnerability was clustered on the same two values, for example, minor and major. Falotico and Quatto’s proposed solution is to permute the columns, which is safe with unordered categorical data. Since the nine vulnerabilities do not have the same answers as each other (that is, the answers are not clustered on the same two values), we happen to avoid the worst of this paradox, but the results for safety impact and mission impact should be interpreted with some care.

This solution identifies another difficulty of Fleiss’ kappa, namely that it does not preserve any order; none and catastrophic are considered the same level of disagreement as none and minor. Table 13 displays a sense of the range of disagreement to complement this weakness. This value is the largest distance between rater selections on a single vulnerability out of the maximum possible distance. So, for safety impact, the most two raters disagreed was by two steps (none to major, minor to hazardous, or major to catastrophic) out of the four possible steps (none to catastrophic). The only values of κ that are reliably comparable are those with the same number of options (that is, the same maximum distance). In other cases, closer to 1 is better, but how close is close enough to be considered “good” changes. In all but one case, if raters differed by two steps then there were raters who selected the central option between them. The exception was mission impact for CVE-201814781; it is unclear whether this discrepancy should be localized to a poor test scenario description, or to SSVC’s mission impact definition. Given it is an isolated occurrence, we expect the scenario description at least partly.

Nonetheless, κ provides some way to measure improvement on this a conceptual engineering task. The pilot evaluation can be repeated, with more diverse groups of stakeholders after the descriptions have been refined by stakeholder input, to measure fit to this goal. For a standard to be reliably applied across different analyst backgrounds, skill sets, and cultures, a set of decision point descriptions should ideally achieve κ of 1 for each item in multiple studies with diverse participants. Such a high level of agreement would be difficult to achieve, but it would ensure that when two analysts assign a priority with the system that they get the same answer. Such agreement is not the norm with CVSS currently [@allodi2018effect].


Table: SSVC pilot scores compared with the CVSS base scores for the vulnerabilities provided by NVD.

| CVE-ID         | Representative SSVC decision values | SSVC recommendation (supplier, deployer) | NVD’s CVSS base score  |
| :---------------- | :--------------------------------: | :--------------------- | :---------------------- |
| CVE-2014-0751  | E:N/T:T/U:L/S:H/X:C/M:C                   | (Sched, OOC)                       | 7.5 (High) (v2)        |
| CVE-2015-1014  | E:N/T:T/U:L/S:J/X:S/M:F                   | (Sched, Sched)                     | 7.3 (High) (v3.0)      |
| CVE-2015-5374  | E:A/T:P/U:L/S:H/X:C/M:F                   | (Immed, Immed)                     | 7.8 (High) (v2)        |
| CVE-2017-3183  | E:N/T:T/U:E/S:M/X:C/M:C                   | (Sched, Sched)                     | 8.8 (High) (v3.0)      |
| CVE-2017-5638  | E:A/T:T/U:S/S:M/X:U/M:C                   | (Immed, OOC)                       | 10.0 (Critical) (v3.0) |
| CVE-2017-9590  | E:P/T:T/U:E/S:M/X:U/M:D                   | (OOC, Sched)                       | 5.9 (Medium) (v3.0)    |
| CVE-2018-14781 | E:P/T:P/U:L/S:H/X:C/M:F                   | (OOC, OOC)                         | 5.3 (Medium) (v3.0)    |
| CVE-2019-2691  | E:N/T:P/U:E/S:M/X:C/M:C                   | (Sched, Sched)                     | 4.9 (Medium) (v3.0)    |
| CVE-2019-9042  | E:A/T:T/U:L/S:N/X:C/M:C                   | (OOC, Sched)                       | 7.2 (High) (v3.0)      |

Table 14 presents the mode decision point value for each vulnerability tested, as well as the recommendation that would result from that set based on the recommended decision trees in SSVC version 1. The comparison with the NVD’s CVSS base scores mostly confirms that SSVC is prioritizing based on different criteria, as designed. In particular, differences in the state of exploitation and safety impact are suggestive.

Based on these results, we made about ten changes, some bigger than others. We did not execute a new rater agreement experiment with the updated descriptions. The pilot results are encouraging, and we believe it is time to open up a wider community discussion.

## Improvements Instigated by the Pilot

The following changes were reflected in the version 1 Section "Decision Trees for Vulnerability Management."

  - Technical impact: We clarified that partial/total is decided regarding the system scope definition, which considers a database or a web server program as the “whole” system. Furthermore, “total” also includes any technical impact that exposes authentication credentials to the adversary, if those credentials are to the whole system.

  - We added advice for information gathering to answer safety impact and mission impact questions. This change is needed because of the particularly wide variety of background assumptions analysts made that influenced results and agreement.

  - We clarified that “MEF failure” refers to any **one** essential function failing, not failure of all of them. We changed most severe mission impact to “mission failure” to better reflect the relationship between MEFs and the organization’s mission.

  - We removed the “supplier portfolio value” question since it had poor agreement, and there is no clear way to correct it. We replaced this question with *Utility*, which better captures the relevant kinds of value (namely, to the adversary) of the affected component while remaining amenable to pragmatic analysis.

  - We clarified that “proof of concept” (see *Exploitation*) includes cases in which existing tooling counts as a PoC. The examples listed are suggestive, not exhaustive.

  - We reorganized the decision trees based on which items are easier to gather information for or which ones have a widely verifiable state. This change moved *exploitation* to the first question.

  - We changed the decision tree results such that if exposure is “small,” then the resulting priority is lower than before the pilot study. That is, “small” exposure has a stronger effect on reducing urgency.

### Questions Removed as Ineffective

In this section, we present ideas we tried but rejected for various reasons. We are not presenting this section as the final word on excluding these ideas, but we hope the reasons for excluding them are instructive, will help prevent others from re-inventing the proverbial wheel, and can guide thinking on future work.

Initially, we brainstormed approximately 12 potential decision points, most of which we removed early in our development process through informal testing. These decision points included adversary’s strategic benefit of exploiting the vulnerability, state of legal or regulatory obligations, cost of developing remediation, patch distribution readiness, financial losses to customers due to potential exploitation, and business losses to the deployer.

Some of these points left marks on other decision points. The decision point “financial losses of customers” led to an amendment of the definition of *Safety* to include “well-being,” such that, for example, bankruptcies of third parties are now a major safety impact. The “business losses to the deployer” decision point is covered as a mission impact insofar as profit is a mission of publicly traded corporations.

Three of the above decision points left no trace on the current system. “State of legal or regulatory obligations,” “cost of developing remediation,” and “patch distribution readiness” were dropped as either being too vaguely defined, too high level, or otherwise not within the scope of decisions by the defined stakeholders. The remaining decision point, “adversary’s strategic benefit of exploiting the vulnerability,” transmuted to a different sense of system value. In an attempt to be more concrete and not speculate about adversary motives, we considered a different sense of value: supplier portfolio value.

The only decision point that we have removed following the pilot is developer portfolio value. This notion of value was essentially an over-correction to the flaws identified in the “adversary’s strategic benefit of exploiting the vulnerability” decision point. “Supplier portfolio value” was defined as “the value of the affected component as a part of the developer’s product portfolio. Value is some combination of importance of a given piece of software, number of deployed instances of the software, and how many people rely on each. The developer may also include lifecycle stage (early development, stable release, decommissioning, etc.) as an aspect of value.” It had two possible values: low and high. As Table 13 demonstrates, there was relatively little agreement among the six analysts about how to evaluate this decision point. We replaced this sense of portfolio value with *Utility*, which combines *Value Density* and *Automatability*.
