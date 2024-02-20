#!/usr/bin/python3

def add_indices(xs: list):
    indexes = range(len(xs))
    return list(zip(indexes, xs))