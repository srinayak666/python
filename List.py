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

#Concatenation of Sequences
firstname="Tom"
lastname="jerry"
print(firstname+" "+lastname) #O/P:Tom jerry

colours1=["red","blue"]
colours2=["orange"]
finalColours=colours1+colours2
print(finalColours) #O/P: ['red', 'blue', 'orange']
colours1+=colours2
print(colours1) #O/P:['red', 'blue', 'orange']


#Checking if an Element is Contained in List
characters=['a','b','c',"x","y"]
print('z' in characters) #O/P: False

print('a' in characters) #O/P: True

print('x' not in characters)#O/P: False



#Repetitions (*)
repeatList=["jan","feb","march"]
print(2*repeatList) #O/P:['jan', 'feb', 'march', 'jan', 'feb', 'march']
print(3*"Hello"+"-") # O/P: HelloHelloHello-
print("Hi-"*4) #O/P:Hi-Hi-Hi-Hi-
print(4*4) #O/P: 16

testList=["a","b","c"]
multipleList=[testList]*2
print(multipleList) #O/P:[['a', 'b', 'c'], ['a', 'b', 'c']]

multipleList[0][0]="z"
print(multipleList) #O/P:[['z', 'b', 'c'], ['z', 'b', 'c']]

################################################################################################################
#pop and append
fruitList=["apple","orange"]
returnValueOfappend=fruitList.append("banana")
print(fruitList) #O/P:['apple', 'orange', 'banana']
print(returnValueOfappend) #O/P:None

popFruit=fruitList.pop();
print(popFruit)#O/P:banana
print(fruitList) #O/P: ['apple', 'orange']


#extend
listNumbers1=[1,2,3,4,5,6]
listNumbers2=[7,8,9]
listNumbers1.extend(listNumbers2)
print(listNumbers1) #O/P:[1, 2, 3, 4, 5, 6, 7, 8, 9]
listNumbers1.extend([0,0,0])
print(listNumbers1)#O/P:[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0]

someString="Hello"
listNumbers2.extend(someString)
print(listNumbers2) #O/P: [7, 8, 9, 'H', 'e', 'l', 'l', 'o']

listDigi=[1,3,5,6,8]
tupleAlpha=('a','b','bo')
listDigi.extend(tupleAlpha)
print(listDigi)#O/P: [1, 3, 5, 6, 8, 'a', 'b', 'bo']

#Extending and Appending Lists with the '+'-Operator
level = ["beginner", "intermediate", "advanced"]
other_words = ["novice", "expert"]
print(level + other_words)#O/P:['beginner', 'intermediate', 'advanced', 'novice', 'expert']
level+=["super expert"]
print(level)#O/P:['beginner', 'intermediate', 'advanced', 'super expert']

#We will compare in the following example the different approaches and calculate their run times.
# To understand the following program, you need to know that time.time() returns a float number,
# the time in seconds time.time() - start_time calculates the time in seconds consumed for the for loops
import time

n= 100000


start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]
print(time.time() - start_time)

start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
print(time.time() - start_time)

start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print(time.time() - start_time)

#O/P:
#13.497818946838379
#0.02602219581604004
#0.023516416549682617

#We can see that the "+" operator is about 1268 slower than the append method.
# The explanation is easy: If we use the append method, we will simply append a further element to the list in each loop pass.
# Now we come to the first loop, in which we use l = l + [i * 2]. The list will be copied in every loop pass.
# The new element will be added to the copy of the list and result will be reassigned to the variable l.
# After this the old list will have to be removed by Python, because it is not referenced anymore.
# We can also see that the version with the augmented assignment ("+="), the loop in the middle, is only slightly slower than the version using "append".

#Removing an element with remove

colours = ["red", "green", "blue", "green", "yellow"]
removedColor=colours.remove("yellow")
print(removedColor) #O/P:None
print(colours)#O/P:['red', 'green', 'blue', 'green']
#colours.remove("yellow") #O/P:  colours.remove("yellow") ValueError: list.remove(x): x not in list

colours.remove("green") #removes the first occurance of green
print(colours) #O/P:['red', 'blue', 'green']

#Find the Position of an Element in a List
colours = ["red", "green", "blue", "green", "yellow"]
print(colours.index("green")) #O/P:1
print(colours.index("green",2))#O/P:3
print(colours.index("green",3,4))#O/P:3
#print(colours.index("green",4,8))#O/P:print(colours.index("green",4,8))#O/P:3 ValueError: 'green' is not in list
print(colours.index("green",0,len(colours)))#O/P:1

#insert
lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
lst.insert(3, "and")
print(lst)#O/P:['German is spoken', 'in Germany,', 'Austria', 'and', 'Switzerland']
lst.insert(100,"hello")
print(lst) #O/P:['German is spoken', 'in Germany,', 'Austria', 'and', 'Switzerland', 'hello']


#Shallow and Deep Copy
x=3
y=x
print(id(x) ,id(y)) #O/P: 1669986256 1669986256
y=3
print(id(x) ,id(y)) #O/P: 1669986256 1669986256
y=30
print(id(x) ,id(y)) #O/P: 1669986256 1669986688
print(x,y) #O/P:3 30

list1=[1,2,3]
list2=[1,2,3]
print(id(list1),id(list2))#O/P:20736488 20736552
list2=list1
print(id(list1),id(list2))#O/P:12413416 12413416
list1[1]=100;
print(list1)#O/P:[1, 100, 3]
print(id(list1),id(list2))#O/P:51145192 51145192
print(list2)#O/P:[1, 100, 3]

#Copy with the Slice Operator
list1 = ['a','b','c','d']
list2 = list1[:]
print(id(list1),id(list2))#O/P:45443624 45443688
list2[1] = 'x'
print(list1)#O/P:['a', 'b', 'c', 'd']
print(list2)#O/P:['a', 'x', 'c', 'd']
print(id(list1),id(list2))#O/P:45443624 45443688

lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[0] = 'c'
print(lst1) #O/P:['a', 'b', ['ab', 'ba']]
print(lst2) #O/P:['c', 'b', ['ab', 'ba']]

lst2[2][1]="Z" #only reference of sublist is copied not the complete sublist
print(lst1) #O/P:['a', 'b', ['ab', 'Z']]
print(lst2) #O/P:['c', 'b', ['ab', 'Z']]

#Using the Method deepcopy from the Module copy

from copy import deepcopy
lst1 = ['a','b',['ab','ba']]
lst2 = deepcopy(lst1)
print(lst1) #O/P:['a', 'b', ['ab', 'ba']]
print(lst2) #O/P:['a', 'b', ['ab', 'ba']]
print(id(lst1),id(lst2)) #O/P:31940520 23423624
print(id(lst1[2]),id(lst2[2])) #O/P:23423784 31940328

lst2[2][0]="XYZ"
print(lst2)#O/P:['a', 'b', ['XYZ', 'ba']]
print(lst1)#O/P:['a', 'b', ['ab', 'ba']]
print(id(lst1[2]),id(lst2[2])) #O/P:46689064 48070440





































