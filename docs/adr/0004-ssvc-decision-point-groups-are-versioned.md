---
# These are optional elements. Feel free to remove any of them.
status: "accepted"
date: 2023-10-31
deciders: adh, jspring, vssarvepalli, cgyarbrough, latyzenhaus, ehatleback
---
# Decision Point Groups are Versioned using SemVer

## Context and Problem Statement

Decision Point Groups are sets of decision points pinned to specific versions of those decision points.
These groups may change over time.

For example, the SSVC _Patch Applier_ and _Deployer_ trees have evolved as follows:

| _Patch Applier_ (SSVC v1) | _Deployer_ (SSVC v2)                                      |                   _Deployer_ (SSVC v2.1)                    |
|:-------------------------:|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| Exploitation 1.0.0        | Exploitation 1.0.0                                        |                     Exploitation 1.0.0                      |
| System Exposure 1.0.0     | System Exposure 1.0.1                                     |                    System Exposure 1.0.1                    |
| Mission Impact 1.0.0      | Mission Impact 1.0.0<br/>(as input to Human Impact 1.0.0) |  Mission Impact 2.0.0<br/>(as input to Human Impact 1.0.0)  |
| Safety Impact 1.0.0       | Safety Impact 1.0.0<br/>(as input to Human Impact 1.0.0)  |  Safety Impact 1.0.0<br/>(as input to Human Impact 1.0.0)   |
| -                         | Automatable 1.0.0<br/>(as input to Utility 1.0.1)         |                      Automatable 1.0.0                      |
| -                         | Value Density 1.0.0<br/>(as input to Utility 1.0.1)       |                              -                              |

We need to be able to discriminate between different versions of these groups.

## Decision Drivers

- Decision Points change over time
- The composition of decision point groups change over time
- It is important that we can discriminate between versions of decision point groups
- Although technically a Decision Point Group is fully defined by the set of pinned Decision Points it contains
(e.g., any column in the table above), we find it convenient to be able to refer to the group as a whole, and to be
able to discriminate between different versions of the group.

## Considered Options

- No versioning
- [Semantic Versioning](https://semver.org/)
- [CalVer](https://calver.org/)

## Decision Outcome

Chosen option: "Semantic Versioning", because it conveys the magnitude of changes to decision point groups, and provides
indication of compatibility expectations between versions.

### Consequences

- Maintaining version numbers for decision point groups will add a small burden to each decision point group.
- Semantic versioning will make it easier to track changes to decision point groups over time.
- Because we don't anticipate frequent changes to decision point groups, the burden of maintaining version numbers should be minimal.

## More Information

- [Github Discussion #303](https://github.com/CERTCC/SSVC/discussions/303)
