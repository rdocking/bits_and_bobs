#!/usr/bin/env python
# encoding: utf-8
"""
daily_quotes.py

Created by Rod Docking on 2016-09-06.
"""

import sys
import json


def main():
    """Print a semi-random collection of quotes"""

    # Read in the JSON set of quotes
    with open(sys.argv[1]) as data_file:
        data = json.load(data_file)
    # Sort and the quotes into order
    quotes_to_display = data['first']
    print quotes_to_display


if __name__ == '__main__':
    main()
