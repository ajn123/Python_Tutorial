"""
Regular Expressions are a way of finding something in a huge body of text
in sort of a notation so you can search for more complicated things than just
exact matches.
"""



import re

def main():
	string = "When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."


	print re.search('the',string)





if __name__ == '__main__':
	main()