# SSVC Namespaces

We use namespaces in SSVC to organize the various components of the framework.
The bulk of our work is done in the `ssvc` namespace, which contains the core
decision points for SSVC. 

!!! question "Why does SSVC need namespaces?"

    We want to provide a clear way to differentiate between decision points we
    developed as part of the SSVC project, and those that are derived from work
    done by other projects. This helps us maintain clarity in our codebase and
    to avoid confusion when integrating with other systems or libraries.

!!! tip "Namespace syntax"

    The syntax for namespaces is `<base>/<extensions>`, where

    - `base` is the name of the namespace
    - `extensions` is an optional set of extensions that can be used to further
      specify the decision point. Extensions are delimited by a `/` 

    See below for additional details on SSVC namespace extensions.

!!! note "Namespace Requirements"
    
    A full namepace string must be between 3 and 1000 characters long. (We recommend 
    keeping them short for ease of use.)

    Further requirements are noted in each section below.


## Registered Namespaces

Registered namespaces appear in the `Namespaces` enum, and are intended to be used as follows:

- Objects in the `ssvc` namespace are managed by the SSVC 
  project team. We have complete control over these ones.
- Objects in other explicitly registered namespaces are provided for convenience,
  but the SSVC team is not responsible for modifying the content or semantics of
  those decision points.

!!! note "Base Namespace Requirements"

    Base namespaces must start with a letter and contain only lowercase 
    alphanumeric characters, dots (`.`),  and dashes (`-`).
    The sole exception is the the `x_` prefix for private namespaces described below.

    Consecutive dots or dashes or combinations thereof are not allowed.
    Base namespaces cannot end with a dot or dash.

    For base namespaces only, we chose to use lowercase alphanumeric 
    characters to ensure consistency and avoid confusion when using namespaces
    in code. (Extensions may contain mixed case alphanumeric characters, dots, and dashes.)

The SSVC project may create, at our discretion, new namespaces to reflect 
administrative scope for decision points we choose to include for user convenience.

!!! example "Potential Standards-based namespaces"

    We may in the future add namespaces when needed to reflect different standards 
    bodies like `nist`, `iso-iec`, `ietf`, `oasis`, etc.

!!! question "How do I request a new registered namespace?"

    If you have a suggestion for a new registered namespace, please open an
    issue in the [SSVC GitHub repository](https://github.com/CERTCC/SSVC/issues)
    and provide a brief description of the namespace and its intended use.

### Current Registered Namespaces

```python exec="true" idprefix=""
from ssvc.namespaces import NameSpace

for ns in NameSpace:
    print(f"- {ns.value}")
```

### Non-`ssvc` Namespaces

We use namespaces other than `ssvc` to indicate decision points that are based 
externally defined standards, specifications, or relevant projects.
We expect for decision points in these namespaces to be technically compatible 
with SSVC, but we do not claim any ownership or responsibility for the
underlying specifications or their semantic content. 
Objects in these namespaces are provided for the convenience
of SSVC users to allow them to use these decision points in their SSVC
decision models without needing to implement them from scratch.

While we are happy to resolve technical issues with these decision points as
technically implemented in the SSVC project, all suggestions for changes to the 
underlying specifications or semantic content should be directed to the 
maintainers of the respective projects or standards. 

!!! example "The `cvss` namespace"

    We wanted to allow SSVC users to include Common Vulnerability Scoring System
    (CVSS) vector elements as [decision points](../decision_points/cvss/index.md)
    in their SSVC decision models. 
    So we created the `cvss` namespace to contain 
    [decision points](../decision_points/cvss/index.md) that are
    based on various versions of the CVSS. These 
    [decision points](../decision_points/cvss/index.md) are provided
    as part of the SSVC project for convenience, but we do not maintain the 
    underlying CVSS specifications, their semantic content or their implementations.
    Suggestions for changes to the CVSS specifications should be directed to the
    [FIRST CVSS Special Interest Group](https://www.first.org/cvss/) (SIG).


## Private / Experimental Namespaces

Private and experimental namespaces may prepend a prefix `x_` to 
an otherwise valid namespace string to create private decision points that 
are not intended to be shared outside of a specific scope, e.g., for internal 
use only. 

The SSVC project does not manage namespaces with the `x_` prefix, so
collisions may occur across organizations who develop their own private SSVC
namespaces. 

!!! warning "Reverse domain name notation recommended"

    We strongly recommend using reverse domain name notation for private namespaces to
    avoid conflicts with other users' private namespaces. This helps to ensure
    that your private namespaces are unique and easily identifiable.
    E.g., `x_org.cert-experimental` for an experimental namespace within the CERT organization.

!!! example "OT Monitoring Service (OTMS) Private Namespace"

    Organization A creates a set of decision points for testing purposes and
    uses the `x_test` namespace. They do not intend to share these decision
    points with anyone outside of their organization, so they use the `x_`
    prefix to indicate that this namespace is private to them.

    Organization B also creates a set of decision points for testing purposes
    and uses the same `x_test` namespace. They also do not intend to share
    these decision points with anyone outside of their organization.

!!! warning "Namespace Conflicts"

    Conflicts are possible in the x_ prefix space. 
    In the previous example, Organizations A and B could both choose to use 
    `x_test`, and there are no guarantees of global uniqueness for the 
    decision points in the `x_test` namespace.

!!! tip "Private vs Extension Namespaces"

    Private namespaces are intended for internal use only and are not registered
    with the SSVC project. They are not intended to be shared or used outside of
    the organization that created them. In contrast, extension namespaces are
    intended to extend the existing SSVC namespaces and may be shared with other
    users of the SSVC framework.

## Namespace Extensions

We allow users to extend the SSVC namespaces to clarify existing decision
points or to add new decision points that are compatible with the SSVC framework.
The intent of an extension is to allow clarification of the application of 
decision points and their values to specific constituencies.

- Extensions must not alter the decision point key, version number, or value keys 
  for any decision point they are derived from.
- Extensions must not alter the meaning of existing values, or add values to 
  existing decision points in the parent namespace.
- Extensions may reduce the set of values for a decision point in the parent
  namespace, but must not add new values.


!!! info "Namespace Extension Syntax and Structure"

    Extension strings may contain alphanumeric characters (upper or lower case),
    dots (`.`), and dashes (`-`).
    Multiple extension segments are separated by a `/` character.

    The structure of the namespace string is intended to show inheritance for
    variations on SSVC objects. 

    Extension order matters. `ssvc/de-DE/ref-arch-1` would describe an extension
    for `ref-arch-1` derived from the German (Germany) translation of SSVC. 
    `ssvc/ref-arch-1/de-DE` would denote an extension of SSVC for `ref-arch-1`
    (in English) that had subsequently been translated in to German (Germany).


!!! note "First Extension Segment Reserved for Language Tag"

    The first extension segment is reserved for a language tag, which is
    optional but recommended. 
    This allows users to specify the language of extension, making it easier to
    understand and use in different linguistic contexts.

    If *any* extensions are present, the first extension segment must be an
    (optionally empty)
    [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag.
    E.g., `ssvc/jp-JP/extension`
    
    The language may be left empty in which case the default language (`en-US`) is 
    implied. An unspecified language tag will result in a `<base>//<extension>` format.

    The use of a language tag in the first segment is intended to be used to 
    indicate translations of entire sets of decision points.

!!! example "Translation and Localization"

    `ssvc/de-DE` might denote a German translation of the corresponding `ssvc` object.

!!! example "Refinement of Concepts for a Specific Constituency"

    A sector-specific information sharing and analysis organization (ISAO)
    might create an extension for their specific constituency. 
    For example, say that namespace foo has a decision point for 
    Regulated System=(Y,N). A medical-focused ISAO might create an extension 
    `foo//example.med-isao` where they refine the values to refer to specific 
    regulations. If multiple regulatory regimes exist, they might even have
    `foo//example.med-isao/regulation-1` and `foo//example.med-isao/regulation-2`
    to cover assessment of the appropriate regulations.


### Usage Suggestions

Although we reserved the first segment of the extension for language tags, 
there are scenarios where it may be appropriate to use a language tag in a later
segment of the extension. 

!!! tip "Use BCP-47 Language Tags"

    Regardless where they appear in the extension strings, we recommend using
    BCP-47 strings for any language-based extension. Note, however that we do not
    strictly enforce this recommendation in the SSVC codebase outside of the 
    first segment.

!!! example "Translation of a custom extension"

    If you have a custom extension that is not a translation of an existing
    decision point, you might use a language tag in a later segment to indicate
    a translation of the extension. 
    For example, `ssvc//com.example/extension/pl-PL` would indicate that the
    an extension in the default `en-US` language has been translated to Polish (Poland).

!!! tip "Use Reverse Domain Name Notation for Extensions"

    To avoid conflicts with other users' extensions, we recommend using reverse
    domain name notation for your extensions. This helps to ensure that your
    extensions are unique and easily identifiable.
    For example, if your organization is `example.com`, you might use an extension
    like `ssvc//com.example/extension`.

!!! example "Reverse Domain Name Notation"

    If your organization has a domain name, you can use it as the base for your
    extension. This helps to ensure that your extensions are unique and easily
    identifiable. 

    For example, if your organization is `example.com`, you might use an extension
    like `ssvc//com.example/extension`.


## Technical requirements

The following technical requirements are enforced for SSVC namespaces,
based on the implementation in `src/ssvc/namespaces.py` and the NS_PATTERN regular expression:

```python exec="true" idprefix=""
from ssvc.namespaces import NS_PATTERN

print(f"`{NS_PATTERN.pattern}`")
```

- **Length**: Namespaces must be between 3 and 1000 characters long.
- **Base Namespace**:
    - Must start with a lowercase letter.
    - Must contain at least 3 total characters in the base part (after the optional experimental/private prefix).
    - Only lowercase letters, numbers, dots (`.`), and hyphens (`-`) are allowed.
    - Must not contain consecutive dots or hyphens (no `..`, `--`, `.-`, `-.`, `---`, etc.).
    - Cannot end with a dot or hyphen.
    - May optionally start with the experimental/private prefix `x_`.
- **Experimental/Private Namespaces**:
    - Must start with `x_` followed by a valid base namespace.
- **Extensions (Optional)**:
    - Extensions are optional and must be delineated by slashes (`/`).
    - If present, the first extension segment must be a valid BCP-47 language tag or empty (`//`).
    - Subsequent extension segments:
        - Must start with a letter (upper or lowercase).
        - May contain letters, numbers, dots (`.`), and hyphens (`-`).
        - Must not start or end with a dot or hyphen.
        - Must not contain consecutive dots or hyphens.
        - Are separated by single forward slashes (`/`).
        - Multiple extension segments are allowed.
- **Examples of valid namespaces**:
    - `ssvc`
    - `cisa`
    - `x_private-test`
    - `ssvc/de-DE/reference-arch-1`
    - `x_custom//extension` (empty language tag)
- **Examples of invalid namespaces**:
    - `custom` (not in enum, no `x_` prefix)
    - `x_custom/extension` (first segment must be a language tag)
    - `x_custom.extension.` (ends with punctuation)
    - `x_custom..extension` (double dot)
    - `x_custom/` (ends with slash)
    - `x_custom/extension//` (double slash at end)
    - `ab` (too short)
    - `x_` (too short after prefix)

These requirements are strictly enforced by the `NS_PATTERN` regular expression 
in the codebase. For full details, see the documentation below and 
implementation in `src/ssvc/namespaces.py`.

## The `ssvc.namespaces` module

The `ssvc.namespaces` module provides a way to access and use these namespaces.

::: ssvc.namespaces

