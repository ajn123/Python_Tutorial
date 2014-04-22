

from math import *

file = open("lastThreeDigits.txt")

nums =int( file.readline())

#Calculates the last three digiets of the base number.

for number in range(nums):
    base = 3 + sqrt(5)
    num =1
    numberToSolve = int(file.readline())
    for x in range(numberToSolve):
        num *= base
        num %= 1000
    print "Case #{}: {}".format(number,int(num))