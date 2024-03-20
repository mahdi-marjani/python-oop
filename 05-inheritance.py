#  Inheritance
class Car: # parent | superclass
    wheel = 4
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'I have a {self.name}')

class Motor(Car): # child | subclass
    wheel = 2

    def __init__(self, name, helmet):
        super().__init__(name)
        self.helmet = helmet

    def show(self):
        super().show() # Calls the show method of the parent class (Car) to display basic information about the vehicle.
        print(f'I ride {self.name}')

c = Car('pride')
c.show()

m = Motor('Honda', 'yes')
m.show()

