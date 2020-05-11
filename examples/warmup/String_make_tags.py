'''


The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'

reduce() in Python
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working : 

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.

# python code to demonstrate working of reduce() 

# importing functools for reduce() 
import functools 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 

# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 

'''
import functools
from _functools import reduce

def make_tag(tag,str):
    list_tags=getTag(tag)
    swap_list_index(list_tags,str)
    return functools.reduce(lambda x,y: x+y, list_tags) #converting list to string
    

def getTag(tag):
    lst_tags=[]
    lst_tags.append('<'+tag+'>')
    lst_tags.append('</'+tag+'>')
    return lst_tags

def swap_list_index(list_tags,str):
    first_index=list_tags[1]
    list_tags[1]=str
    list_tags.append(first_index)



print(make_tag('i','Hello'))
print(make_tag('i', 'Yay'))
print(make_tag('cite', 'Yay'))


#reduce examples
def reduce_Example():
    _list=[1,2,3,4,56,6,7,8,9,11,32,43,54,223,9,0,8,6,5,4] #getting biggest number in list
    largest=reduce(lambda a,b:a if a>b else b,_list)
    print("largest element in list is {}".format(largest))
    _list.remove(largest)
    print("second largest element {}".format(reduce(lambda a,b:a if a>b else b,_list)))


reduce_Example()