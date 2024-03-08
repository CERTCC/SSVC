# Formalization Options

This section briefly surveys the available formalization options against the six design goals described above.
The table below summarizes the results.
This survey is opportunistic; it is based on conversations with several experts and our professional experience.
The search process leaves open the possibility of missing a better option.
However, at the moment, we are searching for a satisfactory formalism, rather than an optimal one.
We focus on highlighting why some common options or suggestions do not meet the above design goals.
We argue that decision trees are a satisfactory formalism.

## Quantitative Options

We rule out many quantitative options, such as anything involving statistical regression techniques or Bayesian belief propagation.
Most machine learning (ML) algorithms are also not suitable because they are both unexplainable (in the common sense meaning) and quantitative.
Random forest algorithms may appear in scope since each individual decision tree can be traced and the decisions explained [@russell2011artificial].
However, they are not transparent enough to simply know how the available decision trees are created or mutated and why a certain set of them works better.
In any case, random forests are necessary only when decision trees get too complicated for humans to manage.
We demonstrate below that in vulnerability management, useful decision trees are small enough for humans to manage.

## Logics

Logics are generally better suited for capturing qualitative decisions.
Boolean first-order logic is the “usual” logic—with material implication (if/then), negation, existential quantification, and predicates.
For example, in program verification, satisfiability problem (SAT) and satisfiability modulo theories (SMT) solvers are used to automate decisions about when some condition holds or whether software contains a certain kind of flaw.
While the explanations provided by logical tools are accessible to experts, non-experts may struggle.
Under special conditions, logical formulae representing decisions about categorization based on exclusive-or conditions can be more compactly and intelligibly represented as a decision tree.

## Decision Trees

Decision trees are used differently in operations research than in ML.
In ML, decision trees are used as a predictive model to classify a target variable based on dependent variables.
In operations research and decision analysis, a decision tree is a tool that is used to document a human process.
In decision analysis, analysts “frequently use specialized tools, such as decision tree techniques, to evaluate uncertain situations” [@howard1983readings, viii].
We use decision trees in the tradition of decision analysis, not ML.

## How Vulnerability Prioritization Options Meet the Design Goals

| | **Outputs are Decisions** | **Pluralistic** | **Qualitative Inputs** | **Qualitative Outputs** | **Transparent** | **Explainable** |
| :---                         | :-: | :-: | :-: | :-: | :-: | :-: |
| *Parametric Regression*      | :x: | :x: | :white_check_mark: | :x: | :x: | :white_check_mark: |
| *CVSS v3.0*                  | :x: | :x: | :white_check_mark: | :x: | :x: | :x: |
| *Bayesian Belief Networks*   | :x: | Maybe | :x: | :x: | :white_check_mark: | :white_check_mark: |
| *Neural Networks*            | :x: | :x: | :x: | :x: | :x: | :x: |
| *Random Forest*              | :white_check_mark: | :white_check_mark:     | :white_check_mark: | Maybe | :x: | Maybe |
| *Other ML*                   | :x: | Maybe | :x: | :x: | :x: | :x: |
| *Boolean First Order Logics* | Maybe | Maybe | :white_check_mark: | :white_check_mark: | :white_check_mark: | Maybe |
| *Decision Trees*             | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |

