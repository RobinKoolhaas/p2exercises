#!/usr/bin/python3

def create_dictionary(keys: list, values: list) -> dict:
    result = dict()
    
    for index in range(len(keys)):
        result[keys[index]] = values[index]

    return result