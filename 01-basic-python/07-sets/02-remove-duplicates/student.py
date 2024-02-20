#!/usr/bin/python3

def remove_duplicates(xs: list) -> list:
    tempSet = set()
    result = list()

    for entry in xs:
        if entry not in tempSet:
            result.append(entry)
            tempSet.add(entry)

    return result