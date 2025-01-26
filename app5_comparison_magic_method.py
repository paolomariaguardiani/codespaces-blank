# Magic methods are method wich have two underscores at the beginning and at the end
# of the name.
# This methods are called authomatically by Python!

class Point:
    def __init__(self, x, y):
        self.x = x  # self è come dire point.x = Point(x,...)
        self.y = y
        
    # We redefine the __str__ method
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    def draw(self):
        print(f"Point({self.x}, {self.y})")

# the __init__ method is called authomatically when we create a new object
point = Point(3,4)
# this is the default implementation of the str method in our point object
print(point)  # it is like: point.__str__
point.__str__
print(point)

