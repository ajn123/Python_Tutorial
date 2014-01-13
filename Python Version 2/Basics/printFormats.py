import math

#
def main():


	string_1 = "Camelot"
	string_2 = "place"

	#Old way to print things out in python.
	print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


	#Simple format to print out strings.
	print 'We are the {} who say "{}!"'.format('knights', 'Ni')


	"""
	The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method.
	A number in the brackets refers to the position of the object passed into the str.format() method.

	This way you can print the same thing in multiple places if desired.
	"""
	print '{0} and {1} and again {0}'.format('spam', 'eggs')

	print '{1} and {0}'.format('spam', 'eggs')


	"""
	An optional ':' and format specifier can follow the field name. 
	This allows greater control over how the value is formatted. The following example rounds Pi to three places after the decimal.
	"""
	print 'The value of PI is approximately {0:.3f}.'.format(math.pi)


	
	"""
	Passing an integer after the ':' will cause that field to be a minimum number of characters wide.
	This is useful for making tables pretty.
	"""
	table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
	for name, phone in table.items():
		print '{0:10} ==> {1:10d}'.format(name, phone)




if __name__ == '__main__':
	main()