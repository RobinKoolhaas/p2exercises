#!/usr/bin/python3

import re


def only_digits(string):
    return re.fullmatch(r'[0-9]*', string)
