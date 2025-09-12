CERTCC SSVC
===========

This is the official Python package for the CERT/CC Stakeholder-Specific Vulnerability Categorization (SSVC) project.

Installation
------------
You can install the latest release from PyPI:

    pip install certcc-ssvc

Demo to explore SSVC decision making
-----
After installation, import the package and explore the examples:

    import ssvc

    # Example decision point usage. A Weather Forecast and Humidity Value decision point
    from ssvc.decision_points.example import weather
    print(weather.LATEST.model_dump_json(indent=2))
    from ssvc.decision_points.example import humidity
    print(humidity.LATEST.model_dump_json(indent=2))


    # Example decision table usage
    from ssvc.decision_tables.example import to_play
    print(to_play.LATEST.model_dump_json(indent=2))

Explanation
------

This demo is a simple decision tree that provides an Outcome based on two conditions: the weather forecast and the humidity level.

Imagine the decision tree as a series of questions. To find the outcome (the YesNo column), you start at the first question (Decision Point), which is the root node of the tree: What is the Weather Forecast?

* Step 1: Look at the Weather Forecast column (e.g., rain, overcast, sunny).
* Step 2: Look at the Humidity Value above 40% column (e.g., high, low).
* Step 3: Based on the combination of these two conditions, the YesNo column will give you the Decision as "Yes" to play and "No" to not to play.

The YesNo column is the Outcome Decision Point, and the other two Decision Points are inputs that will be collected. 

Usage
---------

For usage in vulnerability management scenarios consider the following popular SSVC decisions

    import ssvc

    # Example decision point usage. Exploitation as a Decision Point
    from ssvc.decision_points.ssvc.exploitation import LATEST as Exploitation
    print(Exploitation.model_dump_json(indent=2))
    # Try a CVSS metic Attack Vector using SSVC 
    from ssvc.decision_points.cvss.attack_vector import LATEST as AttackVector
    print(AttackVector.model_dump_json(indent=2))
    from ssvc.decision_points.cisa.in_kev import LATEST as InKEV
    print(InKEV.model_dump_json(indent=2))

    # Example decision table for a Supplier deciding Patch Development Priority
    from ssvc.decision_tables.ssvc.supplier_dt import LATEST as SupplierDT
    print(SupplierDT.model_dump_json(indent=2))

    # Example decision table for a Deployer decision Patch Application Priority
    from ssvc.decision_tables.ssvc.deployer_dt import LATEST as DeployerDT
    print(DeployerDT.model_dump_json(indent=2))

    # View CISA Decision Table as Coordinator for Vulnerability Management writ large
    from ssvc.decision_tables.cisa.cisa_coordinate_dt import LATEST as CISACoordinate
    print(CISACoordinate.model_dump_json(indent=2))


Resources
---------
Source code and full documentation:
https://github.com/CERTCC/SSVC

SSVC Policy Explorer:
https://certcc.github.io/SSVC/ssvc-explorer/

SSVC Calculator:
https://certcc.github.io/SSVC/ssvc-calc/
