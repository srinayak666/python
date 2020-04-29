my_tuple = (2,True,4.96)
print(my_tuple) #O/P:(2, True, 4.96)
print(len(my_tuple)) #O/P:3
print(my_tuple[0]) #O/P:2
print(my_tuple * 3) #O/P:(2, True, 4.96, 2, True, 4.96, 2, True, 4.96)
print(my_tuple[0:2]) #O/P:(2, True)
'''
Below code cause error:
my_tuple[2]="X"
TypeError: 'tuple' object does not support item assignment
'''
