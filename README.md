# SSVC
Stakeholder-Specific Vulnerability Categorization

# What's here

`doc/*`

Draft and final versions of reports. See (`doc/README.md`)[doc/README.md] for
more info.

`doc/pdfs/*.pdf`

Final versions of both reports referenced below can be found in this directory.

`data/*.csv`

Also included in  are the two lookup tables as csv files which `ssvc.py`
reads in. These are just one row per possible path through the trees as
described in the paper. Changing the "outcome" column in this table will
change what the module above recommends.


`src/ssvc.py`

A basic Python module for interacting with the SSVC trees. `ssvc.py` has
two methods: `applier_tree()` and `developer_tree()`

The two methods just loop through their respective lookup tables until
they hit a match, then return the outcome. Maybe not the best implementation,
but it worked well enough for what was needed at the time.

`ssvc-calc`

Directory with SSVC calculator using D3 graph.
See (`ssvc-calc/README.md`)[ssvc-calc/README.md]for more info.

## References

1. Spring, J., Hatleback, E., Householder, A., Manion, A., and Shick, D. "Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization." White Paper, Software Engineering Institute, Carnegie Mellon University (2019). https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=636379
2. Spring, J., Hatleback, E., Householder, A., Manion, A., and Shick, D. "Towards Improving CVSS." White Paper, Software Engineering Institute, Carnegie Mellon University (2018). https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=538368
