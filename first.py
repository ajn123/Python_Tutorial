import unittest



"""This is a
multiline comment"""


#mkkkl
#This is a single comment line

def fun(x):
    return x + 1


def function():
	return 23

class MyTest(unittest.TestCase):

    def test3(self):
    	print "testing string"
        self.assertEqual("YOLO"[0:2], "YO")

    def testLength(self):
    	self.assertEqual(1,len("A"));


    def testStringMethod(self):
    	self.assertEqual("3.14",(str(3.14)))



unittest.main()

