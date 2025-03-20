# Safety

```python exec="true" idprefix=""
from ssvc.decision_points.cvss.supplemental.safety import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

{% include-markdown "../../../_includes/safety_cvss_ssvc.md" %}

## Previous Versions

Following are the previous versions of the decision point:

```python exec="true" idprefix=""
from ssvc.decision_points.cvss.supplemental.safety import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
```
