#!/usr/bin/python3

def make_path(parts: list) -> str:
    string = ""

    for entry in parts:
        string += entry
        string += "/"

    return string[:-1]