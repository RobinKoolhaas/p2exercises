#!/usr/bin/python3

import re


def is_valid_time(string):
    return re.fullmatch(r"^\d{2}:\d{2}:\d{2}(\.\d{3})?", string)
