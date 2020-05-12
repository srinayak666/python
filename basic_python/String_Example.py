import time
import datetime
start_time = time.time()
print("David") #O/P: David
my_name = "DaviHCL d"
print(my_name[3]) #O/P: i
print(my_name.upper()) #O/P: DAVID
print(my_name.center(10))#O/P:   David
print(my_name.find('v'))#O/P:2
print(my_name.split('v'))#O/P:['Da', 'id']

time.sleep(10)
print(my_name)
my_list=[1, 3, True, 6.5]
my_list[0]=2**10
print(my_list[0]) #O/P:1024
#my_name[0]='X' #
#O/P:   my_name[0]='X'
#TypeError: 'str' object does not support item assignment
stri="/App/GG ji/jui"
st=stri.replace('pp','HCL\\',1)
print(f"my_name: {st}")

string="/Applications/HCL Notes.app/Contents/MacOS/libadvutil.dylib: valid on disk"
print(string.index(':'))
res=string[string.index(':'):len(string)]
print(res)






total_time_in_secs=time.time() - start_time
conversion = datetime.timedelta(seconds=total_time_in_secs)
converted_time = str(conversion)
print(f"Total Time taken to execute Script: {converted_time}")