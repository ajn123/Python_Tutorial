"""
A dictionary is mutable and is another container type that can store any number of Python objects, 
including other container types. Dictionaries consist of pairs (called items) of keys and their corresponding values.

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

"""


def main():

	"""
	Declares a dictionary of key value pairs
	listing it as (key):(value)
	"""
	vowels = { 1:'a',2:'b',3:'c',4:'d'}



	"""
	Typing does not have to be consistent across the dictionary
	you can store any type as a key or value.


	this adds a pair with value bobo and key Name
	"""
	vowels["Name"] = "bobo"



	"""
	Updating the name key with a value of 123,
	"""
	vowels["Name"]  = 123


	print vowels.keys() #prints all the keys 
	print vowels.values() #prints all the values




	del vowels['Name']; # remove entry with key 'Name'
	vowels.clear();     # remove all entries in dict
	del vowels ;        # delete entire dictionary






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



if __name__ == '__main__':
	main()