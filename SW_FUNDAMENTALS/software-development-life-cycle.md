#   Table of Contents
- [Table of Contents](#table-of-contents)
- [Software Development Lifecycle](#software-development-lifecycle)
  - [SDLC - An overview](#sdlc---an-overview)
  - [Requirements and Analysis](#requirements-and-analysis)
  - [Design](#design)
  - [Implementation](#implementation)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Maintenance](#maintenance)
- [Waterfall Software Development](#waterfall-software-development)
- [Agile Software Development](#agile-software-development)
  - [Agile Manifesto](#agile-manifesto)
  - [Agile Methods](#agile-methods)
    - [Agile Scrum](#agile-scrum)
    - [Lean](#lean)
    - [Extreme Programming (XP)](#extreme-programming-xp)
    - [Feature-Driven Development](#feature-driven-development)
- [Agile Components](#agile-components)
  - [Sprints](#sprints)
  - [Backlog](#backlog)
  - [User Stories](#user-stories)
  - [Scrum Teams](#scrum-teams)
- [Lean Software Development](#lean-software-development)
  - [Eliminate Waste](#eliminate-waste)

#   Software Development Lifecycle

##  SDLC - An overview
* Requirements and Analysis
* Design
* Implementation
* Testing
* Deployment
* Maintenance

Originally - just waterfall implemented this correctly

While waterfall was originally performed, things barely worked as planned. Agile looks to resolve this.

##  Requirements and Analysis
Product Owner and Team Members
* Stakeholder discovery
  * What are their challenges?
    * How are they resolving them now?
    * What can we do better
  * Risk tolerance?
  * Other constraints
* Scoping
  * What features?
  * Platforms?
  * How many users?
  * Software and platform integration
  * Scale

Deliverables: Requirements documents

In Waterfall
* ROE
* Meeting schedule
* Payment
* How will software be delivered?

In Agile
* User Stories
* Project-wide documents

##  Design

Deliverables:
* UML Diagrams
  * High-level design
  * Low-level design

##  Implementation
Deliverables:
* Code produced
* Testing plan
* TDD - testing before any code is written

##  Testing
Developers have learned not to aim for perfection, but that code should be easily testable and observable.

CI/CD pipeline may build, deploy, and test the product on a daily or more frequent rate

Deliverables:
* Tests and results
  * Integration testing
  * Unit testing
  * Security testing
  * Performance testing

##  Deployment
Software installed in production. 

Final piece of software is released to customers and other end users. 

**DevOps** 
* Focuses an automating deployment, updating, scaling, etc. very early
* Further automates configuration and deployment of all types environments

## Maintenance
At the conclusion, team prepares to begin the process again for the newest software version.

Agile teams do this in much, much shorter sprints.


Deliverables:
* Provide support
* Fix bugs in production
* Work on improvements
* New customer requests

# Waterfall Software Development

One phase directly follows the other, and can never revert.

Popularized by Winston Royce in 1970. 

Contained seven phases
* System Requirements
* Software Requirements
* Analysis
* Program Design
* Coding
* Testing
* Operations

Pros:
* Works well for already-known requirements (gov't bids)
* Easiest to explain to external parties

Cons:
* Changes in requirements can very easily balloon costs
* Documentation must be generated after each phase

# Agile Software Development
Was not official until 2001, even though similar models were being practiced


## Agile Manifesto
* Customer Focus
  * Satisfy through early and continuous delivery of working software
* Embrace Change and Adapt
  * Welcome changing requirements, even late in development
  * Focus on improving competitive advantage
* Frequent Delivery of Working Software
  * Deliver frequently to get feedback and redirection
  * Additional learnings
  * Features can be adjusted
* Collaboration
  * Businesspeople and developers should work together throughout
* Motivated Teams
  * Build projects around motivated individuals
  * Give them the environment, trust, and support they need to get work done.
* Face-to-face Conversations
  * Most effective way to convey information is a face-to-face conversation
* Working Software
  * Measures progress
* Work at a Sustainable Pace
  * Sponsors, developers, and users should be able to maintain a constant pace indefinitely
* Agile Environment
  * Continuous attention to technical excellence and good design
* Simplicity
  * Simplicity is defined as the 'art of maximizing work not done'
* Self-Organizing Teams
  * Self-Organizing teams produce best deliverables.
* Continuous Improvement
  * At regular intervals
  * Reflect on how to change & adjust accordingly

## Agile Methods
The manifesto articulated many of the goals, characteristics, and best practices that the authors deemed essential

However, manifesto was not prescriptive as to how agile should work.

These authors embraced best-practices from front-line software developers, and from other disciplines. Specifically, from process engineering innovations developed in the Japanese automotive industry.

Due to this evolution, many takes on agile have emerged and become widely popular.

### Agile Scrum
* Formulated in the mid-80s by Hirotaka Takeuchi and Ikujiro Nonaka
* Popularized by Ken Schwaber, Jeff Surtherland, etc
* Focus - small, self-organizing teams that meet daily for a short time and work in sprints
* Allows for constantly adapting deliverables for changing requirements
* Scrum says little about engineering specifics
  * Not specific to software development

### Lean
Focus 
* Elimination of wasted effort in planning and execution
* Reduction of programmer cognitive load

### Extreme Programming (XP)
Compared with Scrum, XP is more prescriptive about best-practices
* Deliberately addresses quality-of-life issues facing development teams
* Twelve core practices for improving productivity
* Won't be discussed much, but will examine many of its ideas

### Feature-Driven Development
* Software should proceed in terms of a model and then
  * Broken out
  * Planned
  * Designed
  * Built feature-by-feature

Scrum has been defined as fundamental and most widely adopted of the above methodologies.


# Agile Components
## Sprints
Software Development Life Cycle still applies, in smaller intervals.
* Agile is many quick iterations of the SDLC
* Quick iterations called springs
  * Purpose - accomplish frequent delivery of software
* Duration
  * Between 2-4 weeks
  * Preferably as short as possible
  * Determined before the process begins and should rarely change
* Each team takes on as many user stories as they feel they can accomplish during the sprint
* When sprint has lapsed, software should be working and deliverable, even if it's not delivered

## Backlog
* Created by Product Owner
* Made up of all features for the software in prioritized list
* Created as part of Requirements and Analysis phase
* Not all features will be in immediate release
* New features can be added at any time
* Reprioritized with customer feedback

## User Stories
When feature gets close to the top - broken down into smaller tasks.

These tasks are called `user stories`

Cisco suggested template:

`As a <user or role>, I would like to <action>, so that <value or benefit>`

To complete a story, requires completing all phases of the SDLC. 
* Story itself should have requirements
* Team taking on story performs
  * Design
  * Implementation
  * Testing

## Scrum Teams
Comprised of different people with different roles to complete full SDLC

Scrum teams are:
* Cross-functional
* Collaborative
* Self-managed
* Self-empowered

Whole team is held accountable for completion of the story, even if individual has completed their own tasks.

Teams should be no larger than 10 individuals, but large enough to finish a story within a sprint.

**Daily Standup**
* Daily meeting that lasts no longer than 15 minutes
* Keeps all members in sync with progress and difficulties
* Scrum Master facilitates standups, and reports on and helps to remove obstacles.

# Lean Software Development
Based on lean manufacturing principles
* Focus - reducing waste and maximizing customer value

**Lean Principles**
* Eliminate Waste
* Amplify Learning
* Decide as Late as possible
* Decide as Fast as possible
* Empower the team
* Build integrity in
* Optimize the whole

## Eliminate Waste
Waste - anything that does not add value for customer

**Seven Wastes of Software Development**
* Partially Done Work
  * No customer value
  * Time spent doing this work could have been used to provide value
  * Not maintained - obsoleted easily
* Extra Processes
  * Bunch of paperwork
  * Useless and Unnecessary
* Extra Features
  * If the customer doesn't want it, YAGNI
  * Build exactly what customer wants to avoid obselete features
* Task Switching
  * Waste of time.
  * Avoid assigning to multiple projects
  * More efficient to do tasks synchronously
  * Context switching is a massive effort
* Waiting
  * Delays. All I need to say.
  * **Examples**
    * Starting the project
    * Getting right staff
    * Getting requirements from customer
    * Approvals
    * Getting Answers
    * Making Decisions
    * Implementation
    * Testing
* Motion
  * Motion for people
    * People need to walk away to ask a question and collaborate
    * Task switching time, and moving time
  * Motion of Artifacts
    * Documents or code moved from one person to another
    * Document does not contain all information for the next
      * Need to gather information again
      * Handoff may require time
* Defects
  * Impact of the defect
  * Can snowball with other features
    * Time to debug is a waste
  * Value for customer is reduced when issues occur