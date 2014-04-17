def main():

	"""
	The function then reads a line from input, converts it to a string 
	(stripping a trailing newline), and returns that.
	"""
	name = raw_input("What is your name?")
	quest = raw_input("What is your quest?")
	color = raw_input("What is your favorite color?")

	#the '\' lets you function calls on multiple lines.
	print "Ah, so your name is %s, your quest is %s, " \
	"and your favorite color is %s." % (name, quest, color)


	"""
	REMEMBER: raw_input always returns an string.  So if I want to convert it to a 
	number I have to cast it (turn it into an int) to perform math opertions on it.    
	"""
	num = int(raw_input("give me a num: "))

	print num + 5


if __name__ == '__main__':
	main()