
"""
Unit testing is really easy and this will show how to do it.
"""


#you need to import the unit test module first.
import unittest



"""
Create a class (it can be named anything) that inherits from
"unittest.Testcase"  
"""
class Testing(unittest.TestCase):


	def setUp(self):
		self.seq = range(10)


	"""
	Then you can make methods to test the methods 
	NOTE: THE METHODS NAMES MUST START WITH "test"
	"""
	def testCase(self):
		list = [1,10,3]
		list.sort()

		"""
		assert Equal tests that whatever is given as the two parameters are equal.
		This can be for comparing numbers, lists (as seen below),tuples,dictionaries.
		"""
		self.assertEqual(list,[1,3,10])



	"""
	You can create more tests and do multiple comparisons in one method.
	"""
	def test2(self):
		self.assertEqual(1,1)
		self.assertEqual(2,2)



	"""
	Failed test:
	uncomment this and run it to see what a failed test looks like.

	def test3(self):
		self.assertEqual(12,1)
	"""




if __name__ == '__main__':

	#simply run your tests by the unit test by running "unittest.main()"
	unittest.main()