

def main():
	x = 0
	#this is a while loop
	while(x < 5):
		print x
		x = x+1

	#this is a for loop, it increments by one automaticaaly
	#it goes from 5 to 10 exclusive so  5,6,7,8,9 will be printed NOT 10
	for x in range(5,10):
		print x

	#The 2 represents how big the incrementer is, default is 1, this example is 2
	#this will print out 5 7 9
	for x in range(5,10,2):
		print x


	#Loops through an array
	days = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
	for d in days:
		print d

if __name__ == '__main__':
	main()