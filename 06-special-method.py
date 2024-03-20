# Special methods
# Special methods or Python's built-in methods like __init__
# All of them start with __ and end with __

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self): # method
        print(f'{self.name} costs {self.price}')

    def __str__(self):
        return f'{self.name}-{self.price}'
    
    def __add__(self, other):
        return self.price + other.price
    
    def __len__(self):
        return len(self.name)


c1 = Car('pride', 100)
c2 = Car('benz', 900)

print(c1)

print(c1 + c2)

print(len(c1))
