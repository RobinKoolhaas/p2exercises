#!/usr/bin/python3

import re


def starts_with_a(string):
    return re.match(r'^a', string)

