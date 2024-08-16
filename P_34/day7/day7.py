
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