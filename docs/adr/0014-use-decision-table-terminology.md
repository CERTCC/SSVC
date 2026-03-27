---
status: "accepted"
date: 2025-09-17
---
# Use "Decision Table" Instead of "Decision Tree"

## Context and Problem Statement

SSVC uses a tabular model to map combinations of decision point values to recommended actions.
Historically, this model was referred to as a "decision tree," which is a common term in everyday usage.
However, "decision tree" has a well-established, conflicting meaning in machine learning and statistics,
where it refers to a supervised learning algorithm that partitions a feature space through recursive
binary splits. Using the same term for both concepts creates confusion, especially for audiences
familiar with data science or machine learning.

## Decision Drivers

- Avoid ambiguity with the machine learning and operations research concept of "decision tree"
- Accurately describe the underlying SSVC data structure, which is a table of decision points and outcomes
- Improve clarity in documentation, tooling, and communication with practitioners
- Align terminology with the actual data representations used (CSV and JSON tables)

## Considered Options

- Continue using "decision tree"
- Switch to "decision table"
- Use both terms with explicit disambiguation

## Decision Outcome

Chosen option: "Switch to 'decision table'", because it accurately describes the tabular structure
used by SSVC and avoids the well-established conflicting meaning of "decision tree" in machine
learning and statistics.

### Consequences

- Good, because the terminology now accurately reflects the underlying data model (a table mapping
  decision point values to outcomes)
- Good, because it reduces confusion for practitioners familiar with machine learning or operations
  research
- Neutral, because some existing documentation, external references, and tooling may still use
  "decision tree" — these will be updated incrementally
- Bad, because the change breaks consistency with prior SSVC publications and external references
  that use "decision tree"

### Confirmation

Documentation, code, and tooling use "decision table" as the primary term for the SSVC model.
References to "decision tree" in the visual/hierarchical sense (i.e., tree diagrams used to
illustrate a decision table) may still appear where appropriate but should be clearly distinguished
from the decision table itself.

## More Information

This change was introduced with the [SSVC v2025.9 release](https://github.com/CERTCC/SSVC/releases/tag/v2025.9).

While some documentation may use tree diagrams to visualize a decision table, the underlying
model is always a decision table. The term "decision tree" in SSVC's prior use was closer
in meaning to a lookup table or truth table than to the machine learning construct.
