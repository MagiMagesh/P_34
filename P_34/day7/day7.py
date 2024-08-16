
# Q1. a = [1,'123','magesh',345,'phone','11',234.234,'zer','Earth','Moon','Mars'] the output should be
# 6
# 128
# 350
# 16
# 239.234

a = [1,'123','magesh','234.234',345,'phone','11',234.234,'zer','Earth','Moon','Mars']

# print(a[1].isdigit()) # True
# print(a[2].isdigit()) # False

for i in a:
    if type(i) ==str:
        if i.isdigit():
            print(float(i)+5)
    if type(i) ==int:
        print(i + 5)
    if type(i) ==float:
        print(i + 5)
    

# Q2. a = 'i live in India'
# count of all the elements in a
# ex: 'i' is repeated for 5 times
# ex: 'l' is repeated for 4 times
# ex: ' ' is repeated for 4 times

a = 'i live in India'
for i in a:
    print(i,' is repeated for ',a.count(i),'times')

# Q3. 
# n = 7
# *
# **
# ***
# ****
# *****
# ******
# *******

print(' '.join(1 * '*'))
print(' '.join(2 * '*'))
print(' '.join(3 * '*'))
print(' '.join(4 * '*'))
print(' '.join(5 * '*'))



n = 51

for i in range(1,n+1):
    print(' '.join(i * '*'))

# Q4.
# n = 5
#     *
#    **
#   ***
#  ****
# *****

n = 15
for i in range(1,n+1):
    print((n-i)*' ' + i*'*')


# while loop |  infinite loop | condition loop

# syntax:

# while condition:
#     statement

# if the condition is True wile will be keep on executing the statement.
# till the ocndition is False while loop will be keep on running.

# example for infinite loop
# while True:
#     print(1)


a = 15

while a > 10:
    print(a)
    a = a - 1
print('the value of a is ',a) # 10

# 1. a = 15, print(15) , a = 14
# 2. a = 14, print(14) , a = 13
# 2. a = 13, print(13) , a = 12
# 2. a = 12, print(12) , a = 11
# 2. a = 11, print(11) , a = 10

a = 15

while a > 10:
    a = a - 1
    print(a)



a = 'i live in India'

i = 0
while i < len(a):
    print(a[i])
    i = i + 1

a = [1,1,2,3,4,34,5,543,545,6]
i = 0
while i < len(a):
    print(a[i])
    i = i + 1


# logical operators:
# always will give the output in bool

# and , or, not

# syntax:
# condition1 and condition2

print(True and True) # True
print(True and False) # False
print(False and False) # False

if ('True' and 'False'):
    print(1)
else:
    print(2)

if ('True' and False):
    print(1)
else:
    print(2)

if ('True' and 0):
    print(1)
else:
    print(2)

# syntax:
# or
print(True or False) # True
print(True or True) # True
print(False or False) # False


if ('True' or False):
    print(1)
else:
    print(2)

if ('True' or 0):
    print(1)
else:
    print(2)

if (10%2.5 or 0):
    print(1)
else:
    print(2)

print(10%2.5)

# not:
# change True to False & viceversa

# syntax:
# not condition

print(not 'Magesh') # False
print(not '') # True

if not True:
    print(1)
else:
    print(2)


if not(not 'True'):
    print(1)
else:
    print(2)


# in
#  wehter that particular element is present in that data type or not

# syntax for str:
# 'substring' in  string_data

a = 'I live in India 54321'

print('Z' in a) # False
print('Z' not in a) # True
print('D' in a) # False
print('1' in a) #
print(1 in a) # Error

a = ['I', 'live' , 'in', 'India','1',1 ]

print('i' in a) # False

print('in' not in a) # False

print(1  in a) # True

# to get the unique element
a = '112312312423423534545654'

# 1. to create an empty list
# 2. to take the elements
# 3. to put that element in empty list if elememnt is not already present 
# 4. the element present in the list will be the new elment

a = '112312312423423534545654'

b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

a = '112312312423423534545654'

b = ''
for i in a:
    if i not in b:
        b = b + i
print(b)

# 1. i =1 ; b = '1'
# 2. i = 1; 
# 3. i = 2; b = '12'
# 4. i = 3; b = '123'
# 5. i = 1; 
# 6. i = 2; 
# 7. i = 3; 
# 8. i = 1; 
# 9. i = 2; 
# 0. i = 4; b = '1234'


a = '238462742388368'
# 74
b = 0
for i in a:
    b = b + int(i)
print(b)

# need to discuss:
# join & split for list

a = '238462'

b = 0
for i in a:
    b = b + int(i)
print(b)

# 1. b = 0; i = 2 ;  b = 0 + 2 = 2
# 2. b = 2; i = 3 ;  b = 2 + 3 = 5
# 2. b = 5; i = 8 ;  b = 5 + 8 = 13
# 2. b = 13; i = 4 ;  b = 13 + 4 = 17

# ''.join(list_data)
# to perform join for str all the elements in that list should be a str

a = ['1', '2', '3', '4', '5', '6']
print(''.join(a))
print(' '.join(a))


a = ['1', '2', '3', '4', '5', '6', 7]
print(' '.join(a)) # Error


# Q1. a = 'i live in India' # code optimisation
# count of all the elements in a
# ex: 'i' is repeated for 5 times
# ex: 'l' is repeated for 4 times
# ex: ' ' is repeated for 4 times


# Q2. a = [1,2,3,'magseh',23,3,24,2.5,'23']
# 81.5
# sum of all the valid numbers

# Q3. 
# 12345
# 1234
# 123
# 12
# 1

# Q4.
# Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
# Input Size : N <= 100000
# Sample Testcase :
# INPUT
# 2143
# OUTPUT
# 1 3

# Q5.
# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
# Sample Testcase :
# INPUT
# 4 2
# 1 2 3 3
# OUTPUT
# yes


# Q6.
# You are given an array of ids of prisoners. The jail authority found that there are some prisoners of same id. Your task is to help the authority in finding the common ids.

# Input Description:
# First line contains a number ‘n’ representing no of prisoners. Next line contains n space separated numbers.

# Output Description:
# Print the ids which are not unique. Print -1 if all ids are unique

# Sample Input :
# 7
# 1 1 11 121 131 141 98
# Sample Output :
# 1