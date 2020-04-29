#Numbers - Integers and Floating Point Numbers
#Strings
#Python is completely object oriented, and not "statically typed".
# You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

#Python supports two types of numbers - integers and floating point numbers.

#isinstance(variable,type) method will check if its of which data type
#type() method used to get class of the vaiable declared

integerNumber=100 #integer Number
print(integerNumber)

floatingPointNumber=100.99 #floating Point Number
print(floatingPointNumber)

stringObject="hello Python" #String
print(stringObject)

otherString='Hello World' #single quote can be used for Strings
print(otherString)

stringObject=99.0
print(stringObject)

print(integerNumber+floatingPointNumber) #adding floating point and integer results in Floating Point

#print(integerNumber+otherString) # results in error : TypeError: unsupported operand type(s) for +: 'int' and 'str'

a,b,c=2,3,4 # valid declaration
print(a,b,c)

#a,b,c=2,3,4,5 # this will cause error: ValueError: too many values to unpack (expected 3)

print(isinstance(a,int)) # return true is its of type int
print(isinstance(a,str))
print(isinstance(floatingPointNumber,float))

print(type(a))
print(type(floatingPointNumber))

print((54).__add__(21)) # O/P: 75