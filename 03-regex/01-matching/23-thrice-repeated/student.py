#!/usr/bin/python3

import re


def thrice_repeated(string):
    return re.fullmatch(r"(.+)\1\1", string)
