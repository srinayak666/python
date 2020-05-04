'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

'''


def string_bits(str):
    str_final=str[0]
    for i in range(1,len(str)):
        if i%2==0:
            str_final+=str[i]

    return str_final

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))