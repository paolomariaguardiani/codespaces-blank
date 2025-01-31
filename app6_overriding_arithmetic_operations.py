class Point:
    def __init__(self, x, y):
        self.x = x  # self è come dire point.x = Point(x,...)
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
        
point = Point(20,40)
other = Point(3,4)
print(point + other)  # return an object
combined = point + other
print(combined.x, combined.y) # return the arithmetic operation

