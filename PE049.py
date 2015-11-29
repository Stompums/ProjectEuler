# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:48:10 2015

@author: Jacob
"""

#!/usr/bin/env python
"""
Scratch file
"""
from math import sqrt
from itertools import permutations
from sets import Set
from time import time

start = time()

def isprime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0:
        return False
    i = 3
    while i < sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
    return True
    
def primepermute(n):
    s = Set([])
    if isprime(n):
        perms = [int(''.join(p)) for p in permutations(str(n))]
        for i in perms:
            if isprime(i) and len(str(i)) == len(str(n)) and i >= n:
                s.add(i)
    return s
    
def patternSet(s):
    S = primepermute(s)
    otherS = Set(S)
    if hasPattern(S):
        for i in S:
            otherS.remove(i)
            if not(hasPattern(otherS)):
                otherS.add(i)
        return otherS
    return Set([])

def hasPattern(S):
    otherS = Set(S)
    for i in S:
        otherS.remove(i)
        for j in otherS:
            if (i + j) / 2 in S and (i + j) % 2 == 0:
                return True
        otherS.add(i)
    return False
    
n = 1488

while len(patternSet(n)) == 0 and n != 1487:
    n += 1

resultSet = patternSet(n)
result = ""
for i in range(len(resultSet)):
    k = min(resultSet)    
    result += str(k)
    resultSet.remove(k)

print ""
print result
print ""
end = time()
print "Solution found in " + str(end - start) + " seconds"