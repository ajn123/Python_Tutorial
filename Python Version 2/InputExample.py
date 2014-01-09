


def power(num, x =1):
	result = 1
	for i in range(x):
		result = result + num
	return result



def main():

	name = raw_input("What is your name?")
	quest = raw_input("What is your quest?")
	color = raw_input("What is your favorite color?")

	print "Ah, so your name is %s, your quest is %s, " \
	"and your favorite color is %s." % (name, quest, color)


	x,y =100,100
	if x < y:
		st = "this is true"
	else:
		st = "this is false"

	print st


if __name__ == '__main__':
	main()