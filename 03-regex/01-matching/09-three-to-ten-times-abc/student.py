#!/usr/bin/python3

import re


def three_to_ten_times_abc(string):
    return re.findall(r'(abc){3,10}', string)
