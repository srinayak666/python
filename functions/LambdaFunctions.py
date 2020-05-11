


n=[1,2,2,3]
sum=lambda x,y: x+y
max=lambda x,y: x if x>y else y

square_lambda=lambda x:x**2
square_list=list(map(square_lambda,n))

def squares_of_list(list_data):
    return list(map(square_lambda,list_data))

greater_than_10Filter=lambda x: x>10
even_number_filter=lambda x:x%2==0

def filter_example(list_data,filter_):
    return list(filter(filter_,list_data))


from functools import reduce
reduce_data_filter_1=lambda x,y:x+y
reduce_data_filter_2=lambda x,y:x*y

def reduce_example(list_data,reduce_filter):
    return reduce(reduce_filter,list_data) #It was moved to functools.

print(f"sum-1: {sum(10,20)}")
print(f"sum-2: {sum(10,y=11)}")


print(f"Max-1: {max(10,y=11)}")
print(f"Max-2: {max(10,101)}")

print(square_list)
print(f"squares of List: {squares_of_list([4,3,2,1])}")

print(f"Filter List-1: {filter_example([4,3,20,1],greater_than_10Filter)}")
print(f"Filter List-2: {filter_example([4,3,20,1],even_number_filter)}")


print([x for x in n if x>2] )

print(f"Reduce List-2: {reduce_example([4,3,2,1],reduce_data_filter_1)}")
print(f"Reduce List-2: {reduce_example([4,3,2,1],reduce_data_filter_2)}")






