# Starting Out with SSVC

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
    applies a **Decision Table** to produce a set of output **Outcomes**.
    The **Decision Points** are the factors that influence the decision, and the **Outcomes** are the possible results of the decision.
    Both **Decision Points** and **Outcomes** are defined as ordered sets of enumerated values.
    The **Decision Table** is a mapping from each combination of decision point values to the set of outcome values.
    One of SSVC's goals is to provide a methodology to develop risk-informed guidance at a human scale, while enabling
    data-driven decision-making.

!!! tip "SSVC Calculator"

    We've created a simple [SSVC Calculator](../ssvc-calc/index.md) to help you understand how SSVC decision models work.
    The decisions modeled in the calculator are based on the [Supplier](../howto/supplier_tree.md),
    [Deployer](../howto/deployer_tree.md), and [Coordinator](../howto/coordination_intro.md) decision models.

!!! tip "SSVC Explorer"

    Ready to explore analyzing SSVC policies and writing your own policy? [SSVC Explorer](../ssvc-explorer/index.md) to help you understand how SSVC decision models can be developed, organized in an interactive way.
    The decisions modeled in the SSVC Explorer also use the SSVC Registry. 

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
    See the [CVSS v4 Assessment With SSVC](../howto/cvss_v4/index.md) section for more information.

!!! example "EPSS and SSVC"

    The Exploit Prediction Scoring System (EPSS) provides information regarding the likelihood of a vulnerability being exploited in the wild.
    This information can be used to inform the [Exploitation](../reference/decision_points/exploitation.md) decision point in the
    [Supplier](../howto/supplier_tree.md), [Deployer](../howto/deployer_tree.md), and [Coordinator Publication](../howto/publication_decision.md) decision models.
    See the [EPSS and SSVC](../howto/using_epss/index.md) section for more information.
