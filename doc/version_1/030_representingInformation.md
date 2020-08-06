


# Representing Information for Decisions About Vulnerabilities

We chose to build our model with *decisions* as the central concept. We propose that decisions—rather than severity—are a more useful output.  Our design requirements for an adequate decision-making process is that it clearly define whose decisions are involved, properly use evidentiary categories, be based on reliably available evidence, be transparent, and be explainable. Our inspiration and justification for these design goals is that they are the features of a satisfactory scientific enterprise\[18\] adapted to this vulnerability management problem.

To consider decisions about managing the vulnerability rather than just technical severity, one must be clear about *whose* decisions are involved. Organizations that produce patches and fix software clearly have different decisions to make than those that deploy patches or other security mitigations. Furthermore, organizations in the aviation industry have different priorities than organizations that make word processors. These differences indicate a requirement: any formalism must be able to capture adequately the different decisions and priorities exhibited by different stakeholder groups. And as a usability requirement, the number of stakeholder groups needs to be small enough to be manageable, both by those issuing scores and those seeking them.

The goal of adequacy is more appropriate than optimality. Our search process need not be exhaustive; we are satisficing rather than optimizing.\[19\] Satisficing is more appropriate to qualitative criteria; we do not need to order different methods as to which are more transparent than others, for example. Finding any system that meets all of desired criteria is enough.

Decisions are not numbers. Decisions are qualitative actions that an organization can take. In many cases, numerical values can be directly converted to qualitative decisions. For example, if your child’s temperature is 105°F (40.5°C), you decide to go to the hospital.  Conversion from numerical to qualitative values can be complicated by measurement uncertainty and the design of the metrics. For example, CVSS scores were designed to be accurate with +/- 0.5 points of the given score.\[20\] If we take the recommended dividing line between high and critical—9.0—then it is unclear how to convert a CVSSv3.0 score of 8.9.

For example, under a Gaussian error distribution, 8.9 is really 60\% high and 40\% critical. We want decisions to be distinct and crisp; statistical overlaps of scores within 1.0 unit, for example, would muddy decision recommendations.

We avoid numerical representations and consider only qualitative data as inputs and outputs for any vulnerability management decision process.  Quantified metrics are more useful when (1) data for decision making is available, and (2) the stakeholders agree on how to measure.  Vulnerability management does not yet meet either criterion.  Furthermore, it is not clear to what extent measurements about a vulnerability can be informative about other vulnerabilities. Each vulnerability has a potentially unique relationship to the socio-technical system in which it exists, including the internet. The context of the vulnerability, and the systems it impacts, are inextricably linked to managing it. Temporal and environmental considerations should be primary, not optional as they are in CVSS.

We make the deliberation process as clear as practical; therefore, we risk belaboring some points to ensure our assumptions and reasoning are explicit. Transparency should improve trust in the results.

Finally, any result of a decision-making process should be *explainable*. (Explainable is defined and used with its common meaning.  This meaning is not the same as “explainable,” as used in the research area of explainable artificial intelligence.) An explanation should make the process intelligible to an interested, competent, non-expert person.  There are at least two reasons common explainability is important: (1) for troubleshooting and error correction and (2) for justifying proposed decisions.
  
To summarize, the following are our design goals for a vulnerability
management process:

  - Outputs are *decisions.*

  - Pluralistic recommendations are made among a manageable number of
    stakeholder groups.

  - Inputs are qualitative.

  - Outputs are qualitative, and there are no (unjustified) shifts to
    quantitative calculations.

  - Process justification is transparent.

  - The results are explainable.

## Formalization Options

This section briefly surveys the available formalization options against the six requirements described above. Table 1 summarizes the results.  This survey is opportunistic, and is based on conversations with several experts and our professional experience. The search process leaves open the possibility of missing a better option. However, at the moment, we are searching for a satisfactory formalism, rather than an optimal one.  We need to search only until a satisfactory option is found. Thus, we focus on highlighting why some common options or suggestions do not meet the above criteria. We argue that decision trees are a satisfactory formalism.

We rule out many quantitative options, such as anything involving statistical regression techniques or Bayesian belief propagation. Most machine learning (ML) algorithms are also not suitable because they are both unexplainable (in our sense) and quantitative. Random forest algorithms may appear in scope since each individual decision tree can be traced and the decisions explained.\[21\] However, it’s not transparent enough to simply know how the available decision trees are created or mutated and why a certain set of them works better. In any case, random forests are necessary only when decision trees get too complicated for humans to manage. We demonstrate below that in vulnerability management, useful decision trees are small enough for humans to manage.

Logics are generally better suited for capturing qualitative decisions.  Boolean first-order logic is the “usual” logic—with material implication (if/then), negation, existential quantification, and predicates. For example, in program verification, satisfiability problem (SAT) and satisfiability modulo theories (SMT) solvers are used to automate decisions about when some condition holds or whether software contains a certain kind of flaw. However, while the explanations provided by logical tools are accessible to experts, non-experts may struggle.  However, under special conditions, logical formulae representing decisions about categorization based on exclusive-or conditions can be more compactly and intelligibly represented as a decision tree.

Decision trees are used differently in operations research than in ML.  In ML, decision trees are used as a predictive model to classify a target variable based on dependent variables. In operations research and decision analysis, a decision tree is a tool used to document a human process. In decision analysis “decision analysts frequently use specialized tools, such as decision tree techniques, to evaluate uncertain situations. Unfortunately, many people, some of them educators, have confused decision analysis with decision trees. This is like confusing surgery with the scalpel.”\[22\] We use decision trees in the tradition of decision analysis, not ML.

Table 1: Comparison of Formalization Options for Vulnerability
Prioritization Decisions

|                                              | **Outputs Designed to be Decisions** | **Pluralistic Recommendations** | **Qualitative Inputs** | **Qualitative Outputs** | **Transparent** | **Explainable** |
| -------------------------------------------- | ------------------------------------ | ------------------------------- | ---------------------- | ----------------------- | --------------- | --------------- |
| **Parametric Regression**                    |                                      |                                 |                        |                         |                 |                 |
| **CVSS v3.0**                                |                                      |                                 |                        |                         |                 |                 |
| **Bayesian Belief Networks**                 |                                      | Maybe                           |                        |                         |                 |                 |
| **Neural Networks**                          |                                      |                                 |                        |                         |                 |                 |
| **Random Forest**                            |                                      |                                 |                        | Maybe                   |                 | Maybe           |
| **Other Machine Learning**                   |                                      | Maybe                           |                        |                         |                 |                 |
| **Boolean First Order Logics**               | Maybe                                | Maybe                           |                        |                         |                 | Maybe           |
| **Decision Trees (as in decision analysis)** |                                      |                                 |                        |                         |                 |                 |

## Decision Trees

A decision tree is an acyclic, flowchart-like structure where nodes represent aspects of the decision or relevant properties, and branches represent possible options for each aspect or property. Each decision point can have more than two options and may have different options from other decision points.

Decision trees can be used to meet all of the desired criteria described above. The two less-obvious criteria met by decision trees are plural recommendations and transparent tree-construction processes. Decision trees support plural recommendations simply because a separate tree can represent each stakeholder group. The opportunity for transparency surfaces immediately: any deviation among the decision trees for different stakeholder groups should have a documented reason—supported by public evidence when possible—for the deviation. Transparency may be difficult to achieve, since each node in the tree and each of the values need to be explained and justified, but this cost is paid infrequently.

There has been limited but positive use of decision trees in vulnerability management. For example, Vulnerability Response Decision Assistance (VRDA) studies how to make decisions about how to respond to vulnerability reports.\[23\] This paper continues roughly in the vein of such work to construct multiple decision trees for prioritization within the vulnerability management process.

