#!/usr/bin/env python
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for p in range(1,501):
    for q in range(1,p):
        if p*(p+q) == 500:
            a = p**2 - q**2
            b = 2*p*q
            c = p**2 + q**2
            print a*b*c
