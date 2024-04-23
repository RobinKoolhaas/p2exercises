#!/usr/bin/python3

import re


def is_valid_student_id(string):
    return re.match(r"^[srSR]\d{7}$", string)
