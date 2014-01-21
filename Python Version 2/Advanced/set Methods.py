def main():
	list = set([1,2,3])
	a = set([3,4,5,6,1])



	print a & list  #intersection operation (elemients in both sets)
	print a  | list #union operation (elements combinted into one set)
	print a - list #difference operation (removes all the identical elements from the the second parameter set.
	print a ^ list #symmetric difference (elements that are in the first set and the second, but not in both)



if __name__ == '__main__':
	main()