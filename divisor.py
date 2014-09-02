#!/usr/bin/env python

"""
Developing space for functions to solve Project Euler problem 12.
Prime factorization.
Number of divisors for triangular numbers
"""

import math


def PrimeFactors(n):  #Build a list of the prime factors of a number, n
	PrimeList,PrimeFactorsList = primes(math.floor(math.sqrt(n))),[]
	while n!=1:
		i=0
		while i<len(PrimeList):
			if n%PrimeList[i]==0:
				n=n/PrimeList[i]
				PrimeFactorsList.append(PrimeList[i])
				break
			else:
				i+=1
				if i==len(PrimeList):
					PrimeFactorsList.append(n)
					n=1
	return PrimeFactorsList

def countdivisors(n):     #Counts the number of divisors that a number, n has. So the number 12 has divisors 1,2,3,4,6,12 for a total of 6 divisors.
	PrimeDivisorList,count = PrimeFactors(n), 1
	PrimeList = list(set(PrimeDivisorList))
	for i in PrimeList:
	    count = count*(PrimeDivisorList.count(i)+1)
	return count
"""
def primes(x):         #Build a list of prime numbers less than n.
    prime_list,k = [2],3
    while k<=x:
        if all(k%i!=0 for i in prime_list):
            prime_list.append(k)
        k+=2
    return prime_list
"""
def primes(x):        #Builds a list of prime numbers less than n. It's bulkier but faster.
    primelist,k=[2,3],5
    while k<=x:
        if all(k%i!=0 for i in primelist):
            primelist.append(k)
        k+=2
        if k>x:
            break
        elif all(k%i!=0 for i in primelist):
            primelist.append(k)
        k+=4
    return primelist


def TriangleDivisors(n):   #Count the number of divisors of the sum of the first n integers.
	if n%2==0:
		return countdivisors(n/2)*countdivisors(n+1)
	else:
		return countdivisors(n)*countdivisors((n+1)/2)

