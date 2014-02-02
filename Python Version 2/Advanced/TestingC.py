import subprocess 





def compile(args):
	list = args.split()
	str = subprocess.check_output(list)





def run(command):
	str = subprocess.check_output(["./" + command ])
	print "\n\nprogram outputed:"
	print str




if __name__ == '__main__':
	compile("gcc -o test example.c")
	run("test")