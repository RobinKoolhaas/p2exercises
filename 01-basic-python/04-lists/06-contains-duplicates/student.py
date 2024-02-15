#!/usr/bin/python3

def contains_duplicates(xs: list) -> bool:
    newList = []

    for entry in xs :
        if entry in newList:
            return True
        else:
            newList.append(entry)

    return False
