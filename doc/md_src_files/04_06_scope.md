## Scope

Scope is an important variable in the answers of these decision points.
It has at least three aspects.
The first is how the boundaries of the affected system are set.
The second is whose security policy is relevant.
The third is how far forward in time or causal steps one reasons about effects and harms.
We put forward recommendations for each of these aspects of scope.

However, users of the decision process may want to define different scopes.
Users may define a different scope as long as the scope (1) is consistent across decisions, and (2) is credible, explicit, and accessible to all relevant decision makers.

For example, suppliers often decline to support products beyond a declared end-of-life (EOL) date. In these cases, a supplier could reasonably consider vulnerabilities in those products to be out of scope. However, a deployer may still have active instances of EOL products in their infrastructure. It remains appropriate for a deployer to use SSVC to prioritize their response to such situations, since even if there is no remediation forthcoming from the supplier it may be possible for the deployer to mitigate or remediate the vulnerability in other ways, up to and including decommissioning the affected system(s).

### Boundaries of the Affected System

One distinction is whether the system of interest is software per se or a cyber-physical system.
A problem is that in every practical case, both are involved.
Software is what has vulnerabilities and is what vulnerability management is focused on remediating.
Multiple pieces of software run on any given computer system.
To consider software vulnerabilities in a useful scope, we follow prior work and propose that a vulnerability affects “the set of software instructions that executes in an environment with a coherent function and set of permissions” [@spring2015global].
This definition is useful because it lets us keep to common usage and intuition and call the Linux kernel—at least a specific version of it—“one piece” of software.

But decision points about safety and mission impact are not about the software in isolation; they are about the entire cyber-physical system, of which the software is a part.
The term “physical” in “cyber-physical system” should be interpreted broadly; selling stocks or manipulating press outlet content are both best understood as affecting human social institutions.
These social institutions do not have much of a corporeal instantiation, but they are physical in the sense that they are not merely software, and so are parts of cyber-physical systems.

The hard part of delineating the boundaries of the affected system is specifying what it means for one system to be part of another system.
Just because a computer is bolted to a wall does not mean the computer is part of the wall’s purpose, which is separating physical space.
At the same time, an off-premises DNS server may be part of the site security assurance system if the on-premises security cameras rely on the DNS server to connect to the displays at the guard’s desk.
We define computer software as part of a cyber-physical system if the two systems are mutually manipulable; that is, changes in the part (the software) will (at least, often) make detectable and relevant changes to the whole (the cyber-physical system), and changes in the whole will (often) make relevant and detectable changes in the part [@spring2018generalization].

When reasoning about a vulnerability, we assign the vulnerability to the nearest, relevant—yet more abstract—discrete component.
This assignment is particularly important when assessing technical impact on a component. This description bears some clarification, via each of the adjectives:

  - **Nearest** is relative to the abstraction at which the vulnerability exists.

  - **Relevant** implies that the impacted component must be in the chain of abstraction moving upward from the location of the flaw.

  - **More abstract** means that the impacted component is at least one level of abstraction above the specific location of the vulnerability. For example, if the vulnerability is localized to a single line of code in a function, then the function, the module, the library, the application, the product, and the system it belongs to are all “more abstract.”

  - **Discrete** means there is an identifiable thing that can be remediated (e.g., the unit of patching).

Products, libraries, and applications tend to be appropriate objects of focus when seeking the right level to analyze the impact of a vulnerability.
For example, when reasoning about the technical impact of a vulnerability that is localized to a function in a module in an open source library, the nearest relevant discrete abstraction is the library because the patches are made available at the library level.
Similarly, analysis of a vulnerability in closed source database software that supports an enterprise resource management (ERM) system would consider the technical impact to the database, not to the ERM system.

### Relevant Security Policy

Our definition of a vulnerability includes a security policy violation, but it does not clarify whose security policies are relevant [@householder2020cvd].
For an organizational PSIRT or CSIRT, the organization's security policy is most relevant.
The answer is less clear for coordinators or ISACs.
An example scenario that brings the question into focus is phone OS jailbreak methods.
The owner of the phone may elect to jailbreak it; there is at least an implicit security policy from the owner that allows this method.
However, from the perspective of the explicit phone OS security policy embedded in the access controls and separation of privileges, the jailbreak is exploiting a vulnerability.
If a security policy is embedded in technical controls, such as OS access controls on a phone, then anything that violates that security policy is a vulnerability.

### Reasoning Steps Forward

This aspect of scope is about immediacy, prevalence, and causal importance.
**Immediacy** is about how soon after the decision point adverse effects should occur to be considered relevant.
**Prevalence** is about how common adverse effects should be to be considered relevant.
**Causal importance** is about how much an exploitation of the software in the cyber-physical system contributes to adverse effects to be considered relevant.
Our recommendation is to walk a pragmatic middle path on all three aspects.
Effects are not relevant if they are merely possible, too infrequent, far distant, or unchanged by the vulnerability.
But effects are relevant long before they are absolutely certain, ubiquitous, or occurring presently.
Overall, we summarize this aspect of scope as *consider credible effects based on known use cases of the software system as a part of cyber-physical systems*.
