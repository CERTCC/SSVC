# SSVC Namespaces

We use namespaces in SSVC to organize the various components of the framework.
The bulk of our work is done in the `ssvc` namespace, which contains the core
decision points for SSVC. 

!!! question "Why does SSVC need namespaces?"

    We want to provide a clear way to differentiate between decision points we
    developed as part of the SSVC project, and those that are derived from work
    done by other projects. This helps us maintain clarity in our codebase and
    to avoid confusion when integrating with other systems or libraries.

## Namespace Structure

Namespaces are structured as follows:

```mermaid
---
title: SSVC Namespace Structure
---
flowchart LR
    base_ns[Base Namespace]
    exts[Extensions]
    base_ns -->|/| exts
```

A namespace consists of a base namespace and optional extensions.

### Base Namespace

The base namespace can be either registered or unregistered.
The following diagram illustrates the structure of the base namespace:

```mermaid
---
title: Base Namespace Structure
---
flowchart LR
    
subgraph base_ns[Base Namespace]
    direction LR
    subgraph unregistered[Unregistered Namespace]
        direction LR
        xpfx[x_]
        reverse_ns[Reverse Domain Name Notation]
        xpfx --> reverse_ns 
    end
    subgraph registered[Registered Namespace]
        direction LR
        base_registered[Registered Base Namespace]
    end
    registered ~~~|OR| unregistered
end
```


!!! info inline end "Current Registered Namespaces"

    The SSVC project currently has a set of registered namespaces that are
    intended to be used as part of the framework. These namespaces are defined
    in the `ssvc.namespaces` module and can be accessed via the `NameSpace` enum.
    Current registered namespaces are:

    ```python exec="true" idprefix=""
    from ssvc.namespaces import NameSpace
    
    for ns in NameSpace:
        print(f"- {ns.value}")
    ```

#### Registered Namespace

Registered namespaces are those that are explicitly defined in the SSVC project.
A list of the current registered namespaces can be found in the sidebar.

Registered namespaces are intended to be used as follows:

- Objects in the `ssvc` namespace are managed by the SSVC 
  project team. We have complete control over these ones.
- Objects in other explicitly registered namespaces are provided for convenience,
  but the SSVC team is not responsible for modifying the content or semantics of
  those decision points.

!!! note "Registered Non-`ssvc` Namespaces"

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



!!! example "Potential Standards-based namespaces"

    We may in the future add namespaces when needed to reflect different standards 
    bodies like `nist`, `iso-iec`, `ietf`, `oasis`, etc. 

!!! question "How do I request a new registered namespace?"

    If you have a suggestion for a new registered namespace, please open an
    issue in the [SSVC GitHub repository](https://github.com/CERTCC/SSVC/issues)
    and provide a brief description of the namespace and its intended use.

#### Unregistered Namespace

Unregistered namespaces are those that are not explicitly defined in the SSVC project.
Because unregistered namespaces are not managed by the SSVC project team,
there is no strict guarantee of uniqueness across different users or organizations.
However, because we require unregistered namespaces to use reverse domain name notation,
we expect that this will rarely lead to conflicts in practice.

!!! info "Unregistered Namespace Requirements"

    Unregistered namespaces must follow the following structure:

    - Unregistered namespaces must use the `x_` prefix.
    - Following the `x_` prefix, unregistered namespaces must use reverse domain name notation of a domain under their control to ensure uniqueness.
    - Aside from the required `x_` prefix, unregistered namespaces must contain only alphanumeric characters, dots (`.`), and dashes (`-`).
   - For any domain using other characters, DNS Punycode must be used


!!! warning "Namespace Conflicts"

    Conflicts are possible in the x_ prefix space - especially as the control over a domain may be transferred. 
    Also in tests, Organizations A and B could both choose to use 
    `x_example.test`, and there are no guarantees of global uniqueness for the 
    decision points in the `x_example.test` namespace.


!!! tip "Test Namespace"

    The `x_example.test` namespace is used for testing purposes and is not intended for production use.
    It is used to test the SSVC framework and its components, and may contain decision points that are not fully implemented or tested.

### Namespace Extensions

Namespace extensions allow users to extend the SSVC namespaces to clarify existing decision points
from a base namespace.
Extensions are optional and may be used to refine or clarify existing decision points.
Extensions allow SSVC users to create decision points that are specific to their
constituencies or to provide translations of existing decision points.

!!! info "Namespace Extension Requirements"

    Extensions must follow the following requirements:
    
    - Extensions must not alter the decision point key, version number, or value keys 
      for any decision point they are derived from.
    - Extensions must not alter the meaning of existing values, or add values to 
      existing decision points in the parent namespace.
    - Extensions may reduce the set of values for a decision point in the parent
      namespace, but must not add new values.

!!! question "What if I want to create a new decision point?"

    If you want to create a new decision point, please use a private/experimental namespace
    as described above instead of an extension.
    Extensions are not intended to be used to create new decision points.

!!! question "Why is that important?"

    The way extensions are build enables tools to process the decision points even if
    they do not know the defined extension. As long as the tool knows the base
    namespace, it can process the decision point.

#### Namespace Extension Structure

The first extension segment is reserved for an optional BCP-47 language tag, which may be left empty.
When empty, the default language (`en-US`) is implied.

Subsequent extension segments must begin with a reverse domain name notation string,
and may contain alphanumeric characters (upper or lower case), dots (`.`), and dashes (`-`).
A single fragment identifier (`#`) may be included in an extension segment, but it is optional.
Fragment segments can be used to indicate a specific interpretation or context for the extension.
Note: Without a fragment segment, all decision points of an organization fall into one bucket, which is in most cases not intended. Therefore, the use of a fragment segment is recommended.
The following diagram illustrates the structure of namespace extensions:
```mermaid
---
title: Namespace Extensions
---
flowchart LR

subgraph exts[Extensions]
    direction LR
    subgraph first[1st Extension Segment]
        direction TB
        lang[Language Tag]
        empty_lang[Empty String]
        lang ~~~|OR| empty_lang
    end
    subgraph ext[Subsequent Extension Segments]
        direction LR
        reverse_ns_ext[Reverse Domain Name Notation]
        fragment[#Optional Fragment ID]
        reverse_ns_ext --> fragment
    end
    first -->|/| ext
    ext -->|/| ext
end

base_ns[Base Namespace]
base_ns -->|/| first

```

!!! info "Namespace Extension Requirements"

    Extensions must follow the following structure:
  
    - Extension segments are separated by slashes (`/`).
    - Multiple extension segments are allowed.
    - If any extension segments are present, the first segment must be a valid BCP-47 language tag or an empty string.
    - When the first segment is left as an empty string, the default language (`en-US`) is implied.
    - Subsequent extension segments must begin with a reverse domain name notation string or be a valid, non-empty BCP-47 language tag.
    - A fragment identifier (`#`) may be included in extension segments, but it is optional.
    - Extension segments may contain alphanumeric characters (upper or lower case), dots (`.`), and dashes (`-`), and zero or one hash (`#`).
    - Extensions must not alter the decision point key, version number, or value keys for any decision point they are derived from.
    - Extensions may reduce the set of values for a decision point in the parent namespace, but must not add new values.

    The structure of the namespace string is intended to show inheritance for
    variations on SSVC objects. 

!!! tip "Extension Order Matters"

    Extension order matters. `ssvc/de-DE/example.organization#ref-arch-1`
    denotes that (a) a German (Germany) translation of the SSVC decision points
    is available, and (b) that this translation has been extended with an extension
    by `organization.example` to fit their specific needs for `ref-arch-1`.

    On the other hand, `ssvc//example.organization#ref-arch-1/de-DE`
    denotes that (a) the `example.organization#ref-arch-1` extension is
    available in the default language (`en-US`), and (b) that this extension has
    been translated into German (Germany).


!!! example "Use of fragment identifiers and language tags"

    Imagine an Information Sharing and Analysis Organization (ISAO) `isao.example`
    wants to create an extension to refine an existing decision point in the `ssvc` namespace
    with additional context for a part of their constituency. They could create an extension
    namespace like `ssvc//example.isao#constituency` to indicate that this extension
    is specifically tailored for a particular constituency within the ISAO.
    Note the empty first segment, which implies the default language (`en-US`).

    If they further chose to create a Polish language version of their extension,
    they would add a language segment _following_ their extension namespace,
    e.g., `ssvc//example.isao#constituency/pl-PL`. Note that this is different 
    from a hypothetical `ssvc/pl-PL/example.isao#constituency` extension, which would imply
    that the `ssvc` namespace has been translated to Polish (Poland) and then extended
    (in Polish) with the `example.isao#constituency` extension.

!!! example "Refinement of Concepts for a Specific Constituency"

    A sector-specific information sharing and analysis organization (ISAO)
    might create an extension for their specific constituency. 
    For example, say that a hypothetical registered namespace `foo`
    has a decision point for `Regulated System=(Y,N)`.
    A medical-focused ISAO might create an extension 
    `foo//example.med-isao` where they refine the values to refer to specific 
    regulations. If multiple regulatory regimes exist, they might even have
    `foo//example.med-isao#regulation-1` and `foo//example.med-isao#regulation-2`
    to cover assessment of the appropriate regulations.

### Usage Suggestions

Although we reserved the first segment of the extension for language tags, 
there are scenarios where it may be appropriate to use a language tag in a later
segment of the extension. 

!!! tip "Use BCP-47 Language Tags"

    Regardless where they appear in the extension strings, BCP-47 language tags
    must be used for any language-based extension.
    Note, however that we do not yet strictly enforce this recommendation in the 
    SSVC codebase outside of the first extension segment.

!!! example "Translation of a custom extension"

    If you have a custom extension that is not a translation of an existing
    decision point, you might use a language tag in a later segment to indicate
    a translation of the extension. 
    For example, `ssvc//com.example/extension/pl-PL` would indicate that the
    an extension in the default `en-US` language has been translated to Polish (Poland).

!!! tip "Use Reverse Domain Name Notation for Extensions"

    To avoid conflicts with other users' extensions, we require the use of reverse
    domain name notation for your extensions. This helps to ensure that your
    extensions are unique and easily identifiable.
    For example, if your organization is `example.com`, you might use an extension
    like `ssvc//com.example#extension`.


## Technical requirements

The following technical requirements are enforced for SSVC namespaces,
based on the implementation in `src/ssvc/namespaces.py` and the NS_PATTERN regular expression:

!!! info "Namespace Pattern"

    The regular expression used to validate namespaces is:

    ```python exec="true" idprefix=""
    
    from ssvc.utils.patterns import NS_PATTERN
    
    print(f"`{NS_PATTERN.pattern}`")
    ```

### Length Requirements

- Namespaces must be between 3 and 1000 characters long.

### Base Namespace Requirements

- Must start with a lowercase letter
- Must contain at least 3 total characters in the base part (after the optional experimental/private prefix)
- Must contain only lowercase letters, numbers, dots (`.`), and hyphens (`-`)
- Must not contain consecutive dots or hyphens (no `..`, `--`, `.-`, `-.`, `---`, etc.)
- May optionally start with the experimental/private prefix `{X_PFX}`.

### Extension Requirements (Optional)

- Extensions are optional
- Extensions must be delineated by slashes (`/`)
- If any extension segments are present, the following rules apply:
  - The first extension segment must be a valid BCP-47 language tag or empty (i.e., `//`).
  - Subsequent extension segments:
      - must start with a letter (upper or lowercase)
      - may contain letters, numbers, dots (`.`), hyphens (`-`), and at most one hash (`#`)
      - must not contain consecutive dots or hyphens (no `..`, `--`, `.-`, `-.`, `---`, etc.)
      - if a hash is present, it separates the main part from an optional fragment part
      - are separated by single forward slashes (`/`)
- Multiple extension segments are allowed

  
## The `ssvc.namespaces` module

The `ssvc.namespaces` module provides a way to access and use these namespaces.

::: ssvc.namespaces

