user_name = input("Please enter your name ")
print("Your name in all capitals is",user_name.upper(),"and has length", len(user_name))


user_radius = input("Please enter the radius of the circle ")
radius = float(user_radius)
diameter = 2 * radius
print(diameter)
'''
In the above example if you provide String will get below error:
radius = float(user_radius)
ValueError: could not convert string to float: 'a'
'''

print("Hello")
print("Hello","World") #O/P:Hello World
print("Hello","World", sep="***") #O/P:Hello***World
print("Hello","World", end="***")#O/P:Hello World***
print("Hello", end="***");
print("World") #O/P:Hello***World

name=input("Enter the name:")
age=input("Enter the age:")
converted_age=int(age)
print("%s is %d years old." % (name, converted_age))



price = 24
item = "banana"
print("The %s costs %d cents"%(item,price)) #O/P:The banana costs 24 cents
print("The %+10s costs %5.2f cents"%(item,price)) #O/P: The     banana costs 24.00 cents
print("The %+10s costs %10.2f cents"%(item,price)) #O/P:The     banana costs      24.00 cents
item_dict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%item_dict) #O/P:The banana costs    24.0 cents