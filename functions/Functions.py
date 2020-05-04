
def function1():
    print("Inside Function1")
    print("Second line of Function1")

print("Outside Function1") # this will executed first

def function2(x):
    return 2*x

def function3(x,y):
    return x+y



#calling function
function1()
a=function2("4")
x=function2(4)
print(a,x)
sum=function3(5,5)
print(sum)
# calling function2() without argumnet will cause below error:
'''TypeError: function2() missing 1 required positional argument: 'x' '''




