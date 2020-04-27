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


# instantiate the object
blu = Parrot("Blu", 10)
gree =Parrot("Gree",12)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

# call our instance methods
print(gree.sing("'La La La'"))
print(gree.dance())