"""
imports the numpy library which allows for 
polynomial functions
"""
import numpy as np 


#Value to mod the polynomial by


"""
calculates the  modular inverse of a polynomial
used for the AES algorithm
"""
def polyInverse(num,field,modValue = 2,printOption = False):
	a = num
	ansOld = np.poly1d(a)

	b = field
	ans = np.poly1d(b)

	first = np.poly1d(0)
	sec = np.poly1d(1)

	otherSol = np.poly1d(1)
	secotherSol = np.poly1d(0)

	while  ansOld(0) != 0:
		array = np.polydiv(ans,ansOld)[0]
		array = modPolynomial(array)

		inv = compute(sec,first,array)
		first = sec
		sec = inv


		othInv = compute(secotherSol,otherSol,array)
		otherSol = secotherSol
		secotherSol = othInv
		
		newAns = compute(ansOld,ans,array)
		ans = ansOld
		ansOld = newAns

	list = (inv, othInv)

	if printOption:
		print 'the inverse of \n ',np.poly1d(field),' is \n',inv
		print 'and the other inverse is \n',othInv
	
	return list
		

def humanAbs(num,modValue = 2):
	if num < 0:
		return (num % modValue)
	else:
		return num


#Mods any polynomial to prevent any negatives
def modPolynomial(poly, modValue = 2):
	i = 0
	while i <= len(poly) :
		poly[i] = humanAbs(poly[i],modValue)
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
	pass

if __name__ == '__main__':
	main()
