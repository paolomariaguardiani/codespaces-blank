class Car:
    def __init__(self, make, model, year):
        self.__make = make  # with __ we have a private member
        self.__model = model
        self.__year = year
    
    def get_descriptive_name(self):
        return f"{self.__year} {self.__make} {self.__model}"
    
my_new_car = Car("Audi", "A4", 2010)
print(my_new_car.get_descriptive_name())
# my_new_car.__year = 1000  # it does not work anymore
# my_new_car.year = 2015
