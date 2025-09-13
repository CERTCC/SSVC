CERTCC SSVC
===========

This is the official Python package for the CERT/CC Stakeholder-Specific Vulnerability Categorization (SSVC) project.

Installation
------------
You can install the latest release from PyPI:

    pip install certcc-ssvc

Usage
-----
After installation, import the package and explore the examples:

    import ssvc

    # Example decision point usage. A Weather Forecast and Humidity Value decision point
    from ssvc.decision_points.example import weather
    weather.main()
    from ssvc.decision_points.example import humidity
    humidity.main()
    from ssvc.decision_points.example import base as dp_example
    dp_example.run()

    # Example decision table usage
    from ssvc.decision_tables.example import to_play
    to_play.main()

Explanation
------

This demo is a simple decision tree that provides an Outcome based on two conditions: the weather forecast and the humidity level.

Imagine the decision tree as a series of questions. To find the outcome (the YesNo column), you start at the first question (Decision Point), which is the root node of the tree: What is the Weather Forecast?

* Step 1: Look at the Weather Forecast column (e.g., rain, overcast, sunny).
* Step 2: Look at the Humidity Value above 40% column (e.g., high, low).
* Step 3: Based on the combination of these two conditions, the YesNo column will give you the Decision as "Yes" to play and "No" to not to play.

The YesNo column is the Outcome Decision Point, and the other two Decision Points are inputs that will be collected. 


Resources
---------
Source code and full documentation:
https://github.com/CERTCC/SSVC
