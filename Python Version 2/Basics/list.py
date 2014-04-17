import unittest


"""
A List represents the most versatile type of data structure in Python. It can contain items of different 
types and it has no rule against unicity. List indices start from zero, the elements can be sliced, 
concatenated, and so on. Lists also have a lot of similarities with strings, supporting the same kind 
of operations but unlike strings, lists are mutable.

USE LISTS WHEN:

When the data needs to be ordered.
When you need a mixed collection of data all in one place.
Data can contain duplicates
When your data requires the ability to be changed or extended. Remember, lists are mutable.
"""


class listTest(unittest.TestCase):
	def testInit(self):
		firstlist = [1,2,3]
		self.assertEqual(firstlist,[1,2,3])



	"""
	This special way of creating a list allows you to make a list initialize a 
	list to a specific length or create a huge array at ease that repeats.  You 
	can just multiply  a list by a value to change the length.  


	Doing something  like   a = [0] * 26 creates a list of 26 0's.

	"""
	def testInitAdvanced(self):
		firstlist = [1,2,3] * 4
		self.assertEqual(firstlist,[1,2,3,1,2,3,1,2,3,1,2,3])


	def testConcatenateList(self):
		firstlist = [1,3,4] + [7,8,9]
		self.assertEqual(firstlist, [1,3,4,7,8,9])

	#Lists can be properly sorted using the sort() method
	def testSort(self):
		firstlist = [1,10,3]
		firstlist.sort()
		self.assertEqual(firstlist,[1,3,10])


	#Retrieve data from list using bracket notation,
	def testRetrieve(self):
		firstlist = [1,10,3]
		self.assertEqual(firstlist[0],1)
		self.assertEqual(firstlist[1],10)



	def testModify(self):
		firstlist = [1,2,3]
		firstlist[0] = 100
		self.assertEqual(firstlist[0],100)



		#You can get the index of an elememnt by calling index and pass in the element.
	def testIndex(self):
		firstlist = [1100,223,34]
		self.assertEqual(2, firstlist.index(34))



		#you can use min() and max() to find the maximum and minimum of a list of integers.
	def testMinAndMax(self):
		testList = [1,2,1000,123,2345,654,0]
		self.assertEqual(2345,max(testList))
		self.assertEqual(0,min(testList))

		#you can also find the min(alphabetical first) and max of lists of strings.
		stringList = ["aj","bob","cole"]
		self.assertEqual("cole",max(stringList))
		self.assertEqual("aj",min(stringList))





	def testSize(self):
		firstlist = [1,2,3]
		self.assertEqual(3, len(firstlist) )

	#Adds an element to the back of a list
	def testAppend(self):
		firstlist = [1,2,3]
		firstlist.append(4)
		self.assertEqual(firstlist,[1,2,3,4])

	def testInsert(self):
		firstlist = [1,2,3]
		firstlist.insert(0,0)
		self.assertEqual(firstlist,[0,1,2,3])


	"""
	You can easily split a list up if you want to get a slice of that 
	to just take that part and assign it to another list.
	"""
	#Tests the splicing mechanism of lists
	def testSplicing(self):
		firstlist = [1,2,3,4,5]
		nList = firstlist[1:]
		self.assertEqual(nList,[2,3,4,5])
		secList = firstlist[2:4]
		self.assertEqual(secList,[3,4])

		#increments by two elements at a time starting at index 0 going to the end
		thirdList = firstlist[::2]
		self.assertEqual(thirdList,[1,3,5])

		#You can start at the back if you use negative numbers, -2 = two indeces from the back
		#and the second ":"  number means up to but not including that point
		fourthList = firstlist[-2:-1]
		self.assertEqual(fourthList,[4])


		fifthList = firstlist[4:1:-1]
		self.assertEqual(fifthList,[5,4,3])

		

		#You can delete list indexes by using the "del" keyword and giving the list index.
	def testDeleteListIndex(self):
		firstlist = [1,4,5]
		del firstlist[1]
		self.assertEqual([1,5],firstlist)

		#You can delete splices as well.
		firstlist = [1,4,5]
		del firstlist[1:]
		self.assertEqual([1],firstlist)




	def testListInitialize(self):
	#Creates a list of 26 1's
		firstlist = [1]  * 10
		self.assertEqual(firstlist,[1,1,1,1,1,1,1,1,1,1])

		#initializes a list of 6 elements each having a square of their indices.
		firstlist = [x**2 for x in range(6)]
		self.assertEqual(firstlist,[0,1,4,9,16,25])

	def convertToList(self):

		#I can make a string into a list which takes every character and puts it into 
		#a separate index.

		result = list("aj")
		self.assertEqual(["a","j"],result)


		"""
		NOTE: You can convert anything into a list that is iterable.
		"""




		




if __name__ == '__main__':
	unittest.main()
		
		


