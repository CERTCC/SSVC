# Bootstrapping an SSVC Process from Scratch

Using SSVC to prioritize vulnerability response requires a few steps. The steps are:

!!! note inline end "Bootstrapping SSVC Overview"

    ```mermaid
    flowchart
        start([Start])
        prep[Prepare to use SSVC]
        dataops[Data Operations]
        runtime[Use SSVC]
        r[Vulnerability Response]
        start --> prep
        prep --> dataops
        dataops --> runtime
        runtime --> r
        r --> dataops
    ```

{% include-markdown "howto/bootstrap/_steps_table.md" %}

We cover each of these in the following sections, starting with [Prepare to Use SSVC](prepare.md).
If you want to skip ahead to the full process, see [Bootstrapping SSVC Summary](summary.md).
