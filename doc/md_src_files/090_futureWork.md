

# Future Work

We intend SSVC to offer a workable baseline from which to improve and refine a vulnerability-prioritization methodology. While the method herein should be functional, we do not claim it is ready for use as is. Therefore, we lay out some aspects of future work that would help make it ready to use. We focus on further requirements gathering, further testing of the reliability of the decision process, and expanding to additional types of stakeholders beyond deployers and suppliers.

## Requirements Gathering via Sociological Research

The community should know what users of a vulnerability prioritization system want. To explore their needs, it’s important to understand how people actually use CVSS and what they think it tells them. In general, such empirical, grounded evidence about what practitioners and decision makers want from vulnerability scoring is lacking. We have based this paper’s methodology on multiple decades of professional experience and myriad informal conversations with practitioners. Such evidence is not a bad place to start, but it does not lend itself to examination and validation by others. The purpose of understanding practitioner expectations is to inform what a vulnerability-prioritization methodology should actually provide by matching it to what people want or expect. The method this future work should take is long-form, structured interviews. We do not expect anyone to have access to enough consumers of CVSS to get statistically valid results out of a short survey, nor to pilot a long survey.

## Further Decision Tree Testing

More testing with diverse analysts is necessary before the decision trees are reliable. In this context, **reliable** means that two analysts, given the same vulnerability description and decision process description, will reach the same decision. Such reliability is important if scores and priorities are going to be useful. If they are not reliable, they will vary widely over time and among analysts. Such variability makes it impossible to tell whether a difference in scores is really due to one vulnerability being higher priority than other.

The pilot study provides a methodology for measuring and evaluating reliability of the decision process description based on the agreement measure κ. This study methodology should be repeated with different analyst groups, from different sectors and with different experience, feeding the results into changes in the decision process description until the agreement measure is adequately close to 1.


