#!/usr/bin/python3

def coins(one, two, five, goal):
    for a in range(0, one+1):
        for b in range(0, two+1):
            for c in range(0, five+1):
                if a + 2 * b + 5 * c == goal:
                    return True

    return False