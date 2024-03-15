#!/usr/bin/python3

import re


def two_or_more_abc(string):
    return re.findall(r'(abc){2,}', string)
