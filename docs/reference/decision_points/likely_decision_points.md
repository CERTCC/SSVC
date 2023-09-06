# Likely Decision Points and Relevant Data

We propose the following decision points and associated values should be a factor when making decisions about
vulnerability prioritization.
{== Each decision point is tagged with the stakeholder it is relevant to: deployers, suppliers, or both. ==}
We emphasize that these descriptions are hypotheses to be further tested and validated.
We made every effort to put forward informed and useful decision frameworks with wide applicability,
but the goal of this paper is more to solicit feedback than make a declaration. We welcome questions,
constructive criticism, refuting evidence, or supporting evidence about any aspect of this proposal.

!!! question "Where are the _Unknown_ options?"

    One important omission from the values for each category is an “unknown” option.
    Instead, we recommend explicitly identifying an option that is a reasonable assumption based on prior events.
    Such an option requires reliable historical evidence for what tends to be the case;
    of course, future events may require changes to these assumptions over time.
    Therefore, our assumptions require evidence and are open to debate in light of new evidence.
    Different risk tolerance or risk discounting postures are not addressed in the current work;
    accommodating such tolerance or discounting explicitly is an area for future work.
    This flexibility fits into our overall goal of supplying a decision-making framework that is both transparent and fits
    the needs of different communities. Resisting an “unknown” option discourages the modeler from silently embedding these
    assumptions in their choices for how the decision tree flows below the selection of any “unknown” option.

We propose satisfactory decision points for vulnerability management in the next sections, in no particular order.
Each section has a subsection with advice on gathering information about the decision point.
[SSVC using Current Information Sources](#ssvc-using-current-information-sources) will provide some suggestions about how existing sources of information about vulnerabilities can be used to collate responses to these decision points.

