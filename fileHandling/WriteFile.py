#Write to file
fobj_in = open("fileHandling_Notes/WriteFile.txt")
fobj_out = open("SampleTemp.txt","w")
i = 1
for line in fobj_in:
    print(line.rstrip())
    fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()

#writing with with statement
with open("example.txt", "w") as fh:
    fh.write("To write or not to write\nthat is the question!\n")
fh.close()
#Appending to Existing File
with open("example.txt", "a") as fh:
    fh.write("sample text is appended\nthat is the question!\n")
fh.close()