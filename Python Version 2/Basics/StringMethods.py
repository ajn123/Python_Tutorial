#This imports unit testing into python, similar to Java JUnit testing
import unittest



"""This is a
multi line comment"""

#This is a single line comment


#This class allows for junit testing
#Just use assert Equals
#NOTE: Test methods must start with "test" to be run by junit
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

        #the replace() method replaces all occurrences of the first parameter with the second
    def testReplace(self):
        string = "examplex"
        self.assertEqual('eXampleX',string.replace('x','X'))

        #Strips whitespace if no parameter or all passes of what is given as a parameter
    def testStrip(self):
        string = "    Example   "
        self.assertEqual('Example',string.strip())
        self.assertEqual( 'www.example.com'.strip('cmowz.'),'example')



if __name__ == '__main__':
    unittest.main()

