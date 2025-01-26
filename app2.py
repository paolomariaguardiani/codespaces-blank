class Point:
    # magic method called "constructor"
    # it is called authomatically when we create a new object
    # Every class has at least one parameter wich we call self by convenction
    # Self is the reference to the current point object
    def __init__(self, x, y):
        self.x = x  # self è come dire point.x = Point(x,...)
        self.y = y
        
    def change_x_y(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def draw(self):
        print(f"Point({self.x}, {self.y})")
        
point = Point(3,4) # we need a constructor
# the point objects has methods and attributes
# print(point.x, point.y)
point.draw()
point.change_x_y(7,8)
point.draw()