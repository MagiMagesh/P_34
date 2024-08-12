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
