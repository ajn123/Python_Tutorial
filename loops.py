

def main():
	x = 0
	#this is a while loop
	while(x < 5):
		print x
		x = x+1

	#this is a for loop
	for x in range(5,10):
		print x


	#Loops through an array
	days = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
	for d in days:
		print d



if __name__ == '__main__':
	main()