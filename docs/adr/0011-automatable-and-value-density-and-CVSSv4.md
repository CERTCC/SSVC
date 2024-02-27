---

status: "accepted"
date: 2024-02-23
deciders: adh, jspring

---
# Correspondence between Automatable v2.0.0, Value Density v1.0.0, and CVSS v4

## Context and Problem Statement

Two SSVC decision points happen to match two CVSS v4 supplemental metrics.
This ADR is to make clear what the SSVC support plan is in regards to this overlap for future versions of these decision points and metrics.


## Decision Drivers

* The SSVC and CVSS communities have productively shared ideas and concepts in the past. These two decision points are an example. It was a relatively long process to propose these decision points as CVSS metrics, take feedback from the CVSS community, get text approved, and then port those changes over to SSVC. This all happened several years before we had this formalized decision documentation process within SSVC.

## Considered Options

* No support, expressed or implied, by either group
* SSVC project commits to mirroring any changes made to CVSS
* CVSS SIG commits to mirroring any changes made by the SSVC project
* Both the second and third options, leading to joint decision making on these two decision points / metrics.

## Decision Outcome

Chosen option: "No support, expressed or implied, by either group", because
there are no structured agreements in place that could create a service expectation for any continued synchronization going forwards.
The CVSS SIG is an independent group, even if there may be some overlap with the SSVC community, and SSVC cannot require or expect any changes by CVSS.
While SSVC may mirror any changes the CVSS SIG makes to these metrics in the future, that change should be considered by the SSVC community indepdently on its merits, through the normal change management processes for suggestions to amend decision points.


### Consequences

* Good, because low overhead -- no additional organizational structures
* Good, because leaves the opportunity for continued synchronization open if everyone agrees
* Bad, because no guarantee of future synchronization



### Confirmation

The implementation of this decision is confirmed by continued use of SSVC community change management proceedures for these decision points independent of formal updates to CVSS.

## More Information

This decision could hypothetically be revisited at the request of the CVSS SIG.

