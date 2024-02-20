#!/usr/bin/python3

def odd_keys_dict(dict1: dict) -> dict:
    result = dict()

    for k, v in dict1.items():
        if k % 2 != 0:
            result[k] = v

    return result 