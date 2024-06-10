#!/usr/bin/python3

import re


def parse_time(string):
    re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})(\.\d{3})?", string)
    
