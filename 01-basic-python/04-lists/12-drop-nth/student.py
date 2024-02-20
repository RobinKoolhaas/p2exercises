#!/usr/bin/python3

def drop_nth(xs: list, n: int) -> list:
    result = xs[:n] + xs[n + 1:]
    return result