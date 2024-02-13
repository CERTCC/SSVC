# Data Operations

!!! note inline end

      The diagram below shows two kinds of data emanating from the Data Operations process: _Vulnerability Data_ and _Environment Data_.
      Vulnerability Data is data about the vulnerability itself, such as the technical impact or exploit availability.
      Environment Data is data about the environment in which the vulnerable systems exist, such as network topology or system criticality.
      We generally expect that Environment Data will be more stable than Vulnerability Data, but that is not always the case.

While the actual collection of operational data is outside the scope of SSVC, it is an important part of any implementation
of the process.
SSVC is designed to be flexible enough to accommodate a variety of data collection methods.
The [Data Mapping](prepare.md) step defines the data that is needed to assign a value to each decision point.
The Data Operations process collects that data so that it can be used to assign values to decision points in the 
[Use SSVC](use.md) step.

We include a feedback loop on the data collection node to indicate that it is expected to be a continuous process. 

```mermaid
flowchart LR
    subgraph dmp[Data Mapping]
       dd[/Data Definition/]
    end
    subgraph do[Data Operations]
        cd[Collect Data]
        vd[/Vulnerability Data/]
        ed[/Environment Data/]
        dt[\Available Data/]
    end
    dd --> cd
    cd --> cd
    cd --> vd
    cd --> ed
    vd --> dt
    ed --> dt
```

!!! example

     Having defined a data map that translates certain values from specific threat feeds to the _Exploitation_ decision 
     point values _PoC_ or _Active_, an organization maintains a subscription to those threat feeds and collects the 
     data from them on a continuous basis. 
     They also write a script that parses the data from the threat feeds and applies the data map to assign a value to 
     the _Exploitation_ decision point.

## Guidance for Evidence Gathering

To answer each of these decision points, a stakeholder should, as much as possible, have a repeatable evidence
collection and evaluation process.
However, we are proposing decisions for humans to make, so evidence collection and evaluation is not totally automatable.
That caveat notwithstanding, some automation is possible.

!!! example "Evidence of Exploitation"

    For example, whether exploitation modules are available in ExploitDB, Metasploit, or other sources is straightforward.
    We hypothesize that searching Github and Pastebin for exploit code can be captured in a script.
    A supplier or deployer could then define [*Exploitation*](../../reference/decision_points/exploitation.md) to take the value of [*PoC*](../../reference/decision_points/exploitation.md) if
    there are positive search results for a set of inputs derived from the CVE entry in at least one of these venues.
    At least, for those vulnerabilities that are not “automatically” PoC-ready, such as on-path attackers for TLS or network
    replays.

Some of the decision points require a substantial upfront analysis effort to gather risk assessment or organizational
data.
However, once gathered, this information can be efficiently reused across many vulnerabilities and only refreshed
occasionally.

!!! example "Evidence of Mission Impact"

    An obvious example of this is the mission impact decision point.
    To answer this, a deployer must analyze their essential functions, how they interrelate, and how they are supported.

!!! example "Evidence of Exposure"

    Exposure is similar; answering that decision point requires an asset inventory, adequate understanding of the network
    topology, and a view of the enforced security controls.
    Independently operated scans, such as Shodan or Shadowserver, may play a role in evaluating exposure, but the entire
    exposure question cannot be reduced to a binary question of whether an organization’s assets appear in such databases.

Once the deployer has the situational awareness to understand MEFs or exposure, selecting the answer for each individual
vulnerability is usually straightforward.

Stakeholders who use the prioritization method should consider releasing the priority with which they handled the
vulnerability.
This disclosure has various benefits.
For example, if the supplier publishes a priority ranking, then deployers could consider that in their decision-making
process.
One reasonable way to include it is to break ties for the deployer.
If a deployer has three “scheduled” vulnerabilities to remediate, they may address them in any order.
If two vulnerabilities were produced by the supplier as “scheduled” patches, and one was “out-of-cycle,” then the
deployer may want to use that information to favor the latter.

### Suggested Default Values

In the case where no information is available or the organization has not yet matured its initial situational analysis,
we can suggest something like defaults for some decision points.

!!! tip "Default Exposure Values"

    If the deployer does not know their exposure,<!--lowercase exposure on purpose, this is the general concept--> that
    means they do not know where the devices are or how they are controlled, so they should assume
    [*System Exposure*](../../reference/decision_points/system_exposure.md) is [*open*](../../reference/decision_points/system_exposure.md).

!!! tip "Default Safety Values"

    If the decision maker knows nothing about the environment in which the device is used, we suggest assuming a
    [*major*](../../reference/decision_points/safety_impact.md) [*Safety Impact*](../../reference/decision_points/safety_impact.md).
    This position is conservative, but software is thoroughly embedded in daily life now, so we suggest that the decision
    maker provide evidence that no one’s well-being will suffer.

The reach of software exploits is no longer limited to a research network.

!!! tip "Default Mission Impact Values"

    Similarly, with [*Mission Impact*](../../reference/decision_points/mission_impact.md), the deployer should assume that the software is in use at the
    organization for a reason, and that it supports essential functions unless they have evidence otherwise.
    With a total lack of information, assume [*support crippled*](../../reference/decision_points/mission_impact.md) as a default.
    [*Exploitation*](../../reference/decision_points/exploitation.md) needs no special default; if adequate searches are made for exploit code and none is
    found, the answer is [*none*](../../reference/decision_points/exploitation.md).


!!! tip "Default Automatable Values"

    If nothing is known about [*Automatable*](../../reference/decision_points/automatable.md), the safer answer to assume is [*yes*](../../reference/decision_points/automatable.md).
    [*Value Density*](../../reference/decision_points/value_density.md) should always be answerable; if the product is uncommon, it is probably
    [*diffuse*](../../reference/decision_points/value_density.md).

The resulting decision set `{none, open, yes, medium}` results in a scheduled patch application in our recommended
deployer tree.

