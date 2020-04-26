import pickle

'''
AttributeError: partially initialized module 'pickle' has no attribute 'dump' (most likely due to a circular import)
this error is seen when this file is named as pickle.py so renamed it as pickleExample.py
'''
cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
fh = open("data.pkl", "bw")
pickle.dump(cities, fh)
fh.close()

f = open("data.pkl", "rb")
villes = pickle.load(f)
print(villes) #O/P: ['Paris', 'Dijon', 'Lyon', 'Strasbourg']
#Only the objects and not their names are saved.
# That's why we use the assignment to villes in the previous example, i.e. data = pickle.load(f).

#In our previous example, we had pickled only one object, i.e. a list of French cities.
# But what about pickling multiple objects?
# The solution is easy: We pack the objects into another object, so we will only have to pickle one object again.
# We will pack two lists "programming_languages" and "python_dialects" into a list pickle_objects in the following example:


fh = open("data.pkl","bw")
programming_languages = ["Python", "Perl", "C++", "Java", "Lisp"]
python_dialects = ["Jython", "IronPython", "CPython"]
pickle_object = (programming_languages, python_dialects)
pickle.dump(pickle_object,fh)
fh.close()

f = open("data.pkl", "rb")
villes = pickle.load(f)
print(villes)
f.close()

#The pickled data from the previous example, -
# i.e. the data which we have written to the file data.pkl, - can be separated into two lists again,
# when we read back in again the data:

f = open("data.pkl","rb")
(languages, dialects) = pickle.load(f)
print(languages, dialects)


