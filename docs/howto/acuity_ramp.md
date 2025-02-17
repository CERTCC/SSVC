# Acuity Ramp

!!! question inline end "Why _Acuity_? Isn't this a _Maturity_ Model?"

    The _acuity ramp_ concept is similar to the idea of a _maturity model_, but the term _maturity_ carries a sort of
    moral bias in the sense that it has an implied "good" direction from "immature" to "mature". 

    _Acuity_ has a more neutral connotation, and represents the ability to perceive the world in more detail. 
    In our usage, _Acuity_ as a dimension is more akin to the idea of resolution in the imagery/photography sense.

    Given the choice between a lower-resolution and a higher-resolution decision point, stakeholders should choose the
    one that is most appropriate for both their decision and context. It is not inherently better to use a
    higher-resolution decision point, and it is not inherently worse to use a lower-resolution decision point.

An SSVC _acuity ramp_ is a concept that describes a series of decision functions that are increasingly more detailed and
complex while addressing the same decision. The idea is that a decision maker can start with a simple decision model and
then, as their needs, resources, or abilities change, they can gather and analyze more or different data to understand
their environment with more acuity.

## Acuity Tradeoffs

In Cybersecurity Threat and Vulnerability analysis, as with most decision-making processes, decision makers must
balance trade-offs between the volume, quality, or detail of the information they use and the cost of gathering and
analyzing that information. 
There are many good reasons that decision makers might choose to use a lower resolution indicator that is readily 
available over a higher resolution indicator that comes at a high cost in terms of time, money, or effort.

One way to think about the tradeoffs in acuity is to consider the cost or difficulty of gathering and analyzing data.
Some vulnerability information is readily available for free as a public resource. 
Other information is available for purchase, for example as a subscription to a threat intelligence feed.
Still other information is only available if you set up a system to collect and manage it yourself, such as an internal
asset management system. 
For direct cost tradeoffs, one might conduct a cost-benefit analysis of whether the additional acuity provides value 
more than its cost. Sometimes, tradeoffs are not directly cost-based. 

The quality and readiness for use of the information can also vary. Structured, low resolution public data might be
easier to incorporate into a decision model than unstructured data that requires a lot of manual analysis.
At the CERT/CC, we have observed otherwise high quality threat intelligence provided as PDF files with threat indicators 
embedded as screenshots of text, which would be difficult to extract and use in a decision model.

Another tradeoff is that sometimes one decision point can serve as a close-enough proxy for another decision point that
is more costly or difficult to acquire. For example, in a given deployment context, 
[_Value Density_](../reference/decision_points/value_density.md) might be more readily discerned than
[_Mission Impact_](../reference/decision_points/mission_impact.md) for some stakeholders because it's easier to 
count how many of something there are than to estimate the impact of a loss of specific instances of the thing.
Alternately, information about _Value Density_ might be available from another source, such as a CVSS v4 scoring provider,
whereas _Mission Impact_ might require a more detailed understanding of the stakeholder's mission and environment.
An organization might start with _Value Density_ as a proxy for _Mission Impact_ and then, as they develop a better
understanding of their environment, they could replace _Value Density_ with _Mission Impact_ in their decision model.


## An Acuity Ramp in Action

The _acuity ramp_ idea is a way to show how a stakeholder could "grow into" their desired decision function as their
data collection and analysis capabilities increase. We demonstrate this with the following example.

!!! example "An Acuity Ramp for a Growing System Deployer Organization"

    A system deployer organization with few initial resources might start with a simple decision model that only includes a custom
    `IN_KEV` decision point. The `IN_KEV` decision point would be a simple binary indicator of whether a vulnerability
    has been added to CISA's [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
    ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog. Because this information is free,
    publicly available, and because it is a simple binary indicator, it is easy to gather and analyze even for a very
    small organization.

    The following table shows how the organization might expand their decision model as they grow in capability.
    
    | Acutiy Level | Tree |
    | --- | --- |
    | 1 | ```[IN_KEV]``` |
    | 2 | ```[EXPLOITATION_1]``` |
    | 3 | ```[EXPLOITATION_1, SYSTEM_EXPOSURE_1_0_1]``` |
    | 4 | ```[EXPLOITATION_1, SYSTEM_EXPOSURE_1_0_1, AUTOMATABLE_2]``` |
    | 5 | ```[EXPLOITATION_1, SYSTEM_EXPOSURE_1_0_1, AUTOMATABLE_2, MISSION_IMPACT_2, SAFETY_IMPACT_1]```

    !!! tip "Acuity Levels are Stakeholder-Specific" 

        This example is demonstrating the _concept_ of _acuity levels_ in SSVC adoption. We are specifically
        _not_ saying that there are 5 levels of acuity in SSVC; in principle this concept could be applied to any number
        of levels (including just one). In practice, the number of levels necessary would be a stakeholder-specific implementation choice, so 
        there is no inherent meaning to the "Acuity Levels" shown here outside the context of this example.
    
    The remainder of this example shows one path the organization might take to grow their decision model
    according to the table above.

    ### Improved Exploit Awareness (Acuity Level 2)

    As the organization becomes more capable of gathering and analyzing data, they might start collecting their own
    data on exploitation, allowing them to move to a more detailed decision model that replaces the binary `IN_KEV` 
    decision point with the trinary `EXPLOITATION_1` decision point. For example, they might incorporate data from the
    [Exploit Database](https://www.exploit-db.com/) or the
    [Exploit Prediction Scoring System](https://www.first.org/epss/) ([EPSS](https://www.first.org/epss/))
    into their decision model.

    ```python exec="true" idprefix=""
    from ssvc.decision_points.exploitation import LATEST
    from ssvc.doc_helpers import example_block

    print(example_block(LATEST))
    ```

    ### Improved Asset Management (Acuity Level 3)

    As they continue to develop their internal asset management capabilities, they might find they have enough
    asset data to reflect the degree to which a system is exposed to the internet, allowing them to 
    incorporate the `SYSTEM_EXPOSURE_1_0_1` decision point into their decision model.

    ```python exec="true" idprefix=""
    from ssvc.decision_points.system_exposure import LATEST
    from ssvc.doc_helpers import example_block
    
    print(example_block(LATEST))
    ```

    ### Improved Threat and Vulnerability Analysis (Acuity Level 4)

    Over time, the organization's threat and vulnerability analysis capabilities might reach a point where they can
    begin to collect data on the degree to which a vulnerability is automatable, allowing them to incorporate the
    `AUTOMATABLE_1` decision point into their decision model.
    This decision point might be informed by data from the
    [National Vulnerability Database](https://nvd.nist.gov/) ([NVD](https://nvd.nist.gov/))
    or by translating CVSS v3 or v4 scores into a value for this decision point.

    ```python exec="true" idprefix=""
    from ssvc.decision_points.automatable import LATEST
    from ssvc.doc_helpers import example_block
    
    print(example_block(LATEST))
    ```

    ### Improved Mission and Safety Impact Understanding (Acuity Level 5)

    Now that the deployer organization has been at this for a while, they might have a better understanding of the
    degree to which a vulnerability impacts both their mission and public safety, allowing them to incorporate the
    `MISSION_IMPACT_2` and `SAFETY_IMPACT_1` decision points into their decision model.

    ```python exec="true" idprefix=""
    from ssvc.decision_points.mission_impact import LATEST as MI
    from ssvc.decision_points.safety_impact import LATEST as SI

    from ssvc.doc_helpers import example_block
    
    print(example_block(MI))
    print(example_block(SI))
    ```

    In this way, the organization can grow into a more detailed decision model as their understanding and capabilities improve.


## Conclusion

The _acuity ramp_ concept is a way to show how a stakeholder could "grow into" their desired decision function as their
data collection and analysis capabilities improve. It is a way to show how a decision model can be adapted to the
context of the decision maker, and how the decision maker can make trade-offs between the cost of gathering information
and the quality of the decision they are able to make.

The example above is just a single illustration of the _acuity ramp_ concept. There are many other ways that an
organization might evolve their decision model from a simple starting point toward a more detailed decision model for 
any particular decision. Substituting one decision point for another, adding decision points over time, or even
customizing decision points to better fit the organization's specific context are all ways that an organization might
grow from a simple decision model to a more robust one.
