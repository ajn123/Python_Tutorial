
from string import ascii_lowercase
#aaray of lowercase letters
alph = list(ascii_lowercase)




#Encrypts by adding the text to the key to get the cipher text.
def encrypt(name,num):
	text = []
	for char in name:
		text.append( alph[((ord(char)-19)+num) %26])
	print   "The encrypted text is : "+''.join(text)


#Decrypts by substracting the text by the key to go from cipher text to plain text
def decrypt(name,num):
	text = []
	for char in name:
		text.append( alph[((ord(char)-19)-num) %26])
	print "The decrypted text is : "+''.join(text)


"""
Looks through a dictionary text file to see if any of those
words are similar to the compared text.
"""
def bestGuess(text):
	f = open("dictionary.txt","r+")
	fl = f.readlines()
	for x in fl:
		#print x[:-1].split("\r")[0]
		if  x[:-1].split("\r")[0] in text:
			#print x[:-1].split("\r")[0] 
			return True
	return False
		
	f.close()


"""
Guesses the decrpytion by checking to see if any of the strings contain
english word substrings and prints them out
"""
def bestGuessDecrypt(name):
	text = []
	print "Best guesses for decrption are as follows:"
	for x in range(0,26):
		for char in name:
			text.append(alph[((ord(char)-19)-x) %26])
		if bestGuess(''.join(text)):
			print ''.join(text) +"\tkey is: "+str(x)
		text =[]



#Asks the user for input
name = raw_input("type in your cipher (no spaces)\n")
key = raw_input("what is the key? \n")
DorE= raw_input("are you Encrypting or Decrypting or Best Guess Decryption (E or D or B)?\n")

if DorE == "E":
	encrypt(name,int(key))
elif DorE == "D":
	decrypt(name,int(key))
else:
	bestGuessDecrypt(name)
