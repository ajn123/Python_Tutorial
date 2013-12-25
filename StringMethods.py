#This imports unit testing into python, similar to java JUnit testing
import unittest



"""This is a
multiline comment"""

#This is a single line comment


class MyTest(unittest.TestCase):

    def test3(self):
    	print "testing string"
        self.assertEqual("YOLO"[0:2], "YO")

    def testLength(self):
    	self.assertEqual(1,len("A"));


    def testStringMethod(self):
    	self.assertEqual("3.14",(str(3.14)))



unittest.main()

