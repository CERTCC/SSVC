# Dryad 
Stakeholder-Specific Vulnerability Categorization Calculator

Dryad is a SSVC calculator app that guides you through the simple steps needed in making
a vulnerability priority decision.  The result of applying SSVC is a priority decision,
providing yuo with a recommended action. See the demo in our [SSVC calc website](https://democert.org/ssvc/)

Some examples of actions are 
defer, scheduled, out-of-band, and immediate.

* To explore the decision tree, use the button "Show Full Tree" This will show all the branches, nodes and edges that make up the decision tree.
* There are also a number of sample CVE in a dropdown that will auto-select a number of steps in the decision tree
* Use the "Start Decision" to navigate the tree for assesing your prioritization for a vulnerability.
* You can also import custom decision trees and custom CVE samples for the current decision tree.
* Custom decision trees can be from JSON see example [sample-ssvc.json](./sample-ssvc.json) and the JSON schema file [SSVC_JSON_2.0_min.schema.json](./SSVC_JSON_2.0_min.schema.json)
* Customer decision tree can also be just a text file tab-delimited as in [ssvc.txt](./ssvc.txt) OR [ssvc.tsv](./ssvc.tsv)
* CVE samples files [sample-ssvc-scores.txt](./sample-ssvc-scores.txt) shows a tab-delimited 

