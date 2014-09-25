#!/usr/bin/env python
"""
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def rotator(n):
    alist = []
    for char in str(n):
        alist.append(char)
    newlist, number = [], ''
    for i in range(1,len(alist)):
        newlist.append(alist[i])
    newlist.append(alist[0])
    for char in newlist:
        number += char
    return number 

def iscircular(prime):
    n = str(prime)
    if '0' in n:
        return False
    for a in str(prime):
        if not isprime(int(n)):
            return False
        n = rotator(n)
    return True

def circularcounter(prime):
    n,dopeness = str(prime),[]
    for a in n:
        dopeness.append(n)
        n = rotator(n)
    return(len(set(dopeness)))
    
def isprime(n):
    if n <= 3:
        return n>=2
    if n%2==0 or n%3==0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
funfile = open(r'prime number file location',r') #Opens a document filled with prime numbers.
numberstring = funfile.read()
primeslist = numberstring.split('\n')
primeslist.remove('')
counter = int()
primezlist = []
for prime in primeslist:
    if prime in primezlist:
        continue
    n = str(prime)
    if iscircular(prime):
        counter += circularcounter(prime)
        for char in prime:
            if n not in primezlist:
                primezlist.append(n)
            n = rotator(n)
print counter