#!/usr/bin/env python
# encoding: utf-8
"""
sprint_template.py

Created by Rod Docking on 2016-12-28.
Copyright (c) 2016 Canada's Michael Smith Genome Sciences Centre.
All rights reserved.
"""

import argparse
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR
import csv

SPRINT_TEMPLATE = """---
title: "Sprint {sprint_num}: {sprint_title}"
author: "Rod Docking"
date: '{start_date}'
csl: ../../references/csl/apa.csl
bibliography: ../../references/paperpile_export.bib
---

## Current Sprint

- What are the goals for the current sprint?
- Current analysis:
    - ✅ Done ticket (**POINTS**)
    - ⏩ In-progress ticket (**POINTS**)
    - ◽ Open ticket (**POINTS**)
- Thesis planning:
    - Planning task (**NUM x CATEGORY**)
- Current reading:
    - Reading task (**NUM x CATEGORY**)
- Background reading:
    - Reading task (**NUM x CATEGORY**)
- Meta and Admin:
    - Admin task (**NUM x CATEGORY**)
- Support:
    - Support task (**NUM x CATEGORY**)


## Agile Metrics Tracking

### Story Points

|                    | Last Sprint | Estimate | Actual |
|:-------------------|:------------|:---------|:-------|
| Meeting-free hours | {last_sprint_hours}           |          |        |
| Story points       | {last_sprint_points}           |          |        |

### Story Points and Intervals

- Estimates:
    - Week 1: {w1_committed}h committed
    - Week 2: {w2_committed}h committed
    - Estimate of meeting-free hours: {sprint_hours} - ({w1_committed} + {w2_committed}) = {sprint_committed_hours}h
    - Estimated potential points from `sprint_estimation_tables.rmd`
- Story points assigned at sprint planning meeting:
- Actual:
    - Week 1: $Xh committed
    - Week 2: $Yh committed
    - Actual meeting-free hours: 80 - ($X + $Y) = $Zh
- Story points completed:
- Intervals Goal: (16 * number of working days)
- Interval Targets:

| Category                       | Estimate | Daily | Actual | Diff |
|:-------------------------------|:---------|:------|:-------|:-----|
| Meta                           |          |       |        |      |
| Current Analysis               |          |       |        |      |
| Current Reading                |          |       |        |      |
| Background Reading             |          |       |        |      |
| Meetings and Seminars          |          |       |        |      |
| Informatics Support            |          |       |        |      |
| Scanning, Networking, Browsing |          |       |        |      |
| **SUM**                        |          |       |        |      |

## Schedule

### Week 1 - {start_date} - {w1d5}

- {start_date} -
- {w1d2} -
- {w1d3} -
- {w1d4} -
- {w1d5} -

### Week 2 - {w2d1} - {end_date}

- {w2d1} -
- {w2d2} -
- {w2d3} -
- {w2d4} -
- {end_date} -

## Progress

### Papers Read

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

### Analysis Tickets Completed

- JIRA tickets completed

### Other Accomplishments

- Other noteworthy things that happened

### Push to Next Sprint or Drop

- Things that were dropped at the planning meeting
- Things that were consciously dropped mid-sprint

## Retrospective

- Retrospective thoughts on the sprint

## References
"""


def _parse_args():
    parser = argparse.ArgumentParser(
        description="""Sprint Planning Template""")
    parser.add_argument(
        '-s', '--sprint_num', type=int,
        help='Sprint number', required=True)
    parser.add_argument(
        '-d', '--start_date', type=str,
        help='Sprint start date', required=True)
    parser.add_argument(
        '-t', '--sprint_title', type=str,
        help='Sprint title', required=True)
    parser.add_argument(
        '-e', '--estimation_data', type=str,
        help='Sprint estimation data', required=True)
    parser.add_argument(
        '-n', '--num_days', type=int,
        help='Number of days in the sprint', required=True)
    args = parser.parse_args()
    return args


def fetch_prior_values(args):
    """Fetch prior sprint values from TSV data sheet"""
    productive_hours_actual = 'NA'
    story_points_actual = 'NA'
    with open(args.estimation_data, 'rb') as tsv_input:
        tsv_reader = csv.DictReader(tsv_input, delimiter='\t')
        for row in tsv_reader:
            prior_sprint_num = int(row['sprint_number'])
            if prior_sprint_num == args.sprint_num - 1:
                productive_hours_actual = row['productive_hours_actual']
                story_points_actual = row['story_points_actual']
    return productive_hours_actual, story_points_actual


def main():
    """Main function"""
    # Parse command-line arguments
    args = _parse_args()
    # Calculate sprint end dates
    # Use the dateutil package to calculate 'next Friday'
    start_datetime = parse(args.start_date)
    end_datetime = start_datetime + relativedelta(weekday=FR(+2))
    # Set up the sprint file name
    sprint_file_name = 'sprint_{num}_{start_date}-{end_date}.rmd'.format(
        num=args.sprint_num,
        start_date=start_datetime.date(),
        end_date=end_datetime.date()
    )
    # Grab values from last sprint for productive hours and points
    productive_hours_actual, story_points_actual = fetch_prior_values(args)
    # Set up estimates for hours and intervals
    sprint_hours = args.num_days * 8
    w1_committed = 0
    w2_committed = 0
    sprint_committed_hours = sprint_hours - w1_committed - w2_committed
    # Write out the template with new values filled in
    with open(sprint_file_name, 'w') as sprint_handle:
        sprint_text = SPRINT_TEMPLATE.format(
            sprint_num=args.sprint_num,
            sprint_title=args.sprint_title,
            start_date=args.start_date,
            end_date=end_datetime.date(),
            w1d2=(start_datetime + relativedelta(weekday=TU(+1))).date(),
            w1d3=(start_datetime + relativedelta(weekday=WE(+1))).date(),
            w1d4=(start_datetime + relativedelta(weekday=TH(+1))).date(),
            w1d5=(start_datetime + relativedelta(weekday=FR(+1))).date(),
            w2d1=(start_datetime + relativedelta(weekday=MO(+2))).date(),
            w2d2=(start_datetime + relativedelta(weekday=TU(+2))).date(),
            w2d3=(start_datetime + relativedelta(weekday=WE(+2))).date(),
            w2d4=(start_datetime + relativedelta(weekday=TH(+2))).date(),
            last_sprint_hours=productive_hours_actual,
            last_sprint_points=story_points_actual,
            sprint_hours=sprint_hours,
            w1_committed=w1_committed,
            w2_committed=w2_committed,
            sprint_committed_hours=sprint_committed_hours
            )
        sprint_handle.write(sprint_text)


if __name__ == '__main__':
    main()
