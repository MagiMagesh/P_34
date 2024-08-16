
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

# Q3. 
# n = 7
# *
# **
# ***
# ****
# *****
# ******
# *******

# Q4.
# n = 5
#     *
#    **
#   ***
#  ****
# *****