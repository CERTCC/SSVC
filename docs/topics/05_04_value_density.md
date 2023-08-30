## Value Density

[*Value Density*](#value-density) is described as *diffuse* or *concentrated* based on the resources that the adversary will gain control over with a single exploitation event:

  - [*diffuse*](#value-density): The system that contains the vulnerable component has
    limited resources. That is, the resources that the adversary will
    gain control over with a single exploitation event are relatively
    small. Examples of systems with diffuse value are email accounts,
    most consumer online banking accounts, common cell phones, and most
    personal computing resources owned and maintained by users. (A
    “user” is anyone whose professional task is something other than
    the maintenance of the system or component. As with [*Safety Impact*](#safety-impact),
    a “system operator” is anyone who is professionally responsible for
    the proper operation or maintenance of a system.)

  - [*concentrated*](#value-density): The system that contains the vulnerable component
    is rich in resources. Heuristically, such systems are often the
    direct responsibility of “system operators” rather than users.
    Examples of concentrated value are database systems, Kerberos
    servers, web servers hosting login pages, and cloud service
    providers. However, usefulness and uniqueness of the resources on
    the vulnerable system also inform value density. For example,
    encrypted mobile messaging platforms may have concentrated value,
    not because each phone’s messaging history has a particularly large
    amount of data, but because it is uniquely valuable to law
    enforcement.

### Gathering Information About Value Density

The heuristics presented in the [*Value Density*](#value-density) definitions involve whether the system is usually maintained by a dedicated professional, although we have noted some exceptions (such as encrypted mobile messaging applications).
If there are additional counterexamples to this heuristic, please describe them and the reasoning why the system should have the alternative decision value in an issue on the [SSVC GitHub](https://github.com/CERTCC/SSVC/issues).

An analyst might use market research reports or Internet telemetry data to assess an unfamiliar product.
Organizations such as Gartner produce research on the market position and product comparisons for a large variety of systems.
These generally identify how a product is deployed, used, and maintained.
An organization's own marketing materials are a less reliable indicator of how a product is used, or at least how the organization expects it to be used.

Network telemetry can inform how many instances of a software system are connected to a network.
Such telemetry is most reliable for the supplier of the software, especially if software licenses are purchased and checked.
Measuring how many instances of a system are in operation is useful, but having more instances does not mean that the software is a densely valuable target.
However, market penetration greater than approximately 75% generally means that the product uniquely serves a particular market segment or purpose.
This line of reasoning is what supports a determination that an ubiquitous encrypted mobile messaging application should be considered to have a [*concentrated*](#value-density) Value Density.
