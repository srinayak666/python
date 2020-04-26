import shelve

s = shelve.open("MyShelve")
s["city"]="Bangalore"
s["street"]="M G Road"

for key in s:
    print(key) #o/p: city street



print(dict(s)) # prints as dictionary O/P:{'city': 'Bangalore', 'street': 'M G Road'}
s.close()

#Example

tele = shelve.open("MyPhoneBook")
tele["Mike"] = {"first":"Mike", "last":"Miller", "phone":"4689"}
tele["Steve"] = {"first":"Stephan", "last":"Burns", "phone":"8745"}
tele["Eve"] = {"first":"Eve", "last":"Naomi", "phone":"9069"}
print(tele["Eve"]["phone"])
