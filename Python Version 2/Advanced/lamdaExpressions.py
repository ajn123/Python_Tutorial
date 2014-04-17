"""

lambda expressions have special rules:
1)  The body of a lambda expression can contain only a single line.
2)  The body can only contain an expression, no statements or other elements
3)  The result of the expression is automatically returned.

The form of a lambda expression is:
	lamda arg_list: expression

A lambda is essentially an anonymous function, a function without a name

"""


#I am now assigning this lambda to add so now add is pointing to this lambda function and can call it.
add = lambda num1, num2: num2  + num1


#calling lambda function through add.
print add(2,3) #prints 5.


"""
Another way to use lambda functions is with the map() function, it takes a function and an iterable 
and applies that function to all the iterables.

I defined a lambda expression to square everything and map() applied that function to everything in the
list.
"""
result = map(lambda x: x**2,[2,3,4,56])

print list(result)
"""
prints:
4
9
15
3136
"""



"""
Filters the list based on the lambda rules.
"""
answer = filter(lambda a:a > 2 ,[1,2,3])
print(answer)# Prints a list with only 3 [3].



from functools import reduce


"""
Result can apply a function across a list returning one result 
such as a sum or  multiplication of the list.
"""
result = reduce(lambda a,b:a*b, [5,6,7])

print (result) #prints 210








