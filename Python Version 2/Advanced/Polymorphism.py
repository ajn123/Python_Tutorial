"""
Polymorphism can be used to apply the same method to different class types 
as long as each of those types contains the same method.  In this example,
Dog and Cat each have the same method but they have different effects because
the same objects define the same method differently!
"""
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'



class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

for animal in animals:
    print animal.name + ': ' + animal.talk()

# prints the following:
#
# Missy: Meow!
# Mr. Mistoffelees: Meow!
# Lassie: Woof! Woof!