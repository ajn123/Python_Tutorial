import unittest



class listTest(unittest.TestCase):


	def testInit(self):
		list = [1,2,3]
		self.assertEqual(list,[1,2,3])


	#Lists can be properly sorted using the sort() method
	def testSort(self):
		list = [1,10,3]
		list.sort()
		self.assertEqual(list,[1,3,10])





if __name__ == '__main__':
	unittest.main()
		
		


