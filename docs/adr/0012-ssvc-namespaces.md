---
status: "accepted"
date: 2025-07-22
deciders: @ahouseholer @sei-vsarvepalli
consulted: @tschmidtb51
---
# Use of Namespaces in SSVC objects

## Context and Problem Statement

We need to include decision points and other objects that are not directly
defined by the SSVC project team. For example, CVSS vector elements are a
rich source of structured data that can be used to inform SSVC decisions and
modeled as SSVC decision point objects. However, the
[FIRST CVSS SIG](https://www.first.org/cvss) owns the definition of CVSS vector
elements. So we need a way to describe these objects in SSVC format
without making them part of the SSVC specification.

## Decision Drivers

- Need to include decision points based on data, objects, standards, and other
  definitions that are not part of the SSVC specification.
- Need to clearly distinguish between objects managed by the SSVC project and
  objects provided for convenience by the SSVC project, but whose semantics are
  defined by other projects or standards.

## Considered Options

- One big pile of objects (effectively no namespaces)
- Use namespaces to distinguish between SSVC project objects and other objects

## Decision Outcome

Chosen option: "Use namespaces", because

- Clearly distinguishes between SSVC project objects and objects derived from other sources
- Allows for extension of SSVC objects with additional data from other sources
- Allows for extensions for langauages, translation, localization, etc.

Specifically, we intend to use:

**Registered namespaces** for objects that we create and maintain (even if they are
based on other sources).

!!! example

    We use the `ssvc` namespace for all SSVC objects that are part of the
    main project. We use the `cvss` namespace to contain CVSS vector elements.

**Unregistered namespaces** for objects that we do not create or maintain, but
that others may want for their own use. Unregistered namespaces must start with
an `x_` prefix followed by a reverse domain name and conclude with a fragment,
such as `x_example.test#test`.
Unregistered namespaces are intended for experimental or private use.

!!! example

    A government agency might create a set of decision points for internal use 
    using the `x_example.agency#internal` namespace. This allows them to use SSVC
    objects of their own design alongside existig SSVC objects without needing to
    register their namespace with the SSVC project.

!!! example

    A government agency might create a set of decision points for interagency use 
    using the `x_example.agency#interagency` namespace. This allows them to use,
    organize and share SSVC objects based on their namespace value without the
    need for maintaining an external list. 

**Namespace extensions** for objects that are derived from other objects in an
registered or unregistered namespace. Extensions are not intended to be used to
introduce new objects, but rather to refine existing objects with additional data
or semantics.
Namespace extensions can be used for refining the meaning of decision point
values for a specific constituency, or adding additional nuance to
interpretation of a decision point in a specific context.

!!! example

    An ISAO (Information Sharing and Analyzing Organization) might want to refine
    the meaning of decision point values for their constituency, and could use
    `ssvc//.example.isao#constituency-1` as the namespace for their collection
    of extensions.

### Consequences

#### Positive Consequences

- SSVC users can customize SSVC objects with additional refinements using extensions
- SSVC users can create their own SSVC objects in an unregistered namespace for
  their own use, and share them with others
- Facilitates language translation and localization of SSVC objects to specific
  constituencies

#### Negative Consequences

- Registered namespaces must be managed and maintained
- Potential for confusion if unregistered namespaces are used without care or
  violating the naming conventions

<!-- This is an optional element. Feel free to remove. -->
### Confirmation

- Regular expressions are used in the SSVC specification in both python objects
  and JSON schema to validate the namespace format.
- Object validators can be used to ensure that namespaces are correctly formatted
  and that registered namespaces are used for objects that are part of the SSVC
  specification.

<!-- This is an optional element. Feel free to remove. -->
## Pros and Cons of the Options

### One big pile of objects

We started out with all objects having no namespaces, which meant that
all objects were effectively part of the SSVC specification. This was problematic
because it made it difficult to distinguish between objects that were part of the
SSVC specification under our control and objects that were derived from other sources.

- Good, because it was simple and easy to understand
- Bad, because it made it difficult to distinguish between SSVC project objects and
  objects based on specifications we neither created nor maintained

<!-- This is an optional element. Feel free to remove. -->
## More Information

- [SSVC Namespace Documentation](../reference/code/namespaces.md)
