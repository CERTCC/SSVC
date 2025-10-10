# Gathering Information About Mission Impact

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.mission_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

The factors that influence the mission impact level are diverse.
At a minimum, understanding mission impact should include gathering information about the critical paths that involve vulnerable components, viability of contingency measures, and resiliency of the systems that support the mission.
There are various sources of guidance on how to gather this information; see for example the FEMA guidance in [Continuity Directive 2](https://www.fema.gov/sites/default/files/2020-07/Federal_Continuity_Directive-2_June132017.pdf) or [OCTAVE FORTE](https://insights.sei.cmu.edu/insider-threat/2018/06/octave-forte-and-fair-connect-cyber-risk-practitioners-with-the-boardroom.html).
This is part of risk management more broadly.
It should require the vulnerability management team to interact with more senior management to understand mission priorities and other aspects of risk mitigation.

{% include-markdown "../../_includes/default_mission_impact_values.md" %}
