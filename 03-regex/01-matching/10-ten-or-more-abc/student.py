#!/usr/bin/python3

import re


def ten_or_more_abc(string):
    return re.findall(r'(abc){10,}', string)
