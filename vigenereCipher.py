
def findTrigraphs(text):
	count  = 0
	index = 1
	for char in range(len(text),0,1):
		print text[char]
		for counter in range(len(text),1,1):
			print text[counter]

	#alternative range(start,stop,increment)
	for zero in range(count,len(text)-2,1):
		for second in range(index,len(text)-2,1):
			if text[count] == text[index] and text[count+1] == text[index+1] and text[count+2] == text[index+2] :
				print text[count]+text[count+1]+text[count+2] +" at position " +str(count) +" and at position "+str(index)
				break


		index = index + 1
	index = 0
	count = count + 1


from fractions import gcd
gcd(20,8)

findTrigraphs("abcqwertyabcabcabc")