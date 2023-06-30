## Guidance for Evidence Gathering

To answer each of these decision points, a stakeholder should, as much as possible, have a repeatable evidence collection and evaluation process. However, we are proposing decisions for humans to make, so evidence collection and evaluation is not totally automatable. That caveat notwithstanding, some automation is possible.

For example, whether exploitation modules are available in ExploitDB, Metasploit, or other sources is straightforward.
We hypothesize that searching Github and Pastebin for exploit code can be captured in a script.
A supplier or deployer could then define [*Exploitation*](#exploitation) to take the value of [*PoC*](#exploitation) if there are positive search results for a set of inputs derived from the CVE entry in at least one of these venues.
At least, for those vulnerabilities that are not “automatically” PoC-ready, such as on-path attackers for TLS or network replays.

Some of the decision points require a substantial upfront analysis effort to gather risk assessment or organizational data. However, once gathered, this information can be efficiently reused across many vulnerabilities and only refreshed occasionally. An obvious example of this is the mission impact decision point. To answer this, a deployer must analyze their essential functions, how they interrelate, and how they are supported. Exposure is similar; answering that decision point requires an asset inventory, adequate understanding of the network topology, and a view of the enforced security controls. Independently operated scans, such as Shodan or Shadowserver, may play a role in evaluating exposure, but the entire exposure question cannot be reduced to a binary question of whether an organization’s assets appear in such databases. Once the deployer has the situational awareness to understand MEFs or exposure, selecting the answer for each individual vulnerability is usually straightforward.

Stakeholders who use the prioritization method should consider releasing the priority with which they handled the vulnerability. This disclosure has various benefits. For example, if the supplier publishes a priority ranking, then deployers could consider that in their decision-making process. One reasonable way to include it is to break ties for the deployer. If a deployer has three “scheduled” vulnerabilities to remediate, they may address them in any order. If two vulnerabilities were produced by the supplier as “scheduled” patches, and one was “out-of-cycle,” then the deployer may want to use that information to favor the latter.

In the case where no information is available or the organization has not yet matured its initial situational analysis, we can suggest something like defaults for some decision points.
If the deployer does not know their exposure,<!--lowercase exposure on purpose, this is the general concept--> that means they do not know where the devices are or how they are controlled, so they should assume [*System Exposure*](#system-exposure) is [*open*](#system-exposure).
If the decision maker knows nothing about the environment in which the device is used, we suggest assuming a [*major*](#safety-impact) [*Safety Impact*](#safety-impact). This position is conservative, but software is thoroughly embedded in daily life now, so we suggest that the decision maker provide evidence that no one’s well-being will suffer. The reach of software exploits is no longer limited to a research network.
Similarly, with [*Mission Impact*](#mission-impact), the deployer should assume that the software is in use at the organization for a reason, and that it supports essential functions unless they have evidence otherwise.
With a total lack of information, assume [*support crippled*](#mission-impact) as a default.
[*Exploitation*](#exploitation) needs no special default; if adequate searches are made for exploit code and none is found, the answer is [*none*](#exploitation).
If nothing is known about [*Automatable*](#automatable), the safer answer to assume is [*yes*](#automatable).
[*Value Density*](#value-density) should always be answerable; if the product is uncommon, it is probably [*diffuse*](#value-density).
The resulting decision set {*none*, *open*, *efficient*, *medium*} results in a scheduled patch application in our recommended deployer tree.

