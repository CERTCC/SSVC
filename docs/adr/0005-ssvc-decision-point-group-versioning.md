---
# These are optional elements. Feel free to remove any of them.
status: "accepted"
date: 2023-10-31
deciders: adh, jspring, vssarvepalli, cgyarbrough, latyzenhaus, ehatleback
---
# Decision Point Group Versioning Rules

## Context and Problem Statement

[ADR 004](0004-ssvc-decision-point-groups-are-versioned.md) established that Decision Point Groups should be versioned.

This ADR establishes the rules for versioning Decision Point Groups.

## Decision Drivers

(See [ADR 004](0004-ssvc-decision-point-groups-are-versioned.md) for additional context.)

- Decision Points change over time
- The composition of decision point groups change over time
- It is important that we can discriminate between versions of decision point groups
- Although technically a Decision Point Group is fully defined by the set of 
  pinned Decision Points it contains, we find it convenient to be able to 
  refer to the group as a whole, and to be able to discriminate between different versions of the group.


## Considered Options

A number of options were discussed in
[SSVC Discussion #303](https://github.com/CERTCC/SSVC/discussions/303).

Summarizing that discussion:

- No versioning
- [Semantic Versioning](https://semver.org/) of SSVC as a whole (status quo)
- [Semantic Versioning](https://semver.org/) of individual decision point groups
- [CalVer](https://calver.org/)

## Decision Outcome

Chosen option: "Semantic Versioning of individual decision point groups",
because it conveys the magnitude of changes to decision point groups, and
provides indication of compatibility expectations between versions.

Implemented as follows:

The core identity of a decision point group is derived from the pairing of the
_stakeholder role_ and the specific _decision_ being modeled.

### Create a new object when

- The stakeholder role and/or the decision being modeled changes. Even if the
set of decision points remains the same, a shift in either stakeholder role or
the decision represents a branching in the version history.

**Note:** New objects MUST have a new name.

Otherwise, a change (add, remove) in decision point groups where both the
role and decision being modeled are held constant SHOULD be given a new
version of the existing name according to the following rules.

### Increment the major version when

- Conditions for creating a new object are not met, AND
  - Adding or removing a decision point entirely, OR
  - An existing decision point increments its major version

### Increment the minor version when

- Conditions for incrementing the major version are not met, AND
- An existing decision point increments its minor version

### Increment the patch version when

- Conditions for incrementing the minor version are not met, AND
  - An existing decision point increments its patch version, OR
  - The decision point group description changes, OR
  - The decision point group name changes

### Examples

Assume a decision point group (DPG) named _DPG v1.0.0_,
containing decision points (DP) _A v1.0.0_ and _B v1.3.1_.
In the table below, we show how the Decision Point Group version number changes
as the constituent Decision Points change.

| DPG Start Version |        DP A        |        DP B        |        DP C        | DPG End Version |
|:-----------------:|:------------------:|:------------------:|:------------------:|:---------------:|
|       1.0.0       |       1.0.0        | 1.3.1 &rarr; 1.3.2 |         -          |      1.0.1      |
|       1.0.1       | 1.0.0 &rarr; 1.1.0 |       1.3.2        |         -          |      1.1.0      |
|       1.1.0       |       1.1.0        |     (removed)      |       1.0.0        |      2.0.0      |
|       2.0.0       |       1.1.0        |         -          | 1.0.0 &rarr; 2.0.0 |      3.0.0      |

In row 1, DP B undergoes a patch version increment, which triggers a patch version increment for the DPG.
In row 2, DP A undergoes a minor version increment, which triggers a minor version increment for the DPG.
In row 3, DP B is replaced by DP C, which triggers a major version increment for the DPG.
In row 4, DP C undergoes a major version increment, which triggers a major version increment for the DPG.

### Consequences

- Maintaining version numbers for decision point groups will add a small burden to each decision point group.
- Semantic versioning will make it easier to track changes to decision point groups over time.
- Because we don't anticipate frequent changes to decision point groups, the burden of maintaining version numbers should be minimal.
- We are deliberately avoiding using the _name_ of the Decision Point Group as part of the versioning scheme, as
in the motivating example in
[ADR 0004](0004-ssvc-decision-point-groups-are-versioned.md) we shifted the
group name from _Patch Applier_ to _Deployer_, but since the group is still
intended to represent the same _stakeholder role_ and _decision_, we want
to be able to treat name changes as aliases rather than versioning events.

## More Information

- [Github Discussion #303](https://github.com/CERTCC/SSVC/discussions/303)
