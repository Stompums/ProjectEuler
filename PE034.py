#!/usr/bin/env python
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
def factorial(n):
    if n == 0:
        return 1
    for number in range(1,n):
        n *= number
    return n

def iscurious(number):
    if number == 1 or number == 2:
        return False
    holderlist = []    
    for num in str(number):
        holderlist.append(factorial(int(num)))
    if sum(holderlist) == number:
        return True
    return False
k,very_curious=3,[]
while k<7*factorial(9):
    if iscurious(k):
        very_curious.append(k)
    k+=1
print sum(very_curious)
