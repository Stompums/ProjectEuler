#!/usr/bin/env python

"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. 
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome(string): #A testing function to determine whether or not a string is a palindrome
    LIST,STRING = [],''
    for i in string:
        LIST.insert(0,i)
    for i in LIST:
        STRING += i
    if string == STRING:
        return True
    else:
        return False

n = 900                 #Starting at 900 to reduce the number of calculations
products = {}           #Dictionary used to store products and their palindrome state of True or False
sweet_list = []         #Used to store palindrome products.
while n < 1000:
    for i in range(1000 - n):
        products[n * (n + i)] = palindrome(str(n * (n + i)))
    n += 1
for keys in products:
    if products[keys] == True:
        sweet_list.append(keys)
print max(sweet_list)
