# Public Value Added

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.public_value_added import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

The intent of the definition is that one rarely if ever transitions from *limited* to *ampliative* or *ampliative* to *precedence*.
A vulnerability could transition from *precedence* to *ampliative* and *ampliative* to *limited*.
That is, *Public Value Added* should only be downgraded through future iterations or re-evaluations.
This directionality is because once other organizations make something public, they cannot effectively un-publish it
(it'll be recorded and people will know about it, even if they take down a webpage).
The rare case where *Public Value Added* increases would be if an organization published viable information, but
then published additional misleading or obscuring information at a later time.
Then one might go from *limited* to *ampliative* in the interest of pointing to the better information.
