#Examples of how imports work in Python.

"""
Think of imports like a box, inside the box is the functions or things that you need
this statement below is saying that i am going to take every function out of the box
and display it so I can use it.
"""
from math import *
print sqrt(25)



"""
imprts the math library.  "think of it as getting the math box but not opening it.
So you need to put the library before it (in this case math) to say hey
go into the box and get the sqrt function.  
"""
import math
print math.sqrt(36)



"""
Imports just the sqrt function.  This time no box, just the one sqrt item
for me to use.  Notice I dont need to have math before it as well
"""
from math import sqrt
print sqrt(49)
