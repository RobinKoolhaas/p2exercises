#!/usr/bin/python3

def word_count(string: str) -> int:
    if string == "":
        return 0

    return len(string.split(" "))