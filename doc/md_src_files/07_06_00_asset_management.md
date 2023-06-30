## Relationship to asset management

Vulnerability management is a part of asset management.
SSVC can benefit from asset management practices and systems, particularly in regard to automating data collection and answers for some decision points.
SSVC depends on asset management to some extent, particularly for context on the cost and risk associated with changing or updating the asset.

Asset management can help automate the collection of the [*Mission Impact*](#mission-impact), [*Situated Safety Impact*](#situated-safety-impact), and [*System Exposure*](#system-exposure) decision points.
These decision points tend to apply per asset rather than per vulnerability.
Therefore, once each is assessed for each asset, it can be applied to each vulnerability that applies to that asset.
While the asset assessment should be reviewed occasionally for accuracy, storing this data in an asset management system should enable automated scoring of new vulnerabilities on these decision points for those assets.

Our method is for prioritizing vulnerabilities based on the risk stemming from exploitation.
There are other reasonable asset management considerations that may influence remediation timelines.
There are at least three aspects of asset management that may be important but are out of scope for SSVC.
First and most obvious is the transaction cost of conducting the mitigation or remediation.
System administrators are paid to develop or apply any remediations or mitigations, and there may be other transactional costs such as downtime for updates.
Second is the risk of the remediation or mitigation introducing a new error or vulnerability.
Regression testing is part of managing this type of risk. Finally, there may be an operational cost of applying a remediation or mitigation, representing an ongoing change of functionality or increased overhead.
A decision maker could order work within one SSVC priority class (scheduled, out-of-cycle, etc.) based on these asset management considerations, for example.
Once the organization remediates or mitigates all the high-priority vulnerabilities, they can then focus on the medium-level vulnerabilities with the same effort spent on the high-priority ones.

Asset management and risk management also drive some of the up-front work an organization would need to do to gather some of the necessary information.
This situation is not new; an asset owner cannot prioritize which fixes to deploy to its assets if it does not have an accurate inventory of its assets.
The organization can pick its choice of tools; there are about 200 asset management tools on the market [@captera].
Emerging standards like the Software Bill of Materials (SBOM) [@manion2019sbom] would likely reduce the burden on asset management, and organizations should prefer systems which make such information available.
If an organization does not have an asset management or risk management (see also [Gathering Information About Mission Impact](#gathering-information-about-mission-impact)) plan and process in place, then SSVC provides some guidance as to what information is important to vulnerability management decisions and the organization should start capturing, storing, and managing.

