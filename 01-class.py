class Car: # blueprint --> General state
    pass

a = Car() # object | instance
b = Car()

a.name = 'pride' # attribute | property
b.name = 'benz'

a.price = 100
b.price = 900 # (.) --> dot notation

print(f'{a.name} costs {a.price}')
print(f'{b.name} costs {b.price}')