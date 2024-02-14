---
status: "accepted"
date: 2024-02-08
deciders: adh, jspring
consulted: team
---
# Outcome Sets are Separate from Decision Point Groups

## Context and Problem Statement

Should the outcome set be included in a decision model (tree) definition?

While a decision point group and their combinations of values define the structure of a tree, an Outcome Set defines
the possible labels of each leaf node. However, in order to decide what labels are appropriate for a leaf node, one 
must also be given a policy that maps each input combination (specific decision point values) to a specific outcome 
(drawn from an outcome set). But both the policy and the outcome set are actually stakeholder-specific.

The example trees we provide are at best a guess at a reasonable policy for SSVC adopters for each of the decisions we 
chose to model. And they also make assumptions about the process that the decision supports. So we assumed that 
suppliers have four options for priority. And we assigned outcome labels to leaf nodes based on what seemed reasonable 
to us at the time. But we must acknowledge that (a) stakeholders might have an arbitrary number of categories for 
prioritization (2, 3, 4, 5, ...), and (b) they may have wide variation in what combinations are given which priority.


## Decision Drivers

* There was some discussion during the development of [ADR 0005](0005-ssvc-decision-point-group-versioning.md) about
  whether the outcome set should be included in the tree definition. 

## Considered Options

* Include the outcome set in the decision point group definition.
* Omit the outcome set from the decision point group definition.

## Decision Outcome

Chosen option: "Omit the outcome set from the decision point group definition", because the outcome set is
stakeholder-specific and not part of the decision point group's (aka _the tree's_) identity.

We need to define a few terms here:

- a _decision point group_ is a set of decision points that are used to model a decision. The combinations of the decision
  points' values define the structure of the decision model (aka _tree_).
- an _outcome set_ is the set of possible outcomes for a decision model. Each leaf node of a tree is labeled with an
  outcome from the outcome set.
- a _policy_ is a mapping from specific combinations of decision point values to specific outcomes from the outcome set.

A decision point group fully defines the structure of a decision model (tree). The outcome set and the policy are
both stakeholder-specific. 

Two examples for illustrative purposes:

1. Two organizations could use the same decision point group to model the same decision, but
   one has a 3-category outcome set and the other has a 4-category outcome set. The two organizations would be using the
   same decision model but with different outcome sets. This inherently leads to different policies.
2. Two organizations might use both the same decision point group and the same outcome set, but still have different
   policies mapping the specific decision point value combinations to different outcome values.

In both cases, the structure of the decision model (tree) is the same, but the resulting policies are different.

If we were to include both the outcome set and the policy in the decision point group definition, then both examples
would lead to the conclusion that the two organizations' decision models are different, when in fact they have modeled
the same decision in the same structure, only differing in their policy application.

If we were to include the outcome set but not the policy in the decision point group definition, then the first example
would appear to be "different" whereas the second example would appear to be "the same". This also seems misleading.

For completeness, it is not possible to include the policy without the outcome set, since the policy depends on both 
the decision point group and the outcome set.

Therefore, the decision point group's (aka _the tree's_) identity omits both the outcome set and its specific mapping to
the tree structure. The thing we're asserting is that the structure of the tree (as defined by its constituent decision
points and their specific versions) is invariant to the above, therefore the tree's identity omits both the outcome set 
and its specific mapping to the tree structure.


### Consequences

* Good, because we can avoid decision point group versioning events due to changes in the outcome set or policy.
* Good, because SSVC users can share decision point groups as decision models without needing to share their specific
  outcome sets or policies.
* Bad, because the decision point group definition does not fully specify the decision model including the policy.

### Confirmation

This decision is confirmed by the fact that decision point groups are versioned independently of outcome sets and policies.

## Pros and Cons of the Options

### Include the outcome set in the decision point group definition.

Including the outcome set in the decision point group definition would mean that the decision model (tree) changes
whenever the outcome set changes. This would lead to a large number of versioning events for decision point groups
whenever the outcome set changes, even if the structure of the decision model (tree) remains the same.

* Good, because the combination of decision points and outcome sets would be fully specified, and users would only
  need to establish their own policy to use the decision model.
* Bad, because the decision model (tree) would change whenever the outcome set changes, even if the structure of the
  decision model (tree) remains the same. For example, the same structure with a 3-category outcome set and a 4-category
  outcome set would be considered different decision models. 

Furthermore, including both the outcome group _and_ the policy in the decision point group definition would mean that the
decision model (tree) version would change whenever the policy changes, even if the structure of the decision model (tree) and
the outcome set both remained the same.

* Good, because the decision model (tree) would be fully specified and would not depend on any external factors.
* Bad, because the decision model (tree) would change whenever the policy changes, even if the structure of the
  decision model (tree) and the outcome set both remained the same.
* Bad, because the number of versioning events for decision models would be large.

## More Information

- Issue [#354](https://github.com/CERTCC/SSVC/issues/354) - Create ADR about Outcome Sets are not included in Decision Point Groups
- Discussion [#303](https://github.com/CERTCC/SSVC/discussions/303#discussioncomment-6926935) - Defining tree versions
- [ADR-0005](0005-ssvc-decision-point-group-versioning.md) - SSVC Decision Point Group Versioning
