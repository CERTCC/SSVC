---
status: "accepted"
date: 2025-08-26
---
# Use "Decision Table" Instead of "Decision Tree"

## Context and Problem Statement

SSVC uses a tabular model to map combinations of decision point values to
recommended actions.  Historically, this model was referred to as a "decision
tree" or "decision policy" with both terms being used interchangeably in
documentation and tooling.  However, "decision tree" has a well-established,
conflicting meaning in machine learning and statistics, and "decision policy"
has overloaded meanings beyond our intended usage.  Using the "decision tree"
for both concepts creates confusion, especially for audiences familiar with data
science or machine learning.

## Decision Drivers

- Avoid ambiguity with the machine learning and operations research concept of
  "decision tree"
- Use a less contentious term than "policy" as we are not dictating "capital-P
  Policy"
- Accurately describe the underlying SSVC data structure, which is a table of
  decision points and outcomes
- Improve clarity in documentation, tooling, and communication with
  practitioners
- Align terminology with the actual data representations used (CSV and JSON
  tables)

## Considered Options

- Switch to "decision framework"
- Switch to "decision table"

## Decision Outcome

Chosen option: 'Switch to "decision table"'

### Rationale

"Decision table"accurately describes the tabular structure used by
SSVC and avoids the well-established conflicting meaning of "decision tree" in
machine learning and statistics.

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
the SSVC model. References to "decision tree" in the visual/hierarchical sense
(i.e., tree diagrams used to illustrate a decision table) may still appear where
appropriate but should be clearly distinguished from the decision table itself.

## More Information

This change was introduced with the [SSVC v2025.9 release](https://github.com/CERTCC/SSVC/releases/tag/v2025.9).
