#!/usr/bin/env python
# encoding: utf-8
"""
day_one_entry_splitter.py

Created by Rod Docking on 2017-01-01.
All rights reserved.
"""

import sys
import os
from dateutil.parser import parse


def parse_entry_date(line):
    """Parse the date from a DayOne entry date line to an ISO string"""
    # "Date:	February 14, 2005 at 9:00 AM"
    c = line.split()
    entry_date = parse(' '.join(c[1:])).date().isoformat()
    return entry_date


# def simple_compare(a, b):
#     """Simple date comparison - just year month day"""
#     return (a.year == b.year) and (a.month == b.month) and (a.day == b.day)


def main():
    """Split entries from Day One export into separate files"""

    # Set up directory structure
    root_dir = "/Users/rdocking/Dropbox/rd_docs/rd_writing/journals"

    # Entry headers look like:
    # "Date:	February 14, 2005 at 9:00 AM"
    # Need to:
    #  Loop through all the lines in the input file
    #  When we hit a new date, open a new file with appropriate name
    current_entry_date = "1979-11-24"
    entry_handle = open('tmp.txt', 'wb')
    with open(sys.argv[1]) as in_handle:
        for line in in_handle:
            # Find lines that start new entries, and start a new entry
            if "Date:" in line:
                entry_date = parse_entry_date(line)
                print entry_date
                entry_iso_year = entry_date[:4]
                entry_iso_month = entry_date[5:7]
                entry_iso_day = entry_date[8:10]
                continue
            # If the date has changed, start a new entry
            if not entry_date == current_entry_date:
                print "New entry!!"
                entry_handle.close()
                entry_dir = '{root_dir}/{year}/{month}/'.format(
                    root_dir=root_dir,
                    year=entry_iso_year,
                    month=entry_iso_month,
                    day=entry_iso_day)
                entry_file = 'journal_{year}-{month}-{day}.md'.format(
                    year=entry_iso_year,
                    month=entry_iso_month,
                    day=entry_iso_day)
                pathed_entry_file = os.path.join(entry_dir, entry_file)
                # If the directory doesn't exist, make it
                if not os.path.exists(entry_dir):
                    print "Making directory", entry_dir
                    os.makedirs(entry_dir)
                entry_handle = open(pathed_entry_file, 'wb')
                current_entry_date = entry_date
            # If there's a Photo line, replace it with an image link
            if "Photo:" in line:
                # Photo:	2014-10-14.jpg
                c = line.split()
                line = "\n![]({image})\n".format(image=c[1])
            # Write the new line to the current entry
            entry_handle.write(line)
    entry_handle.close()


if __name__ == '__main__':
    main()
