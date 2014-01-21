"""
A set is an unordered collection with no duplicate values. A set can be created by using the keyword set or by using curly braces {}.
However, to create an empty set you can only use the set construct, curly braces alone will create an empty dictionary.
"""

def main():
	list = {1,2,3}
	a ={3,4,5,6,1}



	print a & list  #intersection operation (elemients in both sets)
	print a  | list #union operation (elements combinted into one set)
	print a - list #difference operation (removes all the identical elements from the the second parameter set.
	print a ^ list #symmetric difference (elements that are in the first set and the second, but not in both)



if __name__ == '__main__':
	main()