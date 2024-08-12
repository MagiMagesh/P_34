# first letter in a variable should be alphabet / _
# we can have number in variable
# in  a variable can use alphabtes/numbers/_

name = 'Magesh'

1name = 'Sun' # Error

name1 = 'Moon'
Name1 = 'Mars' 
# python is caseSensitive

print(name1)
print(Name1)

pla ce = 'Magesh' # not accepted

pla_ce = 'Magesh' #  accepted


# ----------------------------------------------------
# STRING:

print('Magesh')
print("Magesh")

print("It's my pen")
print('It is very "important"')

print('''I live in India
India is my "country"
to give output in multiline.
It's my rights''')

print("""I live in India
India is my "country"
to give output in multiline.
It's my rights""")

# syntax for multiply:
# num1 * num2 

print(10 * )
print( / 10)
print( 10 + 10 + )

name = 'Magesh'
#       012345  positive index_number
#       654321  negitive index_number


# indexing:

# Is a process to take any single element from a string.

# syntax:
# str_data[index_number]
# string_data means either variable or direct str element

# index_number:
# Every element in a string has its own index number
# starts from 0 and ends with length-1

# negitive index_number:
# starts from right to left.
# starts from -1 and end with -length.


# Everything inside a string will be considered as a string element

a = 'I live in India'
  #  012345678901234     - index number

print(a)
# indexing
print(a[10]) # I
print(a[12]) # d

# len(StringDatatype)
# It will give you the length of the string element.
# length total number of elements.

print(len(a))  # 15



b = 'I live in In1234dia'
print(len(b))  # 19
print(b[13]) # 2


b = 'I live in sadf 345435 sdf In1234dia'
print(b[-6]) # 2


# slicing:
# Process to take more than one element from a string.


# syntax:

# string_data[ start_index_number : end_index_number +1 : step  ] by default step is 1

# string_data[ start_index_number : end_index_number +1 ] this is what we need to do

# string_data[  : end_index_number +1 ] by default start_index_number will be 0
# string_data[  start_index_number :  ] by default it will fetch till last element

# string_data[ start_index_number : end_index_number -1 ] this is what python do
# string_data[ start_index_number : end_index_number -1 ] this is what python do

a = 'I live in sadf 345435 sdf In1234dia'

print(a[2:5 ]) # liv
print(a[2:5 + 1]) # live
print(a[2:6]) # live
print(a[4:8]) # ve i
print(a[4:9]) # ve in
print(a[4:9:1]) # ve in


a = 'I live in sadf 345435 sdf In1234dia'
print(len(a))
print(a[0:5]) # I liv
print(a[:6]) # I live
print(a[2:]) # live in sadf 345435 sdf In1234dia
print(a[2: : 2]) # live in sadf 345435 sdf In1234dia


a = 'I live in sadf 345435 sdf In1234dia'
print(a[-9:-3]) # In1234
print(a[-9:]) # In1234dia

a = 'i live in India'
print(len(a))
print(a[2: : 2]) # lv nIda
print(a[7::3]) # iIi 
print(a[ : : 3]) # ii  d
# 2,4,6,8,10,12,14 index number we are going to consider


# reverse slicing:
# we will move from right to left

# syntax:
# string_data[ start_index_number : end_index_number -1 : -step  ] 

a = 'i live in India'
# evil
print(a[5 : 2-1 : -1 ]) # evil
# aidnI
print(a[-1 : -5-1 : -1 ]) # aidnI
# adIn vli
print(a[::-2])

print(dir(str))

# function for string
# capitalize',  'center', 'count',  'endswith', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'istitle', 'isupper', 'join',  'lower', 'lstrip', 'partition', 'removeprefix', 'removesuffix',  'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',  'upper','find'

# str_data.upper()       - Convert all the element in the string to uppercase
# str_data.lower()       - Convert all the element in the string to lowercase
# str_data.capitalize()  - First word in that string will be capital letter
# str_data.title()       - Every word, first letter will be in capital

a = 'i liVe ^&** InDIa. i 767 knOw CODinG'
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())

# string_data.startswith('substring')   # String is starting with that sub string or not
# string_data.endswith('substring')     # String is ending with that sub string or not
# output will be in bool



a = 'i live in India'
print(a.startswith('I'))    # False
print(a.startswith('i l'))  # True
print(a.startswith('i lv')) # False
print(a.endswith('Ia'))     # False



# string_data.count('substring') # it will give the count of that substring

a = 'i live in India. This is my place is it your per'
print(a.count('i')) # 8
print(a.count('is')) # 3
print(a.count('in')) # 1
print(a.count('In ia')) # 0


# string_data.index('substring') 
# if the substring is not present it will give error
# it will give the index of first occured substring, 
# only the first elemetn in that substrig


a = 'i live in India. This is my place is it your per'
print(a.index('i')) # 0
print(a.index('v')) # 4
print(a.index('in')) # 7
# print(a.index('mag')) # error
print(a.index('is')) # 19


# string_data.find('substring')
# similar to index
# if the substring is not present it will not give error it will give -1 

a = 'i live in India. This is my place is it your per'
print(a.find('i')) # 0
print(a.find('v')) # 4
print(a.find('in')) # 7
print(a.find('mag')) # error
print(a.find('is')) # 19

