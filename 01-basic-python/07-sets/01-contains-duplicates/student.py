#!/usr/bin/python3

def contains_duplicates(inputList: list):
    tempSet = set()

    for entry in inputList:
        if entry in tempSet:
            return True
        else:
            tempSet.add(entry)

    return False