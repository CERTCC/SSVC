# Guidance on Communicating Results

There are many aspects of SSVC that two parties might want to communicate.
Not every stakeholder will use the decision points to make comparable decisions.
Suppliers and deployers make interdependent decisions, but the actions of one group are not strictly dependent on the other.
Recall that one reason for this is that SSVC is about prioritizing a vulnerability response action in general, not specifically applying a patch that a supplier produced.
Coordinators are particularly interested in facilitating communication because that is their core function.
This section handles three aspects of this challenge: formats for communicating SSVC, how to handle partial or incomplete information, and how to handle information that may change over time.

This section is about communicating SSVC information about a specific vulnerability.
Any stakeholder making a decision on allocating effort should have a decision tree with its decision points and possible values specified already.
[Representation choices](#representation-choices) and [Tree Construction and Customization Guidance](#tree-construction-and-customization-guidance) discussed how SSVC uses a text file as the canonical form of a decision tree; the example trees can be found in [SSVC/data](https://github.com/CERTCC/SSVC/tree/main/data).
This section discusses the situation where one stakeholder, usually a supplier or coordinator, wants to communicate some information about a specific vulnerability to other stakeholders or constituents.

## Communication Formats

We recommend two structured communication formats, abbreviated and full.
The goal of the abbreviated format is to fill a need for providing identifying information about a vulnerability or decision in charts, graphs, and tables. Therefore, the abbreviated format is not designed to stand alone.
The goal of the full format is to capture all the context and details about a decision or work item in a clear and machine-readable way.

### Abbreviated Format

SSVC abbreviated form borrows directly from the CVSS “vector string” notation.
Since the purpose of the abbreviated form is to provide labels for charts and graphics, it does not stand alone.
The basic format for SSVC is:
```
SSVC/(version)/(decision point):(value)[/decision point:value[/decision point:value[...]]][/time]/
```
Where `version` is `v2` if it is based on this current version of the SSVC.
The term `decision point` is one or two letters derived from the name of the decision point as follows:
 - Start with the decision point name as given in [Likely Decision Points and Relevant Data](#likely-decision-points-and-relevant-data).
 - Remove any text in parentheses (and the parentheses themselves).
 - Remove the word “Impact” if it is part of the name.
 - Create an initialism from remaining title-case words (ignore “of,” etc.), taking only the first two words.
 - The first letter of the initialism is upper case; if there is a second letter, then it is lower case.
 - Verify that the initialism is unique among decision points in the version of SSVC. If two initialisms collide, sort their source names equivalent to `LC_ALL=C sort`. The name that sorts first keeps the initialism for which there is a collision. Set the second letter of the initialism to the first character in the name that resolves the collision. If the names were `Threat` and `Threshold`, `T` would be `Threat` and `Ts` would be `Threshold`. We make an effort to design SSVC without such collisions.

For example, [*Technical Impact*](#technical-impact) becomes `T` and [*Public Safety Impact*](#public-safety-impact) becomes `Ps`.

The term `value` is a statement of the value or possible values of the decision point that precedes it and to which it is connected by a colon (`:`).
Similar to `decision point`, `value` should be made up of one or two letters derived from the name of the decision value in the section for its associated decision point.
For example [MEF support crippled](#mission-impact) becomes `Ms` and [efficient](#utility) becomes `E`.
The process is the same as above except that labels for a `value` do not need to be unique to the SSVC version, just unique to the associated `decision point`.

The character `/` separates decision-point:value pairs.
As many pairs should be provided in the abbreviated form as are required to communicate the desired information about the vulnerability or work item.
A vector must contain at least one decision-point:value pair.
The ordering of the pairs should be sorted alphabetically from A to Z by the ASCII characters representing the decision points.
A trailing `/` is used to close the string.

The vector is not tied to a specific decision tree.
It is meant to communicate information in a condensed form.
If priority labels (*defer*, etc.) are connected to a vector, then the decision tree used to reach those decisions should generally be noted.
However, for complex communication, machine-to-machine communication, or long-term storage of SSVC data, the JSON format and schema should be used.

The optional parameter `time` is the date and time of the SSVCv2 record creation as represented in [RFC 3339, section 5.6](https://datatracker.ietf.org/doc/html/rfc3339). This is a subset of the date format also commonly known as ISO8601 format.

Based on this, an example string could be:
```
SSVCv2/Ps:M/T:T/U:E/2018-11-13T20:20:00Z/
```
For a vulnerability with [minimal](#public-safety-impact) [*Public Safety Impact*](#public-safety-impact), [total](#technical-impact) [*Technical Impact*](#technical-impact), and [efficient](#utility) [*Utility*](#utility), which was evaluated on Nov 13,2018 at 8:20 PM UTC.

While these abbreviated format vectors can be uniquely produced based on a properly formatted JSON object, going from abbreviated form to JSON is not supported.
Therefore, JSON is the preferred storage and transmission method.

### Full JSON format

For a more robust, self-contained, machine-readable, we provide JSON schemas.
The [provision schema](https://github.com/CERTCC/SSVC/blob/main/data/schema/SSVC_Provision.schema.json) is equivalent to a decision tree and documents the full set of logical statements that a stakeholder uses to make decisions.
The [computed schema](https://github.com/CERTCC/SSVC/blob/main/data/schema/SSVC_Computed.schema.json) expresses a set of information about a work item or vulnerability at a point in time.
A computed schema should identify the provision schema used, so the options from which the information was computed are specified.

Each element of `choices` should be an object that is a key-value pair of `decision point`:`value`, where the term `decision point` is a string derived from the name of the decision point as follows:
 - Start with the decision point name as given in [Likely Decision Points and Relevant Data](#likely-decision-points-and-relevant-data).
 - Remove any text in parentheses (and the parentheses themselves).
 - Remove colon characters, if any (`:`).
 - Convert the string to [lower camel case](https://en.wikipedia.org/wiki/Camel_case) by lowercasing the string, capitalizing any letter after a space, and removing all spaces.

The `value` term is derived the same way as `decision point` except start with the value name as given in the relevant decision point subsection of [Likely Decision Points and Relevant Data](#likely-decision-points-and-relevant-data).

## Partial or Incomplete Information    

What an analyst knows about a vulnerability may not be complete.
However, the vulnerability management community may still benefit from partial information.
In particular, suppliers and coordinators who might not know everything a deployer knows can still provide benefit to deployers by sharing what partial information they do know.
A second benefit to providing methods for communicating partial information is the reduction of bottlenecks or barriers to information exchange.
A timely partial warning is better than a complete warning that is too late.

The basic guidance is that the analyst should communicate all of the vulnerability's possible states, to the best of the analyst's knowledge.
If the analyst knows nothing, all states are possible.
For example, [*Utility*](#utility) may be [laborious](#utility), [efficient](#utility), or [super effective](#utility).
In abbreviated form, write this as `U:LESe`.
Since a capital letter always indicates a new value, this is unambiguous.

The reason a stakeholder might publish something like `U:LESe` is that it expresses that the analyst thought about [*Utility*](#utility) but does not have anything to communicate.
A stakeholder might have information to communicate about some decision points but not others.
If SSVC uses this format to list the values that are in play for a particular vulnerability, there is no need for a special “I don't know” marker.

The merit in this “list all values” approach emerges when the stakeholder knows that the value for a decision point may be A or B, but not C.
For example, say the analyst knows that [*Value Density*](#value-density) is [diffuse](#value-density) but does not know the value for [*Automatability*](#automatability).
Then the analyst can usefully restrict [*Utility*](#utility) to one of [laborious](#utility) or [efficient](#utility).
In abbreviated form, write this as `U:LE`.
As discussed below, information can change over time.
Partial information may be, but is not required to be, sharpened over time into a precise value for the decision point.

## Information Changes Over Time

Vulnerability management decisions are dynamic, and may change over time as the available information changes.
Information changes are one reason why SSVC decisions should always be timestamped.
SSVC decision points have different temporal properties.
Some, such as [*Utility*](#utility), are mostly static.
For [*Utility*](#utility) to change, the market penetration or deployment norms of a vulnerable component would have to meaningfully change.
Some, such as [*State of Exploitation*](#state-of-exploitation), may change quickly but only in one direction.

Both of these examples are out of the direct control of the vulnerability manager.
Some, such as [*Exposure*](#exposure), change mostly due to actions taken by the organization managing the vulnerable component.
If the actor who can usually trigger a relevant change is the organization using SSVC, then it is relatively straightforward to know when to update the SSVC decision.
That is, the organization should reevaluate the decision when they make a relevant change.
For those decision points that are about topics outside the control of the organization using SSVC, then the organization should occasionally poll their information sources for changes.
The cadence or rate of polls is different for each decision point, based on the expected rate of change.

We expect that updating information over time will be most useful where the evidence-gathering process can be automated.
Organizations that have mature asset management systems will also find this update process more efficient than those that do not.
For an organization without a mature asset management system, we would recommend putting organizational resources into maturing that function before putting effort into regular updates to vulnerability prioritization decision points.

The following decision points are usually out of the control of the organization running SSVC.
As an initial heuristic, we suggest the associated polling frequency for each.
These frequencies can be customized, as the update frequency is directly related to the organization's tolerance for the risk that the information is out of date.
As discussed in [Tree Construction and Customization Guidance](#tree-construction-and-customization-guidance), risk tolerance is unique to each organization.
Risk tolerance and risk appetite are primarily reflected in the priority labels (that is, decisions) encoded in the SSVC decision tree, but information polling frequency is also a risk tolerance decision and each organization may choose different time values.
 - [*Exploitation*](#exploitation): every 1 day
 - [*Technical Impact*](#technical-impact): never (should be static per vulnerability)
 - [*Utility*](#utility): every 6 months
 - [*Public Safety Impact*](#public-safety-impact): every 1 year

The following decision points are usually in the control of the organization running SSVC and should be reevaluated when a relevant change is made or during annual reviews of assets.

 - [*Situated Safety Impact*](#situated-safety-impact)
 - [*Mission Impact*](#mission-impact)
 - [*System Exposure*](#system-exposure)

If SSVC information is all timestamped appropriately (as discussed earlier in this section), then an analyst can compare the timestamp to the current date and determine whether information is considered stale.
The above rates are heuristic suggestions, and organizations may choose different ones.
Any public repository of vulnerability information should keep a change log of when values change for each decision point, for each vulnerability.
Vulnerability response analysts should keep such change logs as well.
Similar to logging practices recommended for incident response [@nist800-61r2], such practices make the process less error-prone and facilitate after-action reviews.
