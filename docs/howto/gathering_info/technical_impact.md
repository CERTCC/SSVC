# Gathering Information About Technical Impact

Assessing *Technical Impact* amounts to assessing the degree of control over the vulnerable component the attacker stands to gain by exploiting the vulnerability.
One way to approach this analysis is to ask whether the control gained is *total* or not.
If it is not total, it is *partial*.
If an answer to one of the following questions is _yes_, then control is *total*.
After exploiting the vulnerability,

- can the attacker install and run arbitrary software?
- can the attacker trigger all the actions that the vulnerable component can perform?
- does the attacker get an account with full privileges to the vulnerable component (administrator or root user accounts, for example)?

This list is an evolving set of heuristics.
If you find a vulnerability that should have *total* *Technical Impact* but that does not answer yes to any of 
these questions, please describe the example and what question we might add to this list in an issue on the
[SSVC GitHub](https://github.com/CERTCC/SSVC/issues).
