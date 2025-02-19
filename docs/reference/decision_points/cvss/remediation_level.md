# Remediation Level

```python exec="true" idprefix=""
from ssvc.decision_points.cvss.remediation_level import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

## Previous Versions

Following are the previous versions of the decision point:

```python exec="true" idprefix=""
from ssvc.decision_points.cvss.remediation_level import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\n---\n")
```
