
import unittest


"""
Fings similar substring sequences in a string to indicate a vigenere cipher
PRE:string
POST:position of similar substrings are printed out
"""
def findTrigraphs(text):
	if not isinstance(text, str):
		print "needs to be a string not "+ str(type(text))
		return
	count  = 0
	index = 1
	list = []

	#alternative range(start,stop,increment)
	for zero in range(count,len(text)-2,1):
		#print text[count]
		for second in range(index,len(text)-2,1):
			if text[count] == text[index] and text[count+1] == text[index+1] and text[count+2] == text[index+2] :
				print text[count]+text[count+1]+text[count+2] +" at position " +str(count) +" and at position "+str(index)
				list.append(count)
				list.append(index)
				break
			index = index + 1
		
		count = count + 1
		index = count + 1
	list.sort()
	return list





"""
Tests the trigraph function by comparing the returned list.
Uses the unit testing library.
"""
class TestTrigraphs(unittest.TestCase):

    def setUp(self):
       pass

    def test_trigraph(self):
         self.assertEqual(findTrigraphs("asdpooqwertypoolkjhgpoo"),[3,12,12,20])


if __name__ == '__main__':
    unittest.main()