## Relationship to asset management

Our method is for prioritizing vulnerabilities based on the risk stemming from exploitation. There are other reasonable asset management considerations that may influence remediation timelines. There are at least three aspects of asset management that may be important but are out of scope for SSVC. First and most obvious is the transaction cost of conducting the mitigation or remediation. System administrators are paid to develop or apply any remediations or mitigations, and there may be other transactional costs such as downtime for updates. Second is the risk of the remediation or mitigation introducing a new error or vulnerability. Regression testing is part of managing this type of risk. Finally, there may be an operational cost of applying a remediation or mitigation, representing an ongoing change of functionality or increased overhead. A decision maker could order work within one SSVC priority class (scheduled, out-of-cycle, etc.) based on these asset management considerations, for example. Once the organization remediates or mitigates all the high-priority vulnerabilities, they can then focus on the medium-level vulnerabilities with the same effort spent on the high-priority ones.

Asset management and risk management also drive some of the up-front work an organization would need to do to gather some of the necessary information. This situation is not new; an asset owner cannot prioritize which fixes to deploy to its assets if it does not know what assets it owns and their locations. The organization can pick its choice of tools for these things; there are about 200 asset management tools on the market [@captera]. Standards like the Software Bill of Materials (SBOM) [@manion2019sbom] would likely reduce the burden on asset management, but these are still maturing. If an organization does not have an asset management or risk management (see Section 4.4.6.1) plan and process in place, then it will have a non-trivial amount of work to do to establish these processes before it can take full advantage of SSVC.

## Supplier Tree

Figure 1 shows the proposed prioritization decision tree for the supplier. Both supplier and deployer trees use the above decision point definitions. Each tree is a compact way of expressing assertions or hypotheses about the relative priority of different situations. Each tree organizes how we propose a stakeholder should treat these situations. Rectangles are decision points, and triangles represent outcomes. The values for each decision point are different, as described above. Outcomes are priority decisions (defer, scheduled, out-of-cycle, immediate); outcome triangles are color coded:

  - Defer = gray with green outline
  - Scheduled = yellow
  - Out-of-Cycle = orange
  - Immediate = red with black outline

<img src="version_1/gfx/vul-management_v1-6-page2.png" alt="Figure 1: Suggested supplier tree" style="width: 90%;" />

Figure 1: Proposed Vulnerability Prioritization Decision Tree for Patch
Supplier

## Deployer Tree

The proposed deployer tree is depicted in Figure 3, Figure 4, and Figure 5. The state of *Exploitation* is the first decision point, but in an effort to make the tree legible, we split the tree into three sub-trees over three pages. We suggest making the decision about *Exploitation* as usual, and then going to the correct subtree.

<img src="version_1/gfx/vul-management_v1-6-page3.png" alt="Figure 2" style="width: 90%;" />

Figure 2: Proposed Vulnerability Prioritization Decision Tree for Patch
Deployers (Continued in Figure 3 and Figure 4)

<img src="version_1/gfx/vul-management_v1-6-page4.png" alt="Figure 3" style="width: 90%;" />

Figure 3: Proposed Vulnerability Prioritization Decision Tree for Patch
Deployers (Continued from Figure 2 and in Figure 4).

<img src="version_1/gfx/vul-management_v1-6-page5.png" alt="Figure 4" style="width: 90%;" />

Figure 4: Proposed Vulnerability Prioritization Decision Tree for Patch
Deployers (Continued from Figure 2 and Figure 3)

## Tree Construction and Customization Guidance

Stakeholders are encouraged to customize the SSVC decision process to their needs.
Indeed, the first part of SSVC stands for "stakeholder-specific."
However, certain parts of SSVC are more amenable to customization than others.
In this section, we'll cover what a stakeholder should leave static, what we imagine customization looks like, and some advice on building a usable and manageable decision tree based on our experience so far.

We suggest that the decision points, their definitions, and the decision values should not be customized.
Different vulnerability management teams inevitably think of topics such as [*Utility*](#utility) to the adversary in slightly different ways.
However, a key contribution of SSVC is enabling different teams to communicate about their decision process.
In order to clearly communicate differences in the process, the decision points that factor into the process need to be the same between different teams.
A stakeholder community may come together and, if there is broad consensus, add or change decision points.

Which decision points are involved in a vulnerability management team's decision and the priority label for each resulting situation are, for all intents and purposes, totally at the discretion of the team.
We have provided some examples for different stakeholder communities here.
What decision points a team considers reflects what it cares about and the risks prioritizes.
Different teams may legitimately prioritize different objectives.
It should be easier for teams to discuss and communicate such differences if the definitions of the decision points remain static.
The other aspect of risk management that SSVC allows a team to customize is its risk appetite or risk tolerance.

A team's risk appetite is reflected directly by the priority labels for each combination of decision values.
For example, a vulnerability with [no or minor](#public-safety-impact) [*Public Safety Impact*](#public-safety-impact), [total](#technical-impact) [*Technical Impact*](#technical-impact), and [efficient](#utility) [*Utility*](#utility) might be handled with [*scheduled*](#supplier-decisions) priority by one team and [*out-of-cycle*](#supplier-decisions) priority by another.
As long as each team has documented this choice and is consistent in its own application of its own choice, the two teams can legitimately have different appetites for vulnerability risk.
SSVC enables teams with such different risk appetites to discuss and communicate precisely the circumstances where they differ.  

When doing the detailed risk management work of creating or modifying a tree, we recommend working from text files with one line or row for each unique combination of decision values.
For examples, see [SSVC/data](https://github.com/CERTCC/SSVC/tree/main/data).
An important benefit, in our experience, is that it's easier to identify a question by saying "I'm unsure about row 16" than anything else we have thought of so far.


Once the decision points are selected and the prioritization labels agreed upon, it is convenient to be able to visually compress the text file by displaying it as a decision tree.
Making the decision process accessible has a lot of benefits.
Unfortunately, it also makes it a bit too easy to overcomplicate the decision.

The SSVC version 1  ~applier~ deployer tree had 225 rows when we wrote it out in long text form.
It only has four outcomes to differentiate between.
Thus on average that decision process treats one situation (combination of decision values) as equivalent to 65 other situations.
If nothing else, this means analysts are spending time gathering evidence to make fine distinctions that are not used in the final decision.
The added details also make it harder for the decision process to accurately manage the risks in question.
This difficulty arises because more variance and complexity there is in the decision increases the possibility of errors in the decision process itself.

While there is no hard and fast rule for when a tree is too big, we suggest that if all of your outcomes are associated with more than 15 situations (unique combinations of decision values), you would benefit from asking whether your analysts actually use all the information they would be gathering.
Thus, 60 unique combinations of decision values is the point at which a decision tree with four distinct outcomes is, on average, potentially too big.

## Evidence Gathering Guidance

To answer each of these decision points, a supplier or deployer should, as much as possible, have a repeatable evidence collection and evaluation process. However, we are proposing decisions for humans to make, so evidence collection and evaluation is not totally automatable. That caveat notwithstanding, some automation is possible.

For example, whether exploitation modules are available in ExploitDB, Metasploit, or other sources is straightforward. We hypothesize that searching Github and Pastebin for exploit code should be automatable. A supplier or deployer could then define *Exploitation* **PoC available** to be positive search results for a set of inputs derived from the CVE entry in at least one of these venues. At least, for those vulnerabilities that are not “automatically” PoC-ready, such as on-path attackers for TLS or network replays.

Some of the decision points require some substantial upfront analysis effort to gather risk assessment or organizational data. However, once gathered, this information can be efficiently reused across many vulnerabilities and only refreshed occasionally. An obvious example of this is the mission impact decision point. To answer this, a deployer must analyze their essential functions, how they interrelate, and how they are supported. Exposure is similar; answering that decision point requires an asset inventory, adequate understanding of the network topology, and a view of the enforced security controls. Independently operated scans, such as Shodan or Shadowserver, may play a role in evaluating exposure, but the entire exposure question cannot be reduced to a binary question of whether an organization’s assets appear in such databases. Once the deployer has the situational awareness to understand MEFs or exposure, selecting the answer for each individual vulnerability is usually straightforward.

Stakeholders who use the prioritization method should consider releasing the priority with which they handled the vulnerability. This disclosure has various benefits. For example, if the supplier publishes a priority ranking, then deployers could consider that in their decision-making process. One reasonable way to include it is to break ties for the deployer. If a deployer has three “scheduled” vulnerabilities to remediate, they may address them in any order. If two vulnerabilities were produced by the supplier as “scheduled” patches, and one was “out-of-cycle,” then the deployer may want to use that information to favor the latter.

In the case where no information is available or the organization has not yet matured its initial situational analysis, we can suggest something like defaults for some decision points. If the deployer does not know their exposure,<!--lowercase exposure on purpose, this is the general concept--> that means they do not know where the devices are or how they are controlled, so they should assume *Exposure* is **open**. If the decision maker knows nothing about the environment in which the device is used, we suggest assuming a **major** *Safety Impact*. This position is conservative, but software is thoroughly embedded in daily life now, so we suggest that the decision maker provide evidence that no one’s well-being will suffer. The reach of software exploits is no longer limited to a research network. Similarly, with *Mission Impact*, the deployer should assume that the software is in use at the organization for a reason, and that it supports essential functions unless they have evidence otherwise. With a total lack of information, assume **

support crippled** as a default. *Exploitation* needs no special default; if adequate searches are made for exploit code and none is found, the answer is **none**. The decision set {**none**, **open**, **MEF crippled**, **major**} results in a scheduled patch application.

## Guidance on Communicating Results

There are many aspects of SSVC that two parties might want to communicate.
Not every stakeholder will use the decision points to make comparable decisions.
Suppliers and deployers make interdependent decisions, but the actions of one group are not strictly dependent on the other.
Recall that one reason for this is that SSVC is about prioritizing a vulnerability response action in general, not specifically applying a patch that a supplier produced.
Coordinators are particularly interested in facilitating communication because that is their core function.
This section handles three aspects of this challenge: formats for communicating SSVC, how to handle partial or incomplete information, and how to handle information that may change over time.

This section is about communicating SSVC information about a specific vulnerability.
A supplier making a decision on allocating effort or a deployer should have a decision tree and it's decision points and possible values specified already.
[Representation choices](#representation-choices) discussed how SSVC uses a text file as the canonical form of a decision tree; the example trees can be found in [SSVC/data](https://github.com/CERTCC/SSVC/tree/main/data).
A supplier communicating with constituents or a coordinator may communicate partial information about a specific vulnerability to help other stakeholders.

We recommend two structured communication formats, abbreviated and full.
The goal of the abbreviated format is to fill a need for providing identifying information about a vulnerability or decision in charts, graphs, and tables. Therefore, the abbreviated format is not designed to stand alone.
The goal of the full format is to capture all the context and details about a decision or work item in a clear and machine-readable way.  

SSVC abbreviated form borrows directly from the CVSS "vector string" notation.  
The basic format for SSVC is:
```
(version)/(decision point):(value)[/decision point:value[/decision point:value[...]]][/time]/
```
Where `version` is `SSVCv2`, updated with more options in the future as needed.
The term `decision point` is one or two letters derived from the name of the decision point as follows:
 - Start with the decision point name as given in [Likely Decision Points and Relevant Data](#likely-decision-points-and-relevant-data).
 - Remove any text in parentheses (and the parentheses themselves).
 - Remove the word "Impact" if it's part of the name.
 - Create an initialism from remaining title-case words (ignore "of," etc.), taking only the first two words.
 - The first letter of the initialism is upper case; if there is a second letter, then it is lower case.

For example, [*Technical Impact*](#technical-impact) becomes `T` and [*Public Safety Impact*](#public-safety-impact) becomes `Ps`.

The term `value` is a statement of the value or possible values of the decision point that precedes it and to which it is connected by a `:`.
Similar to `decision point`, `value` should be made up of one or two letters derived from the name of the decision value in the section for its associated decision point.
For example [MEF support crippled](#mission-impact) becomes `Ms` and [efficient](#utility) becomes `E`.
Labels on values do not need to be globally unique, just unique to the associated decision point.

The character `/` separates decision-point:value pairs.
As many pairs should be provided in the abbreviated form as are required to communicate the desired information about the vulnerability or work item.
The ordering of the pairs should be sorted alphabetically from A to Z by the ASCII characters representing the decision points.
A trailing `/` is used to close the string.

The optional parameter `time` is the time in seconds since the UNIX epoch that the SSVC information was collected or last checked for freshness and accuracy.

Based on this, an example string could be:
```
SSVCv2/Ps:Nm/T:T/U:E/1605040000/
```
For a vulnerability with [no or minor](#public-safety-impact) [*Public Safety Impact*](#public-safety-impact), [total](#technical-impact) [*Technical Impact*](#technical-impact), and [efficient](#utility) [*Utility*](#utility), which was evaluated on Nov 10, 2020.

    - TODO if we are going to talk about JSON or other structured data formats for decisions, do so here.

What an analyst knows about a vulnerability may not be complete. 
However, the vulnerability management community may still benefit from partial information.
Particularly, suppliers and coordinators, who may not know everything a deployer knows, may still provide benefit to deployers by sharing what partial information they do know.
A second benefit to providing methods for communicating partial information is the reduction of bottlenecks or barriers to information exchange.
A timely partial warning is better than a complete warning that is too late.

The basic guidance is that the analyst should communicate all of the vulnerability's possible states, to the best of the analyst's knowledge.
If the analyst knows nothing, all states are possible.
For example, [*Utility*](#utility) may be [laborious](#utility), [efficient](#utility), or [super effective](#utility).
In abbreviated form, write this as `U:LESe`.
Since a capital letter always indicates a new value, this is unambiguous.

The reason a stakeholder might publish something like `U:LESe` is that it expresses that the analyst thought about [*Utility*](#utility) but does not have anything to communicate.
A stakeholder might have information to communicate about some decision points but not others.
If SSVC uses this format to list the values that are in play for a particular vulnerability, there is no need for a special "I don't know" marker.

The merit in this "list all values" approach emerges when the stakeholder knows that the value for a decision point may be A or B, but not C.
For example, say the analyst knows that [*Value Density*](#value-density) is [diffuse](#value-density) but does not know the value for [*Automatability](#automatability).
Then the analyst can usefully restrict [*Utility*](#utility) to one of [laborious](#utility) or [efficient](#utility).
In abbreviated form, write this as `U:LE`.
As discussed below, information can change over time.
Partial information may be, but is not required to be, sharpened over time into a precise value for the decision point.


    - TODO fix #29 here (changing information)

## Development Methodology

For this tabletop refinement, we could not select a mathematically representative set of CVEs. The goal was to select a handful of CVEs that would cover diverse types of vulnerabilities. The CVEs that we used for our tabletop exercises are CVE-2017-8083, CVE-2019-2712, CVE-2014-5570, and CVE-2017-5753. We discussed each one from the perspective of supplier and deployer. We evaluated CVE-2017-8083 twice because our understanding and descriptions had changed materially after the first three CVEs (six evaluation exercises). After we were satisfied that the decision trees were clearly defined and captured our intentions, we began the formal evaluation of the draft trees, which we describe in the next section.
