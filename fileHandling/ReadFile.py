fileObj=open("fileHandling_Notes/ReadFile.txt","r")
for line in fileObj:
    print(line.rstrip())
fileObj.close()


'''rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed). 
        If no argument is passed, it removes trailing spaces.
        Syntax :string.rstrip([chars])'''
##################################################################################################
#Other examples of rstrip()
string = "pythonnnnn"
# Removes given set of characters from
# right.
print("remove n:--"+string.rstrip('n'))

# string which is to be stripped
string = "   is    "

# Leading whitespaces are removed
print("Python" + string.rstrip() + " Python ")

# string which is to be stripped
string = "python is super language"
# So, no characters are removed
print("String Not stripped:-"+string.rstrip('g')) # Argument doesn't contain trailing 'e'

# string which is to be stripped
string = "python is hot"


print(string.rstrip('toh'))# Removes given set of characters from right.
print(string.rstrip('tgh'))# removes only matching character from the end.
