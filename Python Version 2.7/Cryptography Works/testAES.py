
import unittest
import aes

class AESTest(unittest.TestCase):
	"""docstring for shiftTest"""
	def setUp(self):
		pass

	def testEncrypt(self):
		self.assertEqual(encrypt("abc",2),"cde")


if __name__ == '__main__':
    unittest.main()