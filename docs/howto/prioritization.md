# Prioritization

Given a specific stakeholder decision and set of useful decision points, we are now in a position to combine them into a comprehensive set of decisions about the priority with which to act.
The definition of choices can take a logical form, such as:
 - IF
 - ([*Exploitation*](#exploitation) IS [PoC](#exploitation)) AND
 - ([*Exposure*](#exposure) IS [controlled](#exploitation)) AND
 - ([*Automatable*](#automatable) IS [no](#automatable)) AND
 - ([*Human Impact*](#human-impact) IS [medium](#human-impact))
 - THEN priority is *scheduled*.

This example logical statement is captured in (line 35 of the deployer `.csv` file)[https://github.com/CERTCC/SSVC/blob/main/data/csvs/deployer-options.csv#L35].

There are different formats for capturing these prioritization decisions depending on how and where they are going to be used.
In this paper, we primarily represent a full set of guidance on how one stakeholder will make a decision as a **decision tree**.
This section presents example trees for each stakeholder: supplier, deployer, and coordinator.
This section also provides some guidance on how to [construct and customize a decision tree](#tree-construction-and-customization-guidance) and [gather evidence](#evidence-gathering-guidance) to make decisions.
How this decision information might be stored or communicated is the topic of subsections on [Asset Management](#relationship-to-asset-management) and [Communication](#guidance-on-communicating-results).

