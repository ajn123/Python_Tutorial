
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
Calculates the index of coincidence of a piece of text
"""
def indexOfCoincidence(text):

	text = text.replace(" ", "")
	text = text.lower()
	list = [0] * 26
	for char in text:
		list[(ord(char)-19) %26] = list[(ord(char)-19) %26] +1

	sum = 0.0
	for item in list:
		sum = sum + (item *(item -1))

	sum = sum / (len(text) * (len(text)-1))

	if sum <= 0.0412:
		print "The IoC value indicates that the cipher is likely monoalphabetic"

	return sum

	







"""
Tests the trigraph function by comparing the returned list.
Uses the unit testing library.
"""
class TestTrigraphs(unittest.TestCase):
    def setUp(self):
       pass

    def testIoC(self):
		self.assertAlmostEqual(indexOfCoincidence("Defend the east wall of the castle"),0.082010582010582)



    def test_trigraph(self):
         self.assertEqual(findTrigraphs("asdpooqwertypoolkjhgpoo"),[3,12,12,20])











if __name__ == '__main__':
	unittest.main()
