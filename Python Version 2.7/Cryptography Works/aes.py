
import poly
import numpy

def main():
	num = [0,0,1,0,0,0,0,1]

	#represents x^8 + x^4 + x^3 + x + 1
	field = [1,0,0,0,1,1,0,1,1]


	a =  poly.polyInverse(num,field,2)[0].c
	a = a.tolist()

	while len(a) < 8:
		a.insert(0,0)


	print a



	str = binaryToHex(a)
	maxtrix1 = hexToBinary(str)
	sBox(maxtrix1)

	


def sBox(maxtrix1):

	xorMatrix = [1,1,0,0,0,1,1,0]
	maxtrix1 = numpy.matrix(maxtrix1)

	#matrix for AES
	maxtrix2 = numpy.matrix([   [1,0,0,0,1,1,1,1],
								[1,1,0,0,0,1,1,1],
								[1,1,1,0,0,0,1,1],
								[1,1,1,1,0,0,0,1],
								[1,1,1,1,1,0,0,0],
								[0,1,1,1,1,1,0,0],
								[0,0,1,1,1,1,1,0],
								[0,0,0,1,1,1,1,1]])


	ans = maxtrix2 *  maxtrix1


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
		am += str( int(item)) 

	pm = ''
	string2 = array[-1:3:-1]
	for item in string2:
		pm += str(int(item))


	print lookup(int(pm,2)),lookup(int(am,2))
	return lookup(int(pm,2))+lookup(int(am,2))

	

def lookup(num):
	num %= 16
	array  = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	return array[num]

if __name__ == '__main__':
	main()
	#print int('1001',2)