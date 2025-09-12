CERTCC SSVC
===========

This is the official Python package for the CERT/CC Stakeholder-Specific Vulnerability Categorization (SSVC) project.

Installation
------------
You can install the latest release from PyPI:

    pip install certcc-ssvc

Usage
-----
After installation, import the package and explore the examples:

    import ssvc

    # Example decision point usage
    from ssvc.decision_points.example import base as dp_example
    dp_example.run()

    # Example decision table usage
    from ssvc.decision_tables.example import base as dt_example
    dt_example.run()

The modules in `ssvc/decision_points/example/base.py` and
`ssvc/decision_tables/example/base.py` demonstrate core SSVC decision
points and decision tables.

Resources
---------
Source code and full documentation:
https://github.com/CERTCC/SSVC
