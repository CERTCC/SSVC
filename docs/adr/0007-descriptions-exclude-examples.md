---
status: "accepted"
date: 2023-11-17
deciders: adh, jspring
---
# Object Descriptions Exclude Examples

## Context and Problem Statement

In written definitions of a Decision Point, Decision Point
Value, Outcome Group, Outcome Value, or other elements, it is common to
include examples in the text. In terms of documentation, this is a worthy
practice to promote understanding.

Examples are sometimes timely and need to be updated even though the
underlying concept has not changed. This can lead to unnecessary
versioning of objects.

## Decision Drivers

- In the course of modeling CVSS vectors across versions as SSVC decision
  points, we have found that concepts change less often than examples.
- Our preference is to minimize version changes to objects unless the
  underlying concept has changed.

## Considered Options

- Include examples in descriptions of objects.
- Exclude examples from descriptions of objects.

## Decision Outcome

Chosen option: "Exclude examples from descriptions of objects", because this
helps to minimize version changes to objects unless the underlying concept
has changed.

Examples may be included in the documentation text surrounding the object
definition, but not in the object definition itself.

### Consequences

- Good, because it reduces the likelihood and frequency of version changes to
  objects.
- Good, because it promotes the use of examples in documentation text.
- Bad, because it may make it more difficult to understand the object
  definition solely from the object definition itself.

### Confirmation

The implementation of this decision is confirmed by the absence of examples
in the object definitions.

When generating an object definition from a text description, object
creators should look out for phrases like "for example" and "an example of
this is" and exclude the example from the object definition.

## Pros and Cons of the Options

### Option 1: Include examples in descriptions of objects

- Good, because it makes the object definition easier to understand as a standalone
  element.
- Bad, because it lengthens the object definition.
- Bad, because it may lead to unnecessary versioning of objects.

### Option 2: Exclude examples from descriptions of objects

See [Decision Outcome](#decision-outcome).

## More Information

- [ADR-0006](0006-ssvc-decision-point-versioning-rules.md) - SSVC Decision
  Point Versioning Rules
- [ADR-0005](0005-ssvc-decision-point-group-versioning.md) - SSVC Decision
  Point Group Versioning Rules
