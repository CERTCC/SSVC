# Combining EPSS with other Exploitation-Related Decision Points

SSVC users might want to combine exploitation-related information from multiple
sources into a single decision point for use downstream in a decision table
such as the SSVC [Deployer Decision Model](../deployer_tree.md).

!!! question "What's in this How-To?"

    This How-To explores how to combine information from multiple sources
    via SSVC Decision Points and Decision Tables to create a more nuanced view
    of exploitation risk.

One such source is the [Exploit Prediction Scoring System](https://www.first.org/epss/)
([EPSS](https://www.first.org/epss)) probability score.

!!! question "What is the EPSS Probability Score?"

    The EPSS probability score is a number between 0 and 1 that indicates the likelihood of
    a vulnerability being exploited in the wild within the next 30 days.

## Other Exploitation-Related Information Sources

However, EPSS is not the only source of exploitation-related information.
The
[CISA Known Exploited Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
is another important source.
Additional exploitation-related information can be found in the
[CVSS Exploit Maturity](https://www.first.org/cvss/specification-document#Exploit-Maturity-E)
vector element.

We have implemented SSVC Decision Points to reflect both CISA KEV and CVSS Exploit Maturity:

```python exec="true" idprefix=""
from ssvc.doc_helpers import example_block
from ssvc.decision_points.cvss.exploit_maturity import LATEST as CVSS_E
from ssvc.decision_points.cisa.in_kev import LATEST as CISA_KEV

for dp in [CISA_KEV, CVSS_E]:
    print(example_block(dp))
```

!!! note inline end "EPSS on Probability Binning"

    In a [blog post](https://www.first.org/epss/articles/prob_percentile_bins) on the
    [EPSS website](https://www.first.org/epss), the EPSS SIG discusses the challenges of
    binning probabilities.

    !!! quote "EPSS SIG on Binning"

        However, there are a number of problems with binning. Bins are, by construction, subjective transformations of, in this case, a cardinal probability scale. And because the bins are subjectively defined, there is room for disagreement and misalignment across different users. There is no universal "right" answer to what the cut off should be between a high, and medium, or medium and low.
        
        Moreover, arbitrary cutoffs force two scores, which may be separated by the tiniest of a value, to be labeled and then handled differently, despite there being no practical difference between them. For example, if two bins are set and the cutoff is set at 0.5, two vulnerabilities with probabilities of 0.499 and 0.501 would be treated just the same as two vulnerabilities with probabilities of 0.001 and 0.999. This kind of range compression is unavoidable and so any benefits from this kind of mental shortcut must be weighed against the information loss inevitable with binning.
        
        For these reasons, EPSS does not currently bin EPSS scores using labels. 

    From a data _provider_ perspective, this makes sense.
    Avoiding information loss early in the information pipeline is a good idea.
    However, from a data _consumer_ perspective, and especially when one is making
    a choice between a finite number of options (as in SSVC), binning can be a useful
    tool to reduce the complexity of the decision space.

## Binning Probabilities

We have also provided a few basic SSVC Decision Points to capture probability-based
information in different ways.
Because SSVC is based on categorical decision points, we need to bin the
continuous probability scores into discrete categories.
However, as the EPSS SIG points out (see sidebar), there are *always* tradeoffs
involved in binning.
That's why we provide several different options for binning probabilities so that
SSVC users can choose one that best fits their needs (or create their own if
none of the provided options is suitable).
Expand the example below to see the currently available options.

??? example "Exploring Decision Points for Binning Probabilities"

    We provide a few different decision points based on probability bins.
    You might look these over and choose one that fits your needs.

    ```python exec="true" idprefix=""
    from ssvc.doc_helpers import example_block
    from ssvc.decision_points.basic.probability import DECISION_POINTS as _DPS
    
    for dp in _DPS.values():
        print(example_block(dp))
    ```

For this example, let's say you decide to use the *Probability Scale in 5 weighted levels, ascending*
decision point:

```python exec="true" idprefix=""
from ssvc.doc_helpers import example_block
from ssvc.decision_points.basic.probability.five_weighted import LATEST as DP

print(example_block(DP))
```

With our exploitation and probability binning decision points in hand,
we can now consider how to combine them in a decision table to get
a more nuanced view of exploitation risk.

## Designing an Exploitation-focused Decision Table

Let's say you decide to create a new Decision Table that combines the
EPSS probability information with the other exploitation-related decision
points to determine a more informed outcome using the SSVC [Exploitation](../../reference/decision_points/exploitation.md) decision point.

As a reminder, the SSVC [Exploitation](../../reference/decision_points/exploitation.md) decision point has the following values:

```python exec="true" idprefix=""
from ssvc.doc_helpers import example_block
from ssvc.decision_points.ssvc.exploitation import LATEST as EXP

for dp in [EXP]:
    print(example_block(dp))
```

In conversations with your organization's risk owners, you determine that you
should focus your vulnerability management efforts on the vulnerabilities
that are either already being actively exploited or are very likely to be exploited soon.

You decide to apply the following rules:

| Rule                                                                         | Description                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Prioritize vuls in KEV as Active                                             | If the vulnerability is in the CISA KEV, set the SSVC [Exploitation](../../reference/decision_points/exploitation.md) value to *Active*.                                                                                                |
| Treat very high EPSS probabilities as already Active                         | If the EPSS probability is >90%, set SSVC [Exploitation](../../reference/decision_points/exploitation.md) value to *Active*.                                                                                                            |
| Amplify high EPSS probabilities                                              | If the EPSS probability is 75-90%, bump the SSVC [Exploitation](../../reference/decision_points/exploitation.md) value up one category across the board.                                                                                |
| Assume Public PoCs are Active when EPSS probability is more likely than not. | If the EPSS probability is 55-75%, bump SSVC [Exploitation](../../reference/decision_points/exploitation.md) = *Public PoC* to *Active*                                                                                                 |
| Default: Use CVSS Exploit Maturity                                           | By default, use the [CVSS Exploit Maturity](../../reference/decision_points/cvss/exploit_maturity.md) value to set the SSVC [Exploitation](../../reference/decision_points/exploitation.md) value, unless one of the other rules apply. |

After constructing the decision table according to these rules, you end up with the following table of values:

```python exec="true" idprefix=""
from ssvc.decision_tables.example.epss_percentile import EXAMPLE as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```

A diagram of the decision model is shown below.

???+ example "Example Decision Table Diagram"

    The diagram below shows the decision model for this example.
    Each path through the diagram corresponds to a row in the table above.

    ```python exec="true" idprefix=""
    from ssvc.decision_tables.example.epss_percentile import EXAMPLE as DT
    from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt
    
    rows = DT.mapping
    title = mermaid_title_from_dt(DT)
    print(mapping2mermaid(rows, title=title))
    ```

And here is a JSON object representation of the decision table for programmatic use:

??? example "Example Decision Table JSON"

    The JSON representation of the decision table is shown below.

    ```python exec="true" idprefix=""
    from ssvc.decision_tables.example.epss_percentile import EXAMPLE as DT
    print("```json")
    print(DT.model_dump_json(indent=2))
    print("```")
    ```

Now you've created a clear way to combine EPSS probability scores with other
exploitation-related information to inform your SSVC decisions downstream.

## Conclusion

In this How-To, we've explored how to combine EPSS probability scores with other
exploitation-related information in an SSVC decision table.
By thoughtfully designing decision points and tables, you can create a more nuanced
and effective vulnerability management strategy that prioritizes risks based on
the likelihood of exploitation.
