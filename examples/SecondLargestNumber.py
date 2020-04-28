'''

/*
 * Write a program to return second largest number in the list of integers
 *
 * if list is empty or has only 1 element return 0
 */
'''


def secondLargestNumber(a):
    if(len(a)<2):
        return None
    largest=a[0]
    second_largest=a[1]
    for i in a:
        if(i>largest):
            second_largest=largest
            largest=i
        elif(i>second_largest and i<largest):
            second_largest=i
    return  second_largest



arrList=[4,2,3,1,0,10]
arrList_1=[-4,-2,-3,-1,0,10]
arrList_=[2]
second_largest=secondLargestNumber(arrList)
print("Second Largest Number is TEST-1 {} ".format(second_largest))
print("Second Largest Number is TEST-2 {} ".format(secondLargestNumber(arrList_1)))
print("Second Largest Number is TEST-3 {} ".format(secondLargestNumber(arrList_)))






