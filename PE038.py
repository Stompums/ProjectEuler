#!/usr/bin/env python
"""
Scratch file
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
from msvcrt import getch

def ispandigital(n):
    test = [1,2,3,4,5,6,7,8,9]
    check = sorted([int(j) for j in str(n)])
    if check == test:
        return True
    return False
def SUM(List):
    Sum = ''
    for i in List:
        Sum += i
    return Sum
n = 0
CHAMP = 0
while n < 10000:
    n+=1
    holder,j = [str(n)],2
    while len(SUM(holder)) < 9:
        holder.append(str(n*j))
        j+=1
        if len(SUM(holder))>9:
            break
    challenger = int(SUM(holder))
    if ispandigital(challenger):
        if challenger > CHAMP:
            CHAMP = challenger
print CHAMP
getch()