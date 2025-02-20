[![Link Checker](https://github.com/CERTCC/SSVC/actions/workflows/link_checker.yml/badge.svg?branch=main)](https://github.com/CERTCC/SSVC/actions/workflows/link_checker.yml)

# SSVC

The Stakeholder-specific Vulnerability Categorization (SSVC) is a system for prioritizing actions during vulnerability management.
SSVC aims to avoid one-size-fits-all solutions in favor of a modular decision-making system with clearly defined and tested parts that vulnerability managers can select and use as appropriate to their context.

---

SSVC is mostly conceptual tools for vulnerability management.
These conceptual tools (how to make decisions, what should go into a decision, how to document and communicate decisions clearly, etc.) are described here.

**Note:** This repository contains the *content* for the main SSVC documentation hosted at

## [https://certcc.github.io/SSVC/](https://certcc.github.io/SSVC/)

- If you are just looking for SSVC documentation, you should go there.
- If you are interested in contributing to the SSVC documentation, you are in the right place.

---

# What's here

Here's a quick overview of the main directories and files in this repository.

## `/docs/*`

Raw markdown and graphics files used to build the SSVC documentation website.
See [`project_docs/README.md`](project_docs/README.md) for more info.

### `/docs/ssvc-calc`

Directory with SSVC calculator using D3 graph.
See [`ssvc-calc/README.md`](docs/ssvc-calc/README.md) for more info.

A demo version of `ssvc-calc` can be found at <https://certcc.github.io/SSVC/ssvc-calc/>

## `/pdfs/*`

Static versions of previously issued PDF reports are stored in this directory.

## `/data/*`

The data folder contains detailed data files that define suggested prioritization results based on each combination of information on a vulnerability work item.

There are both `.csv` and `.json` files in this directory.

### `/data/csvs/*`

The `.csv` files are the primary data files used by the `ssvc.py` module.

Also included in data are the lookup tables as csv files which `ssvc_v2.py` reads in.
These files define one row per possible path through the trees as described in the documentation.
Customizing the "outcome" column in this csv is the primary recommended way that stakeholders might adapt SSVC to their environment.

### `/data/json/*`

These json files are generated examples from the python `ssvc` module.

### `/data/schema/*` and `/data/schema_examples/*`

These files are used by the `ssvc-calc` module.

## `/src/*`

This directory holds helper scripts that can make managing or using SSVC easier.

### `/src/ssvc/*`

The `ssvc` python module provides tools to work with decision points, decision point groups, and outcomes.
These modules are used to generate documentation for various [Decision Points](https://certcc.github.io/SSVC/reference/decision_points/)

Documentation for the `ssvc` module can be found at [https://certcc.github.io/SSVC/reference/code/](https://certcc.github.io/SSVC/reference/code/)

### `src/ssvc_v2.py`

A basic Python module for interacting with the SSVC trees. `ssvc_v2.py` has
two methods: `applier_tree()` and `developer_tree()`

The two methods just loop through their respective lookup tables until
they hit a match, then return the outcome. Maybe not the best implementation,
but it worked well enough for what was needed at the time.

## Local development

The simplest way to get started with local development is to use Docker.
We provide a Dockerfile that builds an image with all the dependencies needed to build the site.
We also provide a `Makefile` that simplifies the process of building the site and running a local server,
so you don't have to remember the exact `docker build` and `docker run` commands
to get started.

### Make Commands

To display the available `make` commands, run:

```bash
make help
```

To preview any `make` command without actually executing it, run:

```bash
make -n <command>
```

### Run Local Server With Docker

The easiest way to get started is using make to build a docker image and run the site:

```bash
make docs
```

Then navigate to <http://localhost:8765/SSVC/> to see the site.

Note that the docker container will display a message with the URL to visit, for
example: `Serving on http://0.0.0.0:8000/SSVC/` in the output. However, that port
is only available inside the container. The host port 8765 is mapped to the container's
port 8000, so you should navigate to <http://localhost:8765/SSVC/> to see the site.

Or, if make is not available:

```bash
docker build --target docs --tag ssvc_docs .
docker run --tty --rm -p 8765:8000 --volume .:/app ssvc_docs
```

### Run Local Server Without Docker

If you prefer to run the site locally without Docker, you can do so with mkdocs.
We recommend using a virtual environment to manage dependencies:

```bash
python3 -m venv ssvc_venv
pip install -r requirements.txt
```

Start a local server:

```bash
mkdocs serve
```

By default, the server will run on port 8001.
This is configured in the `mkdocs.yml` file.
Navigate to <http://localhost:8001/> to see the site.

(Hint: You can use the `--dev-addr` argument with mkdocs to change the port, e.g. `mkdocs serve --dev-addr localhost:8000`)

## Run tests

We include a few tests for the `ssvc` module.

### Run Tests With Docker

The easiest way to run tests is using make to build a docker image and run the tests:

```bash
make docker_test
```

Or, if make is not available:

```bash
docker build --target test --tag ssvc_test .
docker run --tty --rm --volume .:/app ssvc_test
```

### Run Tests Without Docker

```bash
pip install pytest
pytest src/test
```

## Environment Variables

If you encounter a problem with the `ssvc` module not being found, you may need to set the `PYTHONPATH` environment variable.
The Dockerfile takes care of this in the Docker environment.
When not running in Docker, make sure that the `src` directory is in your `PYTHONPATH`:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
```

## Contributing

- [SSVC Community Engagement](https://certcc.github.io/SSVC/about/contributing/) has more detail on how to contribute to the project.
- [SSVC Project Wiki](https://github.com/CERTCC/SSVC/wiki) for more detail how to contribute to the project (style guides, etc.)
- [CONTRIBUTING.md](CONTRIBUTING.md) for high-level information and legal details

## Citing SSVC

To reference SSVC in an academic publication, please refer to the version presented at the 2020 Workshop on Economics of Information Security (WEIS):

```
@inproceedings{spring2020ssvc,  
  title={Prioritizing vulnerability response: {A} stakeholder-specific vulnerability categorization},  
  author={Jonathan M Spring and Eric Hatleback and Allen D. Householder and Art Manion and Deana Shick},  
  address={Brussels, Belgium},  
  year={2020},  
  month = dec,  
  booktitle = {Workshop on the Economics of Information Security}  
}
```

## References

1. Spring, J., Hatleback, E., Householder, A., Manion, A., and Shick, D. "Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization." White Paper, Software Engineering Institute, Carnegie Mellon University (2019). <https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=636379>
2. Spring, J., Hatleback, E., Householder, A., Manion, A., and Shick, D. "Towards Improving CVSS." White Paper, Software Engineering Institute, Carnegie Mellon University (2018). <https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=538368>
