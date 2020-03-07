from abc import abstractmethod

# Base (abstract) class
class Animal():
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

    @abstractmethod
    def speak(self) -> str:
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):
    def __init__(self, name: str):
        Animal.__init__(self)
        self.name = name
        print("Dog created")

    def who_am_i(self):
        print("I am a Dog")

    def bark(self):
        print("Woof!")
    
    def speak(self) -> str:
        return self.name + " says woof!"


class Cat(Animal):
    def __init__(self, name: str):
        Animal.__init__(self)
        self.name = name

    def speak(self) -> str:
        return self.name + " says meow!"

class Fish(Animal):
    def __init__(self, name: str):
        Animal.__init__(self)
        self.name = name

    def speak(self) -> str:
        return self.name + " says bubble!"


my_dog = Dog("dog")
my_dog.who_am_i()
my_dog.bark()

felix = Cat("Felix")
niko = Dog("Niko")

print(felix.speak())
print(niko.speak())

animals  = [felix, niko]

for pet in animals:
    print(type(pet))
    print(pet.speak())

nemo = Fish("Nemo")
print(nemo.speak())



