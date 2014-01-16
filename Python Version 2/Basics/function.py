
"""
You can declare a function by starting a line with 'def'
and then a function name followed by "()" which can indicate
the parameters you want to pass in.
"""
def function():
	print "this is a function"




"""
you can pass in values to impact what a function does,
these are known as parameters.
"""
def addition(param1,param2):
	print param1 + param2


"""
You can also return values with the return keyword to get back 
values of a function
"""
def returnAdd(p1,p2):
	return p1 + p2






"""
You can make default parameters by making them after the 
required ones

In this function I have two parameters,the first two are required 
,the third is NOT but you can override it by passing in a third parameter
in this example.
"""
def initialParameters(req1,req2,notreq  = 2):
	print req1 * req2 * notreq


"""
putting ONE '*' before a parameter means you can give 
an infinite amount of parameters that will be made into 
a tuple,
"""
def touple(*arg):
	sum = 1
	for item in arg:
		sum *= item
	print sum


"""
By putting TWO "**" before a parameter means that this function can pass in
named parameters
"""
def dictionary(**arg):
	for item in arg:
		print item, arg[item]


"""
This is how you can return multiple values, this 
yield will return values without exiting the function 
so you can for instance create a range of values to go through.

"""
def inclusive_range(*args):
    numargs = len(args)
    if numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start,stop) = args
        step = 1
    elif numargs == 3:
        (start,stop,step) = args

    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__':
	#ths is how you call a basic function
	function()

	#this is how you call a function with parameters
	addition(2,5)


	#Here I am printing the value returned from the function
	print returnAdd(10,340)


	#I can call this function with multiple parameters
	touple(1,2,3)
	touple(1,2,3,4,5)

	initialParameters(3,2)
	
	#In this method call I am overriding the third parameter
	# with 3 instead of 2
	initialParameters(5,4,3)

	#this is how you pass in a named functions that gets 
	# treated as a dictionary
	#NOTE: you can not just pass in a dictionary.
	dictionary( four = 2, two = 1,baseGod = 234 )


	#calls the range function defined to print certain items
	a = inclusive_range(12,30)
	for item in a:
		print item