'''
Functools module:
-these are for higher order functions
-i.e, functions take functions as arguments, manipulate them and even return them as output



'''
#########################################################################################################################
from functools import reduce
#reduce() function
#originally not part of functools module; later from python 3 its added
#find sum of all the elements in list

'''
Reduce
It applies a function of two arguments repeatedly on the elements of a sequence so as to reduce the sequence to a single value. 
For example, reduce(lambda x, y: x^y, [1, 2, 3, 4]) calculates (((1^2)^3)^4). If the initial is present, it is placed first in the calculation, and if the default result when the sequence is empty.

Syntax :
reduce(function, sequence[, initial]) -> value

'''
list_=[1,2,3,4,5]
print("Sum of list {}".format(reduce(lambda a,b:a+b,list_))) #O/P:15
print("Sum of list with initiator 10 {}".format(reduce(lambda a,b:a+b,list_,10))) #O/P:25 providing 10 as initiator so 1st element will be added with 10 then so on...
print("Max value in the list {}".format(reduce(lambda a,b:max(a,b),list_))) #O/P:55


#########################################################################################################################
'''
Total_ordering
It is a class decorator that fills in the missing comparison methods (__lt__, __gt__, __eq__, __le__, __ge__). 
If a class is given which defines one or more comparison methods, 
"@total_ordering" automatically supplies the rest as per the given definitions.

However, the class must define one of __lt__(),__le__(),__gt__(), or __ge__() and aditionally,
 the class should supply an __eq__() method.


note:Slow's down the execution

'''
from functools import total_ordering 
@total_ordering # when we put this annotation remaining functins will be automatically generated
class N: 
    def __init__(self, value): 
        self.value = value 
    def __eq__(self, other): 
        return self.value == other.value 

    # Reverse the function of 
    # '<' operator and accordingly 
    # other rich comparison operators 
    # due to total_ordering decorator 
    def __lt__(self, other): 
        return self.value > other.value 


print('6 > 2 :', N(6)>N(2)) 
print('3 < 1 :', N(3)<N(1)) 
print('2 <= 7 :', N(2)<= N(7)) 
print('9 >= 10 :', N(9)>= N(10)) 
print('5 == 5 :', N(5)== N(5)) 


'''
#########################################################################################################################
@functools.cached_property(func)

Transform a method of a class into a property whose value is computed once and then cached as a normal attribute for the life of the instance. 
Similar to property(), with the addition of caching.
 Useful for expensive computed properties of instances that are otherwise effectively immutable.
 introduced in python 3.8
'''

from functools import cached_property

class Studentmarks:
    def __init__(self,*grades):
        self.grades=grades
    
    @cached_property
    def sum_total(self):
        print("calculating sum....")
        return sum(self.grades)
    
    @cached_property
    def avg(self):
        print("calculating avg....")
        return self.sum_total/len(self.grades)
        

stumarks=Studentmarks(10,20,30,140)
print(stumarks.sum_total) #no need to call method ; 1st time data will be calculated and saved in cache
print(stumarks.avg)
'''
above output will be:

calculating sum....
200
calculating avg....
50.0

'''

print(stumarks.sum_total)
print(stumarks.avg)
'''
above output will be:

200
50.0

'''
#########################################################################################################################
'''
lru_cache

LRU_cache is a function decorator used for saving up to the maxsize most recent calls of a function. 
This can save time and memory in case of repeated calls with the same arguments.
If *maxsize* is set to None, the cache can grow without bound. 
If *typed* is True, arguments of different data types will be cached separately. 

For example, f(1.0) and f(1) will be memoized distinctly.

Syntax :

lru_cache(maxsize=128, typed=False)

'''

from functools import lru_cache 

def fib(n):
    if n<2:
        return n
    print(f"calculating fib {n} ")
    return fib(n-1)+fib(n-2)


print([fib(x) for x in range(10)])
#without using lru_cache, you can observe in console fib(2) is calculated multiple times


@lru_cache(maxsize=None)
def fib(n):
    if n<2:
        return n
    print(f"calculating fib {n} ")
    return fib(n-1)+fib(n-2)

print(f"using @lru_cache::",[fib(x) for x in range(10)]) #fib(2) is not calculated again
print(fib.cache_info())

@lru_cache(maxsize = None) 
def factorial(n): 
    if n<= 1: 
        return 1
    return n * factorial(n-1) 

print([factorial(n) for n in range(7)]) 
print(factorial.cache_info()) 

'''
CacheInfo(hits=5, misses=7, maxsize=None, currsize=7)

hits: value is in cache
misses: no value in cache so it need to be computed again

'''
#########################################################################################################################

'''
A partial function is an original function for particular argument values. 
They can be created in Python by using "partial" from the functools library. 
The __name__ and __doc__ attributes are to be created by the programmer as they are not created automatically. Objects created by partial() have three read-only attributes:

Syntax:

partial(func[, *args][, **keywords])
partial.func -It returns the name of parent function along with hexadecimal address.
partial.args - It returns the positional arguments provided in partial function.
partial.keywords - It returns the keyword arguments provided in partial function.

'''

from functools import partial

def add(a,b):
    print(f"value of a: {a} and value of b:{b}")
    return a+b

add_one=partial(add,3)
#can also specify the param
add_one_again=partial(add,b=30)
'''
add_for_a=partial(add,a=90)
add_for_a(30) -> This will cause error 

   add_for_a(30)
TypeError: add() got multiple values for argument 'a'
'''
add_par=add_one(5)
print(f"Using partial funtion : {add_par}")
print(f"Using partial funtion : {add_one_again(100)}")



#########################################################################################################################

'''
wraps

Wraps
It is a function decorator which applies update_wrapper() to the decorated function. 
It is equivalent to partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).




'''

from functools import wraps 

def decorator(f): 
    @wraps(f) 
    def decorated(*args, **kwargs): 
        """Decorator's docstring"""
        return f(*args, **kwargs) 

    print('Documentation of decorated :', decorated.__doc__) 
    return decorated 

@decorator
def f(x): 
    """f's Docstring"""
    return x 

print('f name :', f.__name__) 
print('Documentation of f :', f.__doc__) 
########################################################################################################################


'''

SingleDispatch
It is a function decorator. 
It transforms a function into a generic function so that it can have different behaviors depending upon the type of its first argument. 
It is used for function overloading, the overloaded implementations are registered using the register() attribute of the
'''
from functools import singledispatch 

@singledispatch
def fun(obj): 
    print(obj) 
    
@fun.register(int) 
def _(obj): 
    print(obj * 2) 

@fun.register(list)
def _(obj):
    obj.append("object")
    print(obj)

fun('GeeksforGeeks') 
fun(10) 
lst=[1,2,3,4,5]
fun(lst)






