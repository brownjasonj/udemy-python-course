import math

class Coordinate:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:    
    def __init__(self,coor1 : Coordinate,coor2: Coordinate) -> None:
        self.coord1 = coor1
        self.coord2 = coor2
    
    def distance(self) -> float:
        return math.sqrt((self.coord2.x - self.coord1.x)**2 + (self.coord2.y - self.coord1.y)**2)
    
    def slope(self) -> float:
        return (self.coord2.y - self.coord1.y) / (self.coord2.x - self.coord1.x)


coordinate1 = Coordinate(3, 2)
coordinate2 = Coordinate(8, 10)

line = Line(coordinate1, coordinate2)

print(line.distance())
print(line.slope())


class Cylinder:
    def __init__(self,height: float = 1,radius: float = 1):
        self.height = height
        self.radius = radius
        
    # Volume = pi * radius^2 * h
    def volume(self) -> float:
        return math.pi * (self.radius ** 2) * self.height

    # Surface = (2 * pi * r * h) + (2 * pi * r^2)
    def surface_area(self) -> float:
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2)

cylinder = Cylinder(2, 3)
print(cylinder.volume())
print(cylinder.surface_area())
