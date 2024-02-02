---
name: Change Request
about: Propose a Change Request.
title: ''
labels: change request
assignees: ''
---

<!--
Note that text between the HTML comments will be recorded in this issue's source for future editing, but will not render on Github.  So, please delete whatever portion of these comments you do not use.

Also, the Description box of the Issue you file will be edited at one or more points.  At least one edit will be done by a member of the Ontology Committee leadership to add a coordination-steps checklist.  Comment edit history is viewable:
https://docs.github.com/en/communities/moderating-comments-and-conversations/tracking-changes-in-a-comment
-->

# Background

<!--
Give any background you find helpful, if you feel jumping straight to listing requirements might not flow well to a reader.  For instance, if revising a current implementation, explain what that implementation does and why it seems worth changing to you.

It is helpful to at least provide a one-sentence comprehensive answer to the question "What do we achieve for whom and why does that matter?"
-->


# Requirements

<!--Please provide one requirement per subsection.  (The use of sections is for linking to headers on Github.)-->


## Requirement 1


## Requirement 2


# Risk / Benefit analysis


## Benefits


## Risks

<!--
If no risks are known, "The submitter is unaware of risks associated with this change" might suffice.

Risks should include consequences for CDO resources (ontologies, documentation, and/or tooling) resulting from this Change Request.  Consequences can relate to impediments or degradations to functionality, interoperability, reliability, usability, efficiency, maintainability or portability.

As risks are identified (e.g. as implementation-testing might reveal), they will be added to this section.
-->


# Competencies demonstrated

<!--
Please describe at least one enabled or upgraded competency, e.g. a competency question (CQ) you can answer with this proposal that you couldn't answer before. Probably, in order to show how the resulting answer emerges, some narrative or scenario is required to be described. As a minimum, describe the questions and resulting answers in English; optionally, include a SPARQL query or a link to a functioning draft implementation of this proposal that includes a SPARQL query.

Please do consider a scenario that can have ground truth positive and ground truth negative encoded for implementation testing.  For instance, a scenario for CASE that exercises the uco-action:instrument property could be "Three picture files were produced on an analyst's workstation over the course of an investigation."  A competency question for this scenario could be "Which picture files were taken from the evidence, vs. taken of the evidence?"  The results would be "From reviewing the investigative actions in the chain of custody, picture files generated when the instrument was the analyst's camera would be 'taken of', while picture files generated when the instrument was a data extraction kiosk would be 'taken from.'"
-->


## Competency 1

<!--
Include competency narrative or scenario text here, as the preamble to the questions.
-->


### Competency Question 1.1


#### Result 1.1


### Competency Question 1.2

<!--
One scenario setup can fuel multiple questions.  To help with linking on Github, please use section numbering.
-->


#### Result 1.2


# Solution suggestion

<!--
If possible, please summarize the concrete steps to take to satisfy the requirements, e.g.:
* Define new property
* Add unit test showing potential errors in property usage and how to avoid them

To assist with voting, the Ontology Committee should see a summary of intended changes as early as possible.  Please do summarize steps and effects, even if a Pull Request accompanies the Issue.  Discovery of effects from implementation review can lead to disruption in the committee review flow.

Some requirements are narrow enough they could be considered "Self-documenting."  One way to estimate if this is true is if a lone Git commit could have the requirement as a title, have no further message text, and be comprehensible.  In such cases, the following text could be used (though please cut the leading "> " if this line is used):

> Requirement 1 also fully describes the solution, implemented in [PR X](https://github.com/ucoProject/UCO/pull/X).

If there is an accompanying pull request, please do link it under the "Development" box on the right of the Issues page.

If example snippets of instance data are provided, please note if you provide permission for the examples to be transcribed to one of the tested example repositories (such as CASE-Examples).  This is a significant aid in confirming examples represent the semantics that the submitter intended.  "I am fine with my examples being transcribed and credited" should be sufficient.
-->
