import subprocess 





def compile(args):
	list = args.split()
	str = subprocess.check_output(list)





def run(command,output = "", exact = False):
	list = command.split()
	list[0] =  "./" + list[0]

	str = subprocess.check_output(list)
	print "\n\nprogram outputed:"
	print str


	if output in str:
		print "test passed"
	else:
		print "test failed"

	return str







if __name__ == '__main__':
	compile("gcc -o test example.c")
	run("test 5","5")