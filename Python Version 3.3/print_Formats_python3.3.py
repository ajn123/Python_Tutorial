#!/usr/bin/python3


'''
Created on Dec 30, 2013

@author: AJ Norton
'''


def main():
    #this prints a line in python 3, just like in python 2 but with parenthesis
    #as usual, a new line will be printed afterwards.
    print ("Print this line, and print a newline")
    
    
    """
    this is the power of the new print statement.  I can specify what I want the end 
    string to be.  In this case, I do not want to print a new line.
    """
    print ("Print this line, but not a newline", end="")
    
    
    
    print()
    
    #simple tuple
    basket = ('Apple', 'Oranges', 'Banana')
 
 
    """
    I can now print all the contents of the basket and designate separators
    for each item
    this will print
    Apple,   Oranges,   Banana.
    """
    print (*basket, sep=",   ", end=".\n")


if __name__ == '__main__':
    main()
       
    
    
    

    