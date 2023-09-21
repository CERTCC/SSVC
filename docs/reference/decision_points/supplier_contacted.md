!!! tip inline end "Quality Contact Method"

    A quality contact method is a publicly posted known good email address, public portal on vendor website, etc.


!!! note "Supplier Contacted"


    === "Text"
        Has the reporter made a good-faith effort to contact the supplier of the vulnerable component using a quality contact method?
    
        | Value | Description |
        | :---: | :--- |
        | Yes | The reporter has made a good-faith effort to contact the supplier of the vulnerable component using a quality contact method. |
        | No | The reporter has not made a good-faith effort to contact the supplier of the vulnerable component using a quality contact method. |
    === "JSON"
        ```json
        {% include-markdown "../examples/supplier_contacted.json" %}
        ```
    === "Python"
        ```python
        {% include-markdown "../../../src/ssvc/decision_points/supplier_contacted.py" %}
        ```
