#!/usr/bin/env python
"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234, 
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.
"""
pandigital_products = []
def ispandigital(*arg):
    digits = range(1,10)
    for number in arg:
        for char in str(number):
            if int(char) in digits:
                digits.remove(int(char))
            else:
                return False
    if digits == []:
        return True
    return False

for multiplier in range(100):
    for multiplicand in range(multiplier,10000):
        product = multiplier*multiplicand
        if ispandigital(multiplier,multiplicand,product):
            if product not in pandigital_products:
                pandigital_products.append(product)
print sum(pandigital_products)