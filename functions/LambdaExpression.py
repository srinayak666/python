
#LambdaExpressions
'''
Consider a situation where you don't want to perform much computation in a function.
In such a situation writing a full-fledged function doesn't make sense. To solve this we use a lambda expression or lambda function.

So what is a lambda expression?
It is an anonymous function and they are restricted to a single expression.
The lambda expression can take n number of arguments.

The syntax for lambda expression is:

variable = lambda arguments: operation

'''

sum = lambda a: a + 10

'''
Here we have declared a variable sum which we are using to call the lambda function.
 'a' represents the argument that is passed to that function.
'''

print(sum(5)) #O/P will be 15

squares=[]
for x in range(0,10):
    squares.append(x**2)
print(squares)

#the above squares can be derived using lambda expressions

squares = list(map(lambda x: x**2, range(10)))
#Here we are using list constructor to build a list and inside that lambda function which squares out the number.
print(squares)


#Another way
squares = list(x**2 for x in range(10))
print(squares)

'''
What about when we have a condition where we want a set of two numbers that are the same? 
Well, we need to write two for loops and one if loop.

'''
num_list = []
for i in range(10):
    for j in range(10):
            if i == j:
                num_list.append((i,j))

print(num_list)

num_list = list((i,j) for i in range(5) for j in range(6) if i == j)
print(num_list)


