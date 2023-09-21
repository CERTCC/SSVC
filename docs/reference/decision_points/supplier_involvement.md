
!!! note "Supplier Involvement"

    === "Text"
        This decision point accounts for the state of the supplier's work on addressing the vulnerability.
    
        | Value | Description |
        | :--- | :--- |
        | Fix Ready | The supplier has provided a patch or fix. |
        | Cooperative | The supplier is actively generating a patch or fix; they may or may not have provided a mitigation or work-around in the mean time. |
        | Uncooperative/Unresponsive | The supplier has not responded, declined to generate a remediation, or no longer exists. |
    === "JSON"
        ```json
        {% include-markdown "../examples/supplier_involvement.json" %}
        ```
    === "Python"
        ```python
        {% include-markdown "../../../src/ssvc/decision_points/supplier_involvement.py" %}
        ```
