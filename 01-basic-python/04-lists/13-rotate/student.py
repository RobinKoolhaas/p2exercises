#!/usr/bin/python3

#werkt niet
def rotate(xs: list, n: int) -> list:
    return xs[n:] + xs[:n]