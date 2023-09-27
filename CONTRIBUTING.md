# How to contribute

Thanks for your help on improving our stakeholder-specific vulnerability categorization work.
To account for different stakeholder perspectives, we benefit from a diverse group of contributors. 

Please see our project documentation in the [wiki](https://github.com/CERTCC/SSVC/wiki) that accompanies this repository
for more information on how you can contribute to the project.

## Where to contribute

This repository contains both a written document with the English-langauge spec, and some code for automating application of SSVC.
Contributions to these two parts of the project look different.
We are focusing on getting the English right first, so we know what code to write. 
Right now we don't have any plans for translations, but if you have interest in that [let us know](https://github.com/CERTCC/SSVC/issues/123). 

# Contributing to the document

The English text lives in the `docs` [subfolder](https://github.com/CERTCC/SSVC/tree/main/docs). 
We welcome any issues from anyone in the community, so we can discuss them and improve SSVC.
If you have a suggestion, please [create an issue](https://github.com/CERTCC/SSVC/issues/new/choose). 

In general, please create an issue before making a pull request to submit a change, except in the case of fixing a small
typo, etc.
Please check that your suggestion does not overlap with existing [issues](https://github.com/CERTCC/SSVC/issues) 
(including [closed ones](https://github.com/CERTCC/SSVC/issues?q=is%3Aissue+is%3Aclosed+))

Please see the [SSVC project wiki]([wiki](https://github.com/CERTCC/SSVC/wiki) for how to keep any 
suggestions or commits aligned with our style consistently. 

# Contributing code

The tools for working with SSVC live in the `src` [subfolder](https://github.com/CERTCC/SSVC/tree/main/src). 

We have limited tooling at the moment. The expectation is that these will mostly be flexible helper-type scripts and plug-ins.
Therefore, interoperability is important. 
Where the code implements or directly references some aspect of the English document, please make that linkage explicit.
We use config files stored in `data` to prevent code in `src` from having fragile dependencies on the English doc. 
We would like to minimize manual change management, but at the very least we need to document where changes in the
document need to result in changes to code. 
Information likely to change based on changes to the English should go in config files to be stored in the 
`data` [subfolder](https://github.com/CERTCC/SSVC/tree/main/data).
Code in the `src` folder should (as robustly as plausible) be reading that data in. 

The process is similar to that for the doc, though the language is different. Please create issues before making pull requests.
Pull requests on code should be clear about what they've changed and what you've done. Thanks in advance!

# Licenses

 - The license for all code in the repository is [here](https://github.com/CERTCC/SSVC/blob/main/LICENSE)
 - The license for all English writing in the repository is [here](https://github.com/CERTCC/SSVC/blob/main/doc/version_1/900_license.md)
 
# Questions

If you have any questions, an [issue](https://github.com/CERTCC/SSVC/issues) or
[discussion](https://github.com/CERTCC/SSVC/discussions) is the best way to get in touch with us.

