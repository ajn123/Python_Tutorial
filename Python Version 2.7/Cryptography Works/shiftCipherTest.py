from shiftCipher import *
import unittest

"""
Tests shift Cipher tests
"""
class shiftTest(unittest.TestCase):
	"""docstring for shiftTest"""
	def setUp(self):
		pass

	def testEncrypt(self):
		self.assertEqual(encrypt("abc",2),"cde")

	def testDecrypt(self):
		self.assertEqual(decrypt("cde",2),"abc")

	def testBestGuess(self):
		self.assertEqual(bestGuessDecrypt("abc"),[['a', 'b', 'c'], ['z', 'a', 'b'], ['o', 'p', 'q'], ['n', 'o', 'p'], ['m', 'n', 'o'], 
			['h', 'i', 'j'], ['g', 'h', 'i'], ['e', 'f', 'g'], ['d', 'e', 'f'], ['c', 'd', 'e']])


if __name__ == '__main__':
    unittest.main()
