import subprocess 
import filecmp




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





def compareFiles(file1,file2,options = True):
	list = []
	list.append("diff")

	list.append(file1)
	list.append(file2)
	print list
	print "\n\n" 
	str = ""
	subprocess.check_output(list)
	print str






if __name__ == '__main__':
	compile("gcc -o test example.c")
	run("test 5","5")
	#print filecmp.cmp("test1.txt","test2.txt",False)
	compareFiles("test1.txt","test2.txt")


