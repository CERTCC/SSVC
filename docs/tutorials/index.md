# Learning SSVC

SSVC stands for Stakeholder-Specific Vulnerability Categorization.
It is a methodology for prioritizing vulnerabilities based on the needs of the stakeholders involved in the vulnerability management process.
SSVC is designed to be used by any stakeholder in the vulnerability management process, including patch suppliers, patch deployers, coordinators, and others.
One of SSVC's key features is that it is intended to be customized to the needs of the organization using it.
In the [HowTo](../howto/index.md) section, we provide a set of decision models that can be used as a starting point,
but we expect that organizations will need to modify these models to fit their specific needs.
An introduction to how we think about SSVC can be found in the [Understanding SSVC](../topics/index.md) section.
For technical reference, including a list of decision points, see [Reference](../reference/index.md).

!!! info "SSVC in a Nutshell"

    SSVC is built around the concept of a **Decision Model** that takes a set of input **Decision Points** and
    applies a **Policy** to produce a set of output **Outcomes**.
    The **Decision Points** are the factors that influence the decision, and the **Outcomes** are the possible results of the decision.
    Both **Decision Points** and **Outcomes** are defined as ordered sets of enumerated values.
    The **Policy** is a mapping from each combination of decision point values to the set of outcome values.
    One of SSVC's goals is to provide a methodology to develop risk-informed guidance at a human scale, while enabling
    data-driven decision-making.

!!! tip "SSVC Calculator"

    We've created a simple [SSVC Calculator](../ssvc-calc/index.md) to help you understand how SSVC decision models work.
    The decisions modeled in the calculator are based on the [Supplier](../howto/supplier_tree.md),
    [Deployer](../howto/deployer_tree.md), and [Coordinator](../howto/coordination_intro.md) decision models.

SSVC can be used in conjunction with other tools and methodologies to help prioritize vulnerability response.

!!! example "CVSS and SSVC"

    The Common Vulnerability Scoring System (CVSS) is a free and open industry standard for assessing the severity of
    software security vulnerabilities. 
    CVSS assigns technical severity scores to vulnerabilities, and many organizations use this score to inform their 
    vulnerability management process.
    In SSVC, we took a different approach with our stakeholder-specific model, although the information contained in a
    CVSS vector can be applied to SSVC decision models.
    For example, the [Technical Impact](../reference/decision_points/technical_impact.md) decision point in 
    the [Supplier](../howto/supplier_tree.md) decision model can be informed by the CVSS vector.

!!! example "EPSS and SSVC"

    The Exploit Prediction Scoring System (EPSS) provides information regarding the likelihood of a vulnerability being exploited in the wild.
    This information can be used to inform the [Exploitation](../reference/decision_points/exploitation.md) decision point in the
    [Supplier](../howto/supplier_tree.md), [Deployer](../howto/deployer_tree.md), and [Coordinator Publication](../howto/publication_decision.md) decision models.

## Videos

Provided below are videos that provide an overview of SSVC and the implementation of decision models.

| Source | Video                                                                                                                            |
| ------ |----------------------------------------------------------------------------------------------------------------------------------|
| SEI Podcast Series | [A Stakeholder-Specific Approach to Vulnerability Management](https://youtu.be/wbUTizBaXA0)                                      |
| CISA | [SSVC On-Demand Training](https://youtu.be/NqiwyUPLy6I)                                                                          |
| Nucleus Security | [SSVC and Decision Trees](https://youtu.be/BKVvmAaCnSs)                                                                          |
| Nucleus Security | Panel Discussion: [Using Decision Trees for Vulnerability Prioritization with SSVC](https://youtu.be/25RHdcSwHCg) |
| Nucleus Security | [What is SSVC?](https://youtu.be/LV6PclEQ3QA)                                                                                    |
| ICS Cybersecurity Academy | [Create your own SSVC decision tree for ICS patching](https://youtu.be/MLkA2N3aXK4)                                              |
| ICS Cybersecurity Academy | [SSVC: A great replacement for CVSS in ICS?](https://youtu.be/1T36ieOqzNw)                                                       |
| Waterfall Security Solutions | Industrial Security Podcast Eps. 102: [Stakeholder-Specific Vulnerability Categorization (SSVC)](https://youtu.be/n5tVYjGxFj0)   |

## Other Content

We've collected a list of articles and blog posts that provide additional information about SSVC.

| Source        | Link                                                                                                                                                                                                                                    |
|- -------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEI           | [Prioritizing Vulnerability Response with a Stakeholder-Specific Vulnerability Categorization](https://insights.sei.cmu.edu/blog/prioritizing-vulnerability-response-with-a-stakeholder-specific-vulnerability-categorization/)         |
| CISA          | [Stakeholder-Specific Vulnerability Categorization (SSVC)](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc)                                                                                                 |
| Qualys        | [Effective Vulnerability Management with Stakeholder Specific Vulnerability Categorization (SSVC) and Qualys TruRisk](https://blog.qualys.com/product-tech/2022/11/30/effective-vulnerability-management-with-ssvc-and-qualys-trurisk)  |
| Vulcan Cyber  | [The SSVC risk prioritization method: what it is, when to use it, and alternatives](https://vulcan.io/blog/the-ssvc-risk-prioritization-method-what-it-is-when-to-use-it-and-alternatives/)                 |

Have a link to something we missed? Let us know in an [issue](https://github.com/CERTCC/SSVC/issues/new).
