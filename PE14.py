#!/usr/bin/env python
"""
The following iterative sequence is defined for the set of positive integers:

    n => n/2 (n is even)
    n => 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def Collatz(n):
    if n%2==0:
        n = n/2
    else:
        n = 3*n+1
    return n
Chain_Length = [0]
Tested = [0]
n = 1
while n < 1e6:
    k,i = n,1
    Tested.append(n)
    while k != 1:
        k = Collatz(k)
        i += 1
        if k in Tested:
            i = i + Chain_Length[k]
            break
    Chain_Length.append(i)
    n += 1

print Chain_Length.index(max(Chain_Length))