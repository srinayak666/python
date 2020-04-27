
def function1():
    print("Inside Function1")
    print("Second line of Function1")

print("Outside Function1") # this will executed first

def function2(x):
    return 2*x


#calling function
function1()
print(function2(4))