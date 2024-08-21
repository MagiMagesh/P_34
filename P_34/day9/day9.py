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


# function:
    # 1. inbuilt function
    # 2. custom function
        # 1. def
        # 2. lambda

# print()
# type()
# len()
# int()
# float()
# list()


# function using def keyword:

# syntax for a function:
# def function_name():
#     function logic

def  hello():               # created a function
    print('Hello World')

hello()                     # calling a function
hello()
hello()


def  welcome():               # used to get input to a function            
    print('Hello! welcome')
welcome()


name = input("Enter your Name: ")

def  welcome(name):                 # name is called as positional arguments
    print(f'Hello {name}! welcome')

welcome('Magesh')
welcome('Dinesh')
welcome('Ram')


def  welcome(name,age):                 # name is called as positional arguments
    print(f'My name is {name}')
    print(f'My age is {age}')

welcome('Magesh',10)
print(10*'-')
welcome('Dinesh',11)
print(10*'-')
welcome('Ram',12)
print(10*'-')
welcome(11,'Magesh')

a = [1,2,3,4,5,6,7,8,9]
named_data = [111,121,131,141,51,36,4375,84356]
b = 0
for i in a:
    b = b + i
print(b)

# 1. i = 1, b = 0 , b = 0 + 1 = 1
# 2. i = 2, b = 1 , b = 1 + 2 = 3
# 2. i = 3, b = 3 , b = 3 + 3 = 6
# 2. i = 4, b = 6 , b = 6 + 4 = 10 ...