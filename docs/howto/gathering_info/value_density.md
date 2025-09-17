# Gathering Information About Value Density

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.value_density import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

The heuristics presented in the *Value Density* definitions involve whether the system is usually maintained by a dedicated professional, although we have noted some exceptions (such as encrypted mobile messaging applications).

{% include-markdown "../../_includes/question_callout.md" heading-offset=1 %}

An analyst might use market research reports or Internet telemetry data to assess an unfamiliar product.
Organizations such as Gartner produce research on the market position and product comparisons for a large variety of systems.
These generally identify how a product is deployed, used, and maintained.
An organization's own marketing materials are a less reliable indicator of how a product is used, or at least how the organization expects it to be used.

Network telemetry can inform how many instances of a software system are connected to a network.
Such telemetry is most reliable for the supplier of the software, especially if software licenses are purchased and checked.
Measuring how many instances of a system are in operation is useful, but having more instances does not mean that the software is a densely valuable target.
However, market penetration greater than approximately 75% generally means that the product uniquely serves a particular market segment or purpose.
This line of reasoning is what supports a determination that an ubiquitous encrypted mobile messaging application should be considered to have a *concentrated* Value Density.
