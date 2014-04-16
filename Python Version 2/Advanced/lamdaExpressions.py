

"""

Lamda expressions have special rules:
1)  The body of a Lamda expression can contain only a single line.
2)  The body can only contain an expression, no statements or other elements
3)  The result of the expression is automatically returned.

The form of a lamda expression is:
	lamda arg_list: expression

"""



add = lambda num1, num2: num2  + num1

print add(2,3) #prints 5.