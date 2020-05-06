'''


Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'

'''

def non_start(str1,str2):
    return str1[1:len(str1)]+str2[1:len(str2)]



print(non_start('Hello','There'))
print(non_start('java','code'))
print(non_start('shotl','java'))