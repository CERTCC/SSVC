#!/usr/bin/env python
"""
file: value_density
author: adh
created_at: 9/21/23 10:01 AM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

# Diffuse. The system that contains the vulnerable component has limited resources. That is, the resources that the adversary will gain control over with a single exploitation event are relatively
# small. Examples of systems with diffuse value are email accounts, most consumer online banking
# accounts, common cell phones, and most personal computing resources owned and maintained by
# users. (A “user” is anyone whose professional task is something other than the maintenance of the
# system or component. As with safety impact, a “system operator” is anyone who is professionally
# responsible for the proper operation or maintenance of a system.)
# • Concentrated. The system that contains the vulnerable component is rich in resources. Heuristically, such systems are often the direct responsibility of “system operators” rather than users. Examples of concentrated value are database systems, Kerberos servers, web servers hosting login
# pages, and cloud service providers. However, usefulness and uniqueness of the resources on the
# vulnerable system also inform value density. For example, encrypted mobile messaging platforms
# may have concentrated value, not because each phone’s messaging history has a particularly large
# amount of data, but because it is uniquely valuable to law enforcement.

VALUE_DENSITY_1 = SsvcDecisionPoint(
    name="Value Density",
    description="The concentration of value in the target",
    key="VD",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Diffuse",
            key="D",
            description="The system that contains the vulnerable component has limited resources. That is, the resources that the adversary will gain control over with a single exploitation event are relatively small.",
        ),
        SsvcValue(
            name="Concentrated",
            key="C",
            description="The system that contains the vulnerable component is rich in resources. Heuristically, such systems are often the direct responsibility of “system operators” rather than users.",
        ),
    ],
)


def main():
    print(VALUE_DENSITY_1.to_json(indent=2))


if __name__ == "__main__":
    main()
