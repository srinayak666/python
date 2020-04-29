class Parrot:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {} having age {}".format(self.name, song,self.age)

    def dance(self):
        return "{} is now dancing".format(self.name)
    def __str__(self):
        return str(self.name)+"---"+str(self.age)


# instantiate the object
blu = Parrot("Blu", 10)
gree =Parrot("Gree",12)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

# call our instance methods
print(gree.sing("'La La La'"))
print(gree.dance())
print(blu.__str__()) #O/P: <__main__.Parrot object at 0x00DA1FB8>
# we can print actual data by overriding __str__ method in class
print(blu)# object can be printed like this O/P:

