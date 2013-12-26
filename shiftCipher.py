
from string import ascii_lowercase
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


name = raw_input("type in your cipher (no spaces)\n")
key = raw_input("what is the key? \n")


DorE= raw_input("are you Encrypting or Decrypting (E or D)?\n")
if DorE == "E":
	encrypt(name,int(key))
elif DorE == "D":
	decrypt(name,int(key))


