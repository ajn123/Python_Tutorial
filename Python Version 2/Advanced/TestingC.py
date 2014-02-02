import subprocess



def main():
	str = subprocess.check_output(["echo", "Hello World!"])
	print str




if __name__ == '__main__':
	main()