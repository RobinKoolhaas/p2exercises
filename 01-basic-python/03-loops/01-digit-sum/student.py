#!/usr/bin/python3

def last_digit(n: int) -> int:
    return n % 10

def remove_last_digit(n: int) -> int:
    return n // 10

def digit_sum(n: int) -> int:
    sum = 0

    while(n > 0):
        sum += last_digit(n)
        n = remove_last_digit(n)

    return sum