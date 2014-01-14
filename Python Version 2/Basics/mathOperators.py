


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

	a = 40.2
	b = 23
	sum = a / b
	print "{0} / {1}  =  {2}".format(a,b,sum)	

	"""
	This is the modulus operator that takes a number and 
	finds the remainer if you were to divide a by b.
	"""
	a = 40
	b = 23
	sum = a % b
	print "{0} % {1}  =  {2}".format(a,b,sum)	
	
	print "sum is now =  {2}".format(a,b,sum)	

	#increments the value stored in sum by 5
	sum += 5
	print "sum is now =  {2}".format(a,b,sum)	

	sum -= 5
	print "sum is now =  {2}".format(a,b,sum)	


	sum *= 5
	print "sum is now =  {2}".format(a,b,sum)

	sum /= 5
	print "sum is now =  {2}".format(a,b,sum)	

	sum %= 5
	print "sum is now =  {2}".format(a,b,sum)	


	a = 10
	b = 2
	sum = pow(a,b)
	print "{0} to the power of {1}  =  {2}".format(a,b,sum)	


	a = 10
	b = 2
	#divmod gives the result of division and modulus
	sum = divmod(a,b)
	print "{0} divided by {1}  = {2}  and its mod is  {3}".format(a,b,sum[0],sum[1])	


if __name__ == '__main__':
	main()