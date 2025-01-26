class Point:
    def draw(self):
        print("draw a point")
        
point = Point()
print(type(point))
print(isinstance(point, Point)) # we want )to know if point is an instance of Point
point.draw()
