

def main():
	x = 0
	#this is a while loop
	while(x < 5):
		print x
		#this is equal to  x = x + 1
		x += 1

	#this is a for loop,the most used loop in python.  It increments by one automaticaaly
	#it goes from 5 to 10 exclusive so  5,6,7,8,9 will be printed NOT 10
	for x in range(5,10):
		print x

	#The 2 represents how big the incrementer is, default is 1, this example is 2
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
	# the varcable i will print out each character 
	#in the string
	for i in str:
	   print i,

	




def enumerating():
	#this is how you can get the index of what you are looping through
	#in case you need it.  You can pass in your block  to this iterable 
	#function to loop through the list and its index

	list = ("apple","orange","pear")
	# i is the index ant item is the element
	for i,item in enumerate(list):
		print item,i


if __name__ == '__main__':
	enumerating()
	main()





