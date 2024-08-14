# .isupper()
# .islower()
# .isalnum
# .isalpha
# .isdigit
# strip, rstrip, lstrip
# join


# .split


# .isupper() output will be in bool - wether all the alphabtes in that string is Uppercase
# .islower() output will be in bool - wether all the alphabtes in that string is LowerCase
# .isalnum() output will be in bool - wether all the element in that string is either alphabtes (A-Za-z0-9)
# .isalpha() output will be in bool - wether all the element in that string is alphabtes
# .isdigit() output will be in bool - wether all the element in that string is number

a = 'I live in India'
print(a.isalnum()) # False - space is not alphabets or number

a = 'India'
print(a.isalnum()) # True

a = 'It234is345abigs345enten345ce'
print(a.isalnum()) # True

a = 'It234is345abigs345enten345ce'
print(a.isalpha()) # False

a = '234324534534'
print(a.isalnum()) # True

a = '234324534534'
print(a.isdigit()) # True

a = '234324534534'
print(a.isdecimal()) # True

a = '2343245.34534'
print(a.isdecimal()) # False


a = 'HI THIS IS MAGESH'
print(a.isupper()) # True


a = 'HI TH2343IS IS 234234MAGESH'
print(a.isupper()) # True

a = 'HI TH2343iS IS 234234MAGESH'
print(a.isupper()) # False


a = 'i live in india'
print(a.islower()) # True


# strip:
# it will remove only from the right & left extremes substring
# it will remove the substring given inside it
# if im not giving the substring by defualt it will be space


a = '    i live in india     '
print(a.strip(' ')) # 'i live in india'

a = ',,,,,,i live in india,,,,,'
print(a.strip(',')) # 'i live in india'


a = ',,,I,,,i live in india,,I,,,'
print(a.strip(',')) # 'I,,,i live in india,,I'

a = '    i live in india     '
print(a.strip()) # 'i live in india'

a = '    i live in india     '
print(a.rstrip()) # 'i live in india'


# rstrip:
# it will remove substring only from the right extremes 
a = ',,,I,,,i live in india,,I,,,'
print(a.rstrip(',')) # ',,,I,,,i live in india,,I'

# lstrip:
# it will remove substring only from the left extremes 
a = ',,,I,,,i live in india,,I,,,'
print(a.lstrip(',')) # 'I,,,i live in india,,I,,,'


# join:
# a substring will be added in between all the elemts of string

# sytax:
# 'substring'.join(str_element)

a = 'Magesh'
print('-'.join(a)) # M-a-g-e-s-h


# str()
# str_data.upper()
# str_data.lower()
# str_data.capitalize()
# str_data.title()
# str_data.startswith()
# str_data.endswith()
# str_data.count()
# str_data.index()
# str_data.find()
# str_data.isupper()
# str_data.islower()
# str_data.isalnum()
# str_data.isalpha()
# str_data.isdigit()
# str_data.strip(), rstrip, lstrip
# ''.join(str_data)
# + -> concatenate

# str(): '' Empty string
print(str()) # ''
print('')

# it can convert any data type to str

a = 123123
b = str(a)
print(type(a)) # int
print(type(b)) # str


a = 123123.2345324
b = str(a)
print(type(a)) # float
print(type(b)) # str

a = 'India'
b = 'Cricket'
print(a + b) # 'IndiaCricket'
print(b + a) # 'CricketIndia'

a = '10'
b = '20'
c = a+b
print(c) # 1020
print(type(c)) # str


a = 10
b = '20'
c = a+b # Error


a = '10'
b = 20
c = a+b # Error


# int() # 0
# it can convert any number to int.
# it can convert any string to int.
        # when only if all the elements in that str is number
a = 123.123
b = int(a)
print(b) # 123
print(type(b))

a = '123.123'
b = int(a) # Error
print(b) # 123
print(type(b))

a = '123'
b = int(a)  # 123
print(b) 
print(type(b)) # int

a = '123234 234234 234'
b = int(a)  # Error


# float() # 0.0
# it can convert any number to float
# it can convert any string to float.
        # when only if all the elements in that str is number
        # that string can have one decimal

a = 123
b = float(a) # 123.0
print(b) 
print(type(b))

a = '234234.234'
b = float(a) # 234234.234
print(b) 
print(type(b)) # float

a = '2342'
b = float(a) # 2342.0
print(b) 
print(type(b)) # float

# very important concept
print(str == type('sdfa')) # True
print(type(24234) == type(234234)) # True

print(type(242.34) == float) # True
print(type(242) == float) # False


a = int(input())
b = int(input())
print(a + b) # 30


# CONDITIONS & STATEMENTS:

# if,else

# syntax:
# if condition:
#     statement 1
# else:
#     statement 2

# if the condition is True then if statement will be executed
# if the condition is False then else statement will be executed
# if can be presented with else. i.e if has highest priority
# without if else will not persist.

# syntax:
# if condition:
#     statement 1
# elif condition:
#     statement 2
# elif condition:
#     statement 3
# elif condition:
#     statement 4
# else:
#     statement 

# if can be presented with else. i.e if has highest priority
# else is optional.
# if-else - there will be only one output.
# First, true condition statement will only be executed



# condition can be anything
# python will take it as either True or False

# for a condition to be True it is Infinite scanario
# for a condition to be False it is certain scenario - 0,0.0,False,'',[],None or any empty datatype

'234.234' # True
0.0 # False
0.00000001 # True


if True:
    print('If statement')
else:
    print('else statement')


if False:
    print('If statement')
else:
    print('else statement')

if False:
    print('If statement')

if True:
    print('If statement')

if 'Magesh'+ ' Good':
    print('Statement 1')
else:
    print('Statement 2')

if 10 % 2 * 10:
    print('Statement 3')

# 0,0.0,False,'',None

if '10*0':
    print(1) # 
if '':
    print(2)
else:
    print(3) # 3
if str == type('sdfa'):
    print(4) # 
else:
    print(5)
if int == type(int('234')):
    print(6) #


# 1. carrot
# 2. beetroot
# 3. brinjal
# 4. tomato
# 5. whatever we want

wanted = 'carrot'
shop = 'brinjal'

if 'carrot' == shop: 
    print(1)
elif 'beetroot' == shop:
    print(2)
elif 'brinjal' == shop:
    print(3)
elif 'tomato' == shop:
    print(4)
else:
    print(5)

if 1*9*34 / 24: # 0 | 0.0
    print(1)
elif 3424% 2:
    print(2)
elif 'Magesh':
    print(3)
elif True:
    print(4)

if 123234 % 5 ==0 :
    print(1)
elif 'Magseh':
    print(2)
if 'False':
    print(3)
else:
    print(4)
if 89 % 3 + 10 / 2.5:
    print(5)
elif type('Magesh'):
    print(6)
elif '0':
    print(7)
elif True:
    print(8)
if '0':
    print(9)
elif 'False':
    print(10)
else:
    print(11)