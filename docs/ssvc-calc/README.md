# Dryad

Stakeholder-Specific Vulnerability Categorization Calculator

Dryad is a SSVC calculator app that guides you through the simple steps needed in making
a vulnerability priority decision.  The result of applying SSVC is a priority decision,
providing you with a recommended action. See the demo in our [SSVC calc website](https://democert.org/ssvc/)

Some examples of actions are
defer, scheduled, out-of-cycle, and immediate.

- The top drop-down allows you to select from multiple decision trees that map to an appropriate Role in SSVC.
- To explore the decision tree, use the button "Show Full Tree" This will show all the branches, nodes and edges that make up the decision tree. A small zoom control horizontal range slider that can help with very large decision trees.
- A drop-down allows you to move from Graphic mode to Simple mode.
- There are also a number of sample CVE in a dropdown that will auto-select a number of steps in the decision tree
- Use the "Start Decision" to navigate the tree for assesing your prioritization for a vulnerability.
- You can also import custom decision trees and custom CVE samples for the current decision tree.
- There is a [data](../data/) folder where there is a number of examples both of schema and examples of exported outputs.
- You can install this directory as a folder in your public website directory. and expose it. All referenced url's are relative in the scripts and HTML files.
