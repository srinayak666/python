file = open("fileHandling_Notes/Reading_in_one_go.txt").readlines()
print(file) #read as List

file = open("fileHandling_Notes/Reading_in_one_go.txt").read()
print(file) #read as String

print("Slicing String index starting at 16 and ending at 34:--"+file[16:34])
