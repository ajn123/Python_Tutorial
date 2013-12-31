

"""
This is how you declare a class with the class key word and then a name
followed by  "()" everythin within the class is indented just like a look
of if statement.
"""
class Car():
	
	"""
	Not to be thought of a constructor, the constructor calls
	the init method after the object is created
	"""
	def __init__(self,number):
		"""
		I can create instance variables for my class by simply defining them, the
		common thing to do is make the instance variables begin with an "_" to
		indicate instance variables, this is common practice in python
		"""
		self._number = number




	"""
	Simply returns the instance number variable.
	"""
	def number(self):
		return self._number
		




if __name__ == '__main__':
	#Instanciates a car object and assigns it to variable car
	car = Car(1222)
	print car.number()