# Supplying Patches

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

    Without belaboring the point, these methods are similar to how CVE Numbering Authorities discern “independently fixable vulnerabilities” [@mitre2020cna].
    
    We also note that SBOM[@manion2019sbom] seems well-placed to aid in that resolution process for the third-party library scenarios.

- recognize, on further investigation of the initial report, that additional versions of the product are affected
- discover that other products are affected due to code sharing or programmer error consistent across products
- receive reports of vulnerabilities in third party libraries they utilize in one or more of their products
- receive fix bundles for third party libraries used in one or more of their products (where a fix bundle might resolve multiple vulnerabilities or add new features)



In the end, Suppliers provide remediations and/or mitigations for affected products.
A supplier-provided remediation is usually a software update which contains fixes for multiple vulnerabilities and, often, new or improved features.
Supplier output is relevant because it will become input to Deployers.
SSVC focuses only on the remediation in this case; a set of remediations for multiple vulnerabilities is a fix bundle.
Suppliers may also produce mitigations, such as recommended configuration changes, to limit the impact of a vulnerability.

## Supplier Decision Model

At a basic level, the decision at a software development organization is whether to issue a work order and what resources to expend to remediate a vulnerability in the organization’s software. Prioritization is required because, at least in the current history of software engineering, the effort to patch all known vulnerabilities will exceed available resources. The organization considers several other factors to build the patch; refactoring a large portion of the code base may be necessary for some patches, while others require relatively small changes.
We focus only on the priority of building the patch, and we consider four categories of priority, as outlined in the table below.

!!! note "Patch Supplier Priority"
   
    | Supplier Priority | Description |
    | :---              | :----------  |
    | Defer              | Do not work on the patch at present. |
    | Scheduled          | Develop a fix within regularly scheduled maintenance using supplier resources as normal. |
    | Out-of-Cycle       | Develop mitigation or remediation out-of-cycle, taking resources away from other projects and releasing the fix as a security patch when it is ready. |
    | Immediate          | Develop and release a fix as quickly as possible, drawing on all available resources, potentially including drawing on or coordinating resources from other parts of the organization. |

## Supplier Tree

The example supplier tree [PDF](../pdf/ssvc_2_supplier.pdf) shows the proposed prioritization decision tree for the supplier. Both supplier and deployer trees use the above decision point definitions. Each tree is a compact way of expressing assertions or hypotheses about the relative priority of different situations. Each tree organizes how we propose a stakeholder should treat these situations. Rectangles are decision points, and triangles represent outcomes. The values for each decision point are different, as described above. Outcomes are priority decisions (defer, scheduled, out-of-cycle, immediate); outcome triangles are color coded:

  - Defer = gray with green outline
  - Scheduled = yellow
  - Out-of-Cycle = orange
  - Immediate = red with black outline



<embed src="../../pdf/ssvc_2_supplier.pdf" alt="Suggested supplier tree" type="application/pdf"
style="width: 100%;"
height = "700" />


## Table of Values

<!-- relative to /data/csvs/ -->
{{ read_csv('supplier-options.csv') }}