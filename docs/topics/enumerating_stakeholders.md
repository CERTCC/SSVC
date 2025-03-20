# Enumerating Stakeholders

Stakeholders in vulnerability management can be identified within multiple independent axes.
For example, they can be identified by their responsibility: whether the group *supplies*, *deploys*, or *coordinates* remediation actions.
Depending what task a team is performing in a supply chain, the team may be considered a supplier, deployer, or a coordinator.
Therefore, one organization may have teams that take on different roles.

!!! example "Example: Supplier and Deployer Roles within an Organization"

    For example, an organization that develops and uses its own software might delegate the supplier role to its development team and the deployer role to its IT operations team.
    On the other hand, organizations using a DevOps approach to providing services might have a single group responsible for both the supplier and deployer roles.

Organizations may also be distinguished by the type of industry sector.
While it might be useful to enumerate all the sectors of the economy, we propose to draft decision points that include those from multiple important sectors.
For example, we have safety-related questions in the decision path for all suppliers and deployers.
The decision will be assessed whether or not the stakeholder is in a safety-critical sector.

The choice not to segregate the decisions by sector is reinforced by the fact that any given software system might be used by different sectors.
It is less likely that one organization has multiple responsibilities within the vulnerability management process.

Even if there is overlap within an organization, the two responsibilities are often located in distinct business units with distinct decision-making processes.
We can treat the responsibilities as non-overlapping, and, therefore, we can build two decision trees—one for each of the “patch supplier” and “patch deployer” responsibilities in the vulnerability management process.
Each of these trees will have different decision points that they take to arrive at a decision about a given unit of work.
<!-- Consider changing the word patch. There are other responses to a vulnerability (mitigation, isolation, etc.) that are backgrounded by using “patch” here. -->

In [Enumerating Decisions](./enumerating_decisions.md), we describe the decision space and the relevant decision points that we propose for these two responsibilities within the vulnerability management process.

!!! info "Target Audience"

    The target audience for this documentation is professional staff responsible for making decisions about information systems.
    This audience encompasses a broad class of professionals,  including suppliers, system maintainers, and administrators of many types.
    It also includes other roles, such as risk managers, technical managers, and incident responders.
    Although every layperson who owns a computing device makes decisions about managing it, they are not the target audience.
    The following decision system may help such laypeople, but we do not intend it to be used by that audience.

    While C-level executives and public policy professionals often make, shape, or incentivize decisions about managing information systems, they are not the target audience, either.
    To the extent that decision trees for vulnerability management help higher level policy decisions, we believe the best way to help policy makers is by making technical decisions more transparent and explainable.
    Policy makers may see indirect benefits, but they are not our primary audience and we are not designing an approach for them directly.
