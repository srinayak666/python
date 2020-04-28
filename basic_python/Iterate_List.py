#Two ways to iterate elements in List
a= ["item1","item2","item3"]
for elem in a:#first method use normal for loop
    print(elem)



#to understand the 2nd way- need to know what range function does
for i in range(len(a)):
    print("Data from list={} with index {}".format(a[i],i))
