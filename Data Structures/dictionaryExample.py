
"""
Declares a dictionary of key value pairs
listing it as (key):(value)
"""
vowels = { 1:'a',2:'b',3:'c',4:'d'}




def main():
	#Prints outs the key and values
	for k, v in vowels.iteritems():
		print k, v

	#Add value to dictionary
	vowels[10] = "z"
	
	#Prints just the values from the dictionary
	for v in vowels.itervalues():
		print v

	#Deletes the key value pair with 1 as a key
	del(vowels[1])

	#Typing does not have to be consistent across the dictionary
	vowels["aj"] = "bobo"


	print vowels.keys()
	print vowels.values()



if __name__ == '__main__':
	main()