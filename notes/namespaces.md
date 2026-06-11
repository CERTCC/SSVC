# Namespaces

SSVC uses **namespaces** to distinguish between objects managed by the SSVC
project and objects derived from external sources. This makes it possible to
include, for example, CVSS vector elements as SSVC decision point objects
without claiming that the SSVC project controls their definitions.

## Namespace Categories

### Registered namespaces

Registered namespaces are defined in the `NameSpace` enum in
`src/ssvc/namespaces.py`. Only the SSVC project controls which values are
registered.

Current registered namespaces include `ssvc` (for core SSVC objects) and
`cvss` (for CVSS vector element wrappers). Any new registered namespace
requires a code change and a PR to the SSVC repository.

### Extension namespaces

Third-party adopters who want to define custom decision points or refine
existing ones can use **unregistered extension namespaces** without
coordinating with the SSVC project. Extension namespace strings must:

1. Begin with the prefix `x_`.
2. Follow the format `x_<reverse-domain>#<fragment>`.

*Examples:*

| Use case | Example namespace |
|----------|-------------------|
| Internal agency use | `x_example.agency#internal` |
| Interagency sharing | `x_example.agency#interagency` |
| ISAO constituency refinement | `x_example.isao#constituency-1` |

Reverse-domain notation delegates uniqueness to DNS ownership, so no central
registration is needed.

### Namespace extensions (refinements)

A **namespace extension** refines the semantics of an existing namespace for a
specific context, without introducing wholly new objects. The syntax uses a
double-slash separator:

```
<base-namespace>//<extension-domain>#<fragment>
```

*Example:* An ISAO refining SSVC decision point values for its member
constituency might use `ssvc//.example.isao#constituency-1`.

Extensions are not intended to introduce new decision points; they add nuance
to the *interpretation* of existing ones.

---

## Validation

Namespace values are validated at object construction time. Valid values are:

- A member of the `NameSpace` enum (registered namespaces).
- A string that starts with `x_` and matches the extension pattern
  (see `src/ssvc/utils/ssvc_namespace_pattern.abnf` for the ABNF grammar).

Anything else raises a `ValueError` at construction.

Reserved namespace strings (listed in `ssvc.namespaces`) cannot be used as the
base of any namespace, registered or extension.

---

## Practical Guidance for Adopters

**I want to create my own decision points for internal use:**
Use an extension namespace like `x_myorg.example#internal`. You can instantiate
`DecisionPoint` objects with this namespace and they will register in the
in-memory registry without conflicting with SSVC project objects.

**I want to share my decision points with other organisations:**
Use a stable extension namespace based on a domain you control, e.g.
`x_myorg.example#shared`. If your decision points prove broadly useful,
consider proposing them to the SSVC project for registration.

**I want to adapt existing SSVC decision point descriptions for my context:**
Use a namespace extension, e.g. `ssvc//.myorg.example#context`. Document
clearly which base SSVC object you are extending so consumers understand the
relationship.

---

## See Also

- ADR-0012: [SSVC Namespaces](../docs/adr/0012-ssvc-namespaces.md)
- Spec NS: `specs/namespaces.yaml`
- Implementation: `src/ssvc/namespaces.py`
- Pattern grammar: `src/ssvc/utils/ssvc_namespace_pattern.abnf`
