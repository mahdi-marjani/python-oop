# property

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def full_name(self):
        return f'{self.fname} {self.lname}'
    
    @property
    def email(self):
        return f'{self.fname}_{self.lname}@email.com'
    

a = Person('amir', 'big')

a.fname = 'mahdi'

print(a.fname)
print(a.lname)
print(a.full_name) # Method accessed like an attribute (without () in the end)
print(a.email) # Method accessed like an attribute (without () in the end)
