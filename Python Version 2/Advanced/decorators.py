"""
Remember that everything in python is an object and a function is no different.  
As such, we can pass a function as a parameter to another function and have 
in invoked in another method.
"""


def square(x):
	return x**2

def double(a):
	return a *2

def triple(b):
	return b * 3




"""
taking a parameter as a tuple, I can loop through the tuple
and call the functions passed in to me.  Pretty Cool!
"""
def runFunctions(*args):
	for funct in args:
		print funct(5)




"Passing in all my functions as parameters."
runFunctions(square,double,triple)
"""
prints:
25
10 
15
"""