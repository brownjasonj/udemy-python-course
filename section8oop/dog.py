from enum import Enum

class Species(Enum):
    MAMMAL = 1

class Dog:
    # Class variable
    species : Species = Species.MAMMAL
    
    def __init__(self, name: str, breed: str, spots: bool):
        self.name = name
        self.breed = breed
        self.spots = spots

    # Methods
    def bark(self):
        print("Whoof! My name is {}".format(self.name))

myDog : Dog = Dog(name = 'Sammy', breed = 'lab', spots = False)

myDog.bark()
print(myDog.spots)
print(myDog.breed)

