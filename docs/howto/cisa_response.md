# HOW TO USE THE CISA RESPONSE TIMELINE SSVC DECISION TREE

The CISA Response Timeline SSVC Decision Tree is a tool to harmonize previous
Binding Operational Directives (BODs), to provide a consistent timeline for
the federal enterprise in exacting vulnerability response.

The CISA Response Timeline has 4 binary decision points:

1. InKEV
2. Publicly Exposed
3. Automatable
4. Technical Impact

More information about each of these will be at the bottom of this page.

These 4 decision points are combined to yield 4 outcomes for vulnerability
response timelines:

```python exec="true" idprefix=""
    from ssvc.outcomes.cisa.bod2604 import LATEST
    from ssvc.doc_helpers import example_block
    
    print(example_block(LATEST))
```

InKEV, Automatable, and Technical Impact question the vulnernability whereas
PubliclyExposed questions the state of the asset. Agencies should know whether
an asset is exposed, but if they do not, they can refer to the THIS LINKED
DOCUMENTATION on creating an asset inventory.
CISA scans assets on a regular basis. If the asset is in a CISA CyHy report,
it should be considered PubliclyExposed=YES.

With [Vulnrichment](https://www.cve.org/Media/News/item/blog/2024/06/04/CISA-Added-as-CVE-Authorized-Data-Publisher) data, the states of decision points Automatable and
Technical Impact for a vulnerability are often publicly available on the
cve.org record page for the vulnernability in question. See "CISA-ADP" on
the CVE record page for more information.
SUGGEST PUTTING A SCREENSHOT OR HYPERLINK.

If Vulnrichment data is unavailable, agencies can try to gather that
information themselves. Advice for gathering information about [Automatable](../howto/gathering_info/automatable.md) and [Technical Impact](../howto/gathering_info/technical_impact.md) is available on this site.

Additionally, this decision table is not exhaustive. For example, some
vulnerabilities are exploited before having a public CVE ID, let alone a fix,
and are therefore ineligible for a KEV entry. By considering Exploitation,
even outside of KEV, using the SSVC Exploitation decision point, the federal
enterprise can accelerate a mitigation response until a fix is available.
If InKEV:N and E:A, the agency should act to mitigate the vulnernability as if
it were InKEV:Y, and continue to monitor news sources for a better solution.

## More information about decision points

```python exec="tru" idprefix=""
    from ssvc.decision_points.cisa import (
        InKEV,
        PubliclyExposed,
    )

    from ssvc.decision_points.ssvc import (
         Automatable,
         TechnicalImpact,
    )
    from ssvc.doc_helpers import example_block
    
    print(example_block(InKEV))
    print(example_block(PubliclyExposed))
    print(example_block(Automatable))
    print(example_block(TechnicalImpact))
```

## Visualizing the CISA Response Timeline Decision Table as a Tree Diagram

tree diagram goes here.
