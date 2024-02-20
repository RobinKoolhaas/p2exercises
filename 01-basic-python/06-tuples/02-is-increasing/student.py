#!/usr/bin/python3

def is_increasing(ns: list):
    ms = list(zip(ns, ns[1:]))

    for (a, b) in ms:
        if a > b:
            return False

    return True