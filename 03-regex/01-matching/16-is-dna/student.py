#!/usr/bin/python3

import re


def is_dna(string):
    return re.fullmatch(r'([GATC])*', string)
