import math
#While Condition
counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1

#For condition-1

for item in [1,3,6,2,5]:
    print(item)

#For Condition-2
for item in range(5):
    print(item ** 2)


word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
        for a_letter in a_word:
            letter_list.append(a_letter)

print(letter_list) #O/P: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']


#If.. else
n=9
if n < 0:
    print("Sorry, value is negative")
else:
    print(math.sqrt(n)) #O/P: 3.0

score=35
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')


#If with abs()
n=-9
if n < 0:
    n = abs(n)
print(math.sqrt(n)) #O/P:3.0

#For with range
sq_list = []
for x in range(1, 11):# iterate till 1to 10
    sq_list.append(x * x)

print(sq_list) #O/P: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


'''
The variable x takes on the values 1 through 10 as specified by the for construct. The value
of x * x is then computed and added to the list that is being constructed. The general syntax
for a list comprehension also allows a selection criteria to be added so that only certain items
get added
'''
sq_list = [x * x for x in range(1, 11)]
print(sq_list)#O/P: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


sq_list = [x * x for x in range(1, 11) if x % 2 != 0]
print(sq_list) #O/P: [1, 9, 25, 49, 81]

print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou']) #O/P:['C', 'M', 'P', 'R', 'H', 'N', 'S', 'N']

#########################################################

word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
        for a_letter in a_word:
            letter_list.append(a_letter)
print(letter_list)

#Modify the given code so that the final list only contains a single copy of each letter
#the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

final_result=[ ]
for words in word_list:
    for letter in words:
        if not final_result.__contains__(letter):
            final_result.append(letter)

print(final_result) #O/P: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

#OR- another way

final_result=[ ]
for words in word_list:
    for letter in words:
        if letter not in final_result:
            final_result.append(letter)
print(final_result) #O/P: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
