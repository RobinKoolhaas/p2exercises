#!/usr/bin/python3

def double_dict_values(givenDict: dict) -> dict:
    result = dict()

    for key, value in givenDict.items():
        result[key] = value * 2

    return result