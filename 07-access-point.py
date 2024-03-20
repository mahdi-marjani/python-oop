'''
    Access point --> public, protected, private
'''

class Person:
    name = 'mahdi' # public (Can be accessed from anywhere)
    _age = 18      # protected (Accessible within the class and its subclasses)
    __height = 180 # private (Accessible only within the class)

    def __show():
        print('this show method is private')

class Male(Person):
    pass

print(Person.name)
print(Person._age) # warning
print(Person._Person__height) # name mangling

Person._Person__show()