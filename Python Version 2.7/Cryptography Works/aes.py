
import poly
import numpy

def main():
	num = [1,1,1,1,1,1,1,1]

	#represents x^8 + x^4 + x^3 + x + 1
	field = [1,0,0,0,1,1,0,1,1]


	a =  poly.polyInverse(num,field,2)[0].c

	print a

	maxtrix1 = hexToBinary('00')
	sBox(maxtrix1)

	


	

def sBox(maxtrix1):

	xorMatrix = [1,1,0,0,0,1,1,0]

	#matrix for AES
	maxtrix2 = numpy.matrix([   [1,0,0,0,1,1,1,1],
								[1,1,0,0,0,1,1,1],
								[1,1,1,0,0,0,1,1],
								[1,1,1,1,0,0,0,1],
								[1,1,1,1,1,0,0,0],
								[0,1,1,1,1,1,0,0],
								[0,0,1,1,1,1,1,0],
								[0,0,0,1,1,1,1,1]])


	ans = maxtrix2 * maxtrix1


	for i,item in enumerate(ans):
		ans[i] = item % 2

	ans =  ans ^ xorMatrix
	ans =  ans[0]


	ans = ans.tolist()[0]

	binaryToHex(ans)
	

def hexToBinary(str):
	num = int(str , 16)
	i = 0
	lists = []
	while i < 8:
		item = (num >> i) & 1
		smallList = []
		smallList.append(item)
		lists.append(smallList)
		i += 1
	return numpy.matrix(lists)


def binaryToHex(array):

	string = array[3::-1]
	am = ''
	for item in string:
		am += str(item) 

	pm = ''
	string2 = array[-1:3:-1]
	for item in string2:
		pm += str(item)
	print int(pm,2), int(am,2)
	



if __name__ == '__main__':
	main()
	#print int('1001',2)