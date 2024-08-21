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
for i in shop:
    if i == 'cricket':
        print(shop[i])

print(10 * '-')

for i in shop:
    print(shop['cricket'])

# to print the values which are string data type:
shop = {"flowers":['Lily','Lotus','Jasmine'],"cricket":"sachin","place":"India","solar system":"Earth","Book":['harry','davin']}

for i in shop:
    if type(shop[i]) == str:
        print(shop[i])


shop = {"flowers":['Magesh','Lily','Lotus','Jasmine'],"cricket":"Magesh","place":"India","solar system":"Earth","Book":['harry','davin']}
print('Magesh' in shop) # False
print('cricket' in shop) # True

# FORMATTING:
# 1. to create a single string

i = 'Good'
a = 'Sa'

i = "Bad"
print('this is key: ',i,'| this is value: ', a)
a = 'Super'
b = f"this is key: {i} | this is value: {a}"
print(b)
c = 'Magesh'
print(b + c)

a = input("For Name: ")
b = input("For sex: ")
c = 'My name is ' + a + ' My sex is ' + b
d = f"My name is {a} My sex is {b}"
d = f"My name is {a} My age is {2*2.5*8-2/3}"
e = f"My name is {a} My age is {2*2.5*8-2/3 :.3f}"
ef = f"My name is {a} My age is {10/2 :.3f}" # important
print(c)
print(d)
print(e)
print(ef)

print(3.000)
print('3.000')

e = "My name is {} My age is {}".format(24,'Magesh') # positional values
print(e)

