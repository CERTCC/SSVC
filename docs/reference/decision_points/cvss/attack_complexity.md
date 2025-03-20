# Attack Complexity

```python exec="true" idprefix=""
from ssvc.decision_points.cvss.attack_complexity import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

## Previous Versions

Following are the previous versions of the decision point:

```python exec="true" idprefix=""
from ssvc.decision_points.cvss.attack_complexity import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
```
