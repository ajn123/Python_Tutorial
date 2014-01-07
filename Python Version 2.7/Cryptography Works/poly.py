import numpy as np 
import math



modValue = 2



"""
calculates the  modular inverse of a polynomial
used for the AES algorithm
"""
def polyInverse():
	a = [1,0,0,0,0,1]
	ansOld = np.poly1d(a)
	b = [1,0,0,0,1,1,0,1,1]
	ans = np.poly1d(b)

	first = np.poly1d(0)
	sec = np.poly1d(1)
	
	i = 0
	while  ansOld(1000) != 1:
		array = np.polydiv(ans,ansOld)[0]
		array = modPolynomial(array)
		
		#print array
		inv = compute(sec,first,array)
		first = sec
		sec = inv
		
		newAns = compute(ansOld,ans,array)
		ans = ansOld
		ansOld = newAns
		i +=1
	print inv

		


#Mods any polynomial to prevent any negatives
def humanAbs(num):
	if num < 0:
		return (num % modValue)
	else:
		return num

def modPolynomial(poly):
	i = 0
	while i <= len(poly) :
		poly[i] = humanAbs(poly[i])
		if poly[i] % modValue == 0:
			poly[i] = 0
		i += 1
	return poly





def  compute(a1,a2,a3):
	multiAns = np.polymul(a1,a3)
	ans =  np.polysub(a2,multiAns)
	ans = np.poly1d(ans)
	modPolynomial(ans)
	#print ans
	return ans





def main():
	polyInverse()
	

if __name__ == '__main__':
	main()
