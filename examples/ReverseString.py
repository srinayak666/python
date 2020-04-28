'''
write a function which takes 2 strings and return True if they are reverse of Each other
else
Fasle
'''

def check_Strings(str1,str2):
    if len(str1)==len(str2):
        reverse=True
        for i in range(len(str1)):
            j=len(str2)-i-1
            if str1[i]!=str2[j]:
                return False

        return True
    else:
        return False

print("Strings are equal : {}".format(check_Strings("ABC","CBA")))
print("Strings are equal : {}".format(check_Strings("ABC","CDBA")))
print("Strings are equal : {}".format(check_Strings("XYZA","AZYX")))



