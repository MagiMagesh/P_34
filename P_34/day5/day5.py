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
# 4 is even
# 5 is odd
# 6 is even
# even
# even
# even
# even...

print(10 % 2)
print(10 % 2 == 0)

a = 56
if a%2==0:
    print('even')
else:
    print('odd')



a = input('a')
if int(a)%2==0:
    print('even')
else:
    print('odd')

a = '45622426289'
for i in a:
    if int(i)%2==0:
        print('even')
    else:
        print('odd')


a = '45622426289'
for i in a:
    if int(i)%2==0:
        print(i,'is','even')
    else:
        print(i,'is','odd')

# range()
# 1. range(n) # pack of number from 0 to n-1

print(range(5))  # range(0,5) = 0,1,2,3,4

for i in range(5):
    print(i)

a = '98765'

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

a = '98765'

for i in range(5):
    print(a[i])

a = '56789'
b = '12345'

for i in range(5):
    print(int(a[i]) + int(b[i]))

# 6
# 8
# 10
# 12
# 14


a = 'i live in India.This is My country'

for i in range(len(a)): # 0-14
    print(a[i])

a = 'Magesh Magesh Mageesesh Mageesesh'
print(len(a))
print(a[32])
print(a[33]) # Error - str index out of range

a = '123123345'
b = '928378234'
9
4
24
3
14

for i in range(len(b)):
    print(int(a[i]) * int(b[i]))

# list
# heterogeneous datatype
[]
# elements are seperated by ,
a = [ 1, 2.234 , 'Magesh' , True , 5  ]
  #   0   1         2         3    4     

print(a[2])
print(type(a[2])) # str
print(a[1:4]) # [2.234, 'Magesh', True]

# indexing & slicing is same as str



a = [ 1, 2.234 , 'Magesh' , True , 5  , ['Jasmine','Rose','Lotus'] ]
  #   0    1        2        3      4           5
b = a[-1]
print(b) # ['Jasmine', 'Rose', 'Lotus']
print(type(b)) # list
print(b[1]) # 'Rose'
print(a[-1][1]) # 'Rose'
print(type(a[-1][1])) # str
