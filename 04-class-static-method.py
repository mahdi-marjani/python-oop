# method -->  1.object method,  2.class method,  3.static method

import datetime

class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    # object | regular method
    def show(self):
        print(f'{self.name} is {self.height} is {self.age}')

    # class method
    @classmethod
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)

    # static method
    @staticmethod
    def is_adult(age):
        if age > 18:
            print('yes')
        else:
            print('no')

p1 = Person.from_birth('amir', 180, 1990)

p1.is_adult(22)