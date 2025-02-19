class Student:
    # def __init__(self, age):
    #     # self.__age = age
    #     self.set_age(age)
        
    # def get_age(self):
    #     return self.__age
    
    # def set_age(self, value):
    #     if value < 0:
    #         print("Age cannot be negative")
    #     self.__age = value
    
    def __init__(self, age):
        self.age = age
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative")
        self.__age = value
        
john = Student(12)
john.age = 13
print(john.age)