#Accessing List elements
tempList =["tommy","sommy","rani",1,2,3,1.0]
print(tempList[2]) #List index starts from 0 O/P:rani
print(tempList[-1]) #prints last index of list O/P: 1.0
print(tempList) #O/P:['tommy', 'sommy', 'rani', 1, 2, 3, 1.0]

#sublists
#Lists can have sublists as elements.
# These sublists may contain sublists as well, i.e. lists can be recursively constructed by sublist structures.
person = [["Jack","Sparrow"],["17, Oxford Str", "12345","London"],"07876-7876"]
name = person[0]
print(name) #prints 1st sublist O/P: ['Jack', 'Sparrow']
print(person[2]) #07876-7876
#print(person[3]) # IndexError: list index out of range

#Tuples
t = ("tuples", "are", "immutable")
print(t[2]) #O/P: immutable
#t[0]="They" #TypeError: 'tuple' object does not support item assignment
print(t) #O/P: ('tuples', 'are', 'immutable')


#Slicing
str = "Python is Scripting Language"
first_six=str[0:6]
print(first_six) # gets first six characters O/P: Python
print(str[:6]) # gets first six characters O/P: Python
print(str[5:]) # gets next characters starting from index 5 O/P: n is Scripting Language
print(str[:])#prints whole String O/P: Python is Scripting Language
print(str[5:-5]) #starting from 5th character and ignoring 5 characters from last O/P: n is Scripting Lan
print(str[0:-10])#Exclude last 10 characters O/P: Python is Scriptin
print(str[0:100])#prints whole String without error O/P: Python is Scripting Language
print(str[0:1])#prints first character O/P:P
print(str[-100:])#prints whole string O/P: Python is Scripting Language

cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
print(cities[1:4])# O/P: ['London', 'Paris', 'Berlin']
print(cities[0:-4])#O/P: ['Vienna', 'London']
print(cities[100:200])#O/P:[]
#Lists are similar to Strings in Slice operation.

#Slicing works with three arguments as well.
# If the third argument is for example 3, only every third element of the list, string or tuple from the range of the first two arguments will be taken.
str = "Python under Linux is great"
print(str[::3]) #prints every 3rd character in String O/P:Ph d n  e
print(str[::-2])#ignores all 2nd character from backwards and prints O/P: tegs ui en otP
print(str[::-1])#prints whole string reverse (character by character) O/P: taerg si xuniL rednu nohtyP

print(cities[::2])#even number cities ignored O/P:['Vienna', 'Paris', 'Zurich']
print(cities[::-2])#O/P:['Hamburg', 'Berlin', 'London']
print(cities[::200])#Prints only 1st city O/P: ['Vienna']
print(cities[::-200])#Prints only last city O/P: ['Hamburg']

#Length
#below are the two ways to get length
print(cities.__len__())# O/P: 6
len_cities= len(cities)
print(len_cities)#O/P: 6
subLists=[["Jack","Sparrow"],["17, Oxford Str", "12345","London"],"07876-7876"]
print(len(subLists))#O/P: 3











