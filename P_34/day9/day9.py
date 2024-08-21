d = {'key':'value','key2':'value2','key3':'value3',1:['value',2.1,'value2']}
print(d[1])
print(d[1][1])

# whenever we use for loop it will take only the keys  from that key-value pair in dict.

d = {'key':'value','key2':'value2','key3':'value3',1:['value',2.1,'value2']}
for i in d:
    print(i) # is is key

# 'key'
# 'key2'
# 'key3'
# 1

d = {'key':'value','key2':'value2','key3':'value3',1:['value',2.1,'value2']}
for i in d:
    print('this is key: ',i,'| this is value: ', d[i])

shop = {"flowers":['Lily','Lotus','Jasmine'],"cricket":"sachin","Book":['harry','davin']}