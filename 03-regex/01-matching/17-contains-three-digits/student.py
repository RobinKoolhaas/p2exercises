#!/usr/bin/python3

import re


def contains_three_digits(string):
    return re.fullmatch(r'[0-9].*[0-9].*[0-9].*', string)
