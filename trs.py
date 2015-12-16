#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tasks, Resources and Status."""

import csv


# This section reads the task assignments CSV file and converts to dictionary.
TASKFILE = open('task_assignments.csv')
READER = csv.reader(TASKFILE)

TASKS = {}
for row in READER:
    k = row[0]
    TASKS[k] = row[1]

TASKFILE.close()

# This section reads the Resource Manager CSV file and converts to dictionary.
RESOURCEFILE = open('resourcemanager.csv')
READER = csv.reader(RESOURCEFILE)

ESTIMATED_AVAILABILITY = {}
for row in READER:
    k = row[0]
    ESTIMATED_AVAILABILITY[k] = row[1]

RESOURCEFILE.close()

# This section reads the Project Manager CSV file and converts to dictionary.
PROJECTFILE = open('projectmanager.csv')
READER = csv.reader(PROJECTFILE)

TASKHOURS_ASSIGNMENTS = {}
for row in READER:
    k = row[0]
    TASKHOURS_ASSIGNMENTS[k] = row[1]

PROJECTFILE.close()

# This section reads the Team Member CSV file and converts to dictionary.
MEMBERFILE = open('teammember.csv')
READER = csv.reader(MEMBERFILE)

TIME_OFF = {}
for row in READER:
    k = row[0]
    TIME_OFF[k] = row[1]

MEMBERFILE.close()

# This section calculates values and merges dictionary for report functions.

ACTUAL_AVAILABILITY = {
    key: int(ESTIMATED_AVAILABILITY[key]) - int(TIME_OFF.get(key, 0))
    for key in ESTIMATED_AVAILABILITY.keys()}

REMAINING_AVAILABILITY = {
    key: int(ACTUAL_AVAILABILITY[key]) - int(TASKHOURS_ASSIGNMENTS.get(key, 0))
    for key in ACTUAL_AVAILABILITY.keys()}

DICTS = [TASKS, ESTIMATED_AVAILABILITY, TIME_OFF, ACTUAL_AVAILABILITY,
         TASKHOURS_ASSIGNMENTS, REMAINING_AVAILABILITY]
STAFFING = {}
for k in TASKS.iterkeys():
    STAFFING[k] = list(STAFFING[k] for STAFFING in DICTS)


def task_summary(status):
    """This function generates report for 'Green', 'Yellow' & 'Red' statuses.

    Args:
        status(str): 'Green' for tasks that are adequately staffed. 'Yellow' for
        for tasks that are at capacity. 'Red' for tasks that need attention.

    Returns:
        String: A formatted string.

    Examples:
        >>> task_summary('Red')

            -------------------------------------------------------------
            Task: Install New App Servers
            Assigned to: Sneezy
            This task is understaffed by 250 hours.

            -------------------------------------------------------------
            Task: Install New Routers
            Assigned to: Grumpy
            This task is understaffed by 300 hours.

            -------------------------------------------------------------
            Task: Plan Mid Year Conference
            Assigned to: Happy
            This task is understaffed by 60 hours.
    """
    if status == 'Red':
        understaffed = {key: value for key, value in STAFFING.items()
                        if value[5] < 0}
        for key in understaffed.iterkeys():
            staffing_report = """
            -----
            Task: {task}
            Assigned to: {name}
            This task is understaffed by {hr} hours.
            """.format(task=understaffed[key][0], name=key,
                       hr=abs(understaffed[key][5]))
            print staffing_report

    if status == 'Green':
        ontrack = {key: value for key, value in STAFFING.items()
                   if value[5] > 0}
        for key in ontrack.iterkeys():
            staffing_report = """
            -------------------------------------------------------------
            Task: {task}
            Assigned to: {name}
            {name} is only using {ha} hours of the {aa} hours available.
            """.format(task=ontrack[key][0], name=key, ha=ontrack[key][4],
                       aa=ontrack[key][3])
            print staffing_report

    if status == 'Yellow':
        watch = {key: value for key, value in STAFFING.items() if value[5] == 0}
        for key in watch.keys():
            staffing_report = """
            -----
            Task: {task}
            Assigned to: {name}
            {name} has {hr} hours of availability.  Do not assign more tasks!
            """.format(task=watch[key][0], name=key, hr=abs(watch[key][5]))
            print staffing_report


def resource_rpt(name):
    """This function generates a resource report.

    Args:
        name(str): The name of a resource.

    Returns:
        String: A formatted string.

    Examples:
    >>> resource_rpt('Grumpy')
    ALERT: The resource does not have enough availability to complete the task!

        Resource Report For: Grumpy
        ---------------------------------
        Estimated Availability: 160 hours
        Time Off: 160 hours
        Actual Availability: 0 hours
        ---------------------------------
        Assigned Task: Install New Routers
        Assigned For Task: 300 hours
        Remaining Availability: -300 hours
    """
    if name in STAFFING:
        resource_warning = 'ALERT: The resource does not have enough ' \
                 'availability to complete the task!' if STAFFING[name][5] < 0 \
                 else 'This resource has enough availability to complete the ' \
                 'assigned task.'
        resource_report = """
        Resource Report For: {name}
        ---------------------------------
        Estimated Availability: {ea} hours
        Time Off: {to} hours
        Actual Availability: {aa} hours
        ---------------------------------
        Assigned Task: {task}
        Assigned For Task: {ha} hours
        Remaining Availability: {hr} hours

        """.format(name=name, ea=STAFFING[name][1], to=STAFFING[name][2],
                   aa=STAFFING[name][3], task=STAFFING[name][0],
                   ha=STAFFING[name][4], hr=STAFFING[name][5])

        print resource_warning
        print resource_report
    else:
        print ('Unknown Team Member, Please pick:',
               ESTIMATED_AVAILABILITY.keys())
