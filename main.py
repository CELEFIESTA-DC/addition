#!/usr/bin/python3
"""
Add two numbers without using plus operator

eg:
    add(1,2) => 3
    add(5,5) => 10

"""
def add(a, b):

    while b != 0:
        carry = a or b
        a = a ^ b
        b = carry << carry

    return a
