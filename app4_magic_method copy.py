class Point:
    def __init__(self, x, y):
        self.x = x  # self è come dire point.x = Point(x,...)
        self.y = y
    
    # we redefine the __eq__ method
    def __eq__(self, other):  # eq = equals
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):  # gt = greater than
        return self.x > other.x and self.y > other.y

point = Point(30,40)
other = Point(3,4)
# print(point == other)  # False: the comparison is about the two objects in memory!

print(point == other)
print(point > other)
