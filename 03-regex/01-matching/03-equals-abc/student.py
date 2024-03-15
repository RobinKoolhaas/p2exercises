#!/usr/bin/python3

import re


def equals_abc(string):
    return re.fullmatch('abc', string)
