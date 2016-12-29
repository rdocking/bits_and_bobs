#!/usr/bin/env python
# encoding: utf-8
"""
sprint_template.py

Created by Rod Docking on 2016-12-28.
Copyright (c) 2016 Canada's Michael Smith Genome Sciences Centre.
All rights reserved.
"""

import sys
import os
import argparse

SPRINT_TEMPLATE = """---
title: "Sprint $NUM: Witty Subtitle"
author: "Rod Docking"
date: 'YYYY-MM-DD'
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

|                    | Last Sprint | Estimate                                     | Actual |
|:-------------------|:------------|:---------------------------------------------|:-------|
| Meeting-free hours |             | (8.0hrs/day * 10 days) - (meetings in hours) |        |
| Story points       |             |                                              |        |

### Story Points and Intervals

- Estimates:
    - Week 1: $Xh committed
    - Week 2: $Yh committed
    - Estimate of meeting-free hours: 80 - ($X + $Y) = $Zh
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

### Week 1 - YYYY-MM-DD - YYYY-MM-DD

- YYYY-MM-DD -
- YYYY-MM-DD -
- YYYY-MM-DD -
- YYYY-MM-DD -
- YYYY-MM-DD -

### Week 2 - YYYY-MM-DD - YYYY-MM-DD

- YYYY-MM-DD -
- YYYY-MM-DD -
- YYYY-MM-DD -
- YYYY-MM-DD -
- YYYY-MM-DD -

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
        'sprint_title', help='Sprint title')
    args = parser.parse_args()
    return args


def main():
    """Main function"""
    args = _parse_args()
    print SPRINT_TEMPLATE


if __name__ == '__main__':
    main()
