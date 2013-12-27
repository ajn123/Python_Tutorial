animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]


duck_index = animals.index("duck")   # Use index() to find "duck"


#inserts cobra into the end of the list (position 5) not position 9, it will default
#to the end
animals.insert(9,"cobra")


print animals # Observe what prints after the insert operation

start_list = [5, 3, 1, 2, 4]

print start_list.sort()



#You can also declare lists this way
#This makes a list of all squares 1 through 10
my_list = [i**2 for i in range(1,11)]
