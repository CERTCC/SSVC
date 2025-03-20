# Decision Trees

A decision tree is an acyclic structure where nodes represent aspects of the decision or relevant properties and branches represent possible options for each aspect or property.
Each decision point can have two or more options.

Decision trees can be used to meet all of the design goals, even plural recommendations and transparent tree-construction processes.
Decision trees support plural recommendations because a separate tree can represent each stakeholder group.
The opportunity for transparency surfaces immediately: any deviation among the decision trees for different stakeholder groups should have a documented reason—supported by public evidence when possible—for the deviation.
Transparency may be difficult to achieve, since each node in the tree and each of the values need to be explained and justified, but this cost is paid infrequently.

There has been limited but positive use of decision trees in vulnerability management.
For example, Vulnerability Response Decision Assistance (VRDA) studies how to make decisions about how to respond to vulnerability reports [@manion2009vrda].
This paper continues roughly in the vein of such work to construct multiple decision trees for prioritization within the vulnerability management process.

## Representation choices

A decision tree can represent the same content in different ways.
Since a decision tree is a representation of logical relationships between qualitative variables, the equivalent content can be represented in other formats as well.
The R package [data.tree](https://cran.r-project.org/web/packages/data.tree/data.tree.pdf) has a variety of both internal representations and visualizations.

For data input, we elected to keep SSVC simpler than R, and just use a CSV (or other fixed-delimiter separated file) as canonical data input.
All visualizations of a tree should be built from a canonical CSV that defines the decisions for that stakeholder.
Examples are located in [SSVC/data](https://github.com/CERTCC/SSVC/tree/main/data).
An interoperable CSV format is also flexible enough to support a variety of uses.
Every situation in SSVC is defined by the values for each decision point and the priority label (outcome) for that situation (as defined in [Likely Decision Points and Relevant Data](../reference/decision_points/index.md)).
A CSV will typically be 30-100 rows that each look something like:

```
2,none,laborious,partial,significant,scheduled
```

Where “2” is the row number, [*none*](../reference/decision_points/exploitation.md) through [*significant*](../reference/decision_points/public_safety_impact.md) are values for decision points, and *scheduled* is a priority label or outcome.
Different stakeholders will have different decision points (and so different options for values) and different outcomes, but this is the basic shape of a CSV file to define SSVC stakeholder decisions.

### Visualizing Decision Trees

The tree visualization options are more diverse.
We provide an example format, and codified it in [src/SSVC_csv-to-latex.py](https://github.com/CERTCC/SSVC/tree/main/src).
Why have we gone to this trouble when (for example) the R data.tree package has a handy print-to-ASCII function?
Because this function produces output like the following:

```
1    start                                        
2     ¦--AV:N                                     
3     ¦   ¦--AC:L                                 
4     ¦   ¦   ¦--PR:N
...
31    ¦   ¦   ¦   ¦   ¦   ¦       ¦--A:L    Medium
32    ¦   ¦   ¦   ¦   ¦   ¦       °--A:N    Medium
33    ¦   ¦   ¦   ¦   ¦   °--C:N                  
34    ¦   ¦   ¦   ¦   ¦       ¦--I:H              
35    ¦   ¦   ¦   ¦   ¦       ¦   ¦--A:H  Critical
```

This sample is a snippet of the CVSS version 3.0 base scoring algorithm represented as a decision tree.
The full tree can be found [here](cvss_full_tree.md).
This tree representation is functional, but not as flexible or aesthetic as might be hoped.
The visualizations provided by R are geared towards analysis of decision trees in a random forest ML model, rather than operations-research type trees.
