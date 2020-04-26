import shelve

#MyShelve is created in other program and accessing in this
s = shelve.open("MyShelve")
print(s["city"]) #O/P: Bangalore
print(s["street"])#O/P:M G Road
'''
print(s["streets"]) #wrong key name will cause error
#pos, siz = self._index[key]     # may raise KeyError keyError: b'streets'
'''