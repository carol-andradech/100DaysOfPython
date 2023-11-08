# Advanced arguments -  default values
# Unlimited arguments
# Tye of args is a tuple
# Collect all of the arguments in a tuple
def add(*args):
    print(args[0])
    sum=0
    for n in args:
        sum+=n
    print(sum)

add(3,4,5,6)

# kwargs: Many keyworded arguments
# kwargs type is a dictionary. key:value
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-8")
print(my_car.model)