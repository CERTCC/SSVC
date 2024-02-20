# Supplying Patches

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