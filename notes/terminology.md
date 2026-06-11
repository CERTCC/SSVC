# Terminology: Decision Table vs. Decision Tree

## The Canonical Term

**Use "decision table"** when referring to the SSVC data structure that maps
combinations of decision point values to recommended actions.

**Avoid "decision tree"** as the primary term for this structure.

This is formalised in ADR-0014 (accepted 2025-08-26, first applied in
SSVC v2025.9).

---

## Why the Change?

SSVC's data structure is a **table**: a set of rows, each pairing a combination
of decision point values with an outcome. The term "decision tree" caused
confusion with two established concepts in other fields:

- **Machine Learning:** A "decision tree" in ML is a recursive splitting
  algorithm used for classification and regression. Practitioners familiar
  with this meaning were misled by our use of the term.
- **Operations Research:** OR uses "decision tree" for branching probability
  diagrams to model expected-value decisions under uncertainty. Again, a
  different structure from what SSVC does.

The term **"decision policy"** was also in use but has overloaded meanings
beyond what we intend.

**"Decision table"** accurately describes a tabular mapping of inputs to
outputs, matches the actual CSV and JSON data structures we use, and avoids
both established competing meanings.

---

## Usage Guide

| Context | Preferred term | Notes |
|---------|---------------|-------|
| The SSVC data structure (mapping of inputs → outcomes) | *decision table* | |
| The broader class of modeling approaches | *decision model* | "Decision table" is a kind of decision model |
| A tree diagram used to *illustrate* a decision table | *tree diagram* or *tree view* | Visual aid, not the data structure itself |
| The old term in archived/legacy content | *decision tree* | Acceptable when quoting or referencing prior versions |

---

## Updating Existing References

When editing documentation or code, replace "decision tree" with "decision
table" where the SSVC tabular structure is intended. References to tree
*diagrams* used purely as visual aids may retain "tree" wording when it aids
clarity, but should be distinguished from the decision table itself.

The Python class `DecisionTable` (in `src/ssvc/decision_tables/`) already
reflects the canonical term.

---

## See Also

- ADR-0014: [Use "Decision Table" Instead of "Decision Tree"](../docs/adr/0014-use-decision-table-terminology.md)
- `src/ssvc/decision_tables/` — canonical Python implementation using the correct term
