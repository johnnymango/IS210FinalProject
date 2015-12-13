================================
Priorities, Resources & Projects
================================

Many organizations require a high level understanding of project priorities
and their resources to determine what objectives can be met and which cannot.
One way to understand what is possible starts by looking at resource
availability (how much time a resource has to work on any given project) and
project assignments (who is assigned to which projects). The models used to
calculate the relationship between work and resources varies but many rely on
a basic concept: there cannot be more work performed than there are people or
time to perform it.

The PRP python module applies the basic calculation of (resource x hours) /
priorities to determine what work can and cannot be accomplished given a set
of inputs by the various stakeholders in this paradigm.

Personas
========

These personas constitute the four typical actors in the negotiation between
time, resources, priorities and projects. These actors are commonly found in
traditional project management techniques - but since this module performs
only a base calculation, it can easily be adjusted to include actors in Agile
techniques like "product owner" or "scrum master".

Executive Sponsor
-----------------

Carol - Vice President of Information Technology

Details
^^^^^^^

As an executive officer of the company in charge to the technology arm of the
organization, Carol works closely with other Executives to identify the
organization's priorities and authorizes projects.  She then passes down these
priorities and projects to her team for execution.

Goals
^^^^^

Carol needs to know at the highest level which priorities can realistically
be achieved given the resources at her disposal so she can take the
appropriate action.  For example, if a priority project cannot be achieved if
there are not enough resource hours to finish it, Carol may decide to re-
prioritize projects, or hire new resources, or negotiate with Resource Manager
and Project Manager to allocate more hours at the expense of others.  She
reports the state of these priorities back to other Executives.

Resource Manager
----------------

Andrew - Associate Director of Application Development

Details
^^^^^^^

As Associate Director of Application Development, Andrew is responsible for a
team of developers.  More importantly, he is responsible for determining a
team member's availability to perform work over a period of time. He is
ultimately wants to ensure that there are enough resource hours available to
accomplish the work requested and need to know where adjustments are necessary
to meet demand.

Goals
^^^^^

Andrew needs an exact understanding of what resources are available. Based on
resource availability, decisions about project assignments can be made. For
example, Andrew may determine that a team member is available for 50 hours
over a particular stretch of time. The resource manager will communicate this
availability to the Project Manager who will begin assigning the resource and
hours to individual projects.  The combination of availability and
assignments may require the Resource Manager to make adjustments to
availability.  The Project Manager may allocate 60 hours-worth of assignments.
Andrew may decide to approve the additional 10 hours or may inform the
Project Manager that the resource has no additional availability due to
vacation. The Resource Manager needs to know when assignments exceed
availability to make the best decisions about the resource.

Project Manager
---------------

Mike - Project Manager

Details
^^^^^^^

As Project Manager, Mike is responsible for assigning resources to projects.
He determines how many hours of works are needed from each resource to
complete projects. Every assignment reduces the resource's availability.

Goals
^^^^^

The goal of the project manager is to marry resources to projects.  More
importantly, Mike needs to verify that there are adequate hours available for
each resource to complete the project in the priority order in which the
project that needs to be delivered.  Beyond this, the Project Manager needs
to know when assignments exceed availability. Using our example above, the 10
hour difference for a particular team member may trigger negotiations about
the project with the Resource Manager or Executive Sponsor; perhaps the
project will need to take longer to accommodate the difference, or perhaps
the size and scope of the work needs to be reduced down to 50 hours-worth of
work by removing features or functionality.

Team Member
-----------

Laura - Application Developer

Details
^^^^^^^

Team members at an organization can be resources assigned to
projects.  Laura, as a project resource, needs to know her assignments.
However, since Laura has various other responsibilities and obligations that
come up and may not be accounted for in the availability estimated by the
Resource, she needs to ensure her assignments accurately reflect her actual
availability so she can realistically complete that is asked of her.

Goals
^^^^^

As a team member, Laura is expected to perform the work assigned to her.
Laura needs to know what these assignments are so she can plan accordingly.
More importantly, she needs to communicate adjustments to her
availability (which, in turn, may affect her assignments) to the Resource
Manager.  For example, Andrew may estimate Laura's total availability over
several weeks or months.  Andrew may account for all known factors that
affect Laura's availability over that period of time.  However, Laura may
decide to take several vacation days, or may need to take a personal day to
visit the doctor, or attend a three-day conference in another state where she
will not be able to work on her assignments.

Problem Scenarios
=================

The underlying issue with the problems for each persona is that each provides
input into the calculation but requires the information from the other
personas to make decisions about the things that are important to each persona.

Unmet Priorities
----------------

Carol, as the Executive Sponsor am VP of Information Technology cannot see
how many priorities can be completed by her team before she runs out of
resources and hours to complete them.  Without this information, there is a
risk that she will be unable to meet the priorities set by the organization.

Current Alternatives
^^^^^^^^^^^^^^^^^^^^

Carol is making subjective assessments of IT's ability to deliver the
priorities by meeting with teams and managers.  While this gives her a
general indication of what "may" be feasible, it does not show how where
exactly the line between reality and wishful thinking appears.

Value Proposition
^^^^^^^^^^^^^^^^^

Carol's input helps to organize the other inputs so that a point where unmet
priorities can be identified.  A report indicating which priorities can be
staffed and which cannot would be ideal.

Over-assigned Resources
-----------------------

Andrew, as the Resource Manager needs to identify when resources are
assigned for more hours than they have available.  An over-assigned resource
that remains unidentified creates problems for the resource and the project.

Current Alternatives
^^^^^^^^^^^^^^^^^^^^

Andrew is making adhoc adjustments to resource availability by meeting with
teams and managers.  While this allows him to make adjustments, this often
leads to a situation where he cannot anticipate when a resource may be
over-assigned.  This can negatively affect the resource and projects.

Value Proposition
^^^^^^^^^^^^^^^^^

Andrew's input creates the boundary of work for each resource.  A report that
identifies when the boundary has been breached would be ideal.


Under-staffed project
---------------------

Mike, as the Project Manager, needs to identify when a resource is needed
for more work than what he/she is available to work.  A project that is
under-staffed (defined here by not having the estimated resource hours
necessary to complete the work) can delay or derail the project.

Current Alternatives
^^^^^^^^^^^^^^^^^^^^

Mike is adjusting assignments by meeting with teams members and negotiating
with managers.  While this allows him to make adjustments, this often
leads to a situation where he cannot anticipate when a project may be
understaffed and plan accordingly.

Value Proposition
^^^^^^^^^^^^^^^^^

Mike's input creates the relationship between projects and resources.  A
report that identifies when a project can't be completed due to a lack of
resources would be help Mike better staff the projects.

Unhappy Team Member
-------------------

Laura, as a Team Member being assigned as a resource to projects needs to
know her assignments to plan accordingly.  Being over-assigned creates stress
and a loss of productivity as Laura attempts to fit in more work than there
is time to complete it.

Current Alternatives
^^^^^^^^^^^^^^^^^^^^

Laura is negotiating work with team members when she over-assigned. While she
may be able to accommodate the occasional over-assignment, the frequency of
this situation leaves her unable to plan properly negatively affecting her
employment and the projects.

Value Proposition
^^^^^^^^^^^^^^^^^

The resource is the cornerstone of the priorities and project relationship. A
resource that can view their assignments and identify potential assignment
conflicts helps keep the team member happy and productive. A report that lists
these assignments and identifies over-assignment helps the resource make
planning decisions.

User Stories
============

Executive Priorities Input & Report
-----------------------------------

As an Executive Sponsor, I want to input the project list and assign each
project a priority so that the rest of the organization can assign resources and
work on projects based on this prioritization.

As an Executive Sponsor, I want to generate a report that identifies which
priorities cannot be met so that the Executive team can continue to make
adjustments to priorities and staffing.

Acceptance Stories
^^^^^^^^^^^^^^^^^^

Scenario 1: The priority and project list input
```````````````````````````````````````````````
::

    Given that I can list projects and their priorities
    When I enter the data in a CSV file
        And I run the module
    Then the data is added to a dictionary for use by the other resources
        And available for my report.

Scenario 2: The Executive report
````````````````````````````````
::

    Given the priority and project list has been processed by the module
        And the resource availability data has been processed by the module
        And the project assignment data as been processed by the module
        And the team member data has been processed by the module
    When I run the Executive Report function
    Then a report is generated which lists the projects that cannot be
    completed due to availability and assignment.

Resource Manager Availability Input & Report
--------------------------------------------

As Resource Manager, I want to input the list of resources and their
estimated availability so that they can be assigned to projects.

As a Resource Manager, I want to generate a report that identifies when a
resource has more work assigned than hours available to perform the work so
that I can make adjustments to the availability.

Acceptance Stories
^^^^^^^^^^^^^^^^^^

Scenario 1: The resource input
``````````````````````````````
::

    Given that I can list the resources and their availability
    When I enter the data in a CSV file
        And I run the module
    Then the data is added to a dictionary for use by the other resources
        And available for my report.

Scenario 2: The Resource Manager report
```````````````````````````````````````
::

    Given the priority and project list has been processed by the module
        And the resource availability data has been processed by the module
        And the project assignment data as been processed by the module
        And the team member data has been processed by the module
    When I run the Resource Manager Report function
    Then a report is generated which identifies the resources that are
    over-assigned.


Project Manager Assignments & Report
------------------------------------

As Project Manager, I want to input the list of projects, their resources and
the number of hours assigned for that project and resource so that project work
can be completed.

As a Project Manager, I want to generate a report that identifies when a project
requires more hours than currently available to the assigned resource
so that I can make adjustments to the project.

Acceptance Stories
^^^^^^^^^^^^^^^^^^

Scenario 1: The assignment input
````````````````````````````````
::

    Given that I can list projects, their resources and the hours needed for
    each resource to complete the work
    When I enter the data in a CSV file
        And I run the module
    Then the data is added to a dictionary for use by the other resources
        And available for my report.

Scenario 2: The Project Manager report
``````````````````````````````````````
::

    Given the priority and project list has been processed by the module
        And the resource availability data has been processed by the module
        And the project assignment data as been processed by the module
        And the team member data has been processed by the module
    When I run the Project Manager Report function
    Then a report is generated which lists the projects which are understaffed.



Team Member Availability & Report
---------------------------------

As a Team Member, I want to input the additional adjustment (hours and
reason) to my estimated availability so that I can be properly assigned to
projects.

As a Team Member, I want to generate a report that lists my assignments which
identifies over-assignments so that I can make adjustments to my availability.

Acceptance Stories
^^^^^^^^^^^^^^^^^^

Scenario 1: The team member input
`````````````````````````````````
::

    Given that I can enter an adjustment to my availability (in hours)
        And enter a reason for the adjustment
    When I enter the data in a CSV file
        And I run the module
    Then the data is added to a dictionary for use by the other resources
        And available to for my report.

Scenario 2: The Team Member report
``````````````````````````````````
::

    Given the priority and project list has been processed by the module
        And the resource availability data has been processed by the module
        And the project assignment data as been processed by the module
        And the team member data has been processed by the module
    When I run the Team Member Report function
    Then a report is generated which lists my assignments
        and identifies projects where I am over-assigned.

