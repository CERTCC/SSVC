## Tree Construction and Customization Guidance

Stakeholders are encouraged to customize the SSVC decision process to their needs.
Indeed, the first part of SSVC stands for “stakeholder-specific."
However, certain parts of SSVC are more amenable to customization than others.
In this section, we'll cover what a stakeholder should leave static, what we imagine customization looks like, and some advice on building a usable and manageable decision tree based on our experience so far.

We suggest that the decision points, their definitions, and the decision values should not be customized.
Different vulnerability management teams inevitably think of topics such as [*Utility*](#utility) to the adversary in slightly different ways.
However, a key contribution of SSVC is enabling different teams to communicate about their decision process.
In order to clearly communicate differences in the process, the decision points that factor into the process need to be the same between different teams.
A stakeholder community may come together and, if there is broad consensus, add or change decision points.

Which decision points are involved in a vulnerability management team's decision and the priority label for each resulting situation are, for all intents and purposes, totally at the discretion of the team.
We have provided some examples for different stakeholder communities here.
What decision points a team considers reflects what it cares about and the risks prioritizes.
Different teams may legitimately prioritize different objectives.
It should be easier for teams to discuss and communicate such differences if the definitions of the decision points remain static.
The other aspect of risk management that SSVC allows a team to customize is its risk appetite or risk tolerance.

A team's risk appetite is reflected directly by the priority labels for each combination of decision values.
For example, a vulnerability with [no or minor](#public-safety-impact) [*Public Safety Impact*](#public-safety-impact), [total](#technical-impact) [*Technical Impact*](#technical-impact), and [efficient](#utility) [*Utility*](#utility) might be handled with [*scheduled*](#supplier-decisions) priority by one team and [*out-of-cycle*](#supplier-decisions) priority by another.
As long as each team has documented this choice and is consistent in its own application of its own choice, the two teams can legitimately have different appetites for vulnerability risk.
SSVC enables teams with such different risk appetites to discuss and communicate precisely the circumstances where they differ.

When doing the detailed risk management work of creating or modifying a tree, we recommend working from text files with one line or row for each unique combination of decision values.
For examples, see [SSVC/data](https://github.com/CERTCC/SSVC/tree/main/data/csvs).
An important benefit, in our experience, is that it is easier to identify a question by saying  “I'm unsure about row 16” than anything else we have thought of so far.
Once the humans agree on the decision tree, it can be converted to a JSON schema for easier machine-readable communication, following the provided [SSVC provision JSON schema](https://github.com/CERTCC/SSVC/blob/main/data/schema/SSVC_Provision.schema.json).

Once the decision points are selected and the prioritization labels agreed upon, it is convenient to be able to visually compress the text file by displaying it as a decision tree.
Making the decision process accessible has a lot of benefits.
Unfortunately, it also makes it a bit too easy to overcomplicate the decision.

The academic literature surrounding the measurement of decision tree quality is primarily concerned with measuring classification errors given a particular tree and a labeled data set.
In our case, we are not attempting to fit a tree to data.
Rather, we are interested in producing usable trees that minimize extraneous effort.
To that end, we briefly examine the qualities for which decision tree measurement is suitable.

### Decision Tree Construction Concerns

Decision tree construction methods must address five significant concerns: 
- feature selection 
- feature type 
- overfitting 
- parsimony
- versioning

#### Feature selection

Feature selection is perhaps the most important consideration for SSVC, because it directly affects the information gathering requirements placed on the analyst attempting to use the tree.
Each decision point in SSVC is a feature.

The SSVC version 1  ~applier~ deployer tree had 225 rows when we wrote it out in long text form.
It only has four outcomes to differentiate between.
Thus, on average that decision process treats one situation (combination of decision values) as equivalent to 65 other situations.
If nothing else, this means analysts are spending time gathering evidence to make fine distinctions that are not used in the final decision.
The added details also make it harder for the decision process to accurately manage the risks in question.
This difficulty arises because more variance and complexity there is in the decision increases the possibility of errors in the decision process itself.

#### Feature types

Regarding feature types, all of the features included in SSVC version 2 can be considered ordinal data.
That is, while they can be ordered (e.g., for Exploitation, active is greater than poc is greater than none), they can not be compared via subtraction or division (active - poc = nonsense).
The use of ordinal features is a key assumption behind our use of the parsimony analysis that follows.

#### Overfitting

When decision trees are used in a machine learning context, overfitting increases tree complexity by incorporating the noise in the training data set into the decision points in a tree.
In our case, our “data” is just the set of outcomes as decided by humans, so overfitting is less of a concern, assuming the feature selection has been done with care.

#### Parsimony 
Parsimony is, in essence, Occam's Razor applied to tree selection. Given the choice between two trees that have identical outputs, one should choose the tree with fewer decisions.
One way to evaluate the parsimony of a tree is by applying the concept of feature importance to ensure that each feature is contributing adequately to the result.
While there are a few ways to compute feature importance, the one we found most useful is permutation importance.
Permutation importance can be calculated on a candidate tree to highlight potential issues.
It works by randomly shuffling the values for each feature individually and comparing a fitness metric on the shuffled tree to the original.
The change in fitness is taken to be the importance of the feature that was shuffled.
Permutation importance is usually given as a number in the interval [0,1].
Python's scikit-learn [@pedregosa2011scikit-learn] provides a permutation importance method, which we used to evaluate our trees.

Interpreting the results of a permutation importance computation on a tree involves nuance, but one rule we can state is this:
any feature with a computed permutation importance of zero can be eliminated from the tree without losing any relevant information.
When all of the permutation importance scores for all features are relatively equal, that is an indication that each feature is approximately equally relevant to the decision.

More likely, however, is that some subset of features will be of relatively equal importance, and one might be of considerably lower importance (yet not zero).
In this case, the lowest importance feature should be considered for refinement or elimination.
It is possible that adjusting the definition of a feature or its available values (whether redefining, adding, or removing options) could increase its importance.
Reasons to retain a low-importance feature include:
* the feature is relevant to a small set of important circumstances that a tree without the feature would otherwise be unable to discriminate
* the effort required to determine the correct value for the feature is relatively small, for example information that might be collected automatically
* the feature enables other features to be defined more clearly
Features that meet none of the above criteria may be good candidates for elimination.

Customizing a tree by changing the outcome priority labels can also affect the importance of a feature.
This sort of customization is often the simplest way to adjust the importance of a feature.

While there is no hard and fast rule for when a tree is too big, we suggest that if all of your outcomes are associated with more than 15 situations (unique combinations of decision values), you would benefit from asking whether your analysts actually use all the information they would be gathering.
Thus, 60 unique combinations of decision values is the point at which a decision tree with four distinct outcomes is, on average, potentially too big.

#### Tree Versioning

SSVC trees should be identifiable by name and version. A tree name is simply a short descriptive label for the tree derived from the stakeholder and/or function the tree is intended for. Tree versions are expected to share the major and minor version numbers with the SSVC version in which their decision points are defined. Revisions should increment the patch number. For example: “Applier Tree v1.1.0” would be the identity of the version of the Applier Tree as published in version 1.1 of SSVC.
“Coordinator Publish Tree v2.0.3” would be the identity of a future revision of the Coordinator Publish Tree as described in this document. The terms “major”, “minor”, and “patch” with respect to version numbering are intended to be consistent with [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

### Sharing Trees With Others

Communities of shared interest may desire to share information about decision points or even create custom trees to share within their community.
Examples include:
- an Information Sharing and Analysis Organization (ISAO) within a critical infrastructure sector might want to define a custom decision point relevant to their constituents' regulatory compliance.
- a corporate Computer Security Incident Response Team (CSIRT) might choose to adjust decision priorities for an existing tree for use by its subsidiaries.
- a government department might define a separate tree using existing decision points to address a particular governance process within their constituent agencies.
- a regional coordinator might want to produce decision point information as a product of its threat analysis work and provide this information to its constituency in an advisory. 

In these and other scenarios, there are two scopes to consider:
1. Decision Point Scope
2. Decision Tree Scope

#### Decision Point Scope

Each decision point defined in this document has a characteristic scope, either *stakeholder-agnostic* or *stakeholder-specific*.

- **Stakeholder-agnostic decision points** describe the state of the world outside the stakeholder's environment. 
One might think of them as global facts that form the background context in which the stakeholder is making a prioritization decision.
Nearly all stakeholders should agree on the assignment of specific values to these decision points. 
- **Stakeholder-specific decision points** are expected to be contextual to some set of stakeholders.
Information about a stakeholder-specific decision point can still be inherited by other stakeholders using the same tree.
For example in the corporate CSIRT scenario above, the [*System Exposure*](#system-exposure) value might be consistent across all subsidiaries for a centrally managed service.

We generally consider the following decision points to be *stakeholder-agnostic*:
- [*Exploitation*](#exploitation)
- [*Technical Impact*](#technical-impact)
- [*Automatable*](#automatable)

On the contrary, we consider the following decision points to be *stakeholder-specific*:
- [*Value Density*](#value-density)
- [*Utility*](#utility)
- [*Safety Impact*](#safety-impact)
- [*Public Safety Impact*](#public-safety-impact)
- [*Situated Safety Impact*](#situated-safety-impact)
- [*Mission Impact*](#mission-impact)
- [*Human Impact*](#human-impact)
- [*System Exposure*](#system-exposure)

We anticipate that most custom decision points created by stakeholders for themselves or a constituency will be of the *stakeholder-specific* variety.
Examples of these sorts of custom decision points include
- A decision point indicating whether a system or mission context is affected by regulatory oversight that might alter the decision priority.
E.g., a healthcare-focused ISAO might define a decision point about whether a vulnerability affects patient data privacy protection.
- A decision point that incorporates the concept of change risk to a deployer.
E.g., a financial institution might have a very low tolerance for changes to a transaction clearing system.
- A decision point that indicates whether the affected software belongs to a list of critical software for a specific constituency.
E.g., an open-source consortium might want to prioritize fix development for a set of key projects.
 
#### Decision Tree Scope

Two kinds of modifications are possible at the decision tree level.

- A *Risk Appetite Shift* retains the structure of an existing tree and all its decision points, and simply adjusts the decision outputs according to the stakeholder's risk appetite.
For example, an organization with sufficient resources to efficiently deploy fixes might choose to defer fewer cases than the default tree would recommend.
- *Tree Customization* can be done in one of three ways:
  1. incorporating an already-defined decision point into an existing tree that does not already contain it.
  2. defining a new decision point and adding it to an existing tree. 
Note that adding or removing an option from an existing decision point should be treated as creating a new decision point.
The new decision point should be given a distinct name as well.
  3. defining a new tree entirely from existing or new decision points.

Because tree customization changes the tree structure and implies the addition or removal of leaf nodes, it will be necessary for the organization to review the decision outputs in light of its risk appetite as well.

Risk-shifted or customized trees can be shared among a community of interest, of course.
Further customization within each stakeholder remains an option as well, although there is likely a diminishing return on more than a few layers of customization for the same basic decision.
Of course, SSVC users might choose to construct other trees to inform other decisions.

