#!/usr/bin/python3

def median(ns: list) -> int:
    ns.sort()

    if (len(ns) % 2) == 0:
        return (ns[len(ns) // 2] + ns[len(ns) // 2 - 1]) / 2

    return ns[len(ns) // 2]