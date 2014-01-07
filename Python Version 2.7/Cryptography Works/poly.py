"""
imports the numpy library which allows for 
polynomial functions
"""
import numpy as np 


#Value to mod the polynomial by
modValue = 2


"""
calculates the  modular inverse of a polynomial
used for the AES algorithm
"""
def polyInverse(num,field):
	a = num
	ansOld = np.poly1d(a)

	b = field
	ans = np.poly1d(b)

	first = np.poly1d(0)
	sec = np.poly1d(1)

	while  ansOld(1000) != 1:
		array = np.polydiv(ans,ansOld)[0]
		array = modPolynomial(array)

		inv = compute(sec,first,array)
		first = sec
		sec = inv
		
		newAns = compute(ansOld,ans,array)
		ans = ansOld
		ansOld = newAns
	print inv

		



def humanAbs(num):
	if num < 0:
		return (num % modValue)
	else:
		return num


#Mods any polynomial to prevent any negatives
def modPolynomial(poly):
	i = 0
	while i <= len(poly) :
		poly[i] = humanAbs(poly[i])
		if poly[i] % modValue == 0:
			poly[i] = 0
		i += 1
	return poly




"""
computes the euclid-wallis algorithm (google it if you dont know) to bring down values which 
ends up being the inverse.
"""
def  compute(a1,a2,a3):
	multiAns = np.polymul(a1,a3)
	ans =  np.polysub(a2,multiAns)
	ans = np.poly1d(ans)
	modPolynomial(ans)
	return ans



def main():
	#represents x^5 + 1
	num = [1,0,0,0,0,1]

	#represents x^8 + x^4 + x^3 + x + 1
	field = [1,0,0,0,1,1,0,1,1]

	polyInverse(num,field)
	

if __name__ == '__main__':
	main()
