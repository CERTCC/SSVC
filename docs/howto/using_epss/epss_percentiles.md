# EPSS Quantile Binning as an SSVC Amplifier

!!! tip inline end ""

    !!! tip "Obtain SSVC Data"

        If you are using the [SSVC Deployer Decision Model](../deployer_tree.md), you might already know that
        the [CISA Vulnrichment program](https://github.com/cisagov/vulnrichment)
        provides some SSVC data that is made 
        available via the [CVE Services API](https://cveawg.mitre.org/api-docs/).

    !!! tip "Obtain EPSS Data"

        You can get EPSS data from the [EPSS website](https://www.first.org/epss/)
        or use their [API](https://www.first.org/epss/api) to fetch scores programmatically.

In [another how-to](epss_probability.md), we showed how to use the [Exploit Prediction Scoring System](https://www.first.org/epss/)
([EPSS](https://www.first.org/epss))
probability scores as one of a few different inputs to inform the
SSVC [Exploitation](../../reference/decision_points/exploitation.md) decision point.
This approach can be a useful approach to refine or augment the *input* to an existing SSVC decision model.

!!! question "What's in this How-To?"

    In this how-to, we'll explore a different approach that uses EPSS percentiles
    as an amplifier to adjust the *output* of an existing SSVC decision model.

## Starting Out with the SSVC Deployer Decision Model

Let's start with the assumption that you're already using the
[SSVC Deployer Decision Model](../deployer_tree.md) and have a basic understanding of SSVC.
But then after reading
[Probability, Percentiles, and Binning - How to understand and interpret EPSS Scores](https://www.first.org/epss/articles/prob_percentile_bins),
you realize that you would like to use EPSS percentiles to amplify the output of your existing decision model.

!!! question "Why use percentiles instead of raw probabilities?"

    Percentiles provide a relative ranking of vulnerabilities based on their EPSS scores.
    This can be particularly useful when you want to prioritize vulnerabilities in the context of the entire vulnerability landscape.
    By using percentiles, you can identify which vulnerabilities are more likely to be exploited _compared to others_.
    The [EPSS SIG blog](https://www.first.org/epss/articles/prob_percentile_bins) discusses some of the tradeoffs involved in using percentiles versus raw probabilities.

    That said, we are using percentiles for this how-to simply because we already
    we showed how to use probabilities in [another how-to](epss_probability.md).
    Either approach can be valid depending on your specific needs and context.

One straightforward way to use EPSS is to create bins based on the EPSS score
and use these bins as amplifiers in your SSVC decision-making process.

!!! tip "See Also"

    See the sidebar in [this how-to](epss_probability.md) for a discussion of the tradeoffs involved in binning.

## Binning Percentiles

SSVC provides several basic decision points that bin percentiles into discrete quantiles.
Expand the example below to see the currently available options.

??? example "Exploring Decision Points for Binning Percentiles"

    ```python exec="true" idprefix=""
    from ssvc.doc_helpers import example_block
    from ssvc.decision_points.basic.quantiles import DECISION_POINTS as _DPS
    
    for dp in _DPS.values():
        print(example_block(dp))
    ```

Now, your primary concern is to ensure that you are addressing the
vulnerabilities that are most likely to be exploited.
In conversations with your organization's risk owners, you determine that
they'd like to apply a policy that is consistent with the following:

- If the EPSS percentile is significantly higher than the median, the vulnerability
  should be prioritized two levels higher than the default SSVC recommendation.
- If the EPSS percentile is above the median but not significantly so, the vulnerability
  should be prioritized one level higher than the default SSVC recommendation.
- If the EPSS percentile is significantly lower than the median, the vulnerability
  should be deprioritized lower than the default SSVC recommendation.

You can achieve this with the `quartiles` decision point:

```python exec="true" idprefix=""
from ssvc.decision_points.basic.quantiles.quartiles import LATEST as QUARTILES
from ssvc.doc_helpers import example_block

print(example_block(QUARTILES))
```

!!! warning inline end "We're not saying this is a good rule set!"

    The rules given here are just an example to illustrate how you might use EPSS percentiles
    as an amplifier in your decision-making process.
    We are not suggesting that this is a good idea or that you should follow these rules.
    In fact, these rules are rather aggressive and could result in fully _half_ of all
    vulnerabilities being prioritized _higher_ than they would without the EPSS data.
    Your organization's risk owners should determine the appropriate policy for your context,
    but we would recommend something considerably less aggressive than this example.

You decide to apply the following rules:

```python exec="true" idprefix=""
from ssvc.decision_tables.example.epss_quartile import update_map_doc

print(update_map_doc())
```

## Building the Decision Table  

Given the rules outlined above, you build a new Decision Table that takes the
default outcome from the
[SSVC Deployer Decision Model](../deployer_tree.md) and applies the EPSS quartile
information to amplify it. The resulting decision table looks like this:

```python exec="true" idprefix=""
from ssvc.decision_tables.example.epss_quartile import EXAMPLE as DT
from ssvc.decision_tables.helpers import dt2df_md

print(dt2df_md(DT))
```

A diagram of the decision model is shown below.

???+ example "Example Decision Table Diagram"

    ```python exec="true" idprefix=""
    from ssvc.decision_tables.example.epss_quartile import EXAMPLE as DT
    from ssvc.decision_tables.helpers import mapping2mermaid, mermaid_title_from_dt
    
    rows = DT.mapping
    title = mermaid_title_from_dt(DT)
    print(mapping2mermaid(rows, title=title))
    ```

And here is a JSON object representation of the decision table for programmatic use:

??? example "Example Decision Table JSON"

    The JSON representation of the decision table is shown below.

    ```python exec="true" idprefix=""
    from ssvc.decision_tables.example.epss_quartile import EXAMPLE as DT

    print("```json")
    print(DT.model_dump_json(indent=2))
    print("```")
    ```

Now you can use this decision table in your SSVC implementation to adjust
the prioritization of vulnerabilities based on their EPSS percentiles.

!!! question "How can I sort work items within a given SSVC outcome category?"

    While we don't usually recommend sorting within a given SSVC outcome category,
    we recognize that some organizations may want to do this.

    If you want to sort vulnerabilities within a given SSVC outcome (e.g., all vulnerabilities
    that are classified as "Immediate"), you can use the raw EPSS probability score
    as a secondary sorting key.
    This way, even if multiple vulnerabilities fall into the same SSVC category,
    you can still prioritize them based on their predicted likelihood of exploitation.


## Conclusion

In this how-to, we've demonstrated how to use EPSS percentiles as an amplifier
to adjust the output of an existing SSVC decision model.
While the example provided is considerably more aggressive than we would recommend
in practice, it illustrates one way to incorporate EPSS data into an established SSVC-based
vulnerability management strategy.
By incorporating statistical insights from EPSS, you can prioritize
vulnerabilities more effectively based on their likelihood of exploitation.
