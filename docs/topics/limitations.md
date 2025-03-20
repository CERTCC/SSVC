# Limitations

SSVC has some inherent limits in its approach, which should be understood as tradeoffs.
There are other limiting aspects of our implementation, but those have been covered as topics that need improvement and are described in [Future Work](future_work.md).

We made two important tradeoffs compared to the current state of the practice.
Other systems make different tradeoffs, which may be better or worse depending on the context of use.
While these are inherently limitations of SSVC, we do not intend SSVC to be the one and only vulnerability management tool available.
Those for whom these limitations are a must-have may be better supported by a different vulnerability management framework.

## Eliminated Numerical Scores

We eliminated numerical scores; this may make some practitioners uncomfortable.
We explained the reasons for this in depth, but even though CVSS contains false precision, we still must contend with
the fact that, psychologically, users find that comforting.
As this comfort gap may negatively impact adoption, this fact is a limitation.
Although it is ungainly, it would be sound to convert the priority outcomes to numbers at the end of the process,
if existing processes require it.
Which numbers we choose to convert to is immaterial, as long as the ordering is preserved.
CVSS has set a precedent that higher numbers are worse, so a scale \[1, 2, 3, 4\] would work, with *defer* = 1 and
*immediate* = 4.
However, if it were important to maintain backwards compatibility to the CVSS range zero to ten, we could just as well
relabel outcomes as \[2, 5.5, 8, 9.5\] for the midpoints of the current CVSS severity ranges.
This is not a calculation of any kind, just an assignment of a label which may make adoption more convenient.
Of course, these labels are dangerous, as they may be misused as numbers.
Therefore, we prefer the use *defer*, *scheduled*, etc., as listed in
[Enumerating Vulnerability Management Actions](../howto/deployer_tree.md).

## Expanded Context

We incorporated a wider variety of inputs from contexts beyond the affected component.
Some organizations are not prepared or configured to reliably produce such data (e.g., around mission impact or safety impact). There is adequate guidance for how to elicit and curate this type information from various risk management frameworks, including OCTAVE [@caralli2007octave]. Not every organization is going to have sufficiently mature risk management functions to apply SSVC.\

This second limitation should be approached with two strategies:

1. Organizations should be encouraged and enabled to mature their risk management capabilities
2. In the meantime, organizations such as NIST could consider developing default advice.
   The most practical framing of this approach might be for the NIST NVD to produce scores from the perspective of a
   new stakeholder&mdash;something like “national security” or “public well-being” that is explicitly a sort of default
   advice for otherwise uninformed organizations that can then explicitly account for national priorities, such as critical infrastructure.
