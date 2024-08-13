# ITERATION:
# for loop      | finite loop
# while loop    | infinite loop

# taking  one by one element from the iterable data type

# # iterable data type
# 1. str
# 2. list
# 3. tuple
# 4. set
# 5. dict
# 6. range

# # non-iterable data type
# 1. int
# 2. float
# 3. bool
# 4. None

# data type


a = '12345'

a = 'My number is 1234567'
print(a[-4]) # '4'
print(type(a[-4])) # str
# Whenever we take any Element from string, always that output will be a string

# FOR LOOP:

# for variable in iterable_data_type:
    # statement / logic

a = '12345'

for i in a:
    print(i)

a = '12345'
for i in a:
    print(a)


a = '12345'
for i in a:
    print(i + 5) # Error

a = '12345'
for i in a:
    # print(int(i) + 5) 
    b = int(i)
    print(b + 5) 

a = input()
for i in a:
    print(i)

# Q1. to find out whether that particular particular element, this, even or odd

a = '123456789'
# odd
# even
# odd
# even,..
a = '45622426289'
# even
# odd
# even
# even
# even
# even
# even...
