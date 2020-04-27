# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__() # this will call parent constructor
        print("Penguin is ready")
        self.name="Peggy"

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster {}".format(self.name))

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()