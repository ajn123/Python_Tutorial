"""
This program takes an integer and outputs its string representation,

"""
def main():
	ans = ""

	num = raw_input("give me an number: ")

	#strip leading zeros just in case
	num = num.lstrip("0")
	if len(num) == 0:
		print "zero"
		return

	if num[0] == "-":
		ans += "negative "
		num = num[1:]

	numLenth = len(num)
	realLength = len(num)
	num = int(num)

	#python numbers go upto quintillion!!
	bigNumbers = ["thousand " ,"million ","billion ","trillion ","quadrillion ","quintillion "]
	high = num 
	


	while realLength > 3:
		power = closestLength(realLength)
		high = num/(10**(power))
		#print power
		#print high
		numLenth = calcNumLength(high)
		#print numLenth
		ans += solveHundreds(high,numLenth) + " "+bigNumbers[(((realLength-1)/3 )-1) %len(bigNumbers)]
		num %= 10**(power+1)
		realLength -= numLenth

	num %= 1000


	numLenth = calcNumLength(num)
	ans += solveHundreds(num,numLenth)
	print ans





"""
Calcalates the string representation of any number from 1 to 999.
"""
def solveHundreds(num ,numLenth):
	if numLenth == 0:
		return ""
	
	decimal = ["one","two","three","four","five","six","seven","eight","nine"]

	tens = [ "ten","twenty",'thirty',"fourty","fifty","sixty","seventy","eighty","ninety"]

	str = ""

	if numLenth > 2:
		answer = num /  100
		str += decimal[(answer-1)%10] + " hundred " 
		num %= 100


	numLenth = calcNumLength(num)
	if numLenth > 1:
		if num >10 and num < 20:
			str += teens(num)
			return str
		else:	
			this = num /10 - 1
			str += tens[this]
		num %= 10


	#print num
	num = (num-1)%10

	if num > -1 and num < len(decimal):
		str += " " + decimal[num]

	return str



"""
Deals with the special case for the teens.
"""
def teens(num):
	if num == 11:
		return "eleven"
	elif num == 12:
		return "twelve"
	elif num == 13:
		return "thirteen"
	elif num == 14:
		return "fourteen"
	elif num == 15:
		return 'fifteen'
	elif num == 16:
		return 'sixteen'
	elif num == 17:
		return "seventeen"
	elif num == 18:
		return "eighteen"
	elif num == 19:
		return "nineteen"
	

def calcNumLength(num):
	if num == 0:
		return 0

	length =  str(num)

	while length[0] == '0':
		length = length[1:]


	return len(length)


def closestLength(numLength):
	count = 3
	while count < numLength - 3:
		count += 3
	return count


if __name__ == '__main__':
	main()



