#This imports unit testing into python, similar to java JUnit testing
import unittest



"""This is a
multiline comment"""

#This is a single line comment


#This class allows for junit testing
#Just use assert Equals
class MyTest(unittest.TestCase):

	#Tests string length method
    def testLength(self):
    	string = "practice String"
    	#Tests the length of a string
        self.assertEqual(15, len(string))

    def testUpper(self):
    	string = "practice String"
    	self.assertEqual("PRACTICE STRING",string.upper());


    def testLower(self):
    	string = "Practice String"
    	self.assertEqual("practice string",string.lower());



string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


unittest.main()

