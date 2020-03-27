#string common methods

#Get the index of a substring in a string
indexValue="someSTring".index("T")
print(indexValue) # REMEMBER- index starts from 0 so above output will be 5
#indexValue="someSTring".index("z")
#print(indexValue) # this will throw an error : ValueError: substring not found

#Test if a substring is a member of a larger string
find_r="r" in "someSTring"
print(find_r) #returns True if r is present
print("ng" in "someSTring" )
print("nig" in "someSTring" )


#Break a string based on some rule: split(rule) method
stringValue="1,2,3,4,5,6,7,8,9"
splitListOfString=stringValue.split(",")
print(splitListOfString) #A List will be returned (covered in future files)

#Access individual characters in a string.
stringData="This is some string data"
print(stringData[0])
#print(stringData[100]) #IndexError: string index out of range Error seen


# templating strings
#String object can be formatted. You can use %s as a formatter which will enable you to insert different values into a string at runtime and thus format the string.
# The %s symbol is replaced by whatever is passed to the string.
#keyword format can also be used. This will enable you to set your own formatters instead of %s
SomeString="I love %s in %s"
format="programming", "Python"
print(SomeString % (format))
print("I love {programming} in {python}".format(programming="programming", python="Python and Java"))


#A string is considered to be true in Python if it is not an empty string. So, we get the following
print(bool(""))
print(bool("ABC"))

# String upper and lowe case
someString="some string data"
print(someString.upper())
print(someString.upper().lower()+"xyz") #upper to lower and concatinate other string


#String consists of only alphanumeric characters (no symbols) - Returns Boolean
tempString="123ABCxyz"
print(tempString.isalnum())
print((tempString+"_").isalnum())

#String consists of only alphabetic characters (no symbols)
print(tempString.isalpha()) #False
print("AbcdEfg".isalpha()) #True

#String’s alphabetic characters are all lower case
print("tempString".islower()) #Flase
print("tempstring".islower()) #True
print("tempstring123".islower()) #True
print("tempString111".islower()) #Flase

#String consists of only numeric characters
print("tempString111".isnumeric()) #Flase
print("111".isnumeric()) #True

#String consists of only whitespace characters
print("temp String 111".isspace()) #Flase
print("".isspace()) #Flase
print("        ".isspace()) #True  one or more spaces

#String is in title case
print("temp String 111".istitle()) #Flase
print("Temp String".istitle()) #True
print("TempString".istitle()) #False
print("Tempstring".istitle()) #True
print("T E M P".istitle()) #True

#String’s alphabetic characters are all upper case
print("T E M P".isupper()) #True
print("T E M p".isupper()) #False
print("TEMP123".isupper()) #True

#Determining String Length
stringLen="someBigger STring with Space".__len__()
print(stringLen) # 28
print(len("some STring")) # 11


#join() and replace() Methods

#The str.join() method will concatenate two strings, but in a way that passes one string through another.
balloon = "Sammy has a balloon."
print("_".join(balloon)) # S_a_m_m_y_ _h_a_s_ _a_ _b_a_l_l_o_o_n_.

# reversed() method used to reverse the each character in String along with join() method
print(reversed("Tommy Tommy Yes Papa")) # this won't reverse the String O/P will be: <reversed object at 0x0000000001D7E2E0>
print("_".join(reversed(balloon))) #._n_o_o_l_l_a_b_ _a_ _s_a_h_ _y_m_m_a_S


#The str.replace() method can take an original string and return an updated string with some replacement.
print(balloon.replace("has","had")) #Sammy had a balloon.


