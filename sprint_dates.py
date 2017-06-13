#!/usr/bin/env python
# encoding: utf-8
"""
sprint_dates.py

Created by Rod Docking on 2017-06-13.
Copyright (c) 2017 Canada's Michael Smith Genome Sciences Centre.
All rights reserved.
"""

import argparse
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta, FR


def _parse_args():
    parser = argparse.ArgumentParser(
        description="""Sprint Planning Template""")
    parser.add_argument(
        '-s', '--sprint_num', type=int,
        help='Sprint number', required=True)
    parser.add_argument(
        '-d', '--start_date', type=str,
        help='Sprint start date', required=True)
    args = parser.parse_args()
    return args


def main():
    """Generate dates for upcoming sprints"""
    # Parse command-line arguments
    args = _parse_args()
    # Calculate sprint end dates
    # Use the dateutil package to calculate 'next Friday'
    sprint_num = args.sprint_num
    start_datetime = parse(args.start_date)
    end_datetime = start_datetime + relativedelta(weekday=FR(+2))
    # Print the dates as strings
    i = 0
    while i < 20:
        print "Sprint {num} - {start_date} - {end_date}".format(
            num=sprint_num,
            start_date=start_datetime.date(),
            end_date=end_datetime.date()
        )
        sprint_num += 1
        start_datetime = start_datetime + relativedelta(weeks=2)
        end_datetime = end_datetime + relativedelta(weeks=2)
        i += 1

if __name__ == '__main__':
    main()
