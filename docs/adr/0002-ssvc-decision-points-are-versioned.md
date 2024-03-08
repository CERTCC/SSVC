---
status: accepted
date: 2023-10-17 
deciders: adh, jspring, vssarvepalli, latyzenhaus, cgyarbrough, ehatleback
---
# SSVC Decision Points are versioned using Semantic Versioning

## Context and Problem Statement

A decision point represents a unit of information for use in one or more decisions
As SSVC evolves and grows, we occasionally have the need to modify an existing decision point.
This can happen as we learn more about a particular decision and how a particular decision point is used in practice.
It can also happen as we refine our understanding of the concept that a decision point represents.

Our expectation is that decision points could go through a number of revisions over time, but that the revisions
should be relatively infrequent after an initial period of refinement.

Note: This decision addresses the fact that decision points are versioned, but does not address how the version number
is used. We will address that in a separate decision.


## Decision Drivers

* Decision points evolve over time
  * new values (options) are added, modified, or removed
  * descriptions are updated

## Considered Options

* No versioning
* [Semantic versioning](https://semver.org/)
* [CalVer](https://calver.org/)

## Decision Outcome

Chosen option: "Semantic versioning" because it conveys the magnitude of changes to decision points, and provides
indication of compatibility expectations between versions.

- No versioning would be the simplest option, but it would make it difficult to track changes to decision points over time.
- CalVer doesn't reflect the magnitude of changes to decision points, and does not convey much information about
compatibility expectations between versions.
- Semver makes sense for decision point versioning because we don't anticipate them changing much once they go 1.0
  - and typo fixes etc. could just bump the fix version e.g., 1.0.2 -> 1.0.3


### Consequences

- Maintaining version numbers for decision points will add a small burden to each decision point.
- Semantic versioning will make it easier to track changes to decision points over time.
- Because we don't anticipate frequent changes to decision points, the burden of maintaining version numbers should be minimal.

### Confirmation

- JSON schema validation of the Decision Point object will confirm that the version number is a valid semantic version.
- Python unit tests will confirm that the version number is a valid semantic version.

## More Information

- [Discussion #289](https://github.com/CERTCC/SSVC/discussions/289) in the SSVC project. 
- [Semantic Versioning](https://semver.org/)
- [CalVer](https://calver.org/)