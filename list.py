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
		list = [1,2,3]
		self.assertEqual(list,[1,2,3])

	#Lists can be properly sorted using the sort() method
	def testSort(self):
		list = [1,10,3]
		list.sort()
		self.assertEqual(list,[1,3,10])


	#Retrieve data from list using bracket notation
	def testRetrieve(self):
		list = [1,10,3]
		self.assertEqual(list[0],1)
		self.assertEqual(list[1],10)

	def testModify(self):
		list = [1,2,3]
		list[0] = 100
		self.assertEqual(list[0],100)

	def testIndex(self):
		list = [1,2,3]
		self.assertEqual(1, list.index(2))

	def testSize(self):
		list = [1,2,3]
		self.assertEqual(3, len(list) )

	#Adds an element to the back of a list
	def testAppend(self):
		list = [1,2,3]
		list.append(4)
		self.assertEqual(list,[1,2,3,4])

	def testInsert(self):
		list = [1,2,3]
		list.insert(0,0)
		self.assertEqual(list,[0,1,2,3])

	#Tests the splicing mechanism of lists
	def testSplicing(self):
		list = [1,2,3,4,5]
		nList = list[1:]
		self.assertEqual(nList,[2,3,4,5])
		secList = list[2:4]
		self.assertEqual(secList,[3,4])

		#increments by two elements at a time starting at index 0 going to the end
		thirdList = list[::2]
		self.assertEqual(thirdList,[1,3,5])

		#You can start at the back if you use negative numbers, -2 = two indeces from the back
		#and the second ":"  number means up to but not including that point
		fourthList = list[-2:-1]
		self.assertEqual(fourthList,[4])
		




if __name__ == '__main__':
	unittest.main()
		
		


