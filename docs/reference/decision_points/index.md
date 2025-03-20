# Likely Decision Points and Relevant Data

!!! note inline end "Feedback Welcome"

    We made every effort to put forward informed and useful decision frameworks with wide applicability,
    but the goal of this documentation is more to solicit feedback than make a declaration. We welcome questions,
    constructive criticism, refuting evidence, or supporting evidence about any aspect of this proposal.
    Please submit feedback to the [GitHub repository](https://github.com/CERTCC/SSVC/issues).

We propose the following decision points and associated values should be a
factor when making decisions about
vulnerability prioritization.
We emphasize that these descriptions are hypotheses to be further tested and
validated.

We propose satisfactory decision points for vulnerability management in the next
sections, in alphabetical order.
Each decision point page includes advice on gathering information about the
decision point.
[SSVC using Current Information Sources](../../topics/information_sources.md)
provides some
suggestions about how existing sources of information about vulnerabilities can
be used to collate responses to these
decision points.

!!! note "Decision Point Values are Ordered Sets"

    The values for each decision point are ordered sets, meaning that the order
    of the values is significant. The ordering of the values is intended to
    reflect the relative importance of the values, with the first value being the
    least important and the last value being the most important. By requiring
    ordered sets, we can apply consistency checks that ensure that the outcome priority
    of a set of decision point values is greater than or equal to the outcome priority of
    another set of decision point values if the first set of values is greater than or equal to
    the second set of values in every dimension.

!!! question "What determines the ordering?"

    The relevant dimension to which the ordering for both decision points and
    outcomes applies can be different for different decision points and outcomes.
    Sometimes this is a "better" or "worse" dimension, but it seems to generalize to
    a "more likely to act" or "less likely to act" of dimension.

!!! question "Where are the *Unknown* options?"

    One important omission from the values for each category is an *unknown* option.
    Instead, we recommend explicitly identifying an option that is a reasonable assumption based on prior events.
    Such an option requires reliable historical evidence for what tends to be the case;
    of course, future events may require changes to these assumptions over time.
    Therefore, our assumptions require evidence and are open to debate in light of new evidence.
    Different risk tolerance or risk discounting postures are not addressed in the current work;
    accommodating such tolerance or discounting explicitly is an area for future work.
    This flexibility fits into our overall goal of supplying a decision-making framework that is both transparent and fits
    the needs of different communities. Resisting an *unknown* option discourages the modeler from silently embedding these
    assumptions in their choices for how the decision tree flows below the selection of any *unknown* option.
