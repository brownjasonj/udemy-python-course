class Circle():

    # Class Object Attribute
    pi : float = 3.14

    def __init__(self, radius: float = 1.0):
        self.radius = radius

    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.get_circumference())



