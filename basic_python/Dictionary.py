capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals) #O/P:{'Iowa': 'DesMoines', 'Wisconsin': 'Madison'}
print(capitals['Iowa']) #O/P: DesMoines
capitals['Utah']='SaltLakeCity'
print(capitals) #O/P:{'Iowa': 'DesMoines', 'Wisconsin': 'Madison', 'Utah': 'SaltLakeCity'}
capitals['California']='Sacramento'
print(len(capitals)) #O/P: 4

for k in capitals:
    print(capitals[k]," is the capital of ", k)
    '''
    O/P:
    DesMoines  is the capital of  Iowa
    Madison  is the capital of  Wisconsin
    SaltLakeCity  is the capital of  Utah
    Sacramento  is the capital of  California
    '''
capitals['Iowa']='SaltLakeCity'
print(capitals) #O/P:{'Iowa': 'SaltLakeCity', 'Wisconsin': 'Madison', 'Utah': 'SaltLakeCity', 'California': 'Sacramento'}

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison','Iowa':'New Capital'}
print(capitals) #O/P:{'Iowa': 'New Capital', 'Wisconsin': 'Madison'}
key_List=capitals.keys()
print(key_List)#O/P dict_keys(['Iowa', 'Wisconsin'])

phone_ext={'david':1410, 'brad':1137}
print(phone_ext)#O/P:{'brad': 1137, 'david': 1410}
print(phone_ext.keys()) # Returns the keys of the dictionary phone_ext
#O/P:dict_keys(['brad', 'david'])

print(list(phone_ext.keys()))#O/P:['brad', 'david']

print("brad" in phone_ext)
#O/P:True
print(1137 in phone_ext)
#O/P False # 1137 is not a key in phone_ext
print(phone_ext.values())#O/P:dict_values([1137, 1410])# Returns the values of the dictionary
print(list(phone_ext.values()))#O/P:[1137, 1410]
print(phone_ext.items())#O/P: dict_items([('brad', 1137), ('david', 1410)])
print(list(phone_ext.items()))#O/P:[('brad', 1137), ('david', 1410)]
print(phone_ext.get("kent"))#O/P:None
print(phone_ext.get("kent","NO ENTRY")) #O/P:'NO ENTRY'
del phone_ext["david"]
print(phone_ext)#O/P:{'brad': 1137}