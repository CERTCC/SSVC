# Incident Severity

```python exec="true" idprefix=""
from ssvc.decision_points.nciss.incident_severity import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

Version 2.0.0 is based on the
[National Cyber Incident Scoring System](https://www.cisa.gov/sites/default/files/2023-01/cisa_national_cyber_incident_scoring_system_s508c.pdf)
developed by the Cybersecurity and Infrastructure Security Agency (CISA).

Version 1.0.0 is based on the 
[Cyber Incident Severity Schema](https://obamawhitehouse.archives.gov/sites/whitehouse.gov/files/documents/Cyber%2BIncident%2BSeverity%2BSchema.pdf)
adopted by the United States Federal Cybersecurity Centers, in coordination with departments and agencies with a
cybersecurity or cyber operations mission.

## Previous Versions

```python exec="true" idprefix=""
from ssvc.decision_points.nciss.incident_severity import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
```

