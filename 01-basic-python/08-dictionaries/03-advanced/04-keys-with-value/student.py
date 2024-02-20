#!/usr/bin/python3

def keys_with_value(givenDict: dict, givenInt: int) -> list:
    result = list()

    for key, value in givenDict.items():
        if value == givenInt:
            result.append(key)

    return result