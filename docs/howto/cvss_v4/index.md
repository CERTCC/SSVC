# CVSS v4 Assessment With SSVC

[CVSS v4](https://www.first.org/cvss/v4-0/specification-document) introduces an
updated scoring system that includes several metric groupings referred to
as *Equivalence Sets*.
In SSVC, we can model these individual equivalence sets as decision tables
that can be used by analysts to assess each equivalence set value based on
its component metrics (which we have mapped into SSVC decision points).

An Analyst can use these decision tables to assess the CVSS v4 equivalence set
values based either on their own assessments or by using a CVSS v4 vector published
by another source.

!!! question "I thought SSVC and CVSS were different?"

    SSVC and CVSS are indeed different, but they can be used together.
    We do not see SSVC as a replacement for CVSS, but rather as a complementary
    decision-making framework that can help stakeholders make a variety of 
    vulnerability response decisions.
    In fact, we're very interested in using CVSS vector elements as inputs to 
    SSVC decision tables to help stakeholders make more informed prioritization
    decisions that leverage the community's understanding of a vulnerability's
    characteristics and impact assessments.
    In the future, we hope to see more SSVC decision tables that are
    directly informed by CVSS vectors, allowing analysts to use SSVC to
    create a broader set of decision models that incorporate CVSS vector
    elements as inputs.

## CVSS v4 Equivalence Sets

Here we provide the decision points for each of the CVSS v4 equivalence sets.

```python exec="true" idprefix=""
from ssvc.decision_tables.cvss.qualitative_severity import LATEST as DT
from ssvc.doc_helpers import example_block

for dp in [v for k,v in DT.decision_points.items() if k != DT.outcome]:
    print(example_block(dp))
```

We provide a detailed decision table for each equivalence set in the pages that follow:

- [CVSS v4 Equivalence Set EQ1](eq1.md)
- [CVSS v4 Equivalence Set EQ2](eq2.md)
- [CVSS v4 Equivalence Set EQ3](eq3.md)
- [CVSS v4 Equivalence Set EQ4](eq4.md)
- [CVSS v4 Equivalence Set EQ5](eq5.md)
- [CVSS v4 Equivalence Set EQ6](eq6.md)

## CVSS v4 Qualitative Severity Rating

Finally, CVSS v4 provides a *Qualitative Severity Rating* that maps the six equivalence
sets into a single qualitative rating (None, Low, Medium, High, Critical).

```python exec="true" idprefix=""
from ssvc.decision_tables.cvss.qualitative_severity import LATEST as DT
from ssvc.doc_helpers import example_block
dp = DT.decision_points[DT.outcome]
print(example_block(dp))
```

A full decision model for the CVSS v4 Qualitative Severity Rating can be found
in the [CVSS v4 Qualitative Severity Rating](qualitative.md) page.

!!! question "What about CVSS v4 *MacroVectors*?"

    CVSS v4 _MacroVectors_ are a new addition in CVSS v4 that provide a way to
    map the six equivalence sets into a single vector value that can be used
    to assign a CVSS v4 base score.
    In our implementation here, we simply model the MacroVector as another decision
    table that takes the individual equivalence set outcomes as inputs and provides
    the Qualitative Severity Rating as its outcome.

!!! question "How are CVSS v4 scores handled?"

    We do not provide numerical CVSS v4 scores in this implementation. 
    The CVSS v4 specification defines a 
    [lookup table](https://github.com/FIRSTdotorg/cvss-v4-calculator/blob/main/cvss_lookup.js) 
    and a complex algorithm to compute a score between 0.0 and 10.0 based on 
    equivalence set values and the CVSS v4 vector.

    In practice, many analysts convert numerical scores into qualitative 
    severity ratings, such as None, Low, Medium, High, or Critical:

    | Numerical Score | Qualitative Severity Rating |
    |-----------------|----------------------------|
    | 0.0             | None                       |
    | 0.1 - 3.9       | Low                        |
    | 4.0 - 6.9       | Medium                     |
    | 7.0 - 8.9       | High                       |
    | 9.0 - 10.0      | Critical                   |

    One of our [original concerns](https://doi.ieeecomputersociety.org/10.1109/MSEC.2020.3044475) 
    about CVSS v3—and still relevant in CVSS v4—was that numerical scores were 
    often misused or misinterpreted, leading to poor prioritization decisions. 
    To avoid this, we focus on mapping equivalence set values directly to 
    qualitative severity ratings, which is the outcome many organizations actually 
    care about.

    Using SSVC, we can model the same assessment process that an analyst would 
    use with CVSS v4, but entirely bypass the numerical score. 
    The logic is identical: given a set of equivalence values, SSVC produces the
    same qualitative severity rating as the [CVSS v4 Calculator](https://www.first.org/cvss/calculator/4-0).
    This demonstrates that numerical scores are not 
    necessary for effective prioritization or decision-making.
