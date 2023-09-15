# Enumerating Vulnerability Management Units of Work

SSVC models the decision of
“With what priority should the organization take action on a given vulnerability management work unit?”
to be agnostic to whether or not a patch is available.
In this page, we explain what we mean by a “work unit”.
In the next page, we explain what we mean by “priority”.


!!! note "Units of Work"

    A unit of work means either remediating the vulnerability—such as applying a patch—or deploying a mitigation.
    Both remediation and mitigations often address multiple identified vulnerabilities.
    The unit of work may be different for different stakeholders.
    The units of work can also change as the vulnerability response progresses through a stakeholder's process.

We elucidate these ideas with the following examples.

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


## Deployer Units of Work

!!! info inline end "Deployer Unit of Work"

    The unit of work for a Deployer is usually a single deployable patch or patch bundle such as a service pack.

Deployers are usually in the position of receiving remediations or mitigations from their Suppliers for products they have deployed.
They must then decide whether to deploy the remediation or mitigation to a particular instance (or not).
Whether they have the option of deploying only part of a remediation such as a fix bundle depends on whether the Supplier has engineered their release process to permit that degree of flexibility.
For example, if service packs are fix bundles, the Supplier might choose to release individually deployable fixes as well.

The vulnerability management process for deployers has at its core the collation of data including

- an inventory of deployed instances of product versions
- a mapping of vulnerabilities to remediations or mitigations
- a mapping of remediations and/or mitigations to product versions

The first must be collected by the Deployer, while the latter two most often originate from the product Supplier.
Managing this information is generally called **asset management**.
The relationship between SSVC and asset management is discussed further in [Relationship to asset management](#relationship-to-asset-management).

In turn, Deployers must resolve this information into specific actions in which a remediation or mitigation is slated for deployment to replace or modify a particular instance of the product.
The Deployer tree in SSVC considers the mission and safety risks inherent to the category of systems to which those deployed instances belong.
For this reason, we recommend that the pairing of remediation or mitigation to  a product version instance constitutes the unit of work most appropriate for the SSVC.

## Coordinator Units of Work 

!!! info inline end "Coordinator Unit of Work"

    The unit of work for a Coordinator is usually a single report to be coordinated.

Coordinator units of work tend to coincide with whatever arrives in a single report, which spans the range from a single
vulnerability affecting a specific version of an individual product from one Supplier all the way to fundamental design 
flaws in system specifications that could affect every Supplier and product that uses or implements the flawed specification.
Coordinators may need to reorganize reports (e.g., merge, split, expand, or contract) according to their workflow demands.
SSVC can be applied to either the initial report or to the results of such refinement.

## Aggregation of SSVC across units of work

SSVC users should answer the suggested questions for whatever discrete unit of work they are considering. There is not necessarily a reliable function to aggregate a recommendation about remediation out of its constituent vulnerabilities. For the sake of simplicity of examples, we treat the remediation as a patch of one vulnerability, and comment on any difficulty in generalizing our advice to a more complex patch where appropriate.

To further clarify terms, “Remediation occurs when the vulnerability is eliminated or removed. Mitigation occurs when the impact of the vulnerability is decreased without reducing or eliminating the vulnerability” [@dodi_8531_2020, section 3.5]. Examples of remediation include applying patches, fixes and upgrades; or removing the vulnerable software or system from operation. Mitigating actions may include software configuration changes, adding firewall ACLs, or otherwise limiting the system's exposure to reduce the risk of the impact of the vulnerability; or accepting the risk.

