#!/usr/bin/python3

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    result = dict1

    for key, value in dict2.items():
        result[key] = value

    return result