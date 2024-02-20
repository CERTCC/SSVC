# Enumerating Decisions

Stakeholders with different responsibilities in vulnerability management have very different decisions to make.
This section focuses on the differences among organizations based on their vulnerability management responsibilities.
Some decision makers may have different responsibilities in relation to different software.

!!! example "Example: Different Responsibilities for Different Software"

    For example, an Android app developer is a developer of the app, but is a deployer for any changes to the Android OS API.
    This situation is true for libraries in general:
    
    - A web browser developer makes decisions about applying patches to DNS lookup libraries and transport layer security (TLS) libraries.
    - A video game developer makes decisions about applying patches released to the Unreal Engine.
    - A medical device developer makes decisions about applying patches to the Linux kernel.
    
    The list goes on.

Alternatively, one might view applying patches as including some development and distribution of the updated product.
Or one might take the converse view, that development includes updating libraries.
Either way, in each of these examples (mobile device apps, web browsers, video games, medical devices),
we recommend that the professionals making genuine decisions do three things:

1. identify the decisions explicitly
2. describe how they view their role(s)
3. identify which software projects their decision relates to

If their decisions are explicit, then the decision makers can use the recommendations from this documentation that are relevant to them.

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



## Aggregation of SSVC across units of work

SSVC users should answer the suggested questions for whatever discrete unit of work they are considering. There is not necessarily a reliable function to aggregate a recommendation about remediation out of its constituent vulnerabilities. For the sake of simplicity of examples, we treat the remediation as a patch of one vulnerability, and comment on any difficulty in generalizing our advice to a more complex patch where appropriate.

To further clarify terms, “Remediation occurs when the vulnerability is eliminated or removed. Mitigation occurs when the impact of the vulnerability is decreased without reducing or eliminating the vulnerability” [@dodi_8531_2020, section 3.5]. Examples of remediation include applying patches, fixes and upgrades; or removing the vulnerable software or system from operation. Mitigating actions may include software configuration changes, adding firewall ACLs, or otherwise limiting the system's exposure to reduce the risk of the impact of the vulnerability; or accepting the risk.



## Enumerating Action Priority

SSVC models the decision of
“With what priority should the organization take action on a given vulnerability management work unit?”
to be agnostic to whether or not a patch is available.
We explain what we mean by a “work unit” in the previous section.
Here we explain what we mean by “priority”.


