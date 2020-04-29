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
      raise RuntimeError("You can't use a negative number")
    else:
        print(math.sqrt(a_number))
        '''
        line 13, in <module>
    raise RuntimeError("You can't use a negative number")
RuntimeError: You can't use a negative number
        '''