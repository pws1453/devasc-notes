#   Code Review
Goal: Make code that is reliable, standardized, and well-documented

##  Why?
Team
* Tranfer of knowledge between team members
* Find bugs
* Refine working code

Author
* Get input from reviewers
* Implement standard code-style
* Learn from review - especially if reviewed by more senior developer

##  Types of Code Reviews

*   Formal Code Review
*   Change-based Code Review
*   Over-the-Shoulder Code Review
*   Email Pass-Around

### Formal Code Review - Fagan Inspection
*   Series of meetings to review whole codebase
*   Promotes discussion between reviewers
*   Often used for cryptosystems and other critical infra
*   Reviewers may reach consensus
    *   Better Feedback
*   All details of the meeting are documented
*   Common for waterfall-based projects
*   Modern Adaptation - review only code changes

### Change-Based Code Review - Tool-Assisted Code Review
*   Reviews code changed due to
    *   User Stories
    *   Features
    *   Bug fixes
    *   Commmits
*   Often uses tools like git to review changes
*   Review performed independently
*   Determine actual changes for many reviewers

### Over-the-Shoulder Code Review
*   Pair programming, but reviews
*   One dev looks over the shoulder of another
    *   Only one reviewer
*   Reviewer can discuss with developer in real-time

### Email Pass-Around
* Source Code Management systems send automatic emails
  * Developers can review code checked in