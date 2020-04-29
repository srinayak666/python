my_set={3,6,3,"cat",4.5,False}
print(my_set)#O/P:{False, 3, 4.5, 6, 'cat'}
print(len(my_set)) #O/P:5
print(False in my_set) #O/P: True
print("dog" in my_set) #O/P: False
your_set = {99,3,100}
result_Set=my_set.union(your_set)
print(result_Set)#O/P:{False, 3, 4.5, 6, 99, 'cat', 100}
result_Set=my_set | your_set
print(result_Set)#O/P:{False, 3, 4.5, 6, 99, 'cat', 100}
result_Set= my_set.intersection(your_set)
print(result_Set)#O/P:{3}
result_Set=my_set & your_set
print(result_Set)#O/P:{3}
result_Set=my_set.difference(your_set)
print(result_Set)#O/P:{False, 4.5, 6, 'cat'}
result_Set= my_set - your_set
print(result_Set)#O/P:{False, 4.5, 6, 'cat'}
result_Set= {3,100}.issubset(your_set)
print(result_Set)#O/P:True
result_Set= {3,100} <= your_set
print(result_Set)#O/P:True
my_set.add("house")
print(my_set) #O/P:{False, 3, 4.5, 6, 'house', 'cat'}
my_set.remove(4.5)
print(my_set) #O/P:{False, 3, 6, 'house', 'cat'}

print(my_set.pop()) #O/P:False

print(my_set)#O/P:{3, 6, 'house', 'cat'}
my_set.clear()
print(my_set)#O/P:set()