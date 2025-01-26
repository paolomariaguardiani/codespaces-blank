class Point:
    default_color = "blue"  # a class attribute
    
    def __init__(self, x, y):
        self.x = x  # self è come dire point.x = Point(x,...)
        self.y = y
        
    def draw(self):
        print(f"Point({self.x}, {self.y})")


Point.default_color = "red"
        
point = Point(3,4)
print(point.default_color) # attribute of the instance
print(Point.default_color) # attribute of the class
# Because object patterns are dynamic, so we don't have to define all the
# attributes in the constructors
point.z = 30
point.draw()

another = Point(1,2)
print(another.default_color)
another.draw()