


def main():
	a = 11
	b = 23
	sum = 11 + 23
	print "{0} + {1}  =  {2}".format(a,b,sum)	

	a = 11
	b = 23
	sum = 11 - 23
	print "{0} - {1}  =  {2}".format(a,b,sum)	

	a = 11
	b = 23
	sum = 11 * 23
	print "{0} * {1}  =  {2}".format(a,b,sum)	

	a = 40
	b = 23
	sum = float(a / b)
	print "{0} / {1}  =  {2}".format(a,b,sum)	

	"""
	This is the modulus operator that takes a number and 
	finds the remainer if you were to divide a by b.
	"""
	a = 40
	b = 23
	sum = a % b
	print "{0} % {1}  =  {2}".format(a,b,sum)	

	
	#increments the value stored in sum by 5
	sum += 5
	print "{0} / {1}  =  {2}".format(a,b,sum)	















if __name__ == '__main__':
	main()