#!/usr/bin/python3

import re


def one_or_more_abc(string):
    return re.fullmatch(r'(abc)+', string)
