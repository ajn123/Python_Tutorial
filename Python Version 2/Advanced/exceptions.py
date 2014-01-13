"""
An exception is what occurs when you have a run time error in your 
program.



what you can do is "try" a statement wether it is invalid or not
if an error does occur withan that statement you can catch that error
in the except clause and print out a corresponding message 
(or you can print out the error message),

"""



#made up imports will cause an imput error.
try:
	import madeup
except ImportError:
	print ImportError


def main():
	while True:
		#Similar to Try and catch, tries an error and catches it.
		try:
			x = int(raw_input("Please enter a number: "))
			break
		except ValueError:
	         print "Oops!  That was no valid number.  Try again..."



	#A lookup error in whon an a incorrect lookup happens in a dictionary,
	dict = {"string": "a word representation"}

	try:
		dict["ERROR"]
	except LookupError:
		print LookupError


	"""
	You can catch an exception and then use a finally clause
	to take care of your program


	A finally statement is executed no matter if an exception is
	thrown.
	"""
	try:
		a = 4 / 2
	except Exception, e:
		raise e
		
	finally:
		print "finally clause raised"



if __name__ == '__main__':
	main()