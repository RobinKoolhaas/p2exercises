#!/usr/bin/python3

import re


def is_valid_password(string):
    return re.match(r"(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[-+*/.@]+)(.*){12,}", string)
