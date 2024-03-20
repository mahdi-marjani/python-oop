# variable --> 1.object variable, 2.class variable
class Car:
    wheel = 4 # class variable
    obj_nums = 0
    def __init__(self, n, p):
        self.name = n # object variable
        self.price = p
        Car.obj_nums+=1

    def show_wheel(self):
        print(f'{self.name} has {self.wheel} wheel')


c1 = Car('pride', 100)
c2 = Car('benz', 900)

c1.wheel = 5

print(c1.wheel) # 1.object variable

print(Car.obj_nums) # 2.class variable
