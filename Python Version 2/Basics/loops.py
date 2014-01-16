"""
Loops are very important in python.  Loops allow you to go through collections 
and perform operations on them and analyze them.

"""

def main():
	x = 0
	#this is a while loop
	while(x < 5):
		print x
		#this is equal to  x = x + 1
		x += 1

	#this is a for loop,the most used loop in python.  It increments by one automatically
	#it goes from 5 to 10 exclusive so  5,6,7,8,9 will be printed NOT 10
	for x in range(5,10):
		print x

	#The 2 represents how big the incremented is, default is 1, this example is 2
	#this will print out 5 7 9
	#5 is the starting position, 11 is the ending (not including)
	for x in range(5,11,2):
		print x

	#Loops through an array
	days = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
	for d in days:
		print d


	#You can also iterate through strings
	str = "formidable"
	# the variable i will print out each character 
	#in the string
	for i in str:
	   print i



	"""
	You can break out of loops if a certain condition is met.  The break statement stops the 
	iteration of a loop and exits out of it.
	"""
	#this loop will stop once n gets to 4.
	for n in range(2, 10):
		print "n is" , n
		if n == 4:
			break 


	"""
	Another key word is continue, you can use that to still iterate through a loop but 
	when continue is hit by the program the next iteration automatically starts.


	in this case "another statement i is 6" will be skipped over because it hits the continue statement
	"""
	for i in range(10):
		print "i is ", i  
		if i == 6:
			continue
		print "another statement i is ", i


	"""
	You can not just have else statements at the end of if statements but also at the end of loops.

	Loop statements may have an else clause; it is executed when the loop terminates through exhaustion 
	of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
	"""
	for i in range(12,20):
		print i 
	else:
		print "done with the loop"


	for i in range(12,20):
		break
	else:
		print "loop will not execute"





def enumerating():
	#this is how you can get the index of what you are looping through
	#in case you need it.  You can pass in your block  to this iterable 
	#function to loop through the list and its index.

	list = ("apple","orange","pear") #tuple declaration


	# i is the index and item is the element
	for i,item in enumerate(list):
		print item,i
	"""
	this prints out:
	apple 0
	orange 1
	pear 2
	"""


if __name__ == '__main__':
	enumerating()
	main()





