

def main():
	a = [1,2,3,4,5]

	dict = {"bob":32,"aj":22,"joe":100}


	"""
	The "in" keyword is an operator you can use on a set to see in that 
	element exists in the set.

	"""
	print 2 in a #True





	print 5 in range(4,11) #True


	#This will be false as only the dictionaries keys are being checked.
	print 100 in dict  


	print 100 in dict.values() #True


	"""
	There also is a NOT keyword to see if an inverse of a set is true.
	"""
	print 10 not in a #True, 10 is not in the list of a.



if __name__ == '__main__':
	main()