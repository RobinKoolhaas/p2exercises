#!/usr/bin/python3

def includes(xs: list, ys: list) -> bool:
    for y in ys:
        if y not in xs:
            return False

    return True