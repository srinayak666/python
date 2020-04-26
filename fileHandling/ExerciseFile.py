'''

The file cities_and_times.txt contains city names and times.
Each line contains the name of the city, followed by the name of the day ("Sun") and the time in the form hh:mm.
Read in the file and create an alphabetically ordered list of the form:
[('Amsterdam', 'Sun', (8, 52)), ('Anchorage', 'Sat', (23, 52)), ('Ankara', 'Sun', (10, 52)), ('Athens', 'Sun', (9, 52)), ('Atlanta', 'Sun', (2, 52)), ('Auckland', 'Sun', (20, 52)), ('Barcelona', 'Sun', (8, 52)), ('Beirut', 'Sun', (9, 52)),

...

 ('Toronto', 'Sun', (2, 52)), ('Vancouver', 'Sun', (0, 52)), ('Vienna', 'Sun', (8, 52)), ('Warsaw', 'Sun', (8, 52)), ('Washington DC', 'Sun', (2, 52)), ('Winnipeg', 'Sun', (1, 52)), ('Zurich', 'Sun', (8, 52))]



Finally, the list should be dumped for later usage with the pickle module.

'''
import pickle

lines = open("cities_and_time.txt").readlines()
lines.sort()

cities = []
for line  in lines:
    *city, day, time = line.split()
    hours, minutes = time.split(":")
    cities.append((" ".join(city), day, (int(hours), int(minutes)) ))

fh = open("cities_and_times.pkl", "bw")
pickle.dump(cities, fh)
fh.close()
'''
City names can consist of multiple words like "Salt Lake City". 
That is why we have to use the asterisk in the line, in which we split a line. 
So city will be a list with the words of the city, e.g. ["Salt", "Lake", "City"].
 " ".join(city) turns such a list into a "proper" string with the city name, i.e. in our example "Salt Lake City".
'''

f = open("cities_and_times.pkl", "rb")
data = pickle.load(f)
print(data)
f.close()