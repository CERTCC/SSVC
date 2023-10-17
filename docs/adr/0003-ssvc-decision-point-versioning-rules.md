---
status: accepted
date: 2023-10-17 
deciders: adh, jspring, vssarvepalli, latyzenhaus, cgyarbrough, ehatleback
---
# SSVC Decision Points Versioning Rules

## Context and Problem Statement


A decision point represents a unit of information for use in one or more decisions
An SSVC "version" might introduce new decision points or new functions (trees) over existing decision points (or both)
As SSVC evolves and grows, we occasionally have the need to modify an existing decision point.
This can happen as we learn more about a particular decision and how a particular decision point is used in practice.
It can also happen as we refine our understanding of the concept that a decision point represents.

Our expectation is that decision points could go through a number of revisions over time, but that the revisions
should be relatively infrequent after an initial period of refinement.

Note: This decision addresses the rules for versioning, and depends on the decision to version decision points in the first place.


## Decision Drivers

* Decision points evolve over time
  * new values (options) are added, modified, or removed
  * descriptions are updated
* Semantic versioning is a well-known and well-understood standard, but we need to define how it applies to decision points.

## Considered Options

See SSVC [Discussion #289](https://github.com/CERTCC/SSVC/discussions/289).

Strictly speaking, Decision Points might not need to be explicitly versioned because they're basically static once introduced.
(Because any semantic change just forks into a new decision point.)
However, for future-proofing purposes we might want to include a key-value pair in the decision point definition to represent a version ID.

We could establish rules such as
- version 0.x is reserved for pre-support Decision Points and their shorthand key, labels, number of labels, ordering of labels, descriptions, semantics, etc. are all subject to change
- version 1.0 freezes the Decision Point labels, number of labels, and their ordering
- version 1.0.x for x > 0 would be limited to description changes


## Decision Outcome

Chosen option: "Semantic versioning":

> Given a version number MAJOR.MINOR.PATCH, increment the:
> 
> - MAJOR version when you make incompatible API changes
> - MINOR version when you add functionality in a backward compatible manner 
> - PATCH version when you make backward compatible bug fixes
>
> Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

Applied as follows:


| Do this...           | ...when...                                                                                                                                                                                                                                                        |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New Object           | A different or new concept is being represented<br/>Note: new objects get new names                                                                                                                                                                               |
| +1 Major Version     | Existing options are _removed_<br/>Option semantics change in a way that older answers are no longer usable<br/>New options are added that divide previous semantics ambiguously<br/>Note: The ability to map old to new semantics is encouraged but not required |
| +0.1 Minor Version   | New options are added<br/>Option names are changed while semantics are retained<br/>_AND_ all existing options are retained with compatible semantics                                                                                                             |
| +0.0.1 Patch Version | No changes to number of options<br/>No changes to semantics of options<br/>Typo fixes in option names or decision point name                                                                                                                                      |

Decision Points having a major version of 0 are considered to be pre-support and their shorthand key, labels, number of labels, ordering of labels, descriptions, semantics, etc. are all subject to change.
Because the Major Version is 0 for these decision points, the Minor Version and Fix Version can be used to indicate how
significant a change is by combining the above rules for Major and Minor versions into a single rule for Minor versions.
In other words, a Minor version increment of a 0.x decision point may be used to indicate a change in semantics that
is not backwards compatible. This is not the case for decision points with a Major Version of 1 or greater.

The lowest supported version of a decision point is 1.0.0.

### Consequences

- Maintaining version numbers for decision points according to these rules will add a small burden to each decision point.
- Semantic versioning will make it easier to track changes to decision points over time.
- Because we don't anticipate frequent changes to decision points, the burden of maintaining version numbers should be minimal.
- Decision point versions can move in either direction when used repeatedly in other versioned objects (E.g., a decision model could
use use version 2.1 of a decision point at one time and later revert to using version 1.0 if the 2.1 was found to be problematic).
- Multiple versions of decision points will be "live and available for use" by folks modeling decisions unless explicitly deprecated.
- We think that Decision Points SHOULD have a way to indicate a deprecated status as a means to stave off future regrets.
This implies the need for a way to denote the _status_ of a decision point in addition to its _version_.
Decision Point _status_ will need to be addressed in a separate decision (or decisions) regarding decision point lifecycles.

### Confirmation

- The PR process will confirm that the decision point version number is updated according to these rules.

## More Information

- [Discussion #289](https://github.com/CERTCC/SSVC/discussions/289) in the SSVC project. 
- [Semantic Versioning](https://semver.org/)
