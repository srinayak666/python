import math
try:
    a_number=-100
    print(math.sqrt(a_number))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(a_number)))

#This means that the program will not terminate but instead will continue on to the next statements.

    if a_number < 0:
        print(a_number)
     # raise RuntimeError("You can't use a negative number")
    else:
        print(math.sqrt(a_number))
        '''
        line 13, in <module>
    raise RuntimeError("You can't use a negative number")
RuntimeError: You can't use a negative number
        '''
a_number=-99
if a_number < 0:
    print(a_number)
    try:
        a_number/0
    except(RuntimeError,ValueError,ZeroDivisionError):
        print("Error Occured")
    else:
        print(math.sqrt(a_number))

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

