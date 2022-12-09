In "rules.txt" is defined a set of rules.

For each line:

- First, there is the date of start or end of the rule.
- Then, the name of the rule.
- Then, the charachter 'S' or 'E' meaning the rule 'S'tarted or 'E'nded.

A rule might not have an end, meaning it is currently active.

The entire file shall be coherent (a rule cannot end before it started).
If a rule is not coherent, then print an error message and invert start and end.

Given a date, the program shall print all the rules active in that date
(meaning: they started, but they did not finish yet)