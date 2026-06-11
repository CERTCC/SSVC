---
status: "accepted"
date: 2025-08-26
---
# Use "Decision Table" Instead of "Decision Tree"

## Context and Problem Statement

SSVC uses a tabular model to map combinations of decision point values to
recommended actions.  Historically, this model was referred to as a "decision
tree" or "decision policy" with both terms being used interchangeably in
documentation and tooling. While our use of "decision tree" was consistent with
usage in the context of Operations Research
(Wikipedia: [Decision tree](https://en.wikipedia.org/wiki/Decision_tree)),
it caused confusion with the related-yet-different concept from Machine Learning
(Wikipedia: [Decision tree learning](https://en.wikipedia.org/wiki/Decision_tree_learning)).
Furthermore, the term "decision policy" has overloaded meanings beyond our
intended usage.  We want to avoid confusion on both fronts, therefore we need a
new term.

## Decision Drivers

- Avoid ambiguity with the machine learning and operations research concept of
  "decision tree"
- Use a less contentious term than "policy" as we are not dictating "capital-P
  Policy"
- Accurately describe the underlying SSVC data structure, which is a table of
  decision point value combinations and outcomes
- Improve clarity in documentation, tooling, and communication with
  practitioners
- Align terminology with the actual data representations used (CSV and JSON
  tables)

## Considered Options

- Switch to decision framework
- Switch to decision table
- Switch to decision model

## Decision Outcome

Chosen option: "Switch to decision table"

### Rationale

"Decision table" accurately describes the tabular structure used by
SSVC and avoids the well-established conflicting meaning of "decision tree" in
machine learning and statistics.

We may use *decision model* for the more generic class of things to which a
*decision table* belongs, but *decision table* is specific enough to make it
clear exactly what our intended meaning is.

### Consequences

- Good, because the terminology now accurately reflects the underlying data
  model (a table mapping decision point values to outcomes)
- Good, because it reduces confusion for practitioners familiar with machine
  learning
- Bad, because some existing documentation, external references, and tooling may
  still use "decision tree" — these will be updated incrementally
- Bad, because the change breaks consistency with prior SSVC publications and
  external references that use "decision tree"

### Confirmation

Documentation, code, and tooling use "decision table" as the primary term for
an SSVC decision model. References to "decision tree" in the visual/hierarchical sense
(i.e., tree diagrams used to illustrate a decision table) may still appear where
appropriate but should be clearly distinguished from the decision table itself.

## More Information

- This change was introduced with the [SSVC v2025.9 release](https://github.com/CERTCC/SSVC/releases/tag/v2025.9).
- Wikipedia's [Decision table](https://en.wikipedia.org/wiki/Decision_table) page aligns with the concept that
  we are trying to capture.
