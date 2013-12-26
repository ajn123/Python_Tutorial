
def findTrigraphs(text):
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
	print list


from fractions import gcd
#print gcd(20,8)


def findLength(list):
	count = 0
	for item in range(count,len(list)-1,1):



def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))


findTrigraphs("asdpooqwertypoolkjhgpoo")