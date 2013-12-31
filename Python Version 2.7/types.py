
class example(object):
	"""docstring for example"""
	def __init__(self, arg):
		self.arg = arg
		

#bool
print type(True)

#List
print type([1,2,3])

#Dictionary
print type({1:"asd"})

#Float
print type(1.2)

#Integer
print type(1)

#Long
print type(1L)

#Complex Types
print type(1j)

#String
print type("string")

#Unicode
print type(u'unicode')

#Tuple
print type((1,2,3))

a = example(12)
print type(a)