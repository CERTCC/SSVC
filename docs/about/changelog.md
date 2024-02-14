# Changelog

## Version 2.1 Changelog
This section summarizes the changes between SSVC 2.1 and SSVC version 2.0.
The details of what changes were made can be viewed on the SSVC Github under the SSVC v2.1 milestone.

- Introduced a demo SSVC Calc App which became the basis for CISA's SSVC Calculator
- Updated Deployer tree to use *Automatable* instead of *Utility*, which reduced the size from 108 leaf nodes to 72.
- Adjusted Deployer tree decisions based on stakeholder feedback
- Adjusted Supplier tree decisions based on stakeholder feedback
- Added section on Sharing Trees With Others including a discussion of decision point scope and decision tree scope.
- Improved clarity of time-sensitivity of some decision points in Representing Information for Decisions About Vulnerabilities
- Improved description of *Mission Impact*
- Improved consistency of *Public Safety Impact* usage throughout the document and tooling
- Improved consistency of *Human Impact* usage throughout the document
- Clarified that known default passwords are an example of *Exploitation*:PoC
- Clarified that unreachable code (as in unused library features) are _System Exposure_:small
- Mention DoD MEF definition in _Mission Impact_
- Updated references to EPSS to reflect recent publications
- Refactored markdown files to better track chapter and section numbering, improving findability when editing
- Automated HTML and PDF generation into a Github Workflow
- Updated python tools to maintain sync with current SSVC decision models
- Consolidated the SSVC document style guide into a single file in the repository
- Miscellaneous typo fixes and readability improvements (e.g., headings, bulleted lists)
  

## Version 2 Changelog

This section summarizes the changes between SSVC version 2 and SSVC version 1.1 as published at the Workshop on the Ecnomics of Information Security (WEIS 2020).
The details of what changes were made can be viewed on the SSVC GitHub issues closed under the `SSVC v2 Development` project.
We addressed about 60 issues.
About 10 issues identified “bugs” or errors in version 1.1.
About 20 issues improved documentation of tools or improved the clarity of document text.
The remaining 30 issues were focused on enhancing SSVC based on feedback received on version 1, though several of the bug fixes and documentation improvements also provided improvements.
This section focuses on changes that provided enhancements.

### Coordinator stakeholder

Version 1 only considered two stakeholders: those who make software, and those who use information systems.
Version 2 introduces a coordinator stakeholder and two distinct decisions for that stakeholder group: vulnerability intake triage and publication about a vulnerability.
These decisions use some existing decision points, but also introduce six new decision points to support coordinators in making these decisions.
The coordinator stakeholder is based on CERT/CC's experience coordinating vulnerabilities.

### Terminology changes

Some terms have been adjusted to better align with other usage in the field or based on feedback.
Therefore, “patch developer” became **supplier** and “patch applier” became **deployer**.
These terms in version 2 better reflect the stakeholder's relationship to the vulnerable component and also help keep clear that SSVC is about prioritization of work items in vulnerability management, not just patches.
We have also generally removed the word patch and instead use the more general “remediation” for a complete fix and “mitigation” for actions that reduce risk but do not remove a vulnerability from a system.
“Virulence” was renamed *Automatable* in a effort to be more direct and clear, rather than relying on an epidemiology metaphor.
We changed “out-of-band” to **out-of-cycle**.

Some concepts needed to be clarified or added.
These changes are a bit more substantive than the above terminology changes, but are similar.
For example, we clarified how end-of-life products are prioritized with SSVC.
We also clarified in Scope concepts around vulnerability identificatin and disambiguation.
Version 2 adopts an explicit definition of **risk** (from ISO Guide 73).
We also differentiated between vulnerability risk, or that risk arising from an unmanaged vulnerability in an information system, and change risk, or that risk from modifying or updating an information system to mitigate or remediate a vulnerability.
SSVC version 2 focuses on assessing and managing vulnerability risk, not change risk.
This stance was not explicit in SSVC version 1.

### Improvements to decision points

Version 1 had a decision point for well-being impact that was shared between **supplier** and **deployer** stakeholders.
Since these types of stakeholder have access to different information about safety and well-being, Version 2 splits this concept into *Public Safety Impact* and *Situated Safety Impact*.
The underlying definition remains largely the same.
However, *Public Safety Impact* has fewer output options (it is less granular) in recognition that a supplier or coordinator has less information about the context of deployment than a deployer does.

In addition, based on feedback from SSVC users, the SSVC version 2 recommended applier tree makes use of a combined value for *Mission Impact* and *Situated Safety Impact*.
The intuition behind this change is that if a person is going to die OR the organization is going to fail (for example, go bankrupt), then the organization will likely want to act with highest priority.
Either situation is sufficient to increase the priority, and there do not appear to be situations where a low  *Mission Impact* would mitigate a high *Situated Safety Impact* or vice versa.
On the other hand, a low *Utility* or *System Exposure* may mitigate a high mission or well-being impact.
So the Version 2 recommended tree is more usable than the Version 1 tree, thanks to these changes.


### Tree management and communication tools

The section Tree Construction and Customization Guidance is largely new or revised.
We produced new software tools for interacting with SSVC, which are documented in that section.
Version 2 adds reasoning behind why a stakeholder might customize a decision tree, what aspects of the tree are best to customize, tools for encoding custom trees in JSON, and scripts for visualizing custom trees.

Similarly, the section on Guidance on Communicating Results is largely new.
The section presents both an abbreviated and unabridged format for communicating SSVC information about a vulnerability.
This communication may be connected to the formats for communicating a whole decision tree.
Version 2 also addresses several other questions about SSVC information management, such as handling information changes over time, partial information, sourcing information for each decision point, and how collection and analysis of SSVC decision points can be automated.
