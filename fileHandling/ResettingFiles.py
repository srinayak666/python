#Resetting the Files Current Position
fh = open("sampleTestFIle.txt")
print(fh.tell())#fh.tell() returns int value
data=fh.read(37)
print(fh.tell())
print("Data from file reading till 37 position:"+data)
print(fh.tell())
print(fh.read(5)) #reads from 37th position to 5 places
fh.seek(91) #seek to position 91
print(fh.read(6))
print(fh.tell())
fh.seek(fh.tell()-6) #set the current position 6 characters to the left
print(fh.read(5))
fh.seek(fh.tell() + 29) # now, we will advance 29 characters to the 'right' relative to the current position:
print(fh.read(10))
