"""
This file exhibits file IO.
"""



"""
Reads a file by opening with "r+" meaning you have reading properties
the read line method  gives back a list of each line
"""
def readFile(fileName):
	file = open(fileName,"r+")
	txt = file.readlines()
	print txt
	for item in txt:
		print item

	file.close()


""""
to write, you open the file bit give it "w+" so you have the right to
write to the file

The write method writes to the file just five it a string
"""
def writeFile(fileName):
	file = open(fileName,"w+")
	file.write("hello, world \nanother line")
	file.close()



if __name__ == '__main__':
	writeFile("text.txt")
	readFile("text.txt")
	

	
