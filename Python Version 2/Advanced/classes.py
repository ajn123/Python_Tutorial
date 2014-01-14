

"""
This is how you declare a class with the class key word and then a name
followed by  "()" everythin within the class is indented,
"""
class Car():
	"""
	Not to be thought of a constructor, the constructor calls
	the init method immediatly after the object is created,


	The self keyword refers to this particular object, a class can be thought of as 
	a definition of an object.  When you create an object, you are creating an instance 
	of that object or one object.  We are defining a car object but there are many cars 
	in the world and you can create a car object to represent them.  Self is passed 
	automatically to each method and you DO NOT need to pass it in and python will  
	automatically put it in for you.
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