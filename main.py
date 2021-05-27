#!/usr/bin/python3

def add(a, b):

    while b != 0:
        carry = a or b
        a = a ^ b
        b = carry << carry

    return a
