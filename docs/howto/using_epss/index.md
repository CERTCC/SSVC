# EPSS &rarr; SSVC Intro

!!! quote inline end "The [FIRST EPSS SIG](https://www.first.org/epss) Explains [EPSS](https://www.first.org/epss/model)"

    EPSS is a daily estimate of the probability of exploitation activity being observed over the next 30 days

The [Exploit Prediction Scoring System](https://www.first.org/epss) ([EPSS](https://www.first.org/epss)) is a statistical model that estimates the likelihood of a vulnerability being exploited in the wild. EPSS can be a valuable input when assessing the exploitation risk associated with vulnerabilities. EPSS provides two key metrics:

- **EPSS Score**: A score between 0 and 1 indicating the probability of exploitation.
- **EPSS Percentile**: A ranking percentile that indicates how the EPSS score compares to other vulnerabilities.

In the following pages, we'll demonstrate a few different ways to incorporate EPSS data into your SSVC decision models.

<div class="grid cards" markdown>

- :material-dice-multiple: [Using EPSS Probability Scores as an Input to SSVC Decisions](epss_probability.md)

    ---

    How to use EPSS probability scores to augment other data sources to
    inform the SSVC Exploitation decision point.
  
- :material-percent: [Using EPSS Percentiles to Amplify SSVC Decisions](epss_percentiles.md)

    ---

    How to use EPSS percentiles to amplify the output of an existing SSVC decision model.

</div>
