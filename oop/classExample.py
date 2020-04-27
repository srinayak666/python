class Parrot:
    type="bird" #this is class attribute

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
woo.type="Animal"

# access the class attributes
print("Blu is a {}".format(blu.__class__.type))
print("Woo is also a {}".format(woo.__class__.type))
print("class Attribute can also be accessed as:"+blu.type)
print("class Attribute can also be accessed as:"+woo.type)
'''The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}

txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'am {1}".format("John",36)
txt3 = "My name is {}, I'am {}".format("John",36)

'''

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
