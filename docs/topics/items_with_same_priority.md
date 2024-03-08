# Items With the Same Priority

Within each setting, the decisions are a kind of equivalence class for priority.
That is, if an organization must deploy patches for three vulnerabilities, and if these vulnerabilities are all assigned
the *scheduled* priority, then the organization can decide which to deploy first.
The priority is equivalent.

!!! tip "This is not CVSS"

    This approach may feel uncomfortable since CVSS gives the appearance of a finer grained priority.
    CVSS appears to say,

    > Not just 4.0 to 6.9 is ‘medium’ severity, but 4.6 is more severe than 4.5.

    However, CVSS v3.1 is designed to be accurate only within +/- 0.5,
    and, in practice, is scored with errors of around +/- 1.5 to 2.5 [@allodi2018effect, see Figure 1].

    An error of this magnitude is enough to make all of the “normal” range from 4.0 to 6.9 equivalent, because 
    5.5 +/- 1.5 is the range 4.0 to 7.0.
    
    Our proposal is an improvement over this approach.

    CVSS errors often cross decision boundaries; in other words, the error range often includes the transition between “high” and “critical” or “medium.” Since our approach keeps the decisions qualitatively defined, this fuzziness does not
    affect the results.

!!! example "Three Vulnerabilities of Equivalent Priority"

    Returning to the example of an organization with three vulnerabilities to remediate that were assigned *scheduled*
    priority, in SSVC, they can be patched in any order.
    This is an improvement over CVSS, since based on the scoring errors, CVSS was essentially just giving random 
    fine-grained priorities within qualitative categories anyway.

With our system, organizations can be more deliberate about conveniently organizing work that is of equivalent priority.


