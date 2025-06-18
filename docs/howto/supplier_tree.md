# Prioritizing Patch Creation

Here we describe an example decision model for a Supplier deciding the priority of creating a patch for a
vulnerability in their software.

!!! info "Supplier Patch Creation Priority"

    As noted in [Enumerating Decisions](../topics/enumerating_decisions.md),
    the root of a decision model's identity is the combination of the stakeholder and the decision being modeled.
    In this case, the stakeholder is the **Supplier** and the decision is the **priority of creating a patch**.

## Supplier Units of Work

On the input side of the Supplier process, Suppliers typically receive reports of vulnerabilities in one or more versions of their product.
Part of the Supplier's task on initial report intake is to resolve the initial report into a set of products and versions that are affected by the reported vulnerability.

!!! info inline end "Supplier Unit of Work"

    For the purposes of SSVC, we consider the unit of work for a Supplier to be combination of the vulnerability with each affected product.

Our working assumption is that for SSVC purposes, the supplier's unit of work is the combination of the vulnerability with each affected product.
This implies the need for Suppliers to be able to resolve whatever they receive to that level of granularity in order to make best use of SSVC.

Products will often need to be addressed individually because they may have diverse development processes or usage scenarios.
There are a variety of ways a Supplier might need to resolve the set of affected products. For example, they might

!!! tip inline end "Independently Fixable Vulnerabilities"

    Without belaboring the point, these methods are similar to how [CVE Numbering Authorities](https://www.cve.org/ResourcesSupport/AllResources/CNARules#section_7_assignment_rules) discern “independently fixable vulnerabilities”.
    
    We also note that [Software Bill of Materials](https://www.cisa.gov/sbom) (SBOM) seems well-placed to aid in that resolution process for the third-party library scenarios.

- recognize, on further investigation of the initial report, that additional versions of the product are affected
- discover that other products are affected due to code sharing or programmer error consistent across products
- receive reports of vulnerabilities in third party libraries they utilize in one or more of their products
- receive fix bundles for third party libraries used in one or more of their products (where a fix bundle might resolve multiple vulnerabilities or add new features)

In the end, Suppliers provide remediations and/or mitigations for affected products.
A supplier-provided remediation is usually a software update which contains fixes for multiple vulnerabilities and, often, new or improved features.
Supplier output is relevant because it will become input to [Deployers](deployer_tree.md).
SSVC focuses only on the remediation in this case; a set of remediations for multiple vulnerabilities is a fix bundle.
Suppliers may also produce mitigations, such as recommended configuration changes, to limit the impact of a vulnerability.

## Supplier Decision Outcomes

At a basic level, the decision at a software development organization is whether to issue a work order and what
resources to expend to remediate a vulnerability in the organization’s software.
Prioritization is required because, at least in the current history of software engineering,
the effort to patch all known vulnerabilities will exceed available resources.
The organization considers several other factors to build the patch; refactoring a large portion of the code base may
be necessary for some patches, while others require relatively small changes.
We focus only on the priority of building the patch, and we consider four categories of priority, as outlined in the table below.

!!! note "Patch Supplier Priority"

    | Supplier Priority | Description |
    | :---              | :----------  |
    | Defer              | Do not work on the patch at present. |
    | Scheduled          | Develop a fix within regularly scheduled maintenance using supplier resources as normal. |
    | Out-of-Cycle       | Develop mitigation or remediation out-of-cycle, taking resources away from other projects and releasing the fix as a security patch when it is ready. |
    | Immediate          | Develop and release a fix as quickly as possible, drawing on all available resources, potentially including drawing on or coordinating resources from other parts of the organization. |

## Supplier Decision Points

The decision to create a patch is based on the following decision points:

- [*Exploitation*](../reference/decision_points/exploitation.md) - A vulnerabilty with known exploitation is more likely to be given a higher priority.
- [*Utility*](../reference/decision_points/utility.md) - The more useful a vulnerability is to an attacker, the more likely it is to be given a higher priority.
- [*Technical Impact*](../reference/decision_points/technical_impact.md) - The more severe the technical impact of a vulnerability, the more likely it is to be given a higher priority.
- [*Public Safety Impact*](../reference/decision_points/public_safety_impact.md) - The more severe the public safety impact of a vulnerability, the more likely it is to be given a higher priority.

More detail about each of these decision points is provided at the links above, here we provide a brief summary of each.

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.exploitation import LATEST as EXP
from ssvc.decision_points.ssvc.utility import LATEST as U
from ssvc.decision_points.ssvc.technical_impact import LATEST as TI
from ssvc.decision_points.ssvc.public_safety_impact import LATEST as PSI

from ssvc.doc_helpers import example_block

for dp in [EXP, U, TI, PSI]:
    print(example_block(dp))
```

!!! tip "Public Safety Impact is a notational convenience"

    The [Public Safety Impact](../reference/decision_points/public_safety_impact.md) decision point is a
    simplification of the more detailed [Safety Impact](../reference/decision_points/safety_impact.md) decision point.

## Supplier Decision Model

The example supplier decision model below shows a prioritization policy for the supplier.
We display the decision model as a decision tree, which provides a compact representation of the policy,
showing the relative priority of different situations.

{% include-markdown "../_includes/_tree_notation_tip.md" %}

<embed src="../../pdf/ssvc_2_supplier.pdf" alt="Suggested supplier tree" type="application/pdf"
style="width: 100%;"
height = "700" />

### Table of Values

<!-- relative to /data/csvs/ -->
{{ read_csv('supplier-options.csv') }}
