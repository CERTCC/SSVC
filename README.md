[![pandoc_html_pdf](https://github.com/CERTCC/SSVC/actions/workflows/pandoc_html_pdf.yaml/badge.svg)](https://github.com/CERTCC/SSVC/actions/workflows/pandoc_html_pdf.yaml)

# SSVC

The Stakeholder-specific Vulnerability Categorization (SSVC) is a system for prioritizing actions during vulnerability management.
SSVC aims to avoid one-size-fits-all solutions in favor of a modular decision-making system with clearly defined and tested parts that vulnerability managers can select and use as appropriate to their context.

# What's here

SSVC is mostly conceptual tools for vulnerability management.
These conceptual tools (how to make decisions, what should go into a decision, how to document and communicate decisions clearly, etc.) are described here.

## `/docs/*`

Raw markdown and graphics files used to build the SSVC documentation website.
See [`project_docs/README.md`](project_docs/README.md) for more info.


### `/docs/ssvc-calc`

Directory with SSVC calculator using D3 graph.
See [`ssvc-calc/README.md`](docs/ssvc-calc/README.md) for more info.

A demo version of `ssvc-calc` can be found at https://certcc.github.io/SSVC/ssvc-calc/


## `/draft/*`

Generated drafts of reports.
Up through SSVC v2.1.1, these were recent versions of the main document in both `pdf` and `html` formats.

With the recent conversion from the SSVC documentation from `pdf`-document orientation to a website orientation,
we are no longer generating `pdf` versions of the main document.

## `/pdfs/*.pdf`

Static versions of previously issued reports are stored in this directory.

## `/data/*.csv`

The data folder contains detailed data files that define suggested prioritization results based on each combination of information on a vulnerability work item.
Also included in data are the lookup tables as csv files which `ssvc.py` reads in.
These files define one row per possible path through the trees as described in the documentation.
Customizing the "outcome" column in this csv is the primary recommended way that stakehodlers might adapt SSVC to their environment.

## `/src/*`

The tools in the `src` folder provide an interface to work with these data files.

### `src/ssvc.py`

A basic Python module for interacting with the SSVC trees. `ssvc.py` has
two methods: `applier_tree()` and `developer_tree()`

The two methods just loop through their respective lookup tables until
they hit a match, then return the outcome. Maybe not the best implementation,
but it worked well enough for what was needed at the time.

## Local development

Install prerequisites:

```bash
pip install -r requirements.txt
```

Start a local server:

```bash
mkdocs serve
```

Navigate to http://localhost:8000/ to see the site.

(Hint: You can use the `--dev-addr` argument with mkdocs to change the port, e.g. `mkdocs serve --dev-addr localhost:8001`)

## Citing SSVC

To reference SSVC in an academic publication, please refer to the version presented at the 2020 Workshop on Economics of Information Security (WEIS):

@inproceedings{spring2020ssvc,  
  title={Prioritizing vulnerability response: {A} stakeholder-specific vulnerability categorization},  
  author={Jonathan M Spring and Eric Hatleback and Allen D. Householder and Art Manion and Deana Shick},  
  address={Brussels, Belgium},  
  year={2020},  
  month = dec,  
  booktitle = {Workshop on the Economics of Information Security}  
}

## References

1. Spring, J., Hatleback, E., Householder, A., Manion, A., and Shick, D. "Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization." White Paper, Software Engineering Institute, Carnegie Mellon University (2019). https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=636379
2. Spring, J., Hatleback, E., Householder, A., Manion, A., and Shick, D. "Towards Improving CVSS." White Paper, Software Engineering Institute, Carnegie Mellon University (2018). https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=538368
