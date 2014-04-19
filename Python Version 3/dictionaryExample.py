

def main():

    """
    Declares a dictionary of key value pairs
    listing it as (key):(value)
    """
    vowels = { 1:'a',2:'b',3:'c',4:'d'}
    print(vowels)


    """
    Typing does not have to be consistent across the dictionary
    you can store any type as a key or value.

    this adds a pair with value bobo and key Name
    """
    vowels["Name"] = "bobo"


    """
    Updating the name key with a value of 123,
    """
    vowels["Name"]  = 123
    print(vowels)



    del vowels['Name']; # remove entry with key 'Name'




    #Prints outs the key and values
    for k, v in vowels.items():
        print(k, v)

    #Add value to dictionary
    vowels[10] = "z"
    
    #Prints just the values from the dictionary
    for v in vowels.values():
        print (v)
    
    #prints a list of keys
    for k in vowels.keys():
        print(k)

    #Deletes the key value pair with 1 as a key
    del vowels[1]


if __name__ == '__main__':
    main()