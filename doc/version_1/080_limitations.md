

# Limitations

Even as a working proposal, SSVC has some limitations. These are inherent limits of the approach, which should be understood as tradeoffs. There are other limiting aspects of our implementation, but those have been covered as topics that need improvement and are described in Section 7.

We made two important tradeoffs compared to the current state of the practice with CVSS:

1.  We eliminated numerical scores; this may make some practitioners uncomfortable. We explained the reasons for this in depth, but even though CVSS contains false precision, we still must contend with the fact that, psychologically, users find that comforting. As this comfort gap may negatively impact adoption, this fact is a limitation. Although it is ungainly, it would be sound to convert the priority outcomes to numbers at the end of the process, if existing processes require it. Which numbers we choose to convert to is immaterial, as long as the ordering is preserved. CVSS has set a precedent that higher numbers are worse, so a scale \[1, 2, 3, 4\] would work, with defer = 1 and immediate = 4. However, if it were important to maintain backwards compatibility to the CVSS range zero to ten, we could just as well relabel outcomes as \[2, 5.5, 8, 9.5\] for the midpoints of the current CVSS severity ranges.

1.  We incorporated a wider variety of inputs from contexts beyond the affected component. Some organizations are not prepared or configured to reliably produce such data (e.g., around mission impact or safety impact). There is adequate guidance for how to elicit and curate this type information from various risk management frameworks, including OCTAVE.\[47\] Not every organization is going to have sufficiently mature risk management functions to apply SSVC.  

This limitation should be approached with two strategies: (1) organizations should be encouraged and enabled to mature their risk management capabilities and, in the meantime, (2) organizations such as NIST could consider developing default advice. The most practical framing of this approach might be for the NIST NVD to produce scores from the perspective of a new stakeholder—something like “national security” or “public well-being” that is explicitly a sort of default advice for otherwise uninformed organizations that can then explicitly account for national priorities, such as critical infrastructure.
