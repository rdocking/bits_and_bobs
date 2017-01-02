#!/usr/bin/env python
# encoding: utf-8
"""
day_one_entry_splitter.py

Created by Rod Docking on 2017-01-01.
All rights reserved.
"""

import sys


def main():
    """Split entries from Day One export into separate files"""

    # Entry headers look like:
    # "Date:	February 14, 2005 at 9:00 AM"
    # Need to:
    #  Loop through all the lines in the input file
    #  When we hit a new date, open a new file with approriate name
    with open(sys.argv[1]) as in_handle:
        for line in in_handle:
            if "Date:" in line:
                print line


if __name__ == '__main__':
    main()
